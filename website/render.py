def render(item, ctx=None):
    if isinstance(item, str):
        return item
    elif hasattr(item, "render_opts"):
        return item.render_opts(ctx)
    else:
        return item.render()


class RenderLines:
    def __init__(self, *items):
        self.items = items

    def __iter__(self):
        for item in self.items:
            if isinstance(item, str):
                yield item
            elif isinstance(item, RenderLines):
                for subitem in item:
                    yield "  " + subitem
            else:
                raise TypeError(f"Unsupported item type: {type(item)}")
