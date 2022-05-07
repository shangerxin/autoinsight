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

    def click(self):
        pass

    def rightClick(self):
        pass

    def doubleRightClick(self):
        pass

    def doubleClick(self):
        pass

    def drag(self):
        pass

    def drop(self):
        pass

    def isVisible(self) -> bool:
        pass

    def isEnable(self) -> bool:
        pass

    def highlight(self):
        pass

    def mouseHover(self):
        pass

    def scrollIntoView(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def snapshot(self):
        pass
