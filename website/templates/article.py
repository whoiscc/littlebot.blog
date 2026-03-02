from website import render

from .base import Page as BasePage


class Page:
    def __init__(self, title, date, items):
        self.title = title
        self.date = date
        self.items = items

    def render(self):
        content = f"<h1>{self.title}</h1>\n"
        content += f"<div class='post-date'>{self.date.strftime('%Y-%m-%d')} {self.date.tzinfo}</div>\n"
        content += "\n".join([render(item) for item in self.items])
        title = self.title or "(随记)"  # probably should write less of this kind
        base_page = BasePage(f"{title} - Little Bot Blog", content)
        return base_page.render()
