from .TargetBase import TargetBase


class Text(TargetBase):
    @property
    def value(self):
        return self._value
