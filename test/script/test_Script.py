import unittest

from autoui.script.Script import Script
from autoui.infra.context.NullContext import NullContext


class TestScript(unittest.TestCase):
    def setUp(self):
        pass

    def test_currentContext(self):
        s = Script()
        self.assertTrue(False)
        self.assertIsInstance(s.currentContext, NullContext)


if __name__ == '__main__':
    unittest.main()
