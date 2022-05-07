from typing import Callable, Optional

from .ControlBase import ControlBase


class ComboBox(ControlBase):
    def iterateAvailableValues(self, intervalSecond: int = 2,
                               callbackOnEachValue: Optional[Callable[[str], bool]] = None):
        pass

    def select(self, value: Optional[str] = None, index: int = -1):
        pass
