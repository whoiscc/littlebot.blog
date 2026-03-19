from website.article_prelude import *

title = Path(__file__).stem
date = datetime(2026, 5, 19, tzinfo=ZoneInfo("Asia/Singapore"))
s = PageStage(title, date)
with Paragraph.of(s):
    s += "和牛，烤鸭，鹅肝，韩式烤猪大肠。"
write_article_page("four-delicacies", s.context)
