from website.config import BUILD_DIR
from website.fs import write_page

content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
# articles should have already populated sitemap
# maybe bad design but ok for now
if (BUILD_DIR / "sitemap.xml").exists():
    content += (BUILD_DIR / "sitemap.xml").read_text()
content += """</urlset>"""

write_page("sitemap.xml", content)
