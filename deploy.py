from subprocess import run


# Stamp/upgrade article proofs before publishing: each article is stamped if new,
# restamped if changed, upgraded toward its Bitcoin attestation if still pending,
# else skipped. Cheap on every deploy -- the only network calls are for genuinely
# changed articles and the handful of proofs still pending (anchored ones are
# skipped via a local check).
run("uv run timestamp.py", shell=True, check=True)
run("uv run build.py", shell=True, check=True)
run("npx wrangler pages deploy build", shell=True, check=True)