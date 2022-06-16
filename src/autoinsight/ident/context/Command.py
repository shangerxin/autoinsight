from .ProcessBase import ProcessBase
from .WindowShellBase import WindowShellBase


class Command(WindowShellBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start(self) -> ProcessBase:
        pass

    def __enter__(self):
        super().__enter__()

    def __exit__(self):
        super().__exit__()

    def setCurrent(self):
        pass

    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    def snapshot(self):
        pass
