from website.fs import asset_url
from website.render import RenderLines


class Head:
    def __init__(self, title):
        self.title = title

    def render(self):
        return RenderLines(
            """<head>""",
            RenderLines(
                """<meta charset="UTF-8">""",
                """<meta name="viewport" content="width=device-width, initial-scale=1.0">""",
                f"""<title>{self.title}</title>""",
                """<link rel="preconnect" href="https://fastly.jsdelivr.net" crossorigin>""",
                """<link rel="preconnect" href="https://challenges.cloudflare.com">""",
                # maybe skip loading on pages that don't need it
                """<link rel="preload" href="https://fastly.jsdelivr.net/npm/cn-fontsource-fz-kai-z-03-regular@1.0.1/font.css" as="style" crossorigin>""",
                """<link rel="stylesheet" href="https://fastly.jsdelivr.net/npm/cn-fontsource-fz-kai-z-03-regular@1.0.1/font.css" crossorigin>""",
                f"""<link rel="stylesheet" href="{asset_url("main.css")}">""",
            ),
            """</head>""",
        )
