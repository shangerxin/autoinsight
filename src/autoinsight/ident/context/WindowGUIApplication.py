from .GUIApplicationBase import GUIApplicationBase
from ..AutomationTyping import AutomationInstance


class WindowGUIApplication(GUIApplicationBase):
    def find(self, description: str, *args, **kwargs) -> AutomationInstance:
        pass

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
