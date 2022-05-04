from typing import Iterable


from .FormBase import FormBase
from ..target.TargetBase import TargetBase


class WindowForm(FormBase):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    @property
    def targets(self) -> Iterable[TargetBase]:
        pass

    @property
    def title(self) -> str:
        pass

    def snapshot(self):
        pass

    def scroll(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def focus(self):
        pass

    def maximize(self):
        pass

    def minimize(self):
        pass

    def drag(self):
        pass

    def drop(self):
        pass

    def dragTo(self, x: int, y: int):
        pass
