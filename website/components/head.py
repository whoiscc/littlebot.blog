class Head:
    def __init__(self, title):
        self.title = title

    def render(self):
        return f"""<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <link rel="stylesheet" href="main.css">
</head>"""