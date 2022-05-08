from abc import ABC, abstractmethod
from typing import Optional

from autoinsight.common.Utils import matchScore
from autoinsight.ident.AutomationTyping import AutomationInstance, ElementsInfo
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService


class ContextBase(IdentObjectBase, ABC):
    def __init__(self,
                 ioc: IoCService = IoCService(),
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._ioc: IoCService = ioc
        self._cms: ContextManagementService = ioc.getService(ContextManagementService)
        self._cms.registerContext(self)

    def __enter__(self):
        self.setCurrent()

    def __exit__(self, *args):
        self.tearDown()

    def setCurrent(self):
        self._cms.currentContext = self

    def tearDown(self):
        self._cms.unregisterContext(self)

    @abstractmethod
    def wait(self, timeoutSeconds: int = 0):
        """
        Wait for the object to be displayed
        """
        pass

    def find(self, query: str, *args, **kwargs) -> Optional[AutomationInstance]:
        if self._automationInstance:
            info: ElementsInfo = self._automationInstance.get_elements_info()

            bestIndex, bestScore = -1, 0
            for index, names in info.allCtrlIndexNameMaps.items():
                score = matchScore(query, names)
                if score > bestScore:
                    bestIndex = index

            if bestIndex > -1:
                return info.allCtrl[bestIndex]
