from abc import ABC, abstractmethod


class JiraBase(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

    def __str__(self):
        return self.render()