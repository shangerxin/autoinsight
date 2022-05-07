from abc import ABC, abstractmethod

from autoinsight.ident.AutomationTyping import AutomationInstance
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.services.IoCService import IoCService
from autoinsight.services.ContextManagementService import ContextManagementService


class ContextBase(IdentObjectBase, ABC):
    def __init__(self,
                 ioc: IoCService = IoCService(),
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self._cms: ContextManagementService = ioc.getService(ContextManagementService)
        self._cms.registerContext(self)

    def __enter__(self):
        self.setCurrent()

    def __exit__(self):
        self.tearDown()

    def setCurrent(self):
        self._cms.currentContext = self

    def tearDown(self):
        self._cms.unregisterContext(self)

    @abstractmethod
    def find(self, query: str, *args, **kwargs) -> AutomationInstance:
        pass
