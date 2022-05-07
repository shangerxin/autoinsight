import unittest

from pywinauto.application import WindowSpecification
import autoinsight.extend.ExtendPywinautoApplicationWindowSpecification  # noqa: F401


class TestExtendPywinautoApplicationWindowSpecification(unittest.TestCase):
    def test_extend_get_elements_tree(self):
        dummy_search_criteria = {}
        ws: WindowSpecification = WindowSpecification(dummy_search_criteria)

        self.assertTrue(callable(ws.get_elements_info))
