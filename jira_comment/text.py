from .base import JiraBase
from .utils import render


class Text(JiraBase):
    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text


class Modifier(Text):
    def __init__(self, modifier, text):
        super().__init__(f"{modifier} {text}")

class H1(Modifier):
    def __init__(self, text):
        super().__init__("h1.", text)

class H2(Modifier):
    def __init__(self, text):
        super().__init__("h2.", text)

class H3(Modifier):
    def __init__(self, text):
        super().__init__("h2.", text)

class Paragraph(Text):
    def __init__(self, *content):
        self.content = list(content)

    def render(self) -> str:
        inner = "\n".join([render(c) for c in self.content])
        return f"{inner}\n\n"