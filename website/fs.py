from pathlib import Path

from website.config import BUILD_DIR


def write_page(path, content):
    path = Path(path)
    if not path.suffix:
        path = path / "index.html"
    build_path = BUILD_DIR / path
    build_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  -> {build_path}")
    with open(build_path, "w") as f:
        f.write(content)
