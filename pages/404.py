from website.fs import write_page
from website.render import RenderLines


write_page("404.html", RenderLines("undefined"))
