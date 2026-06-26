from subprocess import run


# Stamp any new/changed article before publishing it, so every deployed article
# carries a proof of existence. Cheap: unchanged articles are skipped via a local
# hash check. Completing pending proofs (`timestamp.py upgrade`) is slow and not
# time-sensitive, so it's left out of the deploy path -- run it occasionally.
run("uv run timestamp.py stamp", shell=True, check=True)
run("uv run build.py", shell=True, check=True)
run("npx wrangler pages deploy build", shell=True, check=True)