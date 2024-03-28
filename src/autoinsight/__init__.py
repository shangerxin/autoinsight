import os


import autoinsight.extend.ExtendEnum
import autoinsight.extend.ExtendPywinautoApplicationWindowSpecification
from autoinsight.ident.target.Button import Button
from autoinsight.ident.target.ComboBox import ComboBox
from autoinsight.ident.context.WindowOS import WindowOS
from autoinsight.ident.target.StartMenu import StartMenu
from autoinsight.ident.target.SearchBox import SearchBox
from autoinsight.script.Wait import Wait
from autoinsight.ident.context.WindowGUIApplication import WindowGUIApplication

__version__ = "0.1.0"
packageRoot = os.path.dirname(__file__)
packageDataRoot = os.path.join(packageRoot, "data")
