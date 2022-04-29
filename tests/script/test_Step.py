import unittest

from autoinsight.script.Step import Step


class TestStep(unittest.TestCase):
    def test_init(self):
        self.assertTrue(Step())
