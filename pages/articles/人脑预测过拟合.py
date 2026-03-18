from zoneinfo import ZoneInfo

from website.components import Paragraph, SideNote
from website.fs import write_page, write_sitemap_entry
from website.templates.article import Page
from datetime import datetime


title = "人脑预测过拟合"
date = datetime(2026, 3, 4, tzinfo=ZoneInfo("Asia/Singapore"))
body = [
    Paragraph(
        "我们生在一个好时代，每天有各种各样的事情可以预测。",
        SideNote("就像我这个博客就是我各种各样的预测。"),
    ),
    Paragraph(
        "之所以说这是好的，是因为人脑就是个预测模型。在这一点上和基于机器学习的预测模型并无什么两样。",
    ),
    Paragraph("预测模型要有训练集。不同时代给人脑提供的训练集是完全不同的。"),
    Paragraph(
        "由此我们可以知道，相比当下，那些更稳定的时代的人脑会更加过拟合到那时一成不变的训练集上面去，从而那时候的人脑的泛化能力会更差，鲁棒性更差。"
    ),
    Paragraph("所以我们可以知道，现在的人是更加稳定的预测模型了。"),
]
page = Page(title, date, body)
write_page("articles/brain-prediction-overfitting", page.render())
write_sitemap_entry("articles/brain-prediction-overfitting", page.lastmod())
