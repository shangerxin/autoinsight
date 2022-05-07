import unittest

from autoinsight.script.Script import Script


class TestScript(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        s = Script()
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()
