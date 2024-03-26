from enum import Enum, auto

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


class GUIContainerTypes(Enum):
    Dialog = "Dialog"
    Panel = "Panel"
    Form = "Form"
    Window = "Window"
    Pane = "Pane"
    Group = "Group"


class BinaryTypes(Enum):
    Bit16 = auto()
    Bit32 = auto()
    Bit64 = auto()


class KnownContextQueries(Enum):
    WindowStartMenu = "Window start menu"
    SearchBox = "Search box"
