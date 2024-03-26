import collections
from typing import Union, NewType, Optional, Dict, Callable
from pathlib import Path

import numpy as np
from PIL.Image import Image

from pywinauto.application import WindowSpecification
from pywinauto.uia_element_info import UIAElementInfo
# TODO the imports should be replaced with the wrapper in autoinsight.automation.*
from pywinauto.win32_element_info import HwndElementInfo

# TODO in the future we need to separate the implementation for technical instance and visual instance
# Implement __getitem__ etc to simplified the try catch calling
AutomationInstance = NewType("AutomationInstance", Optional[Union[UIAElementInfo,
                                                                  HwndElementInfo,
                                                                  WindowSpecification]])

ElementTreeNode = collections.namedtuple("ElementTreeNode", ["elem", "id", "children"])
ElementsInfo = collections.namedtuple("ElementsInfo", ["ctrlTreeRoot",
                                                       "textCtrls",
                                                       "allCtrlIndexNameMaps",
                                                       "allCtrl"])

Serializable = NewType("Serializable", Union[bool,
                                             int,
                                             float,
                                             complex,
                                             str,
                                             bytes,
                                             bytearray,
                                             tuple,
                                             list,
                                             set,
                                             frozenset,
                                             Dict,
                                             Callable])

IMG = NewType("IMG", Union[str, Image, np.array])
PathStr = NewType("PathStr", Union[Path, str])
