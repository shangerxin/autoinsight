from .GUIApplicationBase import GUIApplicationBase


class BrowserBase(GUIApplicationBase):
    @property
    def tabs(self):
        pass

    def navigate(self, url: str):
        pass

    def focus(self):
        pass

    def close(self):
        pass

    def closeTab(self):
        pass
