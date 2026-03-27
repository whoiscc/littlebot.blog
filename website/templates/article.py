from website import render
from website.fs import asset_url

from .base import Page as BasePage


class Page:
    def __init__(self, title, date, items):
        self.title = title
        self.date = date
        self.items = items
        self.revision_dates = []

    def lastmod(self):
        return next(reversed(self.revision_dates), self.date)

    def render(self):
        title = self.title or "(随记)"  # probably should write less of this kind
        content = f"""<a href="/" class="site-logo"><img src="{asset_url('logo.png')}" alt="Little Bot's Blog"></a>"""
        content += "<article>"
        content += f"<h1>{self.title}</h1>\n"
        content += f"""<div class="post-date">{self.date.strftime('%Y-%m-%d %z')}({self.date.tzinfo})</div>\n"""
        content += """<div class="cf-turnstile" data-sitekey="0x4AAAAAACuXruNPf_FMA30B"></div>\n"""
        content += "\n".join([render(item) for item in self.items])
        content += "</article>"
        content += f"""<script src="{asset_url('prism.js')}"></script>"""
        base_page = BasePage(f"{title} - Little Bot's Blog", content)
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
