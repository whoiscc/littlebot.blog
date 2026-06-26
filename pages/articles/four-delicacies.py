from website.article_prelude import *

title = "以高油脂为核心的四大美食"
date = datetime(2026, 3, 19, tzinfo=ZoneInfo("Asia/Singapore"))
s = PageStage(title, date)
with Paragraph.of(s):
    s += "和牛，烤鸭，鹅肝，韩式烤猪大肠。"
write_article_page(Path(__file__).stem, s.context)
