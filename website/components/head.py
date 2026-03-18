KAI_FONT_LOADER_SCRIPT = """<script>
    (function () {
        var candidates = ["Kaiti SC", "STKaiti", "KaiTi", "Microsoft KaiTi"];
        var hasLocalKaiti = false;

        if (document.fonts && document.fonts.check) {
            for (var i = 0; i < candidates.length; i++) {
                if (document.fonts.check('16px "' + candidates[i] + '"', '汉')) {
                    hasLocalKaiti = true;
                    break;
                }
            }
        }

        if (!hasLocalKaiti) {
            document.documentElement.classList.add("no-local-kaiti");
            var link = document.createElement("link");
            link.rel = "stylesheet";
            link.href = "https://fastly.jsdelivr.net/npm/cn-fontsource-fz-kai-z-03-regular@1.0.1/font.css";
            document.head.appendChild(link);
        }
    })();
</script>"""


class Head:
    def __init__(self, title):
        self.title = title

    def render(self):
        return f"""<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    {KAI_FONT_LOADER_SCRIPT}
    <link rel="stylesheet" href="/main.css">
</head>"""