from typing import Optional, Any
from enum import Enum, EnumMeta


def _fromStr(cls: EnumMeta, value: str, default: Any = None) -> Optional[Enum]:
    for item in cls:
        if item.value == value:
            return item

    return default


def _str(self: Enum) -> str:
    return str(self.value)


Enum.fromStr = classmethod(_fromStr)
Enum.str = property(_str)
