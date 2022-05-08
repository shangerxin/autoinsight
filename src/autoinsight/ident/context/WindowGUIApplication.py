from .GUIApplicationBase import GUIApplicationBase
from .ProcessBase import ProcessBase


class WindowGUIApplication(GUIApplicationBase):
    def __init__(self, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def focus(self):
        pass

    def start(self) -> ProcessBase:
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def snapshot(self):
        pass
