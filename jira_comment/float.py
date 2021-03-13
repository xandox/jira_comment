from .base import JiraBase
from .settings import settings

FLOAT_TYPES = [float]

try:
    import numpy

    FLOAT_TYPES.append(numpy.floating)
except ModuleNotFoundError:
    pass


class FloatValue(JiraBase):
    def __init__(self, value, float_foramt=None):
        self.value = value
        if float_foramt:
            self.float_foramt = float_foramt
        else:
            self.float_foramt = settings.float_format

    def render(self):
        fmt_str = f"{{:{self.float_foramt}}}"
        return fmt_str.format(self.value)


def is_float_value(v):
    return isinstance(v, tuple(FLOAT_TYPES))