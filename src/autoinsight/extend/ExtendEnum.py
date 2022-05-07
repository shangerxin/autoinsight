from typing import Optional
from enum import Enum, EnumMeta


def _fromStr(cls: EnumMeta, value: str) -> Optional[Enum]:
    for item in cls:
        if item.value == value:
            return item


Enum.fromStr = classmethod(_fromStr)
