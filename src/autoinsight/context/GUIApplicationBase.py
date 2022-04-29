from typing import Iterable
from abc import abstractmethod

from .ApplicationWindow import ApplicationWindow
from .ProcessBase import ProcessBase


class GUIApplicationBase(ProcessBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._windows: Iterable[ApplicationWindow] = []
        self._currentWindow: ApplicationWindow = None

    @property
    def windows(self) -> Iterable[ApplicationWindow]:
        return self.windows

    @property
    def currentWindow(self):
        return self._currentWindow

    @abstractmethod
    def focus(self):
        pass
