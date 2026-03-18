from glob import glob
from pathlib import Path
from shutil import copy
from subprocess import run

from website.config import BUILD_DIR


def write_page(path, content):
    is_dir = path.endswith("/")
    path = Path(path)
    if is_dir or not path.suffix:
        path = path / "index.html"
    build_path = BUILD_DIR / path
    build_path.parent.mkdir(parents=True, exist_ok=True)
    with open(build_path, "w") as f:
        f.write(content)
    print(f"  -> {build_path}")


def build():
    build_dir = Path(BUILD_DIR)
    build_dir.mkdir(exist_ok=True)
    with open(build_dir / ".gitignore", "w") as f:
        f.write("*")

    for file in glob("website/static/*"):
        print(file)
        copy(file, build_dir)
        print(f"  -> {build_dir}/{Path(file).name}")

    for file in glob("pages/articles/**/*.py", recursive=True):
        print(file)
        run(f"uv run {file}", shell=True, check=True)

    for file in glob("pages/**/*.py", recursive=True):
        if file.startswith("pages/articles/"):
            continue
        print(file)
        run(f"uv run {file}", shell=True, check=True)
