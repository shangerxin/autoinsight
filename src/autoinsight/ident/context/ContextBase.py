from abc import ABC
from typing import Optional

from autoinsight.common.CustomTyping import AutomationInstance, ElementsInfo
from autoinsight.common.Utils import matchScore, isIEqual
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase
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
        self._cs: ConfigurationServiceBase = ioc.getService(ConfigurationServiceBase)
        self._searchDepth: int = 50
        self._searchWidth: int = 30

    def __enter__(self):
        self.setCurrent()

    def __exit__(self, *args):
        self.tearDown()

    def setCurrent(self):
        self._cms.currentContext = self

    def tearDown(self):
        self._cms.unregisterContext(self)

    def find(self, query: str, target: IdentObjectBase = None, *args, **kwargs) -> Optional[AutomationInstance]:
        if self._automationInstance:
            try:
                info: ElementsInfo = self._automationInstance.get_elements_info(depth=self._searchDepth,
                                                                                max_width=self._searchWidth)
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

    def addDialogHandler(self, dialogQuery: str, ActionQuery: str, key: Optional[str] = None):
        """
        Create a background thread to handle random popup dialog
        """
        pass

    def addOneTimeDialogHandler(self, dialogQuery: str, ActionQuery: str, key: Optional[str] = None):
        """
        """
