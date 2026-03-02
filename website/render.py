def render(item, ctx=None):
    if isinstance(item, str):
        return item
    elif hasattr(item, "render_opts"):
        return item.render_opts(ctx)
    else:
        return item.render()
