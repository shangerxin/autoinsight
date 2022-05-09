import os


import autoinsight.extend.ExtendEnum
import autoinsight.extend.ExtendPywinautoApplicationWindowSpecification
from autoinsight.ident.target.Button import Button
from autoinsight.ident.target.ComboBox import ComboBox
from autoinsight.ident.context.WindowOS import WindowOS
from autoinsight.ident.context.WindowGUIApplication import WindowGUIApplication

__version__ = "0.0.7"

packageRoot = os.path.dirname(__file__)
packageDataRoot = os.path.join(packageRoot, "data")
