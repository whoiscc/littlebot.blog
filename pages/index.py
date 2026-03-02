from website.templates.base import Page
from website.config import BUILD_DIR

content = """<h1>全体目光向我看齐，我宣布个事</h1>
<p>等下把featured博客挂在这里。</p>

<p>
    在撰写博客时，我们经常需要添加补充说明。传统的脚注需要跳转到页面底部，而页边注则直接显示在旁边
    <span class="sidenote-wrapper">
        <label for="sn-1" class="margin-toggle-label"></label>
        <input type="checkbox" id="sn-1" class="margin-toggle">
        <span class="sidenote">这是一个页边注。在宽屏下，它会安静地呆在右侧的空白处；在手机上，您可以点击十字星标展开它。</span>
    </span>
    。这种设计能够极大地保持阅读的流畅性。
</p>
"""
page = Page("Little Bot Blog", content)
with open(f"{BUILD_DIR}/index.html", "w") as f:
    f.write(page.render())
