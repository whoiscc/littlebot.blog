from functools import cache
from glob import glob
from hashlib import blake2s
from os import environ
from pathlib import Path
from shutil import copy, rmtree
from subprocess import run

from website.config import BUILD_DIR


@cache
def path_with_content_suffix(path: Path, suffix_len: int = 8) -> Path:
    """Return a new path with a short content-based suffix in the filename.

    The returned path keeps the same parent directory and extension, and only
    changes the filename stem. The suffix is derived from file content, so it
    changes whenever the file content changes.
    """
    if not isinstance(path, Path):
        raise TypeError("path must be a pathlib.Path instance")
    if suffix_len <= 0:
        raise ValueError("suffix_len must be positive")
    if not path.is_file():
        raise FileNotFoundError(path)

    digest = blake2s(path.read_bytes()).hexdigest()[:suffix_len]
    return path.with_name(f"{path.stem}.{digest}{path.suffix}")


def asset_url(filename: str) -> str:
    """Resolve a static asset URL from the current content hash on disk."""
    source_path = Path("website/static") / filename
    return f"/{path_with_content_suffix(source_path).name}"


def write_page(path, content):
    if environ.get("LBB_CONTEXT"):
        return

    is_dir = path.endswith("/")
    path = Path(path)
    if is_dir or not path.suffix:
        path = path / "index.html"
    build_path = BUILD_DIR / path
    build_path.parent.mkdir(parents=True, exist_ok=True)
    with open(build_path, "w") as f:
        f.write(content)
    print(f"  -> {build_path}")


def write_sitemap_entry(path, lastmod):
    if environ.get("LBB_CONTEXT") != "sitemap":
        return

    print(
        f"""<url>
    <loc>/{path}</loc>
    <lastmod>{lastmod}</lastmod>
    <priority>0.5</priority>
</url>"""
    )


def write_article_page(path, page):
    write_page(f"articles/{path}", page.render())
    write_sitemap_entry(f"articles/{path}", page.lastmod())


def build():
    build_dir = Path(BUILD_DIR)
    if build_dir.exists():
        rmtree(build_dir)
    build_dir.mkdir(exist_ok=True)
    with open(build_dir / ".gitignore", "w") as f:
        f.write("*")

    for file in glob("website/static/*"):
        print(file)
        source_path = Path(file)
        target_name = path_with_content_suffix(source_path).name
        target_path = build_dir / target_name
        copy(file, target_path)
        print(f"  -> {target_path}")

    for file in glob("pages/**/*.py", recursive=True):
        if file == "pages/index.py":
            continue
        print(file)
        run(f"uv run {file}", shell=True, check=True)

    file = "pages/index.py"
    print(file)
    run(f"uv run {file}", shell=True, check=True)
