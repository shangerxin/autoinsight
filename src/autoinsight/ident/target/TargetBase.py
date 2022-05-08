from __future__ import annotations

import time
from typing import Optional

from autoinsight.common.models.Point import Point
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.common.models.Size import Size
from autoinsight.ident.AutomationTyping import AutomationInstance
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService


class TargetBase(IdentObjectBase):
    def __init__(self,
                 query: str,
                 ioc: IoCService = IoCService(),
                 automationInstance: Optional[AutomationInstance] = None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._cms: ContextManagementService = ioc.getService(ContextManagementService)
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self._automationInstance: AutomationInstance = automationInstance
        self._query = query

    @property
    def automationInstance(self):
        if not self._automationInstance and self._query:
            self._automationInstance = self._cms.currentContext.find(self._query)
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

    @property
    def parent(self) -> Optional[TargetBase]:
        pass

    def click(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.click()
                return True
            except:
                return False

    def rightClick(self):
        if self.automationInstance:
            try:
                self.automationInstance.right_click_input()
                return True
            except:
                return False

    def doubleRightClick(self):
        if self.automationInstance:
            try:
                self.automationInstance.double_click_input()
                return True
            except:
                return False

    def doubleClick(self):
        if self.automationInstance:
            try:
                self.automationInstance.double_click_input()
                return True
            except:
                return False

    def drag(self):
        pass

    def drop(self):
        pass

    def isVisible(self) -> bool:
        if self.automationInstance:
            try:
                return self.automationInstance.is_visible()
            except:
                return False

    def isEnable(self) -> bool:
        if self.automationInstance:
            try:
                return self.automationInstance.is_enabled()
            except:
                return False

    def highlight(self):
        if self.automationInstance:
            try:
                # TODO make the wait time configurable
                for i in range(50):
                    self.automationInstance.draw_outline()
                    return True
            except:
                return False

    def mouseHover(self):
        pass

    def scrollIntoView(self, timeout: int = 5) -> bool:
        # TODO extend to support scroll down, up, left and right etc.
        parent = self._getScrollableParent()
        startTime = time.time()
        isTimeout = False
        while not self.isVisible() and parent:
            parent().scroll("down", "line")

            if time.time() - startTime > timeout:
                isTimeout = True
                break

        return not isTimeout

    def reFind(self):
        self._automationInstance = None

    def isScrollable(self):
        try:
            if not self.automationInstance:
                return False
            else:
                return not not self.automationInstance.iface_scroll
        except:
            return False

    def _getScrollableParent(self) -> Optional[TargetBase]:
        parent = self.parent

        while parent:
            if parent.isScrollable():
                return parent

            parent = parent.parent

    def snapshot(self):
        pass
