import os
import platform
import signal
from collections.abc import Sequence
from time import sleep
from typing import Iterable, Mapping, Optional

import pyautogui
from wmi import WMI, _wmi_object

from autoinsight.common.EnumTypes import ButtonTypes
from autoinsight.common.models.Point import Point
from autoinsight.services.KnowledgeServiceBase import KnowledgeServiceBase
from autoinsight.services.WindowKnowledgeService import WindowKnowledgeService
from .Command import Command
from .OSBase import OSBase
from .PowerShell import PowerShell
from .ProcessBase import ProcessBase
from .WindowGUIApplication import WindowGUIApplication


class WindowOS(OSBase):
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._wmi: _wmi_object = self._ioc.getService(WMI)
        self._ks: WindowKnowledgeService = self._ioc.getService(KnowledgeServiceBase)

    def __repr__(self):
        if not self._repr:
            self._repr = f"{self.__str__()} id:{self.id} {self.version}"
        return self._repr

    def __str__(self):
        if not self._str:
            self._str = "Window OS Context"
        return self._str

    @property
    def processes(self) -> Iterable[ProcessBase]:
        pass

    @property
    def desktop(self):
        pass

    @property
    def ks(self) -> WindowKnowledgeService:
        return self._ks

    @property
    def wmi(self) -> _wmi_object:
        return self._wmi

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
        return f"{platform.system()} {platform.version()} {platform.release()} {platform.win32_edition()}"

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

    @property
    def services(self):
        pass

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

    def changeServiceState(self, serviceInfo: str, isEnable: bool):
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

    def launchApp(self, cmdline: str, isAsAdmin: bool = False, *args, **kwargs) -> WindowGUIApplication:
        instance = self.ks.recognize(cmdline)
        if instance:
            return WindowGUIApplication(automationInstance=instance)
        else:
            return WindowGUIApplication(cmdline=cmdline, *args, **kwargs)

    def launchShell(self, isAsAdmin: bool = False, *args, **kwargs) -> Optional[Command]:
        return Command(*args, **kwargs)

    def launchPowershell(self, *args, **kwargs) -> Optional[PowerShell]:
        return PowerShell(*args, **kwargs)

    def launchFromStartMenu(self, appName: str, appQuery: str, *args, **kwargs) -> Optional[WindowGUIApplication]:
        pass

    def kill(self, processId: int = 0, processName: str = ""):
        if processId:
            os.kill(processId, signal.SIGKILL)

    def terminate(self, processId: int = 0, processName: str = ""):
        if processId:
            os.kill(processId, signal.SIGTERM)

    def updateDriver(self):
        pass

    def typeKeys(self, visibleKeys: Iterable[str], intervalSec: int = 0.25):
        """
        Simulate typing the visible characters
        """
        pyautogui.write(visibleKeys, interval=intervalSec)

    def snapshot(self):
        pass

    def select(self, start: Point, end: Point, button: ButtonTypes = ButtonTypes.Left):
        pyautogui.mouseDown(x=start.x, y=start.y, button=button.str)
        pyautogui.mouseUp(x=end.x, y=end.y, button=button.str)

    def wait(self, timeoutSeconds: int = 0):
        sleep(timeoutSeconds)

    def switchUser(self):
        pass

    def logout(self):
        pass

    def waitForWindow(self, query: str) -> WindowGUIApplication:
        pass
