from subprocess import run


run("npx wrangler pages deploy build", shell=True, check=True)