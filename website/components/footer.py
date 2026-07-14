"""Per-article footer: source link + (when available) OpenTimestamps proof.

The footer discovers the article's own source file by walking the call stack for
the `pages/articles/*.py` frame that is rendering it -- every article calls
`.render()` from its own module, whether it went through `write_article_page` or a
bare `write_page`. That running file is the single source of truth: the source
link and the `.ots` proof both derive from it, so a custom output slug can never
point them at the wrong file, and no slug has to be threaded through.

The proof sentence only appears when the article's `.ots` file is present in the
build tree -- true on the deploy branch (which carries the proofs), false on a
local main checkout. The displayed hash is the SHA256 of the source `.py`, exactly
the digest the proof certifies. The "时间戳" link points at the full, durable proof
on deploy; the verify link inlines a minimal self-contained proof (see
website.proof) so the URL stays small. The Bitcoin block height is read straight
out of the proof -- no network lookup, no stored timestamp.
"""

import sys
from hashlib import sha256
from pathlib import Path

from website.proof import summarize

REPO = "https://github.com/whoiscc/littlebot.blog"
ARTICLE_SRC_DIR = Path("pages/articles")
OTS_SITE = "https://opentimestamps.org/"


def _article_source() -> Path:
    """The `pages/articles/*.py` file currently being rendered, from the stack."""
    frame = sys._getframe()
    while frame is not None:
        module_file = frame.f_globals.get("__file__")
        if module_file and Path(module_file).match("pages/articles/*.py"):
            return Path(module_file)
        frame = frame.f_back
    raise RuntimeError("article_footer: no pages/articles/*.py frame on the stack")


def article_footer() -> str:
    source = ARTICLE_SRC_DIR / _article_source().name  # repo-relative, real file
    source_url = f"{REPO}/blob/main/{source.as_posix()}"

    lines = [
        """<footer class="article-footer">""",
        f"""<p>本页面生成自<a href="{source_url}">源码</a>，"""
        f"""欢迎创建 <a href="{REPO}/issues">issue</a> / """
        f"""<a href="{REPO}/pulls">PR</a> 进行讨论。</p>""",
    ]

    ots = source.with_name(source.name + ".ots")  # X.py -> X.py.ots
    if ots.exists():
        file_hash = sha256(source.read_bytes()).hexdigest()
        proof = summarize(ots.read_bytes())
        ots_url = f"{REPO}/blob/deploy/{ots.as_posix()}"
        verify_url = (
            f"{OTS_SITE}?digest={file_hash}&algorithm=SHA256&ots={proof.ots_hex}"
        )
        anchor = (
            f"""记录于比特币区块 #{proof.height}"""
            if proof.height is not None
            else """等待比特币确认"""
        )
        lines.append(
            f"""<p>源码文件哈希值 <code>{file_hash}</code> 借助 """
            f"""<a href="{OTS_SITE}">OpenTimestamps</a> 取得"""
            f"""<a href="{ots_url}">时间戳</a>，{anchor}。"""
            f"""<a href="{verify_url}">在线验证</a>。</p>"""
        )

    lines.append("""</footer>""")
    return "\n".join(lines)
