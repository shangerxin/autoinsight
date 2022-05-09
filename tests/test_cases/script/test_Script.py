import unittest
import os

from autoinsight.script.Script import Script


class TestScript(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        s = Script()
        self.assertTrue(s)

    def test_location(self):
        s = Script()

        self.assertTrue(os.path.isdir(s.location))


if __name__ == '__main__':
    unittest.main()
