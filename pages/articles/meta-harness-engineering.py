from website.article_prelude import *

title = "元Harness工程"
date = datetime(2026, 4, 25, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Monologue
    对于harness engineering的翻译目前还没有合适的。
    当然，「元」（meta）这个翻译也不怎么样就是了。
@@
@Paragraph
    一开始人们叫嚣着苦涩的教训，把精心设计的自然语言处理管线替换成了大模型。
@@
@Paragraph
    然后人们又叫嚣着苦涩的教训，把精心设计的大模型训练管线替换成了提示词工程。
@@
@Paragraph
    后来人们又叫嚣着苦涩的教训，把精心设计的提示词工程替换成了harness工程。
@@
@Paragraph
    最近Claude Code被大量指责严重降智。有报道说是因为harness中的三个bug共同导致的。
    叫嚣了那么久，现在又在精心设计复杂而容易出错的harness上越走越远，真的有在吸取教训了吗。
@@
@Paragraph
    大模型就像操作系统，人类编写的代码就像引导程序。
    引导程序应当以最小的代码量完成最简单的工作，将一个最小化的可供操作系统运行的环境搭建起来就立刻移交给操作系统。
    任何可以由操作系统完成的工作都应该交给操作系统。
    在代理（agent）系统中，任何可以由大模型自行编写的代码都不应该由人类编写在harness中。
    人类应该提供一个最小化的harness，引导大模型把解决任务所需的工作流自行编写出来。
    换言之，人类所编写的harness不应该是用来直接完成任务的，而是用来创建真正用来完成任务的harness的。
    相比起让编写的harness拟合到最终的编程或是其他种类任务的特性上去，应该让编写的harness拟合到创建和改进harness这个任务上去。
    这个
    @Emphasize
        元
    @@
    harness可以指导大模型创建出一个初步的harness来解决某种任务，然后再指导大模型改进这个harness来更好地解决这个任务。
    最终，元harness将会有能力指导大模型改进它本身，带领我们离AGI更进一步。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page(Path(__file__).stem, page)
