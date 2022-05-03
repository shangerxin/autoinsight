from __future__ import annotations

import os
import signal
from abc import abstractmethod

from .ContextBase import ContextBase


class ProcessBase(ContextBase):
    def __init__(self, processId: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._processId = processId

    @property
    def exitcode(self) -> int:
        pass

    @property
    def workdir(self) -> str:
        pass

    @property
    def cmdline(self) -> str:
        pass

    @property
    def processId(self) -> int:
        return self._processId

    @abstractmethod
    def launch(self):
        pass

    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    def close(self):
        if self._processId:
            os.kill(self._processId, signal.SIGTERM)

    def kill(self):
        if self._processId:
            os.kill(self._processId, signal.SIGKILL)
