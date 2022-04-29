from os import environ
from typing import Dict, Iterable
from abc import abstractmethod, abstractproperty

from .ContextBase import ContextBase
from .GUIApplicationBase import GUIApplicationBase


class OSBase(ContextBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._environ = environ

    @abstractmethod
    def launchApp(self, path) -> GUIApplicationBase:
        pass

    @abstractmethod
    def launchShell(self, path) -> ShellBase:
        pass

    @abstractmethod
    def kill(self, processId: int, processName: str):
        pass

    @abstractmethod
    def terminate(self, processId: int, processName: str):
        pass

    @abstractproperty
    def userHome(self):
        pass

    @property
    def processes(self):
        pass

    @property
    def desktops(self):
        pass

    @property
    def currentDesktop(self):
        pass

    @property
    def environ(self) -> Dict:
        return self._environ

    @abstractproperty
    def displays(self):
        pass

    @abstractproperty
    def systeminfo(self) -> str:
        pass

    @abstractproperty
    def version(self) -> str:
        pass

    @abstractproperty
    def drivers(self) -> Iterable[str]:
        pass

    @abstractproperty
    def SBIOS(self) -> str:
        pass

    @abstractproperty
    def VBIOS(self) -> str:
        pass

    @abstractmethod
    def updateDriver(self):
        pass

    @abstractmethod
    def type(self, visibleKeys: Iterable[str], intervalSec: int = 0.25):
        """
        Simulate typing the visible characters
        """
        pass

    @abstractmethod
    def combineKeys(self, firstKey, secondKey, ThirdKey=None):
        pass

    @abstractmethod
    def snapshot(self):
        pass
