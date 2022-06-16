from enum import Enum

import autoinsight.extend.ExtendEnum  # noqa:F401


class OSTypes(Enum):
    Any = "Any"
    Windows = "Windows"
    Linux = "Linux"
    Java = "Java"
    MacOS = "Darwin"


class ButtonTypes(Enum):
    Left = "left"
    Middle = "middle"
    Right = "right"


class ScrollDirectionTypes(Enum):
    Up = "up"
    Down = "down"
    Left = "left"
    Right = "right"


class ScrollAmountTypes(Enum):
    Lines = "lines"
    Page = "page"
    End = "end"


class CVImageTypes(Enum):
    RGBA = "RGBA"
    RGB = "RGB"
    BGR = "BGR"


class EventTypes(Enum):
    pass
