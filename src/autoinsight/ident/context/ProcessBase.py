from __future__ import annotations

import os
import signal
from abc import abstractmethod
from typing import Optional

from autoinsight.ident.AutomationTyping import AutomationInstance
from .ContextBase import ContextBase


class ProcessBase(ContextBase):
    def __init__(self,
                 processId: Optional[int] = 0,
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
    def automationInstance(self) -> Optional[AutomationInstance]:
        if not self._automationInstance:
            self._automationInstance = self._cms.os.find(
                f"{self._processId} {self.cmdline} {self._title} {self.workdir}")
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
    def start(self) -> ProcessBase:
        pass

    def __enter__(self):
        super().__enter__()
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    def close(self):
        if self._processId:
            os.kill(self._processId, signal.SIGTERM)
            self.tearDown()
            return

        if self._automationInstance:
            self._automationInstance.close()
            self.tearDown()
            return

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
