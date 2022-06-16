from .ProcessBase import ProcessBase
from .ShellBase import ShellBase


class WindowShellBase(ShellBase):
    def start(self) -> ProcessBase:
        pass

    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    def snapshot(self):
        pass

    def __init__(self, *args, **kwargs):
        self.args = args
        super().__init__(*args, **kwargs)
