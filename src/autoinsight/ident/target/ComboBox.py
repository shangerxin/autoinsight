from typing import Callable, Optional, Iterable
from difflib import get_close_matches

from .ControlBase import ControlBase
from autoinsight.decorator.Log import log
from autoinsight.decorator.Step import step


class ComboBox(ControlBase):
    def __init__(self, query: str, *args, **kwargs):
        super().__init__(query, *args, **kwargs)

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    @property
    def values(self) -> Iterable[str]:
        pass

    @log
    def iterateValues(self, intervalSecond: int = 2,
                      callbackOnEachValue: Optional[Callable[[str], bool]] = None):
        pass

    @log
    @step
    def select(self, value: Optional[str] = None, index: int = -1) -> bool:
        if self.isExist():
            try:
                cb = self.automationInstance
                matches = get_close_matches(value, cb.texts())
                if matches:
                    self.automationInstance.select(matches[0])
                    return True
                else:
                    return False
            except:
                return False

    @log
    @step
    def randomSelect(self) -> bool:
        pass

    @log
    @step
    def selectFirstValue(self):
        pass

    @log
    @step
    def selectLastValue(self):
        pass
