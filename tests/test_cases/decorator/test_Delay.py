import unittest
from unittest.mock import Mock
from timeit import timeit

from autoinsight.decorator.Delay import delay


class TestDelay(unittest.TestCase):
    def test_delay(self):
        m: Mock = Mock()

        @delay(1)
        def foo():
            m()

        self.assertTrue(timeit(foo, number=1) > 0.9)
        m.assert_called()
