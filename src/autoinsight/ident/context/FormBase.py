from abc import abstractmethod
from typing import Tuple, Iterable

from .ContextBase import ContextBase
from autoinsight.ident.target.TargetBase import TargetBase


class FormBase(ContextBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0

    @property
    def title(self):
        pass

    @property
    def position(self) -> Tuple[int, int]:
        return (self._x, self.y)

    @property
    def targets(self) -> Iterable[TargetBase]:
        pass

    @property
    def size(self) -> Tuple[int, int]:
        return (self._width, self._height)

    @property
    def rectangle(self) -> Tuple[int, int, int, int]:
        return (self._x, self._y, self._width, self._height)

    @abstractmethod
    def focus(self):
        pass

    @abstractmethod
    def maximize(self):
        pass

    @abstractmethod
    def minimize(self):
        pass

    @abstractmethod
    def drag(self):
        pass

    @abstractmethod
    def drop(self):
        pass

    @abstractmethod
    def dragTo(self, x: int, y: int):
        pass

    @abstractmethod
    def snapshot(self):
        pass

    @property
    def application(self) -> ContextBase:
        pass

    @abstractmethod
    def scroll(self):
        pass
