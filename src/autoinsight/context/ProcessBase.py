import os
import signal

from .ContextBase import ContextBase


class ProcessBase(ContextBase):
    def __init__(self, id: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = id

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
    def id(self) -> int:
        return self._id

    def close(self):
        if self._id:
            os.kill(self._id, signal.SIGTERM)

    def kill(self):
        if self._id:
            os.kill(self._id, signal.SIGKILL)
