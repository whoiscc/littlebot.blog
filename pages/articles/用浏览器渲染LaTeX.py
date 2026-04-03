from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 4, 3, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    TeX是一个排版引擎。
    浏览器也是一个排版引擎。
    两者排版的对象范围自然有所不同，但是对于我们对LaTeX最关心的那些：段落、浮动元素（图和表格）与段落的关系等等，浏览器完全可以胜任。
    最重要的是，对于数学公式这一LaTeX的核心功能，浏览器方案几乎可以说是已经彻底抹平差异了。
@@
@Paragraph
    因此，可以将LaTeX文档变换为HTML，直接交给浏览器渲染。
    这里说的不是pandoc和arXiv实现的那种「网页式」的渲染，而是形如PDF的渲染效果。
    可以先用一些样式在网页上画出PDF页，在页内设置好CSS内边距，然后把段落直接套在
    @Code
    p
    @@
    元素里，由浏览器来处理段落的换行和段落间距。
@@
@Paragraph
    这种方案最大的好处是兼顾LaTeX式的程序化写作和浏览器式的所见即所得，彻底消除了两者之间已经持续了几十年的权衡。
    目前在这方面最有实力的方案是Typst。
    那是一个相比之下非常激进的方案，从头发明编程语言、排版引擎、用户界面和生态。
    而这个方案则选择充分复用现有的LaTeX和浏览器为基础，虽然寄人篱下，但是开发和采用成本都要小很多。
@@
"""

page = Page(title, date, eval(transpile(content)))
write_article_page("browser-rendered-latex", page)
