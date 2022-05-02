import os
import signal
from typing import Iterable, Mapping
from collections.abc import Sequence

import pyautogui
import wmi

from .OSBase import OSBase
from .WindowGUIApplication import WindowGUIApplication
from .ShellBase import ShellBase


class WindowOS(OSBase):
    def shutdown(self, delaySeconds: int = 0):
        delaySeconds: int = int(delaySeconds)
        os.system("shutdown /s /t %s" % delaySeconds)

    def holdAndTypeKeys(self, keys: Iterable[str], holdKeys: Sequence[str]):
        countOfControlKeys: int = len(holdKeys)
        if countOfControlKeys == 0:
            self.typeKeys(keys)
        elif countOfControlKeys == 1:
            with pyautogui.hold(holdKeys[0]):
                self.typeKeys(keys)
        elif countOfControlKeys == 2:
            with pyautogui.hold(holdKeys[0]):
                with pyautogui.hold(holdKeys[1]):
                    self.typeKeys(keys)
        elif countOfControlKeys == 3:
            with pyautogui.hold(holdKeys[0]):
                with pyautogui.hold(holdKeys[1]):
                    with pyautogui.hold(holdKeys[2]):
                        self.typeKeys(keys)

    def changeDriverState(self, driverInfo: str, isEnable: bool):
        pass

    def install(self, path: str):
        """Automatic install an application
        """
        pass

    def typeControlKeys(self, controlKeys: Iterable[str]):
        """Send simulated control keys

        Args:
            controlKeys (str): a string contain the control keys like {ENTER} etc.
        """
        pyautogui.write(controlKeys)

    def hotkeys(self, *keys):
        pyautogui.hotkey(*keys)

    def querySystemEvent(self, eventPattern: str, level):
        pass

    def restart(self, delaySeconds: int = 0):
        delaySeconds: int = int(delaySeconds)
        os.system("shutdown /s /r /t %s" % delaySeconds)

    def sleep(self, delaySeconds: int = 0):
        delaySeconds: int = int(delaySeconds)

    def hibernate(self, delaySeconds: int = 0):
        delaySeconds: int = int(delaySeconds)
        os.system("shutdown /s /hybrid /t %s" % delaySeconds)

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
        pyautogui.write(visibleKeys, interval=intervalSec)

    def snapshot(self):
        pass
