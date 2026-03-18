from datetime import datetime
from zoneinfo import ZoneInfo

from website.components import Paragraph, Emphasize
from website.fs import write_page, write_sitemap_entry
from website.templates.article import PageStage


title = "预期寿命与市场微观结构"
date = datetime(2026, 3, 8, tzinfo=ZoneInfo("Asia/Singapore"))
s = PageStage(title, date)
with Paragraph.of(s):
    s += "交易策略对于盈利的需求受限于交易者的预期寿命。"
with Paragraph.of(s):
    s += "就像知乎常说的，人人都知道复利指数增长的威力，但是这并不会让大多数人去实践，因为他们并不想清贫几十年以后获得花不动的钱。"
with Paragraph.of(s):
    s += "我不反对这个世界上一定有愚公。"
    s += "但是对于绝大部分投资策略，即便是强调复利的，强调价值投资的，它们也必然要在十年之内取得几乎", Emphasize("全部"), "预期收益。"
    s += "这一方面是市场的演进会导致策略失效，另一方面就是因为人生中十年的个数是很少的。"
    s += "这并不是在讲这十年被套牢在这个策略中损失机会成本的老生常谈；我们就假定十年以后这个策略能带来的收益比在这十年里实践任何其他策略都要高得多了。"
    s += "我们仅仅是在讨论一个人在他二十多岁的时候拿这笔钱去消费和三十多岁的区别。"
    s += "有些消费的机会，或者说享受这些消费的机会，在人生中再也不会出现了。"
with Paragraph.of(s):
    s += "因此，就像市场容量对于策略规模的限制，人类的预期寿命也对策略的周期产生了限制，二者是在空间和时间上的对应关系。"
    s += "进一步地，一个市场中交易者策略的周期，就会对这个市场的微观结构产生影响。"
    s += "比如说，人们会如何划定止损点？"
    s += "策略周期对止损点产生影响，导致同一市场情况下处罚止损的情况产生差异，进而导致市场微观结构的差异。"
with Paragraph.of(s):
    s += "如果长生方面的技术取得了突破，那么市场的微观结构会发生很大的变化。"
    s += "一个由可以活成千上万年的人所组成的市场，它每天的交易情况会如何？它还会每天交易吗？"
    s += "我认为是会的，因为生产周期并没有随着预期寿命的增加而增加。"
    s += "但是它的交易情况会和现在完全不一样了。"

write_page("articles/expected-lifetime-market-microstructure", s.context.render())
write_sitemap_entry("articles/expected-lifetime-market-microstructure", s.context.lastmod())
