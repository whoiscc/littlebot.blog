from glob import glob
from subprocess import PIPE, run
from os import environ

from website.fs import write_page

content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for file in glob("pages/articles/**/*.py", recursive=True):
    print(" ", file, "(sitemap)")
    p = run(f"uv run {file}", shell=True, check=True, env={**environ, "LBB_CONTEXT": "sitemap"}, stdout=PIPE, text=True)
    content += p.stdout
content += """</urlset>"""

write_page("sitemap.xml", content)
