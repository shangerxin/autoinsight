import unittest
from unittest.mock import patch, MagicMock, PropertyMock

from autoinsight.common.CustomTyping import ElementsInfo, ElementTreeNode
from tests.fixtures.dummys.Dummies import DummyControl, DummyAutomationInstance, DummyTarget
from tests.fixtures.dummys.ident.context.DummyContext import DummyContext


class TestContextBase(unittest.TestCase):
    @patch.object(DummyContext,
                  "_automationInstance",
                  new_callable=PropertyMock,
                  return_value=DummyAutomationInstance(
                      get_elements_info=MagicMock(return_value=ElementsInfo(allCtrl=[
                          DummyControl(friendlyclassname="button"),
                          DummyControl(friendlyclassname="checkBox"),
                          DummyControl(friendlyclassname="comboBox"),
                          DummyControl(friendlyclassname="Button"),
                          DummyControl(friendlyclassname="Static"),
                          DummyControl(friendlyclassname="Pane")
                      ],
                          textCtrls=[],
                          allCtrlIndexNameMaps={
                              0: ["ok", "Ok", "button", "yes", "good"],
                              1: ["good", "checkbox"],
                              2: ["feedbacks", "Combox"],
                              4: ["welcome", "Static"],
                              3: ["cancel", "button", "no"],
                              5: ["ok pane"]},
                          ctrlTreeRoot=ElementTreeNode(id=0,
                                                       children=[],
                                                       elem=MagicMock())))),
                  create=True)
    def test_find(self, *args):
        dc = DummyContext()
        pane = dc.find("ok")
        self.assertEqual("Pane", pane.friendlyclassname)

        okButton = dc.find("ok", DummyTarget(classname="button"))
        self.assertEqual("button", okButton.friendlyclassname)
