from typing import Iterable, Optional

from .GUIApplicationBase import GUIApplicationBase
from .ProcessBase import ProcessBase
from .WindowForm import WindowForm
from autoinsight.decorator.Log import log


class WindowGUIApplication(GUIApplicationBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._description = ""

    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    @property
    def description(self) -> str:
        if not self._description:
            if self.processName:
                self._description += f"name:{self.processName}"
            elif self.processId:
                self._description += f"pid:{self.processId}"
            elif self._title:
                self._description += f"title:{self._title}"

        return self._description

    @property
    def forms(self) -> Optional[Iterable[WindowForm]]:
        return

    @property
    def currentForm(self) -> Optional[WindowForm]:
        return self._currentForm

    @log
    def focus(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.set_focus()
                return True
            except:
                return False

    @log
    def start(self) -> ProcessBase:
        pass

    @log
    def wait(self, timeoutSeconds: int = 0):
        pass

    @log
    def snapshot(self):
        pass
