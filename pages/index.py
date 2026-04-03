from glob import glob
from pathlib import Path

from website.config import BUILD_DIR
from website.fs import asset_url, write_page
from website.templates.base import Page

content = f"""<div class="site-logo"><img src="{asset_url('logo.png')}" alt="Little Bot's Blog"></div>
<h1>Little Bot's Blog</h1>
<h2 style="margin-top: 0;">人是预测机器，偶尔许愿</h2>
<p>你可以<a href="/search/">借助AI搜索内容</a>。以下列出本站所有页面的链接以保证基本的连通性。</p>
"""
for page in glob(f"{BUILD_DIR}/**/index.html", recursive=True):
    path = Path(page).parent.relative_to(BUILD_DIR)
    content += f"""<a href="{path}/"><em>{path}</em></a><br>"""
page = Page("Little Bot's Blog", content)
write_page(".", page.render())
