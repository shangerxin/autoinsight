import os
import sys

from .ScriptBase import ScriptBase
from autoinsight.common.models.Configuration import Configuration


class Script(ScriptBase):
    """
    Should have the ability to persistent the execution state after restart
    """

    def save(self, path: str) -> bool:
        pass

    def run(self):
        pass

    def load(self):
        pass

    def resume(self):
        pass

    def pause(self):
        pass

    def __init__(self, location: str = os.path.dirname(sys.argv[0]), *args, **kwarg):
        self._location = location

    @property
    def location(self) -> str:
        return self._location

    @property
    def runtimeConfig(self) -> Configuration:
        pass
