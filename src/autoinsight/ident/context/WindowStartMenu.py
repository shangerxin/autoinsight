from typing import Optional, Union

from PIL import Image
from mss.windows import MSS as mss

from .WindowForm import WindowForm
from autoinsight.ident.automation.WindowStartMenuAuto import WindowStartMenuAuto
from autoinsight.ident.automation.WindowSearchBoxAuto import WindowSearchBoxAuto
from autoinsight.ident.target.TargetBase import TargetBase
from autoinsight.common.EnumTypes import KnownContextQueries
from autoinsight.common.Utils import isSimilar, first, matchScore
from autoinsight.common.models.IdentResult import IdentResult
from autoinsight.services.AIServiceBase import AIServiceBase


class WindowStartMenu(WindowForm):
    @property
    def parent(self):
        if not self._parent:
            self._parent = self.desktop
        return self._parent

    @property
    def description(self) -> str:
        return f"the {KnownContextQueries.WindowStartMenu} context"

    def isDraggable(self):
        return False

    def _isQualified(self, result: IdentResult) -> bool:
        return result and result.confidence > 0.6

    def _queryToString(self, query: Union[KnownContextQueries, str]) -> str:
        if isinstance(query, str):
            return query
        else:
            return query.value

    def find(self, query: KnownContextQueries, target: TargetBase) -> Optional[Union[WindowStartMenuAuto, WindowSearchBoxAuto]]:
        with mss() as sct:
            screen = sct.grab(sct.monitors[1])
            screen = Image.frombytes('RGB', screen.size, screen.bgra, 'raw', 'BGRX')
            ident: AIServiceBase = self._ioc.getService(AIServiceBase)
            results: IdentResult = ident.predict(screen)

            # 0: button_create 1: search_box 2: start_bar
            if query == KnownContextQueries.WindowStartMenu:
                result: IdentResult = first(results, isRevert=True, filterFunc=lambda x: x.classnum == 2, sortKeyFunc=lambda x: x.confidence)
                if result and self._isQualified(result):
                    return WindowStartMenuAuto(self._ioc, result.rect)
            elif isSimilar(query, KnownContextQueries.SearchBox):
                result: IdentResult = first(results, isRevert=True, filterFunc=lambda x: x.classnum == 1, sortKeyFunc=lambda x: x.confidence)
                if result and self._isQualified(result):
                    return WindowSearchBoxAuto(self._ioc, result.rect)
                else:
                    windows = self.desktop.windows()
                    window = first(windows, isRevert=True, sortKeyFunc=lambda x: matchScore("start window", [str(x)]))
                    self._automationInstance = window
                    return super().find(self._queryToString(query), target)


