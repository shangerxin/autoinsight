import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)
sys.path.insert(0, PROJECT_PATH)

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
        ComboBox("Framing grid").select("Rule of thirds")
        self.assertEqual(ComboBox("Framing grid").selected, "Rule of thirds")
        Button("back").click()
        windowCamera.close()

    def tearDown(self) -> None:
        self.cms.reset()


if __name__ == "__main__":
    unittest.main()
