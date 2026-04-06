from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 4, 6, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    @Hyperlink
        https://zh.wikipedia.org/zh-cn/%E8%AA%9E%E8%A8%80%E7%9B%B8%E5%B0%8D%E8%AB%96
        温和版本的语言相对论「认为语言结构及使用可能影响思考模式及决策方式」
    @@
    。
    写博客所用的工作流会显著地体现这一点。
    使用Markdown写博客会使作者偏向于使用Markdown支持的样式，比如小标题、列表、引用等。
    如果引入了MathJax，那么作者就会倾向于使用数学公式来表达一些概念。
@@
@Monologue
    因此，发明自己的标记语言来写博客，不仅可以应用自定义的样式，还可以根据最终发展出的样式集合来分析自己逻辑思考和表达上的特点和偏好。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page("linguistic-relativity-in-blogging", page)
