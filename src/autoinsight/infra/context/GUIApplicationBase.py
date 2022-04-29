from typing import Iterable
from abc import abstractmethod

from .ContextBase import ContextBase
from .NullContext import NullContext


class GUIApplicationBase(ContextBase):
    _windows = []
    _currentWindow = NullContext()

    @property
    def windows(self) -> Iterable[GUIApplicationBase]:
        return self.windows

    @propert
    def currentWindow(self):
        return self._currentWindow

    @abstractmethod
    def setCurrent(self):
        pass

    def close(self):
        pass
