from website.article_prelude import *

title = "凌乱的代码项目就是凌乱的房间"
date = datetime(2026, 8, 8, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    一个逐渐变得凌乱的代码项目，和一间逐渐变得凌乱的房间并没有本质上的不同。
    就连一篇代码文件，它变乱的方式也和一张桌面如出一辙。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page(Path(__file__).stem, page)