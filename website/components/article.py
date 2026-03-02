class Paragraph:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f"<p>{self.content}</p>"

class SideNote:
    count = 0

    def __init__(self, content):
        self.content = content

    def render(self):
        SideNote.count += 1
        return f"""<span class="sidenote-wrapper">
        <label for="sn-{SideNote.count}" class="margin-toggle-label"></label>
        <input type="checkbox" id="sn-{SideNote.count}" class="margin-toggle">
        <span class="sidenote">{self.content}</span>
</span>"""
