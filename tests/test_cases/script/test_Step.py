import unittest
from unittest.mock import MagicMock

from autoinsight.script.Step import Step


class TestStep(unittest.TestCase):
    def test_init(self):
        self.assertTrue(Step("dummy", "test", MagicMock(), MagicMock()))
