from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 6, 22, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    也许别的方向也会。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page("system-research-is-legacy", page)
