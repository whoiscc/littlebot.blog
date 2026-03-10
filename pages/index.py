from glob import glob
from pathlib import Path

from website.config import BUILD_DIR
from website.fs import write_page
from website.templates.base import Page

content = """<div class="site-logo"><img src="/logo.png" alt="Little Bot's Blog"></div>
<h1>Little Bot's Blog</h1>
<h2 style="margin-top: 0;">人是预测机器，偶尔许愿</h2>
<div class="monologue-block"><p>你可以<a href="/search/">借助AI搜索内容</a>。以下是所有文章的链接。</p></div>
"""
for page in glob(f"{BUILD_DIR}/**/index.html", recursive=True):
    path = Path(page).parent.relative_to(BUILD_DIR)
    if not path.is_relative_to("articles"):
        continue
    content += f"""<p><a href="{path}/">{path}</a></p>"""
page = Page("Little Bot's Blog", content)
write_page(".", page.render())
