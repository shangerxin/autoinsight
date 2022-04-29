import unittest

from autoinsight.script.Script import Script
from autoinsight.infra.context.NullContext import NullContext


class TestScript(unittest.TestCase):
    def setUp(self):
        pass

    def test_currentContext(self):
        s = Script()
        self.assertTrue(False)
        self.assertIsInstance(s.currentContext, NullContext)


if __name__ == '__main__':
    unittest.main()
