from PIL.Image import Image

from autoinsight.ident.context.WindowGUIContextBase import WindowGUIContextBase

class WindowDesktop(WindowGUIContextBase):
    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        pass

    def switch(self):
        pass

    def snapshot(self) -> Image:
        pass
