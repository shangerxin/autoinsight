import unittest

from autoinsight.ident.context.ContextBase import ContextBase
from autoinsight.services.ContextManagementService import ContextManagementService


class TestContextManagementService(unittest.TestCase):
    def setUp(self) -> None:
        self.cms = ContextManagementService()

    def test_register(self):
        s0 = ContextManagementService()
        s1 = ContextManagementService()

        self.assertEqual(s0, s1)

    def test_change_current_context(self):
        context0 = ContextBase()
        context1 = ContextBase()
        context2 = ContextBase()

        self.assertEqual(self.cms.currentContext, context0)

        context2.setCurrent()
        self.assertEqual(self.cms.currentContext, context2)

        context1.setCurrent()
        self.assertEqual(self.cms.currentContext, context1)

        context0.setCurrent()
        self.assertEqual(self.cms.currentContext, context0)

        context2.tearDown()
        self.assertEqual(self.cms.currentContext, context0)

        context0.tearDown()
        self.assertEqual(self.cms.currentContext, context1)

    def tearDown(self) -> None:
        self.cms.reset()
