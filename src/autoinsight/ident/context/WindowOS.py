import os
import signal
from typing import Dict, Iterable

import pyautogui
import wmi

from .OSBase import OSBase
from .WindowGUIApplication import WindowGUIApplication
from .ShellBase import ShellBase


class WindowOS(OSBase):

    def changeDriverState(self, driverInfo: str, isEnable: bool):
        pass

    def install(self, path: str):
        """Automatic install an application
        """
        pass

    def typeControlKeys(self, controlKeys: str):
        """Send simulated control keys

        Args:
            controlKeys (str): a string contain the control keys like {ENTER} etc.
        """
        pass

    def hotkeys(self, firstKey: str, secondKey: str, ThirdKey=None):
        pass

    def querySystemEvent(self, eventPattern: str, level):
        pass

    def restart(self, delaySeconds: int = 0):
        pass

    def sleep(self, delaySecond: int = 0):
        pass

    def hibernate(self, delaySecond: int = 0):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def setCurrent(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wmi = wmi.WMI()

    def launchApp(self, path: str, *args, **kwargs) -> WindowGUIApplication:
        return WindowGUIApplication.launch(*args, **kwargs)

    def launchShell(self, path, *args, **kwargs) -> ShellBase:
        pass

    def kill(self, processId: int = 0, processName: str = ""):
        if processId:
            os.kill(processId, signal.SIGKILL)

    def terminate(self, processId: int = 0, processName: str = ""):
        if processId:
            os.kill(processId, signal.SIGTERM)

    @property
    def userHome(self):
        return self.environ["USERPROFILE"]

    @property
    def environ(self) -> Dict:
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
        pass

    @property
    def disks(self) -> Iterable[str]:
        pass

    @property
    def SBIOS(self) -> str:
        pass

    @property
    def VBIOS(self) -> str:
        pass

    def updateDriver(self):
        pass

    def typeKeys(self, visibleKeys: Iterable[str], intervalSec: int = 0.25):
        """
        Simulate typing the visible characters
        """
        pyautogui.typewrite(visibleKeys)

    def combineKeys(self, firstKey, secondKey, ThirdKey=None):
        pass

    def snapshot(self):
        pass
