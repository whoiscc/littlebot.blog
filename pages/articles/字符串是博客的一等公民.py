from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 4, 3, tzinfo=ZoneInfo("Asia/Singapore"))
content = r"""
@Paragraph
    我在开始搭建这个博客时做出了一个判断：我不需要借助Markdown也可以足够方便地写博客，从而可以绕开Markdown会带来的一些限制。
    @SideNote
        比方说缺乏页边旁注。
    @@
@@
@Paragraph
    然后，加上这篇我已经写了十篇博客了，并且在过程中设计了一套基于
    @Code
        with
    @@
    块的领域特定语言（DSL）。站在当下回顾，我的判断基本是对的。
    我没有任何一篇文章受到了写作条件的限制，或是因为我没有使用Markdown而显著额外花费了精力。
    @SideNote
        确实碰到了一个（有点黑色幽默的）小细节：Cloudflare的AI Search在索引内容时会先自动将其转换成Markdown再生成索引向量。
        因此最终我写的博客还是会以Markdown的格式（短暂地）存在于世间。
    @@
    我认为，就这样一直写下去也是完全没有问题的。
@@
@Paragraph
    不过，我承认直接写Python有
    @Emphasize
        一点
    @@
    确实是矫枉过正了。
    如同绝大多数
    @SideNote
        是哪个PHP导致我不能宣称「所有」我就不说了（逃
    @@
    通用编程语言一样，Python默认用户写下的是代码，而「文本模式」需要特定的符号进入和离开。
    然而，在写博客的时候，就算我想要玩再多的花活，我还是希望能默认处于文本模式。
    这一点是Python，乃至任何主流语言都没办法做到的小众需求。
    @SideNote
        Racket一定可以的，但是（如下文所述的）我的方案和Racket又有什么区别呢。
    @@
    这并不意味着我就要用回Markdown了。
    我只是收获了这个新的感悟，然后写了个简单的预处理器来吧文本模式和代码模式给翻转了过来。
@@
@Paragraph
    比方说我正在写的这段话，在原始的Python文件里是这样的
    @CodeBlock
    plaintext
    # "".join(open(__file__).readlines()[43:57])
    @@
    然后，预处理器会把它转换成
    @CodeBlock
    python
    # transpile("".join(open(__file__).readlines()[43:57]))
    @@
    预处理的逻辑非常简单。
    默认在文本模式下，遇到#开头的「注释」行则进入代码模式，@行则是一种特殊的代码模式，简化了最常见的元素定义代码行。
@@
@Monologue
    代码行长得像注释存粹是为了节目效果。
    （好吧，一个次要原因是@和#是可以在中文输入法下直接打出的为数不多的英文符号。）
    说起来，如果Python的ast模块给注释再多一点点尊重，也许我就不用这么大费周折了。
@@
@Paragraph
    也许这个方案象征着我的纯Python策略已经破产了。
    我已经走上了在自己的项目中包含一个
    @Emphasize
        ad hoc, informally-specified, bug-ridden, slow implementation of half of Common Lisp（划掉）Markdown
    @@
    的老路了。
    但起码以现在这个状况，我觉得还不至于。
@@
"""


def transpile(content):
    source = ["["]
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        if line == "@@":
            source.append("),")
        elif line.startswith("@"):
            source.append(line[1:] + "(")
        elif line.startswith("#"):
            source.append(line[2:])
        else:
            source.append(f'"{line}",')
    source.append("]")
    return "\n".join(source)


compiled_content = eval(transpile(content))
page = Page(title, date, compiled_content)
write_article_page("blogs-are-strings", page)
