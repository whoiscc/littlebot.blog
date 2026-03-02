from pathlib import Path


BUILD_DIR = Path("build")
BUILD_DIR.mkdir(exist_ok=True)

with open(BUILD_DIR / ".gitignore", "w") as f:
    f.write("*")
with open(BUILD_DIR / "index.html", "w") as f:
    f.write(
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web App</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to My Web App</h1>
    <p>This is a simple web application built with Python.</p>
    <script src="app.js"></script>
</body>
</html>"""
    )
with open(BUILD_DIR / "styles.css", "w") as f:
    f.write(
        """body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
}
h1 {
    color: #333;
}
p {
    color: #666;
}"""
    )
with open(BUILD_DIR / "app.js", "w") as f:
    f.write("""console.log("Hello, World! This is my web app.");""")
