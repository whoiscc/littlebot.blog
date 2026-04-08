from pathlib import Path

from website.fs import asset_url, write_page
from website.render import RenderLines
from website.templates.base import Page


with Path(__file__).with_name("search.js").open() as f:
    search_js = f.readlines()

page = Page(
    "Search",
    RenderLines(
        f"""<a href="/" class="site-logo"><img src="{asset_url('logo.png')}" alt="Little Bot's Blog"></a>""",
        """<div class="search-wrapper">""",
        RenderLines(
            """<input type="text" id="search-input" placeholder="检索相关内容">""",
        ),
        """</div>""",
        """<div id="search-title"></div>""",
        """<div id="search-results"></div>""",
    ),
    layout="search",
    epilogue_items=[
        """<script src="https://fastly.jsdelivr.net/npm/dompurify@3.3.2/dist/purify.min.js"></script>""",
        """<script src="https://fastly.jsdelivr.net/npm/marked@17.0.4/lib/marked.umd.min.js"></script>""",
        """<script>""",
        RenderLines(*(line.rstrip("\n") for line in search_js)),
        """</script>""",
    ],
)
write_page("search/index.html", page.render())
