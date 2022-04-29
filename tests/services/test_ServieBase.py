import unittest

from autoinsight.services.ServiceBase import ServiceBase


class TestServiceBase(unittest.TestCase):
    def test_singleton_instance(self):
        s0 = ServiceBase()
        s1 = ServiceBase()

        self.assertEqual(s0, s1)
