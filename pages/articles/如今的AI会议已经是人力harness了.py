from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 5, 10, tzinfo=ZoneInfo("Asia/Singapore"))
page = Page(title, date, [])
write_article_page("human-harness", page)
