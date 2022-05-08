import unittest

from autoinsight.ident.context.WindowGUIApplication import WindowGUIApplication
from autoinsight.ident.context.WindowOS import WindowOS
from autoinsight.ident.target.Button import Button


class TestButton(unittest.TestCase):
    def test_button_with_camera_take_photo(self):
        os = WindowOS()
        camera: WindowGUIApplication = os.launchApp("camera")
        camera.setCurrent()
        result = Button("take photo").click()
        camera.close()

        self.assertTrue(result)
