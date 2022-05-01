from os import environ
from typing import Dict, Iterable
from abc import abstractmethod, abstractproperty

from .ContextBase import ContextBase
from .GUIApplicationBase import GUIApplicationBase
from .ShellBase import ShellBase
from .ProcessBase import ProcessBase


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
    def kill(self, processId: int = 0, processName: str = ""):
        pass

    @abstractmethod
    def terminate(self, processId: int = 0, processName: str = ""):
        pass

    @abstractproperty
    def userHome(self):
        pass

    @property
    def processes(self) -> Iterable[ProcessBase]:
        pass

    @property
    def desktop(self):
        """
        Display desktop and minimize all the other application
        """
        pass

    @property
    def currentDesktop(self):
        pass

    @property
    def environ(self) -> Dict:
        return self._environ

    @abstractproperty
    def monitors(self):
        pass

    @abstractproperty
    def systeminfo(self) -> str:
        pass

    @abstractproperty
    def version(self) -> str:
        pass

    @abstractproperty
    def drivers(self) -> Iterable[str]:
        """
        Return the hardware driver information
        """
        pass

    @abstractmethod
    def disks(self) -> Iterable[str]:
        """
        Return all the avaliable harddrive partitions
        """
        pass

    @abstractmethod
    def changeDriverState(self, driverInfo: str, isEnable: bool):
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
    def install(self, path: str):
        """
        Automatic an application
        """
        pass

    @abstractmethod
    def typeKeys(self, visibleKeys: Iterable[str], intervalSec: int = 0.25):
        """
        Simulate typing the visible characters
        """
        pass

    @abstractmethod
    def typeControlKeys(self, controlKeys: str):
        pass

    @abstractmethod
    def hotkeys(self, firstKey: str, secondKey: str, ThirdKey=None):
        pass

    @abstractmethod
    def snapshot(self):
        pass

    @abstractmethod
    def querySystemEvent(self, eventPattern: str, level):
        pass

    @abstractmethod
    def restart(self, delaySeconds: int = 0):
        pass

    @abstractmethod
    def sleep(self, delaySecond: int = 0):
        pass

    @abstractmethod
    def hibernate(self, delaySecond: int = 0):
        pass
