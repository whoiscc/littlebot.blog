from website.article_prelude import *

title = "我们做系统方向科研的将会成为非遗传承人"
date = datetime(2026, 6, 22, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    也许别的方向也会。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page(Path(__file__).stem, page)
