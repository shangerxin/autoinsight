from .ControlBase import ControlBase
from autoinsight.decorator.Log import log
from autoinsight.decorator.Step import step


class Hyperlink(ControlBase):
    def __init__(self, query: str, *args, **kwargs):
        super().__init__(query, *args, **kwargs)

    def __repr__(self):
        return

    def __str__(self):
        pass

    @log
    @step
    def click(self) -> bool:
        if super().click():
            return True
        else:
            return False

    @property
    def text(self) -> str:
        return self._text
