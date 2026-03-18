from website.fs import asset_url


KAI_FONT_LOADER_SCRIPT = """<script>
    (() => {
        const candidates = ["Kaiti SC", "STKaiti", "KaiTi", "Microsoft KaiTi"];
        const canCheckFonts = document.fonts && typeof document.fonts.check === "function";
        const hasLocalKaiti = canCheckFonts && candidates.some((family) => (
            document.fonts.check(`16px "${family}"`, "汉")
        ));
        console.log("Local Kaiti fonts available:", hasLocalKaiti);

        if (!hasLocalKaiti) {
            document.documentElement.classList.add("no-local-kaiti");
            const link = document.createElement("link");
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
    <link rel="stylesheet" href="{asset_url('main.css')}">
</head>"""