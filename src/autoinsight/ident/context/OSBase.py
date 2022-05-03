from os import environ
from typing import Iterable, Mapping
from abc import abstractmethod
from collections.abc import Sequence

from .ContextBase import ContextBase
from .GUIApplicationBase import GUIApplicationBase
from .ShellBase import ShellBase
from .ProcessBase import ProcessBase


class OSBase(ContextBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._environ: Mapping[str] = environ

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

    @property
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
    def environ(self) -> Mapping[str, str]:
        return self._environ

    @property
    def monitors(self):
        pass

    @property
    def systeminfo(self) -> str:
        pass

    @property
    def version(self) -> str:
        pass

    @property
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

    @property
    def SBIOS(self) -> str:
        pass

    @property
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
    def typeControlKeys(self, controlKeys: Iterable[str]):
        pass

    @abstractmethod
    def hotkeys(self, *keys):
        pass

    @abstractmethod
    def holdAndTypeKeys(self, keys: Iterable[str], holdKeys: Sequence[str]):
        """
        Hold the control keys specified in holdKeys and press the keys.
        """
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
    def sleep(self, delaySeconds: int = 0):
        pass

    @abstractmethod
    def hibernate(self, delaySeconds: int = 0):
        pass

    @abstractmethod
    def shutdown(self, delaySeconds: int = 0):
        pass
