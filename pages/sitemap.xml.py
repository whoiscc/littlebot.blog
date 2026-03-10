from glob import glob
from pathlib import Path

from website.config import BUILD_DIR
from website.fs import write_page

content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for page in glob(f"{BUILD_DIR}/**/index.html", recursive=True):
    path = Path(page).relative_to(BUILD_DIR)
    if not path.is_relative_to("articles"):
        continue
    # TODO: support lastmod if possible
    content += f"""
<url>
    <loc>/{path}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
</url>
"""
content += """
</urlset>
"""

write_page("sitemap.xml", content)
