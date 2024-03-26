from abc import abstractmethod
from typing import Iterable, Optional

from .ProcessBase import ProcessBase
from autoinsight.common.models.Point import Point
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.common.models.Size import Size
from autoinsight.ident.target.TargetBase import TargetBase
from autoinsight.common.CustomTyping import AutomationInstance


class FormBase(ProcessBase):
    def __init__(self,
                 automationInstance: Optional[AutomationInstance] = None,
                 parent: Optional[ProcessBase] = None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self._parent: Optional[ProcessBase] = parent
        self._automationInstance = automationInstance

    @property
    def automationInstance(self) -> Optional[AutomationInstance]:
        return self._automationInstance

    @property
    def title(self) -> str:
        if self.automationInstance:
            self.automationInstance.tite()

    @property
    def position(self) -> Point:
        return Point(x=self._x, y=self._y)

    @property
    def parent(self) -> Optional[ProcessBase]:
        return self._parent or super().parent

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
    def isDraggable(self):
        pass
