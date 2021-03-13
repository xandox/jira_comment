from .base import JiraBase
from .float import is_float_value, FloatValue


def render(element):
    if isinstance(element, JiraBase):
        return element.render()
    elif isinstance(element, str):
        return element
    elif is_float_value(element):
        return FloatValue(element).render()
    else:
        raise ValueError(f"Do not know how to render: {element!r}")