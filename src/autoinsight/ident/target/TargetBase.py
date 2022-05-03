from abc import abstractmethod
from typing import Tuple, Optional, Iterable

from autoinsight.ident.IdentObject import IdentObjectBase


class TargetBase(IdentObjectBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0

    @property
    def size(self) -> Tuple[int, int]:
        return (self._width, self._height)

    @property
    def rectangle(self) -> Tuple[int, int, int, int]:
        return (self._x, self._y, self._width, self._height)

    @property
    def center(self):
        pass

    @property
    def parent(self) -> Optional[IdentObjectBase]:
        pass

    @property
    def next(self) -> Optional[IdentObjectBase]:
        pass

    @property
    def previous(self) -> Optional[IdentObjectBase]:
        pass

    @property
    def children(self) -> Iterable[IdentObjectBase]:
        pass

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def doubleClick(self):
        pass

    @abstractmethod
    def drag(self):
        pass

    @abstractmethod
    def drop(self):
        pass

    @abstractmethod
    def isInViewPort(self) -> bool:
        pass

    @abstractmethod
    def isEnable(self) -> bool:
        pass

    @abstractmethod
    def highlight(self):
        pass

    @abstractmethod
    def scrollIntoView(self):
        pass

    @abstractmethod
    def mouseHover(self):
        pass
