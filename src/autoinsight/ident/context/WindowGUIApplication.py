from .GUIApplicationBase import GUIApplicationBase


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

    def close(self):
        super().close()
        if self.automationInstance:
            self.automationInstance.close()

    def snapshot(self):
        pass
