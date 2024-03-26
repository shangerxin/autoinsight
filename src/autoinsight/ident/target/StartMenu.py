from .TargetBase import TargetBase
from autoinsight.decorator.Log import log
from autoinsight.decorator.Step import step
from autoinsight.ident.context.WindowStartMenu import WindowStartMenu
from autoinsight.common.EnumTypes import KnownContextQueries
from autoinsight.ident.automation.WindowStartMenuAuto import WindowStartMenuAuto


class StartMenu(TargetBase):
    def __init__(self, *args, **kwargs):
        super().__init__(KnownContextQueries.WindowStartMenu.name, *args, **kwargs)
        self._alias.extend(["start", "StartMenu", "StartButton"])
        self._isToggled = False
        self._query = KnownContextQueries.WindowStartMenu

    @property
    def description(self) -> str:
        return KnownContextQueries.WindowStartMenu.name

    def __repr__(self):
        return

    def __str__(self):
        pass

    @property
    def automationInstance(self) -> WindowStartMenuAuto:
        if not self._automationInstance:
            self._cms.currentContext = WindowStartMenu()
            self._automationInstance = self._cms.currentContext.find(self._query, self)
        return self._automationInstance

    def _toggle(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.toggle()
                self._isToggled = not self._isToggled
                return True
            except:
                return False

    @step
    def click(self) -> bool:
        return self._toggle()

    @step
    def toggle(self) -> bool:
        return self._toggle()

    @log
    def isToggleButton(self) -> bool:
        return True

    @log
    def isExist(self) -> bool:
        return True
