from abc import ABC, abstractmethod
from typing import Optional

from autoinsight.common.Utils import matchScore, isIEqual
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

    # TODO match should also consider the control type!
    def find(self, query: str, target: IdentObjectBase = None, *args, **kwargs) -> Optional[AutomationInstance]:
        if self._automationInstance:
            try:
                info: ElementsInfo = self._automationInstance.get_elements_info()

                if target:
                    invalidIndexes = (i for i, c in enumerate(info.allCtrl) if not isIEqual(c.friendlyclassname,
                                                                                            target.classname))
                    for index in invalidIndexes:
                        if index in info.allCtrlIndexNameMaps:
                            del info.allCtrlIndexNameMaps[index]

                bestIndex, bestScore, bestSecond = -1, -1, -1
                for index, names in info.allCtrlIndexNameMaps.items():
                    score, secondScore = matchScore(query, names)
                    if score and score > bestScore:
                        bestIndex = index
                        bestScore = score
                        bestSecond = secondScore

                    elif score == bestScore and secondScore > bestSecond:
                        bestIndex = index
                        bestScore = score
                        bestSecond = secondScore

                if bestIndex > -1:
                    return info.allCtrl[bestIndex]
            except:
                return
