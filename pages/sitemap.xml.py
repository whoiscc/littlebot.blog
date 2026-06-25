from glob import glob
from subprocess import PIPE, run
from os import environ

from website.config import BUILD_DIR
from website.fs import write_page

content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for file in glob(f"{BUILD_DIR}/.state/**/sitemap.entry.xml", recursive=True):
    with open(file, "r") as f:
        content += f.read()
content += """</urlset>"""

write_page("sitemap.xml", content)
