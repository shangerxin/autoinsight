import unittest
import platform

from autoinsight.services.IoCService import IoCService
from autoinsight.common.EnumTypes import OSTypes
from autoinsight.services.KnowledgeServiceBase import KnowledgeServiceBase
from autoinsight.services.WindowKnowledgeService import WindowKnowledgeService
from autoinsight.services.ContextManagementService import ContextManagementService


class TestIoCService(unittest.TestCase):
    def setUp(self) -> None:
        self.ioc = IoCService()

    @unittest.skipUnless(OSTypes.fromStr(platform.system()) == OSTypes.Windows, "Only test on Windows")
    def test_getService_on_Windows(self):
        ks = self.ioc.getService(KnowledgeServiceBase)
        cms = self.ioc.getService(ContextManagementService)

        self.assertEqual(ks, WindowKnowledgeService())
        self.assertEqual(cms, ContextManagementService())
