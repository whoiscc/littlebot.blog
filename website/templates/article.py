from .base import Page as BasePage


class Page:
    def __init__(self, title, elements):
        self.title = title
        self.elements = elements

    def render(self):
        content = f"<h1>{self.title}</h1>\n"
        content += "\n".join([element.render() for element in self.elements])
        title = self.title or "(随记)"  # probably should write less of this kind
        base_page = BasePage(f"{title} - Little Bot Blog", content)
        return base_page.render()
