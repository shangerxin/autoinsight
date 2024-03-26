from __future__ import annotations

import os
import signal
from abc import abstractmethod
from typing import Optional
from subprocess import Popen

from autoinsight.common.CustomTyping import AutomationInstance
from autoinsight.decorator.Log import log
from autoinsight.ident.IdentObjectBase import IdentObjectBase


class ProcessBase(IdentObjectBase):
    def __init__(self,
                 processId: Optional[int] = 0,
                 processName: Optional[str] = None,
                 processHandle: Optional[Popen] = None,
                 cmdline: Optional[str] = None,
                 title: Optional[str] = None,
                 workdir: Optional[str] = None,
                 automationInstance: Optional[AutomationInstance] = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._processId: int = processId
        self._processHandle: Optional[Popen] = processHandle
        self._processName: str = processName
        self._cmdline: str = cmdline
        self._title: str = title
        self._workdir: str = workdir
        self._exitcode: int = 0

        if automationInstance:
            self.automationInstance: Optional[AutomationInstance] = automationInstance
            self._isStarted = True
        else:
            self._automationInstance: Optional[AutomationInstance] = None
            self._isStarted: bool = False

    def __repr__(self):
        if not self._repr:
            self._repr = f"name:{self._processName} id:{self.processId} cmdline:{self.cmdline} workdir:{self.workdir}"
        return self._repr

    def __str__(self):
        if not self._str:
            if self.cmdline:
                self._str = os.path.basename(self.cmdline)
            elif self._title:
                self._str = self._title
            elif self._processName:
                self._str = self._processName
            elif self._processId:
                self._str = str(self._processId)
            else:
                self._str = ""

        return self._str

    @property
    def parent(self) -> IdentObjectBase:
        return self._parent

    @property
    def automationInstance(self) -> Optional[AutomationInstance]:
        if not self._isStarted:
            self.start()

        if not self._automationInstance:
            self.automationInstance = self._cms.os.find(
                f"{self._processId} {self.cmdline} {self._title} {self.workdir}")
        return self._automationInstance

    @automationInstance.setter
    def automationInstance(self, value: AutomationInstance):
        if value and value != self._automationInstance:
            self._automationInstance = value
            if hasattr(value, 'process') and isinstance(value.process, int):
                self._processId = value.process
            elif hasattr(value, 'process_id'):
                self._processId = value.process_id()

    @property
    def exitcode(self) -> int:
        return self._exitcode

    @property
    def workdir(self) -> str:
        return self._workdir

    @property
    def cmdline(self) -> str:
        return self._cmdline

    @property
    def processName(self) -> str:
        return self._processName

    @property
    def processId(self) -> int:
        return self._processId

    def __enter__(self):
        super().__enter__()
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def start(self) -> ProcessBase:
        self._isStarted = True

    @classmethod
    @abstractmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    @log
    def close(self):
        if self._processId:
            os.kill(self._processId, signal.SIGTERM)
            self.tearDown()
            return

        if self._processHandle:
            self._processHandle.terminate()
            return

        if self.automationInstance:
            self.automationInstance.close()
            self.tearDown()
            return

    @log
    def kill(self):
        if self._processId:
            os.kill(self._processId, signal.SIGKILL)
            self.tearDown()
            return

    def _printElementsTree(self):
        """
        Print debug element tree information to the console.
        """
        pass
