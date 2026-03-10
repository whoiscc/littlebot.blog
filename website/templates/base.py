from datetime import datetime, timezone
from website.components import Head


class Page:
    def __init__(self, title, content):
        self.head = Head(title)
        self.content = content

    def render(self):
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
{self.head.render()}
<body>
    <div class="container">
    {self.content}
    <footer class="site-footer">构建于{datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")}</footer>
    </div>
</body>
</html>"""
