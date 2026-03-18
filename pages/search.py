from website.fs import asset_url, write_page
from website.templates.base import Page


content = f"""
<a href="/" class="site-logo"><img src="{asset_url('logo.png')}" alt="Little Bot's Blog"></a>
<div class="search-wrapper">
  <input type="text" id="search-input" placeholder="检索相关内容">
</div>
<div id="search-title"></div>
<div id="search-results"></div>
<script src="https://fastly.jsdelivr.net/npm/dompurify@3.3.2/dist/purify.min.js"></script>
<script src="https://fastly.jsdelivr.net/npm/marked@17.0.4/lib/marked.umd.min.js"></script>
<script src="{asset_url('search.js')}"></script>
"""

page = Page("Search - Little Bot's Blog", content, layout="search")
write_page("search/index.html", page.render())
