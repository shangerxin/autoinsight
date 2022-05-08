import unittest
import platform
from queue import Queue


from autoinsight.common.EnumTypes import OSTypes
from autoinsight.ident.context.WindowGUIApplication import WindowGUIApplication
from autoinsight.ident.context.WindowOS import WindowOS
from tests.fixtures.tkwindows import showInput


@unittest.skipUnless(OSTypes.fromStr(platform.system()) == OSTypes.Windows, "Only test on Windows")
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

    def test_launch_ms_camera(self):
        windowCamera: WindowGUIApplication = self.window.launchApp("camera")

        self.assertTrue(windowCamera)
        windowCamera.close()

    def test_launch_calculator(self):
        calculator: WindowGUIApplication = self.window.launchApp("calc")

        self.assertTrue(calculator)
        calculator.close()

    def test_launch_media_player(self):
        mp: WindowGUIApplication = self.window.launchApp("mediaplayer")

        self.assertTrue(mp)
        mp.close()

    def test_launch_control_panel(self):
        cp: WindowGUIApplication = self.window.launchApp("control panel")

        self.assertTrue(cp)
        cp.close()
