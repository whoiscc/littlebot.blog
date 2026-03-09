from glob import glob
from pathlib import Path

from website.config import BUILD_DIR
from website.fs import write_page
from website.templates.base import Page

content = """<div class="site-logo"><img src="/logo.png" alt="Little Bot's Blog"></div>
<h1>Little Bot's Blog</h1>
<h2 style="margin-top: 0;">人是预测机器，偶尔许愿</h2>
"""
for page in glob(f"{BUILD_DIR}/**/index.html", recursive=True):
    path = Path(page).parent.relative_to(BUILD_DIR)
    if path == Path("."):
        continue
    content += f"""<p><a href="{path}/">{path}</a></p>"""
page = Page("Little Bot's Blog", content)
write_page(".", page.render())
