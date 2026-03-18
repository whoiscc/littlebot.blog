from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from website.components import Paragraph
from website.fs import write_page, write_sitemap_entry
from website.templates.article import PageStage


title = Path(__file__).stem
date = datetime(2026, 3, 10, tzinfo=ZoneInfo("Asia/Singapore"))
s = PageStage(title, date)
with Paragraph.of(s) as p:
    s += "氛围编程（vibe coding）的限制是，人类只能在项目可以观察的边界检查代码的正确性。"
    s += "受限于人类的观察能力，有些项目根本无法观察，而更多的项目只有外边薄薄一层可以观察，隐藏大量的内部实现细节。"
    s += "可以观察的皮占整个项目的比例越大，氛围编程的效果就越好。"
    s += "比如这个博客的CSS样式，就是一个极致的100%可观察的项目，氛围编程的效果非常好。"
with Paragraph.of(s) as p:
    s += "项目的皮馅比如果是一个由项目的内在特质决定的特性，那么氛围编程可能将会永远局限。"
    s += "但我倾向于认为，今后会开发出新的技术来提升项目的可观察性，最后让所有的项目都变得皮厚馅小。"
write_page("articles/vibe-coding-vs-project-skin-thickness", s.context.render())
write_sitemap_entry("articles/vibe-coding-vs-project-skin-thickness", s.context.lastmod())