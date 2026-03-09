from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from website.components import Paragraph, Emphasize, SideNote
from website.fs import write_page
from website.templates.article import PageStage

title = Path(__file__).stem
date = datetime(2026, 3, 9, tzinfo=ZoneInfo("Asia/Singapore"))
s = PageStage(title, date)
with Paragraph.of(s):
    s += "AI论文已经很多了。"
    s += "随着大模型写论文的能力赶超平均人类，", Emphasize("AIAI论文"), "的加入会让其数目增长至无穷无尽。"
    s += "这会比指数级增长还可怕；指数级增长好歹还算是有个预测模型。"
with Paragraph.of(s):
    s += "这意味着真正的通胀。"
    s += "在此之前，有限的人类把有限的总精力稀释到更多的论文中去，产出平均含金量更低的论文，这更像是降本增效。"
    s += SideNote("总人数的增加确实导致总精力也有上升，但是和总需求的增长大致打平。")
    s += "而现在，大模型直接引入了无穷无尽的精力。"
    s += "论文通胀真的要到来了。"
with Paragraph.of(s):
    s += "那么可以预见的「论文当糊墙纸」的时代到来又过去以后，新的AI论文的价值锚定会是什么呢？"
    s += "我认为会回归工业界的应用。"
    s += "会议和同行评审只能验证论文的置信度，换句话说只能验钞，但是不能控制增发。"
    s += "未来会真的出现非常多完全具有科研价值的工作，但是却完全没有在工业界落地而造福人类的可能，单纯是因为它们的数量太多了。"
    s += "在这种情况下，工业界会越俎代庖，成为AI论文含金量的生产者/担保者而不再是消费者。"
    s += "一篇论文收到关注和尊敬的程度完全由它在工业界带来的影响决定，是否发表在会议上（过）并无关系。"
    s += "这被评论为「变成系统领域了」，但是我觉得更像是半导体领域。"
write_page("articles/paper-inflation", s.context.render())
