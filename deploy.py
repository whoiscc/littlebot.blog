from subprocess import run


run("uv run build.py", shell=True, check=True)
run("npx wrangler pages deploy build", shell=True, check=True)