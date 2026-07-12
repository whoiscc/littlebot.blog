from website.article_prelude import *

title = "手写代码是一种手工艺"
date = datetime(2026, 7, 12, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    手工编写代码正在进入制作手工艺品的范畴，和手工制作衣服，皮包，家具等等变得相同。
    人工智能编写代码则对应着大规模工业化生产。
@@
@Paragraph
    这个类比可以自然而然地进一步推广。
    手写代码永远不会彻底消失，但是不再决定主流软件开发和行业发展的效率。
    手写的代码项目会成为一种奢侈品，也可能被融入到艺术风格当中去。
    而人工智能产品的代码则简单得多，一句话：人工智能生产日常生活中实际被消费的绝大多数代码。
@@
@Paragraph
    我曾经听过对于工业化生产的肉类质感的批评，说是比以前手工养殖的肉类口感下降很多。
    我也听过更多对于工业化生产带来行业整体劣化的评论。
    如此同时，以芯片之类的精细加工和极端条件下加工生产，彻底消除了手工制作的可行性。
    是时候写一些手工写不出来的软件了。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page(Path(__file__).stem, page)