import unittest

from autoinsight.services.ContextManagementService import ContextManagementService


class TestContextManagementService(unittest.TestCase):
    def test_singleton_instance(self):
        s0 = ContextManagementService()
        s1 = ContextManagementService()

        self.assertEqual(s0, s1)
