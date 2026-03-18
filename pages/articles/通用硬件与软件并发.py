from zoneinfo import ZoneInfo

from website.components import Paragraph, SideNote, Emphasize, Monologue
from website.fs import write_page, write_sitemap_entry
from website.templates.article import Page
from datetime import datetime


title = "通用硬件与软件并发"
date = datetime(2026, 3, 2, tzinfo=ZoneInfo("Asia/Singapore"))
body = [
    Paragraph("软件之所以需要处理并发，完全是因为它运行在", Emphasize("通用"), "硬件上。"),
    Paragraph("设想一个微服务系统。系统中一共有三台机器承接同一个服务，每台机器最高处理1000个并发请求。可以发现系统中存在两个层级。如果要把某一时刻正在处理的请求进行标号，那么这个标号应该是「机器序号-请求序号」这样的形式。"),
    Paragraph(
        "为什么机器层面引入并发性以后，软件层面也必须引入并发性呢？正是因为软件正运行在通用机器上面。如果是专门为这个服务设计的定制硬件，那么很可能所有的并发、调度这些细节就都可以对软件屏蔽掉了。在这个例子中，一个硬件单元的处理能力超出了一个软件单元的需求，所以软件必须自己做一层并发来充分利用硬件资源。反过来也是显然：如果一个硬件单元的处理能力不足以满足一个软件单元的需求，那么软件也必须自己做一层并发",
        SideNote("注意这里是异构并发。这里我们把异构和同构并发合在一起分析。"),
        "来把这个软件单元分布到多个硬件单元上去。",
        SideNote("这一整段话基本都是Copilot补全出来的，感觉它已经学会了怎么写技术博客了（这句话也是）。"),
        SideNote("从这里我让它先歇个五分钟。"),
    ),
    Paragraph("历史上面，新型硬件被开发起来的契机，基本都伴随着并发范式的改变。最主流的例子当然是显卡：这些任务的软件单元对于CPU硬件单元来说实在太小了，在CPU上处理这些任务的效率太低，所以开发了内建大量并发的、针对更小软件单元的新硬件。反过来用来解决软件单元过大的问题的例子一定也可以举出来，就不赘述了。"),
    Paragraph("制作新硬件的成本正在持续下降。已经有人提出要为每一款大模型权重制作专门的硬件了。由此我们可以推测出，未来的硬件将会精确契合每一种软件单元，从而消除一切软件需要软件自身处理并发的场景。也许是某种极致的软硬件协同设计，也许是什么别的更超乎我想象的。"),
    Monologue("是时候从分布式转行了。"),
]
page = Page(title, date, body)
write_page("articles/common-hardware-software-concurrency", page.render())
write_sitemap_entry("articles/common-hardware-software-concurrency", page.lastmod())
