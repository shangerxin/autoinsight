from .ShellBase import ShellBase


class WindowShellBase(ShellBase):
    def __init__(self, *args, **kwargs):
        self.args = args
        super().__init__(*args, **kwargs)
