from website import render

from .base import Page as BasePage


class Page:
    def __init__(self, title, date, items):
        self.title = title
        self.date = date
        self.items = items

    def render(self):
        content = f"<h1>{self.title}</h1>\n"
        content += f"<div class='post-date'>{self.date.strftime('%Y-%m-%d %z')}({self.date.tzinfo})</div>\n"
        content += "\n".join([render(item) for item in self.items])
        content += """<script src="/prism.js"></script>"""
        title = self.title or "(随记)"  # probably should write less of this kind
        base_page = BasePage(f"{title} - Little Bot Blog", content)
        return base_page.render()


class PageStage:
    def __init__(self, title, date):
        self.context = Page(title, date, [])

    def __iadd__(self, other):
        if isinstance(other, tuple):
            self.context.items.extend(other)
        else:
            self.context.items.append(other)
        return self
