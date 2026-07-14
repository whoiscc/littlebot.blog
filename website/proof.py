"""Read an OpenTimestamps `.ots` proof, fully offline, for the article footer.

Two things come out of a proof at build time, with no network and no bookkeeping:

  - the Bitcoin block height it is anchored to (once upgraded), shown in the footer;
  - the smallest self-contained proof to inline into the opentimestamps.org verify
    URL, so the URL (and page) stays small.

A freshly `ots stamp`ed proof carries one branch per calendar and, once the daily
`ots upgrade` runs, each branch ends in a BitcoinBlockHeaderAttestation -- four
redundant Bitcoin paths (~5 KB). For the verify link we only need ONE of them, so
we prune to the single shortest path reaching the earliest block. That branch alone
re-computes to the real block merkle root, so it verifies against Bitcoin with no
calendar dependency and no maturation wait -- at roughly a quarter of the size.

Before that upgrade the proof is still calendar-pending (no Bitcoin height yet); we
report height=None and inline the pending proof as-is (already small). The verify
page will complete it from the calendars when a visitor checks it. The full,
multi-branch proof stays committed on the deploy branch as the durable record.
"""

from opentimestamps.core.notary import BitcoinBlockHeaderAttestation
from opentimestamps.core.serialize import (
    BytesDeserializationContext,
    BytesSerializationContext,
)
from opentimestamps.core.timestamp import DetachedTimestampFile, Timestamp


class ProofSummary:
    def __init__(self, height: int | None, ots_hex: str):
        self.height = height  # earliest Bitcoin block; None while still pending
        self.ots_hex = ots_hex  # smallest proof to inline into the verify URL


def _paths(timestamp, prefix):
    """Yield (path_of_ops, attestation) for every attestation in the tree."""
    for attestation in timestamp.attestations:
        yield prefix, attestation
    for op, child in timestamp.ops.items():
        yield from _paths(child, prefix + [op])


def _prune(timestamp, path, attestation):
    """Rebuild a timestamp keeping only `path` down to `attestation`."""
    kept = Timestamp(timestamp.msg)
    if not path:
        kept.attestations.add(attestation)
    else:
        head, *tail = path
        kept.ops[head] = _prune(timestamp.ops[head], tail, attestation)
    return kept


def summarize(ots_bytes: bytes) -> ProofSummary:
    detached = DetachedTimestampFile.deserialize(BytesDeserializationContext(ots_bytes))
    timestamp = detached.timestamp

    anchors = [
        (len(path), path, att)
        for path, att in _paths(timestamp, [])
        if isinstance(att, BitcoinBlockHeaderAttestation)
    ]
    if not anchors:
        return ProofSummary(None, ots_bytes.hex())  # still pending -- inline as-is

    # earliest block == strongest existence claim; shortest path to it == smallest proof
    earliest = min(att.height for _, _, att in anchors)
    _, path, att = min(
        (a for a in anchors if a[2].height == earliest), key=lambda a: a[0]
    )
    pruned = DetachedTimestampFile(detached.file_hash_op, _prune(timestamp, path, att))
    out = BytesSerializationContext()
    pruned.serialize(out)
    return ProofSummary(earliest, out.getbytes().hex())
