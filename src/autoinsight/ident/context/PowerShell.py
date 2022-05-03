from .WindowShellBase import WindowShellBase


class PowerShell(WindowShellBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def launch(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def setCurrent(self):
        pass
