from website.article_prelude import *

title = "预训练模型是新时代的CPU"
date = datetime(2026, 5, 12, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    预训练大模型什么都能做。
    通过提示词和harness可以实现非常灵活的功能。
    可以调用外部工具，包括知识库和微调过的模型，这些东西就像加速器。
    显然，我们要像以前看待CPU一样看待预训练大模型。
@@
@Paragraph
    那么，接下来就要考虑两个问题了。
    一个是，那么谁是新时代的GPU；
    另一个是，还有什么事是属于CPU的能力范围而目前还没见到预训练大模型有涉猎的。
    我目前想到的一个是虚拟化。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page(Path(__file__).stem, page)