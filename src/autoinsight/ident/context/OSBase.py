from abc import abstractmethod
from collections.abc import Sequence
from os import environ
from typing import Iterable, Mapping, Optional

from autoinsight.common.CustomTyping import AutomationInstance
from autoinsight.common.EnumTypes import ButtonTypes
from autoinsight.common.models.Point import Point
from .ContextBase import ContextBase
from .GUIApplicationBase import GUIApplicationBase
from .ProcessBase import ProcessBase
from .ShellBase import ShellBase


class OSBase(ContextBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._environ: Mapping[str] = environ

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
    def environ(self) -> Mapping[str, str]:
        """
        Return the system environment variable mapping
        """
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
    def SBIOS(self) -> str:
        pass

    @property
    def VBIOS(self) -> str:
        pass

    @property
    def drivers(self) -> Iterable[str]:
        """
        Return the hardware driver information
        """
        pass

    @abstractmethod
    def launchApp(self, path, isAsAdmin: bool = False) -> GUIApplicationBase:
        pass

    @abstractmethod
    def launchShell(self, isAsAdmin: bool = False, *args, **kwargs) -> ShellBase:
        pass

    @abstractmethod
    def kill(self, processId: int = 0, processName: str = ""):
        pass

    @abstractmethod
    def terminate(self, processId: int = 0, processName: str = ""):
        pass

    @abstractmethod
    def disks(self) -> Iterable[str]:
        """
        Return all the available hard drive partitions
        """
        pass

    @abstractmethod
    def changeDriverState(self, driverInfo: str, isEnable: bool):
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
    def select(self, start: Point, end: Point, button: ButtonTypes = ButtonTypes.Left):
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

    @abstractmethod
    def switchUser(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def find(self, query: str, *args, **kwargs) -> Optional[AutomationInstance]:
        if self._cms.currentContext != self:
            # TODO improve the find logic
            return self._cms.currentContext
