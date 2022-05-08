from typing import Callable, Optional, Iterable

from .ControlBase import ControlBase


class ComboBox(ControlBase):
    def __init__(self, query: str, *args, **kwargs):
        super().__init__(query, *args, **kwargs)
        self._query += " combobox"

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

    def select(self, value: Optional[str] = None, index: int = -1):
        pass
