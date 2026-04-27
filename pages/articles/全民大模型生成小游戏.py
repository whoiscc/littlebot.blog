from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 4, 27, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    我们已经走过了全民大模型生成文字、图像、音视频的时代了。
    再下一步就是全民使用大模型端到端生成小游戏。
@@
@Paragraph
    相比前几步，生成小游戏的难点在于缺乏现有的社交平台。
    现有的小程序/小游戏平台都可以承接这个需求，就看谁会率先为此优化了。
@@
@Paragraph
    当然不可否认，从大模型生成文本到图像到音视频，实际的用户数和使用频率都是在逐步递减的。
    到了小游戏，每一个用户生成的内容要更多的用户共享消费。
    另一方面，也许如今主流的互联网平台是短视频而不是小游戏也正是由于创作门槛导致的。
    也许下一代的互联网平台就改成刷一下换一个小游戏了。
    起码是某种
    @Emphasize
        互动视频
    @@
    之类的吧。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page("user-generated-mini-games", page)
