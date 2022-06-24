from PIL.Image import Image

from .ProcessBase import ProcessBase


class WindowDesktop(ProcessBase):
    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    def switch(self):
        pass

    def snapshot(self) -> Image:
        pass
