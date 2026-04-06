from datetime import datetime, timezone
from website.components import Head
from website.render import RenderLines


class Page:
    def __init__(self, title, content, epilogue=None, layout=None):
        self.head = Head(title)
        self.content = content
        self.epilogue = epilogue or []
        self.layout = layout

    def render(self):
        body_attrs = f' class="{self.layout}-layout"' if self.layout else ""
        return RenderLines(
            """<!DOCTYPE html>""",
            """<html lang="zh-CN">""",
            self.head.render(),
            f"""<body{body_attrs}>""",
            RenderLines(
                """<main class="container">""",
                self.content,
                """</main>""",
                f"""<footer class="site-footer">构建于{datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")}</footer>""",
                """<script
        src="https://challenges.cloudflare.com/turnstile/v0/api.js"
        async
        defer
    ></script>""",
            ),
            """</body>""",
            """</html>""",
        )
