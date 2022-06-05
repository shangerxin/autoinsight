import unittest
from unittest.mock import Mock
from timeit import timeit

from autoinsight.decorator.Delay import Delay, delay


class TestDelay(unittest.TestCase):
    def test_delay_class(self):
        m: Mock = Mock()

        @Delay(1)
        def foo():
            m()

        self.assertTrue(timeit(foo, number=1) > 0.9)
        m.assert_called()

    def test_delay(self):
        m: Mock = Mock()

        @delay
        def foo():
            m()

        self.assertTrue(timeit(foo, number=1) > 0.9)
        m.assert_called()
