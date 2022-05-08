from .TargetBase import TargetBase


class Text(TargetBase):
    def __init__(self, value="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass
