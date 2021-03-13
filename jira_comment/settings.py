from abc import ABC, abstractmethod
from pathlib import Path


class Option(ABC):
    def __init__(self, initial_value):
        self.initial_value = initial_value
        self.values_stack = []

    @abstractmethod
    def check_type(self, value):
        pass

    @property
    def value(self):
        if self.values_stack:
            return self.values_stack[-1]
        return self.initial_value

    def push(self, new_value):
        self.values_stack.append(self.check_type(new_value))

    def pop(self):
        if self.values_stack:
            return self.values_stack.pop()
        return self.initial_value

    def reset(self):
        self.values_stack = []


class PathOption(Option):
    def check_type(self, value):
        return Path(value)


class FloatFormat(Option):
    def check_type(self, value):
        return str(value)


class Settings:
    def __init__(self):
        self._image_directory = PathOption(Path("./images"))
        self._float_format = FloatFormat(".4f")

    @property
    def image_directory(self):
        return self._image_directory.value

    def push_image_directory(self, new_value):
        self._image_directory.push(new_value)

    def pop_image_directory(self):
        return self._image_directory.pop()

    def reset_image_directory(self):
        self._image_directory.reset()

    @property
    def float_format(self):
        return self._float_format.value

    def push_float_format(self, new_value):
        self._float_format.push(new_value)

    def pop_float_format(self):
        return self._float_format.pop()

    def reset_float_format(self):
        self._float_format.reset()


settings = Settings()
