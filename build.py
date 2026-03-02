from pathlib import Path
from website.config import BUILD_DIR
from subprocess import run
from shutil import copy
from glob import glob


BUILD_DIR = Path(BUILD_DIR)
BUILD_DIR.mkdir(exist_ok=True)
with open(BUILD_DIR / ".gitignore", "w") as f:
    f.write("*")

for file in glob("website/static/*"):
    print(file)
    copy(file, BUILD_DIR)

for file in glob("pages/**/*.py", recursive=True):
    print(file)
    run(f"uv run {file}", shell=True, check=True)
