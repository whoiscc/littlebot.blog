from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from website.components import Emphasize, Monologue, Paragraph
from website.fs import write_page
from website.templates.article import PageStage


title = Path(__file__).stem
date = datetime(2026, 5, 18, tzinfo=ZoneInfo("Asia/Singapore"))
s = PageStage(title, date)
with Paragraph.of(s):
    s += "公交车是一种泄漏抽象（leaky abstraction）。"
    s += "坐上公交车的人各自有各自的精确目的地，但是被量化（quantize）到了公交站的颗粒度。"
    s += "我们可以允许乘客在上车之前预先在手机上设定他们实际的目的地，在上车时收集这一信息（比如利用刷手机支付的时机），并借助这个信息来优化公交车的运行方式。"
with Paragraph.of(s):
    s += "这种新的公交车最突出的特点就是", Emphasize("没有固定的站点"), "。"
    s += "同一编号的公交车沿着同一线路运行，但是根据车上乘客的情况动态调整停靠的地点。"
    s += "这可以带来的优化我目前想到了两个。"
    s += "一个是根据乘客的目的地来调整停靠的地点，从而减少乘客的步行距离，优化每个乘客的体验。"
    s += "二是将最终目的地接近（比如目前在相邻公交站下车）的乘客统一下车地点，从而减少公交车的停靠次数，优化整体的运行效率。"
    s += "可以看出这两个优化是互相矛盾的，而公交车就可以根据实际情况来进行权衡。"
with Paragraph.of(s):
    s += "这样的公交车面临的一大问题是如何上车。"
    s += "我们需要在乘客上车之前，指引他们前往接下来的停靠点。"
    s += "在产生这个问题的同时，这也带来了一个新的优化机会：将乘客均匀分布在同一线路的不同公交车上。"
    s += "在没有指引的情况下，乘客会登上最先到达的公交车。"
    s += "如果一辆车开慢了一点点，那么前方的公交站就会积累更多的乘客，更多乘客上车时就会让它更慢。"
    s += "如果我们的系统能够主动调控乘客上哪辆车，那么不但可以提升系统的吞吐量，甚至有可能反而提高每个乘客的出行效率。"
    s += "当然，这会让本来就很麻烦的向后兼容变得更麻烦了。"
with Monologue.of(s):
    s += "我的公交车3.0方案是具有独占路权的无人驾驶网约车，日后再写。"
write_page("articles/bus2.0/", s.context.render())
