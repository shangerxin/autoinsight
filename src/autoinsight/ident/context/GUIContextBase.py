from abc import ABC
from typing import Optional, Iterable, Any
from time import sleep

from autoinsight.common.CustomTyping import AutomationInstance, ElementsInfo
from autoinsight.common.models.Rectangle import Rectangle
from autoinsight.common.EnumTypes import GUIContainerTypes
from autoinsight.decorator.Log import log, Log
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService


class GUIContextBase(IdentObjectBase, ABC):
    def __init__(self,
                 ioc: IoCService = IoCService(),
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._ioc: IoCService = ioc
        self._cms: ContextManagementService = ioc.getService(ContextManagementService)
        self._cms.registerContext(self)
        self._cs: ConfigurationServiceBase = ioc.getService(ConfigurationServiceBase)
        self._searchDepth: int = 500
        self._searchWidth: int = 300

    def __enter__(self):
        self.setCurrent()

    def __exit__(self, *args):
        self.tearDown()

    def __collectChildCtrls(self, ctrl) -> Iterable[Any]:
        pass

    @property
    def containers(self):
        return (c.name for c in GUIContainerTypes)

    @property
    def rectangle(self) -> Rectangle:
        return self._rectangle

    @property
    def automationInstance(self):
        return self._automationInstance

    def _updateRectangle(self):
        if self.automationInstance:
            rect = self.automationInstance.element_info.rectangle
            self._rectangle = Rectangle(rect.left, rect.top, rect.width(), rect.height())

    @log
    def setCurrent(self):
        self._cms.currentContext = self
        self._updateRectangle()

    @log
    def tearDown(self):
        self._cms.unregisterContext(self)

    @log
    def find(self, query: str, target: IdentObjectBase = None, *args, **kwargs) -> Optional[AutomationInstance]:
        pass

    @log
    def addDialogHandler(self, dialogQuery: str, ActionQuery: str, key: Optional[str] = None):
        """
        Create a background thread to handle random popup dialog
        """
        pass

    @log
    def addOneTimeDialogHandler(self, dialogQuery: str, ActionQuery: str, key: Optional[str] = None):
        """
        """

    @log
    def wait(self, seconds: int):
        sleep(seconds)
