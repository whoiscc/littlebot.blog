from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 4, 3, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Monologue
    也许是一种文艺复兴吧。
    或者说是历史的螺旋形上升。
@@
@Paragraph
    应当开设一个期刊，专注于收录那些
    @Emphasize
        不
    @@
    以发表为目的而撰写的报告或是技术博客。
    @SideNote
        我这个博客又怎么不算是呢（
    @@
@@
@Paragraph
    「投稿」意味着以发表为导向。
    人工智能领域以发表为导向的一整套工作流
    @SideNote
        或者说产业链
    @@
    已经算是彻底腐朽了。
    避免以发表为导向，就要避免投稿。
@@
@Paragraph
    我们所提议的期刊由审稿人以不透明的机制发现（discover）和认可（endorse）工作。
    这套机制必须时对文章作者隐藏的，因为
    @Hyperlink
        https://zh.wikipedia.org/wiki/%E5%8F%A4%E5%BE%B7%E5%93%88%E7%89%B9%E5%AE%9A%E5%BE%8B
        一项指标一旦变成了目标，它将不再是个好指标。
    @@
    收到邀请的作者只需要将现成的文章改写为学术论文的格式，或是只需要对期刊授权，由期刊代为改写。
    随后，我们保留一年一度的线下会议，但是其与发表周期完全脱钩，主要是象征意义。
    这套流程的设计有点像是更有实效性的奥斯卡奖。
@@
@Paragraph
    我们希望提议的期刊可以降低创作真正有价值工作的研究者的工作量和承担的风险。
    当这个期刊「嗅觉的灵敏性」得到普遍的认可以后，这些研究者就可以在完成一项工作后简单地把它提交到公开环境，比如arXiv甚至是个人博客，然后他们的工作就完成了。
    他们不需要再劳神与千军万马一起挤在会议投稿中，承担被分配到不称职审稿人的风险。
    会议依然有存在的意义，它们可以验证研究者能够胜任一项工作的完整流程。
    如果研究者出于某些原因依然要承担「使自己的工作获得业界一定程度认可」的压力，提交到会议上依然是他们最好的选择。
    但如果他们没有这个压力但仍然做出了有价值的工作，这个期刊就可以接手了。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page("invitation-based-journal-for-ai", page)
