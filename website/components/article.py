from contextlib import contextmanager

from website import render


class Container:
    def __init__(self, *items):
        self.items = list(items)

    @classmethod
    @contextmanager
    def of(cls, stage, *args):
        yield from cls(*args).of_impl(stage)

    def of_impl(self, stage):
        context = stage.context
        stage.context = self
        try:
            yield stage.context
        finally:
            context.items.append(stage.context)
            stage.context = context

    def render(self):
        return "".join(render(item) for item in self.items)


class Paragraph(Container):
    def render(self):
        return f"<p>{super().render()}</p>"


class SideNote(Container):
    count = 0

    def render(self):
        SideNote.count += 1
        return f"""<span class="sidenote-wrapper">\
<sup><label for="sn-{SideNote.count}" class="margin-toggle-label"></label></sup>\
<input type="checkbox" id="sn-{SideNote.count}" class="margin-toggle">\
<label for="sn-{SideNote.count}" class="sidenote-backdrop"></label>\
<span class="sidenote">{super().render()}</span>\
</span> """  # space here to easily separate consecutive sidenotes


class Emphasize(Container):
    def render(self):
        return f"<em>{super().render()}</em>"


class Monologue(Container):
    def render(self):
        return f"<div class='monologue-block'>{super().render()}</div>"


class CodeBlock(Container):
    def __init__(self, language, *items):
        super().__init__(*items)
        self.language = language

    def render(self):
        return f"""<pre><code class="language-{self.language}">{super().render()}</code></pre>"""


class Code:
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<code>{self.text}</code>"


class Hyperlink(Container):
    def __init__(self, href, *items):
        super().__init__(*items)
        self.href = href

    def render(self):
        return f"""<a href="{self.href}">{super().render()}</a>"""
