from typing import Iterable

from .FormBase import FormBase
from .ProcessBase import ProcessBase
from autoinsight.ident.target.TargetBase import TargetBase
from autoinsight.decorator.Log import log


class WindowForm(FormBase):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def description(self) -> str:
        return f"form {self._title}"

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

    @log
    def snapshot(self):
        pass

    @log
    def scroll(self):
        pass

    @log
    def wait(self, timeoutSeconds: int = 0):
        pass

    @log
    def focus(self):
        pass

    @log
    def maximize(self):
        pass

    @log
    def minimize(self):
        pass

    @log
    def drag(self):
        pass

    @log
    def drop(self):
        pass

    @log
    def dragTo(self, x: int, y: int):
        pass

    @log
    def start(self) -> ProcessBase:
        """
        For will do noting for the start method
        """
        pass
