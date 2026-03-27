from datetime import datetime, timezone
from website.components import Head


class Page:
    def __init__(self, title, content, layout=None):
        self.head = Head(title)
        self.content = content
        self.layout = layout

    def render(self):
        body_attrs = f' class="{self.layout}-layout"' if self.layout else ""
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
    {self.head.render()}
    <link rel="preconnect" href="https://challenges.cloudflare.com">
<body{body_attrs}>
    <main class="container">
    {self.content}
    </main>
    <footer class="site-footer">构建于{datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")}</footer>
    <script
        src="https://challenges.cloudflare.com/turnstile/v0/api.js"
        async
        defer
    ></script>
</body>
</html>"""
