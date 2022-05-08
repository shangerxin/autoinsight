import collections
from typing import Union, NewType, Optional

from pywinauto.application import WindowSpecification
from pywinauto.uia_element_info import UIAElementInfo
# TODO the imports should be replaced with the wrapper in autoinsght.automation.*
from pywinauto.win32_element_info import HwndElementInfo

# TODO in the future we need to separate the implementation for technical instance and visual instance
AutomationInstance = NewType("AutomationInstance", Optional[Union[UIAElementInfo,
                                                                  HwndElementInfo,
                                                                  WindowSpecification]])

ElementTreeNode = collections.namedtuple("ElementTreeNode", ["elem", "id", "children"])
ElementsInfo = collections.namedtuple("ElementsInfo", ["ctrlTreeRoot",
                                                       "textCtrls",
                                                       "allCtrlIndexNameMaps",
                                                       "allCtrl"])
