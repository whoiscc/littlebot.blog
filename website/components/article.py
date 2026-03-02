from website import render


class Paragraph:
    def __init__(self, *items):
        self.items = items

    def render(self):
        content = "".join(render(item) for item in self.items)
        return f"<p>{content}</p>"


class SideNote:
    count = 0

    def __init__(self, *items):
        self.items = items

    def render(self):
        SideNote.count += 1
        content = "".join(render(item) for item in self.items)
        return f"""<span class="sidenote-wrapper">\
<sup><label for="sn-{SideNote.count}" class="margin-toggle-label"></label></sup>\
<input type="checkbox" id="sn-{SideNote.count}" class="margin-toggle">\
<label for="sn-{SideNote.count}" class="sidenote-backdrop"></label>\
<span class="sidenote">{content}</span>\
</span> """  # space here to easily separate consecutive sidenotes


class Emphasize:
    def __init__(self, *items):
        self.items = items

    def render(self):
        content = "".join(render(item) for item in self.items)
        return f"<em>{content}</em>"


class Monologue:
    def __init__(self, *items):
        self.items = items

    def render(self):
        content = "".join(render(item) for item in self.items)
        return f"<div class='monologue-block'>{content}</div>"
