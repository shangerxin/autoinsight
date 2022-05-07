from __future__ import annotations
import os
import signal
from abc import abstractmethod
from typing import Optional

from .ContextBase import ContextBase
from autoinsight.ident.AutomationTyping import AutomationInstance


class ProcessBase(ContextBase):
    def __init__(self,
                 processId: int = 0,
                 cmdline: Optional[str] = None,
                 title: Optional[str] = None,
                 workdir: Optional[str] = None,
                 automationInstance: Optional[AutomationInstance] = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._processId = processId
        self._cmdline = cmdline
        self._title = title
        self._workdir = workdir
        self._exitcode = 0
        self._automationInstance: Optional[AutomationInstance] = automationInstance

    def __repr__(self):
        if not self._repr:
            self._repr = f"{self.__str__()} id:{self.processId} cmdline:{self.cmdline} workdir:{self.workdir}"
        return self._repr

    def __str__(self):
        if not self._str:
            if self.cmdline:
                self._str = os.path.basename(self.cmdline)
            elif self._title:
                self._str = self._title

        return self._str

    @property
    def automationInstance(self) -> AutomationInstance:
        return self._automationInstance

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
    def processId(self) -> int:
        return self._processId

    @abstractmethod
    def launch(self):
        pass

    def __enter__(self):
        super().__enter__()
        self.launch()

    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    def close(self):
        if self._processId:
            os.kill(self._processId, signal.SIGTERM)
            self.tearDown()
            return

        if self.automationInstance:
            self.automationInstance.close()
            self.tearDown()
            return

    def kill(self):
        if self._processId:
            os.kill(self._processId, signal.SIGKILL)
            self.tearDown()
            return
