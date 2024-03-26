import os
import platform
import signal
from collections.abc import Sequence
from subprocess import Popen
from typing import Iterable, Mapping, Optional

import pyautogui
from pywinauto import WindowSpecification
from wmi import WMI, _wmi_object

from .Command import Command
from .OSBase import OSBase
from .PowerShell import PowerShell
from .ProcessBase import ProcessBase
from .WindowGUIContextBase import WindowGUIContextBase
from .WindowGUIApplication import WindowGUIApplication
from autoinsight.common.EnumTypes import ButtonTypes
from autoinsight.common.models.Point import Point
from autoinsight.services.KnowledgeServiceBase import KnowledgeServiceBase
from autoinsight.services.WindowKnowledgeService import WindowKnowledgeService
from autoinsight.decorator.Log import log, Log
from autoinsight.decorator.Step import step
from autoinsight.common.CustomTyping import AutomationInstance


class WindowOS(OSBase, WindowGUIContextBase):
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
    def description(self) -> str:
        return self.version

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

    @log
    @step
    def shutdown(self, delaySeconds: int = 0):
        delaySeconds: int = int(delaySeconds)
        os.system("shutdown /s /t %s" % delaySeconds)

    @log
    @step
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

    @log
    @step
    def changeDriverState(self, driverInfo: str, isEnable: bool):
        pass

    @log
    @step
    def changeServiceState(self, serviceInfo: str, isEnable: bool):
        pass

    @log
    @step
    def install(self, path: str):
        """Automatic install an application
        """
        pass

    @log
    @step
    def typeControlKeys(self, controlKeys: Iterable[str]):
        """Send simulated control keys

        Args:
            controlKeys (str): a string contain the control keys like {ENTER} etc.
        """
        pyautogui.write(controlKeys)

    @log
    @step
    def hotkeys(self, *keys):
        pyautogui.hotkey(*keys)

    @log
    @step
    def querySystemEvent(self, eventPattern: str, level):
        pass

    @log
    @step
    def restart(self, delaySeconds: int = 0):
        delaySeconds: int = int(delaySeconds)
        os.system("shutdown /s /r /t %s" % delaySeconds)

    @log
    @step
    def sleep(self):
        os.system("POWERCFG /HIBERNATE OFF")
        os.system("RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0")

    @log
    @step
    def hibernate(self):
        os.system("POWERCFG /HIBERNATE ON")
        os.system("shutdown /s /hybrid")

    # TODO: Refactor the knowledge into the WindowGUIApplication initialization parameters
    @log
    @step
    def launchApp(self, cmdline: str, isAsAdmin: bool = False, *args, **kwargs) -> WindowGUIApplication:
        instance = self.ks.recognize(cmdline)
        Log.logger.info("Launch application %s as admin %s", cmdline, isAsAdmin)
        if instance:
            return WindowGUIApplication(automationInstance=instance)
        else:
            return WindowGUIApplication(cmdline=cmdline, *args, **kwargs)

    @log
    @step
    def launchShell(self, cmds: Iterable[str], isAsAdmin: bool = False, *args, **kwargs) -> Optional[Command]:
        Log.logger.info("Launch shell %s as admin %s", cmds, isAsAdmin)
        return Command(cmds, isAsAdmin, *args, **kwargs)

    @log
    @step
    def launchShellWaitWindow(self, cmds: Sequence[str], windowQuery: str, isAsAdmin: bool = False, *args, **kwargs):
        Log.logger.info("Launch shell and wait window %s as admin %s", cmds, isAsAdmin)
        return self.waitForWindow(windowQuery, Popen(cmds))

    @log
    @step
    def launchPowershell(self, *args, **kwargs) -> Optional[PowerShell]:
        return PowerShell(*args, **kwargs)

    @log
    @step
    def launchFromStartMenu(self, appName: str, appQuery: str, *args, **kwargs) -> Optional[WindowGUIApplication]:
        pass

    @log
    @step
    def kill(self, processId: int = 0, processName: str = ""):
        if processId:
            os.kill(processId, signal.SIGKILL)

    @log
    @step
    def terminate(self, processId: int = 0, processName: str = ""):
        if processId:
            os.kill(processId, signal.SIGTERM)

    @log
    @step
    def updateDriver(self):
        pass

    @log
    @step
    def typeKeys(self, visibleKeys: Iterable[str], intervalSec: int = 0.25):
        """
        Simulate typing the visible characters
        """
        pyautogui.write(visibleKeys, interval=intervalSec)

    @log
    @step
    def snapshot(self):
        pass

    @log
    @step
    def select(self, start: Point, end: Point, button: ButtonTypes = ButtonTypes.Left):
        pyautogui.mouseDown(x=start.x, y=start.y, button=button.str)
        pyautogui.mouseUp(x=end.x, y=end.y, button=button.str)

    @log
    @step
    def switchUser(self):
        pass

    @log
    @step
    def logout(self):
        pass

    @log
    @step
    def waitForWindow(self, query: str, processHandle: Optional[Popen] = None) -> WindowGUIApplication:
        window: AutomationInstance = WindowSpecification({"backend": "uia", "best_match": query})

        window.wait("exists visible ready",
                    timeout=self._cs.config.ident.wait_seconds_for_window,
                    retry_interval=self._cs.config.ident.wait_retry_interval_for_window)
        return WindowGUIApplication(automationInstance=window, processHandle=processHandle)
