from abc import abstractmethod

from autoinsight.common.models.Size import Size
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.common.models.Point import Point
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.ident.AutomationTyping import AutomationInstance
from autoinsight.services.IoCService import IoCService
from autoinsight.services.ContextManagementService import ContextManagementService


class TargetBase(IdentObjectBase):
    def __init__(self,
                 description: str,
                 ioc: IoCService = IoCService(),
                 automationInstance: AutomationInstance = AutomationInstance,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._cms: ContextManagementService = ioc.getService(ContextManagementService)
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self._automationInstance: AutomationInstance = automationInstance
        self._description = description

    @property
    def automationInstance(self):
        return self._automationInstance

    @property
    def size(self) -> Size:
        return Size(width=self._width, height=self._height)

    @property
    def rectangle(self) -> Rectangle:
        return Rectangle(left=self._x, top=self._y, width=self._width, height=self._height)

    @property
    def center(self) -> Point:
        return Point(x=self._x + self._width // 2, y=self._y + self._height // 2)

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def rightClick(self):
        pass

    @abstractmethod
    def doubleRightClick(self):
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
    def isVisible(self) -> bool:
        pass

    @abstractmethod
    def isEnable(self) -> bool:
        pass

    @abstractmethod
    def highlight(self):
        pass

    @abstractmethod
    def mouseHover(self):
        pass

    @abstractmethod
    def scrollIntoView(self):
        pass

    @abstractmethod
    def reFind(self):
        pass
