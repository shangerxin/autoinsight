from shutil import copy2

from .Step import Step
from autoinsight.common.Utils import makeDirs


class Copy(Step):
    def __init__(self, source: str, destination: str, isOverWrite: bool = False):
        super().__init__(Copy.__name__, Copy.__name__, self.os, self.os)
        self._source: str = source
        self._destination: str = destination
        self._isOverWrite: bool = isOverWrite

    def __repr__(self) -> str:
        return f"step {self.name} from {self._source} to {self._destination}"

    def __str__(self) -> str:
        return self.__repr__()

    def execute(self, isPaused: bool = False):
        super().execute(isPaused)
        makeDirs(self._destination, self._isOverWrite)
        copy2(self._source, self._destination)
