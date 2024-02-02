import unittest

from autoinsight import WindowGUIApplication, WindowOS, Button, ComboBox
from autoinsight.services.ContextManagementService import ContextManagementService


class TestComboBox(unittest.TestCase):
    def setUp(self) -> None:
        self.cms = ContextManagementService()
        self.cms.reset()

    def test_Select(self):
        windowCamera: WindowGUIApplication = WindowOS().launchApp("camera")
        windowCamera.setCurrent()
        Button("settings").click()
        Button("Camera settings").click()
        self.assertTrue(ComboBox("Framing grid").select("Rule of thirds"))
        Button("back").click()
        windowCamera.close()

    def tearDown(self) -> None:
        self.cms.reset()
