from subprocess import run


# Stamp any new/changed article before publishing it, so every deployed article
# carries a proof of existence. Idempotent: unchanged articles are skipped, and
# pending proofs are upgraded toward their Bitcoin attestation.
run("uv run timestamp.py", shell=True, check=True)
run("uv run build.py", shell=True, check=True)
run("npx wrangler pages deploy build", shell=True, check=True)