from website.article_prelude import *

title = "如今的AI会议已经是人力harness了"
date = datetime(2026, 5, 10, tzinfo=ZoneInfo("Asia/Singapore"))
page = Page(title, date, [])
write_article_page(Path(__file__).stem, page)
