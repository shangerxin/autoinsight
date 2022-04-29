from typing import Iterable
from abc import abstractmethod

from .ApplicationWindow import ApplicationWindow
from .ContextBase import ContextBase
from .NullContext import NullContext


class GUIApplicationBase(ContextBase):
    _windows = []
    _currentWindow = NullContext()

    @property
    def windows(self) -> Iterable[ApplicationWindow]:
        return self.windows

    @property
    def currentWindow(self):
        return self._currentWindow

    @abstractmethod
    def setCurrent(self):
        pass

    def close(self):
        pass
