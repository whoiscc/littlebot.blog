"""On-demand OpenTimestamps stamping for article sources.

OpenTimestamps is NOT idempotent: each `ots stamp` submits a fresh commitment to
the calendar servers anchored at the current time, so re-stamping an unchanged
file would keep moving its proof forward and discard the earlier (and whole point)
proof of early existence. So we stamp on demand, keyed on content:

  - no `.ots`                          -> stamp
  - `.ots` hash == current file hash   -> leave it; just try to upgrade pending proofs
  - `.ots` hash != current file hash   -> content changed, this is a new document -> restamp

The `.ots` proof embeds the SHA256 of exactly what it certified, so the proof file
itself is the cache key -- no separate manifest needed.

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


def _embedded_hash(ots_path: Path) -> str | None:
    """The SHA256 the proof certifies, parsed from `ots info` (local, no network)."""
    result = run(["ots", "info", str(ots_path)], stdout=PIPE, stderr=PIPE, text=True)
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("File sha256 hash:"):
            return line.split(":", 1)[1].strip()
    return None


def stamp_articles(pattern: str = ARTICLES_GLOB) -> None:
    print("PHASE stamp")
    for file in sorted(glob(pattern)):
        source = Path(file)
        ots = source.with_name(source.name + ".ots")  # X.py -> X.py.ots
        current = _file_hash(source)

        if not ots.exists():
            print(f"  stamp (new): {source}")
            run(["ots", "stamp", str(source)], check=True)
        elif _embedded_hash(ots) != current:
            print(f"  restamp (content changed): {source}")
            ots.unlink()  # `ots stamp` refuses to overwrite; old proof lives on in git
            run(["ots", "stamp", str(source)], check=True)
        else:
            print(f"  unchanged: {source}")
    print()


def upgrade_articles(pattern: str = ARTICLES_GLOB) -> None:
    """Complete pending proofs (pending calendar -> Bitcoin attestation).

    Best-effort: a still-pending proof simply can't upgrade yet, and the network may
    be unavailable -- neither should abort the run. `ots upgrade` moves the original
    to `<name>.bak`; we discard those (git already holds prior versions)."""
    print("PHASE upgrade")
    for file in sorted(glob(pattern)):
        ots = Path(file).with_name(Path(file).name + ".ots")
        if not ots.exists():
            continue
        result = run(["ots", "upgrade", str(ots)], stdout=PIPE, stderr=PIPE, text=True)
        message = (result.stdout + result.stderr).strip().splitlines()
        print(f"  {ots}: {message[-1] if message else 'no output'}")
        bak = ots.with_name(ots.name + ".bak")
        bak.unlink(missing_ok=True)
    print()


def main() -> None:
    stamp_articles()
    upgrade_articles()


if __name__ == "__main__":
    main()
