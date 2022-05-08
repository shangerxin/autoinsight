from abc import abstractmethod
from typing import Iterable, Optional

from .ProcessBase import ProcessBase
from autoinsight.common.models.Point import Point
from autoinsight.common.models.Size import Size
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.ident.target.TargetBase import TargetBase


class FormBase(ProcessBase):
    def __init__(self,
                 parent: Optional[ProcessBase] = None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self._parent: Optional[ProcessBase] = parent

    @property
    def title(self) -> str:
        pass

    @property
    def position(self) -> Point:
        return Point(x=self._x, y=self._y)

    @property
    def parent(self) -> Optional[ProcessBase]:
        return self._parent

    @property
    def targets(self) -> Iterable[TargetBase]:
        pass

    @property
    def size(self) -> Size:
        return Size(width=self._width, height=self._height)

    @property
    def rectangle(self) -> Rectangle:
        return Rectangle(left=self._x, top=self._y, width=self._width, height=self._height)

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

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def _printElementsTree(self):
        """
        Print debug element tree information to the console.
        """
        pass
