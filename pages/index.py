from website.templates.base import Page
from website.config import BUILD_DIR

content = """<h1>Welcome to My Web App</h1>
<p>This is a simple web application built with Python.</p>
"""
page = Page("My Web App", content)
with open(f"{BUILD_DIR}/index.html", "w") as f:
    f.write(page.render())
