from typing import Union, NewType, Optional

# TODO the imports should be replaced with the wrapper in autoinsght.automation.*
from pywinauto.win32_element_info import HwndElementInfo
from pywinauto.uia_element_info import UIAElementInfo
from pywinauto.application import WindowSpecification

# TODO in the future we need to separate the implementation for technical instance and visual instance
AutomationInstance = NewType("AutomationInstance", Optional[Union[UIAElementInfo,
                                                                  HwndElementInfo,
                                                                  WindowSpecification]])
