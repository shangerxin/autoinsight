from .GUIApplicationBase import GUIApplicationBase
from ..AutomationTyping import AutomationInstance


class WindowGUIApplication(GUIApplicationBase):
    def __init__(self, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def focus(self):
        pass

    def launch(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def snapshot(self):
        pass

    def find(self, query: str, *args, **kwargs) -> AutomationInstance:
        pass
