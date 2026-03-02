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
    {self.content}
</body>
</html>"""
