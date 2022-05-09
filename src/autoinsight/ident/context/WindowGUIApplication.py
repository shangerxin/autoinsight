from typing import Iterable, Optional

from .GUIApplicationBase import GUIApplicationBase
from .ProcessBase import ProcessBase
from .WindowForm import WindowForm


class WindowGUIApplication(GUIApplicationBase):
    def __init__(self, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def forms(self) -> Optional[Iterable[WindowForm]]:
        return

    @property
    def currentForm(self) -> Optional[WindowForm]:
        return self._currentForm

    def focus(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.set_focus()
                return True
            except:
                return False

    def start(self) -> ProcessBase:
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def snapshot(self):
        pass
