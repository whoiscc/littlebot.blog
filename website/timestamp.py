"""On-demand OpenTimestamps stamping for article sources.

OpenTimestamps is NOT idempotent: each `ots stamp` submits a fresh commitment to
the calendar servers anchored at the current time, so re-stamping an unchanged
file would keep moving its proof forward and discard the earlier (and whole point)
proof of early existence. So we stamp on demand, keyed on content. One pass over
every article does exactly what each one needs:

  - no `.ots`                          -> stamp
  - `.ots` hash != current file hash   -> content changed, a new document -> restamp
  - `.ots` not yet Bitcoin-anchored    -> try to upgrade it (network)
  - `.ots` already Bitcoin-anchored    -> skip

The `.ots` proof embeds the SHA256 of exactly what it certified, so the proof file
itself is the cache key -- no separate manifest needed. A freshly (re)stamped proof
is pending and can't upgrade for hours, so it skips the upgrade attempt this pass.
Both the content check and the anchored check read `ots info` locally (no network),
so the only network calls are stamping changed articles and upgrading the handful
still pending -- cheap enough to run on every deploy.

History is git: each commit holds a matching (source preimage, `.ots`) pair, so an
old timestamp stays provable by checking out the commit it was made in, even after
the current source has been revised and restamped. Commit both files together.
"""

from glob import glob
from hashlib import sha256
from pathlib import Path
from subprocess import run, PIPE

ARTICLES_GLOB = "pages/articles/*.py"


def _file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _info(ots_path: Path) -> str:
    """`ots info` output -- local, no network."""
    return run(["ots", "info", str(ots_path)], stdout=PIPE, stderr=PIPE, text=True).stdout


def _embedded_hash(info: str) -> str | None:
    """The SHA256 the proof certifies, parsed from `ots info` output."""
    for line in info.splitlines():
        line = line.strip()
        if line.startswith("File sha256 hash:"):
            return line.split(":", 1)[1].strip()
    return None


def _is_complete(info: str) -> bool:
    """True once the proof carries a Bitcoin attestation -- then it never needs
    upgrading again, and we can tell offline without hitting a calendar."""
    return "BitcoinBlockHeaderAttestation" in info


def _stamp(source: Path, ots: Path, label: str) -> None:
    print(f"  {label}: {source}")
    ots.unlink(missing_ok=True)  # `ots stamp` refuses to overwrite; git keeps the old one
    run(["ots", "stamp", str(source)], check=True)


def _upgrade(ots: Path) -> None:
    """Complete a pending proof (pending calendar -> Bitcoin attestation).

    Best-effort: a still-pending proof simply can't upgrade yet, and the network may
    be unavailable -- neither should abort the run. `ots upgrade` moves the original
    to `<name>.bak`; we discard those (git already holds prior versions)."""
    result = run(["ots", "upgrade", str(ots)], stdout=PIPE, stderr=PIPE, text=True)
    message = (result.stdout + result.stderr).strip().splitlines()
    print(f"  upgrade {ots}: {message[-1] if message else 'no output'}")
    ots.with_name(ots.name + ".bak").unlink(missing_ok=True)


def timestamp_articles(pattern: str = ARTICLES_GLOB) -> None:
    print("PHASE timestamp")
    for file in sorted(glob(pattern)):
        source = Path(file)
        ots = source.with_name(source.name + ".ots")  # X.py -> X.py.ots

        if not ots.exists():
            _stamp(source, ots, "stamp (new)")
            continue
        info = _info(ots)  # one local read serves both the content and anchored checks
        if _embedded_hash(info) != _file_hash(source):
            _stamp(source, ots, "restamp (content changed)")
        elif not _is_complete(info):
            _upgrade(ots)
        else:
            print(f"  complete: {source}")
    print()


def main() -> None:
    timestamp_articles()


if __name__ == "__main__":
    main()
