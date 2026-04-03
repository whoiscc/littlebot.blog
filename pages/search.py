from pathlib import Path

from website.components.head import Head
from website.fs import asset_url, write_page
from website.templates.base import Page


with Path(__file__).with_name("search.js").open() as f:
    search_js = f.read()
source = f"""
{Head("Search - Little Bot's Blog").render()}
<html>
<!-- Import the library -->
<script type="module" src="https://84b379a3-48bb-49d5-83e5-f96851f774a8.search.ai.cloudflare.com/assets/v0.0.29/search-snippet.es.js"></script>

<chat-page-snippet
  api-url="https://84b379a3-48bb-49d5-83e5-f96851f774a8.search.ai.cloudflare.com"
  placeholder="输入关键词查询相关文章"
>
</chat-page-snippet>
</html>
"""
write_page("search/index.html", source)
