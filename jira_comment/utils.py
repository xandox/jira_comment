from .base import JiraBase

def render(element):
    if isinstance(element, JiraBase):
        return element.render()
    elif isinstance(element, str):
        return element
    else:
        raise ValueError(f"Do not know how to render: {element!r}")