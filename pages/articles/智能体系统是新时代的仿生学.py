from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 6, 2, tzinfo=ZoneInfo("Asia/Singapore"))
content = """
@Paragraph
    这一世代的仿生学是仿人学。
@@
@Paragraph
    这固然有其价值，但是同时意味着明显的上限。
    我们要遵循苦涩的教训，才能走得更远。
@@
"""
page = Page(title, date, eval(transpile(content)))
write_article_page("agents-are-neo-bionics", page)