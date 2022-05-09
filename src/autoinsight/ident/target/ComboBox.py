from typing import Callable, Optional, Iterable

from .ControlBase import ControlBase
from difflib import get_close_matches


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

    def iterateValues(self, intervalSecond: int = 2,
                      callbackOnEachValue: Optional[Callable[[str], bool]] = None):
        pass

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
