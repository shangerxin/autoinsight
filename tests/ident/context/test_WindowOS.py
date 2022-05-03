import unittest
from queue import Queue

from autoinsight.ident.context.WindowGUIApplication import WindowGUIApplication
from autoinsight.ident.context.WindowOS import WindowOS

from tests.fixtures.tkWindow import showInput


class TestWindowOS(unittest.TestCase):
    def setUp(self):
        self.window: WindowOS = WindowOS()

    def test_environ(self):
        self.assertTrue(self.window.environ["windir"])

    @unittest.skip("waiting for the focus feature")
    def test_typeKeys(self):
        result: Queue = showInput()
        self.window.typeKeys("abcd")
        self.assertEqual(result.get(), "abcd")

    def tearDown(self) -> None:
        self.window.tearDown()

    def test_launch_knowledge_applications(self):
        windowCamera: WindowGUIApplication = self.window.launchApp("camera")

        self.assertTrue(windowCamera)
        windowCamera.close()
