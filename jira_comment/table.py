from .base import JiraBase
from .utils import render


class Row(JiraBase):
    def __init__(self, *columns):
        self.columns = list(columns)

    def render(self) -> str:
        inner = "|".join([render(c) for c in self.columns])
        return f"|{inner}|"


class HeadRow(Row):
    def render(self) -> str:
        inner = "||".join([render(c) for c in self.columns])
        return f"||{inner}||"


class Table(JiraBase):
    def __init__(self, *rows):
        self.rows = list(rows)

    def append(self, *columns):
        self.rows.append(Row(*columns))

    def render(self) -> str:
        inner = "\n".join([render(r) for r in self.rows])
        return f"\n{inner}\n"