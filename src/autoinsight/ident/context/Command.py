from .ProcessBase import ProcessBase
from .WindowShellBase import WindowShellBase


class Command(WindowShellBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start(self) -> ProcessBase:
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def setCurrent(self):
        pass
