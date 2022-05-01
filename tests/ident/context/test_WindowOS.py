import unittest

from autoinsight.ident.context.WindowOS import WindowOS


class TestWindowOS(unittest.TestCase):
    def setUp(self):
        self.window: WindowOS = WindowOS()

    def test_environ(self):
        self.assertTrue(self.window.environ["windir"])

    async def test_typeKeys(self):
        self.window.visibleKeys
