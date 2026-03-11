from datetime import datetime, timezone
from website.components import Head


class Page:
    def __init__(self, title, content, extra_container_classes=None):
        self.head = Head(title)
        self.content = content
        self.extra_container_classes = extra_container_classes

    def render(self):
        container_classes = "container"
        if self.extra_container_classes:
            extra_container_classes = " ".join(self.extra_container_classes)
            container_classes += f" {extra_container_classes}"

        return f"""<!DOCTYPE html>
<html lang="zh-CN">
{self.head.render()}
<body>
    <div class="{container_classes}">
    {self.content}
    <footer class="site-footer">构建于{datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")}</footer>
    </div>
</body>
</html>"""
