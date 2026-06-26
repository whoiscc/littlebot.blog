from website.article_prelude import *

title = "无重MultiPaxos"
date = datetime(2026, 3, 25, tzinfo=ZoneInfo("Asia/Singapore"))
s = PageStage(title, date)
with Paragraph.of(s):
    with Hyperlink.of(s, "https://dl.acm.org/doi/pdf/10.1145/2673577"):
        s += "标准的MultiPaxos协议"
    s += "并不保证不同槽位提议的指令各不相同。"
    s += "而其他的复制协议，比如Raft和Viewstamped Replication，都很容易做到这一点。"
    s += "我在几年前仔细研究了无重MultiPaxos的可行性，并且最近又重新确认并实现了一遍。"
with Paragraph.of(s):
    s += "想要做到无重，要确保两件事。"
    s += "首先是同一个提议者不会在不同槽位提议同样的指令。"
    s += "实现这一点很直接，唯一要注意的是MultiPaxos不要求严格按照槽位递增提议，所以在提议一个指令之前要检查所有提议过的指令，而不是只检查提议的槽位之前的指令。"
    s += "其次便是在汇总来自大多数节点的接收提议（即p1b）时，如何处理不同槽位提议的指令相同的情况。"
    s += "换句话说，我们不仅要像MultiPaxos要求的那样以每个槽位为单位做去重，还要以提议的指令为单位做去重。"
    s += "在第一点保证的情况下，不同槽位的相同指令一定是由不同的提议者以不同的投票号（ballot number）提议的。"
    s += "此时我们可以安全地忽略投票号较小的提议，只将投票号最大的提议所选择的槽位赋予这个指令。"
    s += "论证安全性的思路和MultiPaxos以槽位为单位去重的情况是相似的。"
    s += "出现了不同槽位的投票号更高的提议，说明那些投票号更小的对这个指令的提议都没有成功扩散到大多数节点上，否则投票号更高的提议就会观测到它而不会以不同的槽位提议了。"
    s += SideNote("此处我们隐含地利用了最高投票号的提议者也采用了同一个去重机制的前提。")
    s += "至于是先以槽位为单位去重还是先以指令为单位去重，我认为不影响安全性，目前实现的是先以指令为单位。"
with Paragraph.of(s):
    s += "总的来说，对MultiPaxos做无重实践上并没有什么意义。"
    s += "只要保证了最基础的幂等性，客户端重发不会无条件地导致重复的提议，其实真正会产生重复指令的情况是非常罕见的了。"
    s += "这里提出的方案只是理论上的论证。"
write_article_page(Path(__file__).stem, s.context)
