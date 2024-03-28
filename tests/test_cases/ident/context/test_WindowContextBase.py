import os
import sys

PROJECT_PATH = os.getcwd().replace(r'tests\test_cases\ident\context\test_ContextBase.py', '')
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)
sys.path.insert(0, PROJECT_PATH)
import unittest
from unittest.mock import patch, MagicMock, PropertyMock

from autoinsight.common.CustomTyping import ElementsInfo, ElementTreeNode
from tests.fixtures.dummys.Dummies import DummyControl, DummyAutomationInstance, DummyTarget, dummy_func
from tests.fixtures.dummys.ident.context.DummyContext import DummyContext


class TestWindowContextBase(unittest.TestCase):
    @patch.object(DummyContext,
                  "_automationInstance",
                  new_callable=PropertyMock,
                  return_value=DummyAutomationInstance(
                      get_elements_info=MagicMock(return_value=ElementsInfo(allCtrl=[
                          DummyControl(friendly_class_name=dummy_func("button"), id=0),
                          DummyControl(friendly_class_name=dummy_func("checkBox"), id=1),
                          DummyControl(friendly_class_name=dummy_func("comboBox"), id=2),
                          DummyControl(friendly_class_name=dummy_func("Button"), id=3),
                          DummyControl(friendly_class_name=dummy_func("Static"), id=4),
                          DummyControl(friendly_class_name=dummy_func("Pane"), id=5)
                      ],
                          textCtrls=[],
                          allCtrlIndexNameMaps={
                              0: ["ok", "Ok", "button", "yes", "good"],
                              1: ["ok", "checkbox"],
                              2: ["feedbacks", "Combox"],
                              4: ["welcome", "Static"],
                              3: ["cancel", "button", "no"],
                              5: ["pane"]},
                          ctrlTreeRoot=ElementTreeNode(id=0,
                                                       children=[],
                                                       elem=MagicMock())))),
                  create=True)
    def test_find(self, *args):
        dc = DummyContext()
        pane = dc.find("ok")
        self.assertEqual(1, pane.id)

        okButton = dc.find("ok button", DummyTarget(friendly_class_name=dummy_func("button"), aliases=["hyperlink", "link", "button", "toggle", "checkbutton"]))
        self.assertEqual("button", okButton.friendly_class_name())


if __name__ == '__main__':
    unittest.main()
