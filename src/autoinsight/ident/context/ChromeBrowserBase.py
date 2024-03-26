from .BrowserBase import BrowserBase


class ChromeBrowserBase(BrowserBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def tabs(self):
        pass

    def navigate(self, url: str):
        pass

    def focus(self, window_id: int = None, index: int = None, title: str = None):
        pass

    def close(self):
        pass

    def closeTab(self):
        pass

