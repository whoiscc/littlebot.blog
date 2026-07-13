from glob import glob
from hashlib import blake2s
from os import environ
from pathlib import Path
from shutil import copy, rmtree
from subprocess import run

from website.config import BUILD_DIR


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
    source_path = Path(BUILD_DIR) / '.state' / 'static' / filename
    return f"/{source_path.resolve().name}"


def write_page(path, render_lines):
    is_dir = path.endswith("/")
    path = Path(path)
    if is_dir or not path.suffix:
        path = path / "index.html"
    build_path = BUILD_DIR / path
    build_path.parent.mkdir(parents=True, exist_ok=True)
    with open(build_path, "w") as f:
        if isinstance(render_lines, str):
            f.write(render_lines)
        else:
            for line in render_lines:
                f.write(line + "\n")
    print(f"  -> {build_path}")


def write_sitemap_entry(path, lastmod):
    if not path.endswith("/"):
        path += "/"
    entry = f"""<url>
    <loc>/{path}</loc>
    <lastmod>{lastmod}</lastmod>
    <priority>0.5</priority>
</url>
"""
    build_path = BUILD_DIR / '.state' / path
    build_path.mkdir()
    with open(build_path / "sitemap.entry.xml", "w") as f:
        f.write(entry)


def write_article_page(path, page):
    write_page(f"articles/{path}", page.render())
    write_sitemap_entry(f"articles/{path}", page.lastmod())


def build():
    build_dir = Path(BUILD_DIR)
    if build_dir.exists():
        rmtree(build_dir)
    build_dir.mkdir()
    with open(build_dir / ".gitignore", "w") as f:
        f.write("*")
    (build_dir / '.state').mkdir()

    print("PHASE static")
    symlink_dir = build_dir / '.state' / 'static'
    symlink_dir.mkdir()
    for file in glob("website/static/*"):
        print(file)
        source_path = Path(file)
        target_name = path_with_content_suffix(source_path).name
        target_path = build_dir / target_name
        copy(file, target_path)
        
        symlink = symlink_dir / source_path.name
        symlink.symlink_to(target_path.relative_to(symlink_dir, walk_up=True))
        print(f"  -> {target_path}")
    print()

    def run_pages(files):
        for file in files:
            print(file)
            run(f"python3 {file}", shell=True, check=True)
        print()

    print("PHASE article")
    (build_dir / '.state' / 'articles').mkdir()
    run_pages(glob("pages/articles/*.py"))

    # The flat pages/*.py scripts split across the final two phases by input
    # scope. `collection` pages consume article metadata -- the sitemap today,
    # tag/category/year-archive listings later. `site` pages read the whole
    # built site (e.g. index.py's connectivity list over every page), so they
    # must run last. New drop-in pages default to collection; only site-level
    # pages need adding to the set below.
    pages = glob("pages/*.py")
    site_pages = {"pages/index.py"}
    assert site_pages <= set(pages), f"site_pages not found: {site_pages - set(pages)}"

    print("PHASE collection")
    run_pages(f for f in pages if f not in site_pages)

    print("PHASE site")
    run_pages(site_pages)
