from .GUIApplicationBase import GUIApplicationBase
from ...services.WindowKnowledgeService import WindowAutomationInstance


class WindowGUIApplication(GUIApplicationBase):
    def __init__(self, *args,
                 automationInstance: WindowAutomationInstance = None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._instance: WindowAutomationInstance = automationInstance

    def focus(self):
        pass

    def launch(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def close(self):
        super().close()
        if self._instance:
            self._instance.close()
