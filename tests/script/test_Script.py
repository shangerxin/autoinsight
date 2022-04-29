import unittest

from autoinsight.script.Script import Script
from autoinsight.infra.ident.context.NullContext import NullContext


class TestScript(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        s = Script()
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()
