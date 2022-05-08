import platform
from typing import Type, Optional

from autoinsight.common.EnumTypes import OSTypes
from .ConfigurationService import ConfigurationService
from .ContextManagementService import ContextManagementService
from .KnowledgeServiceBase import KnowledgeServiceBase
from .OCRServiceBase import OCRServiceBase
from .ServiceBase import ServiceBase
from .TesseractOCRService import TesseractOCRService


class IoCService(ServiceBase):
    OSType = OSTypes.fromStr(platform.system())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registeredServices = {
            OSTypes.Any: {
                OCRServiceBase: TesseractOCRService(),
                ConfigurationService: ConfigurationService(),
                ContextManagementService: ContextManagementService()
            },
            OSTypes.Windows: {},
            OSTypes.Linux: {},
            OSTypes.MacOS: {}
        }
        self._registerWindowServices()

    def getService(self, serviceType: Type[ServiceBase]) -> Optional[ServiceBase]:
        try:
            rss = self._registeredServices
            if serviceType in rss[OSTypes.Any]:
                return rss[OSTypes.Any][serviceType]

            return rss[self.OSType][serviceType]
        except KeyError:
            return

    def _registerWindowServices(self):
        if self.OSType == OSTypes.Windows:
            from autoinsight.services.WindowKnowledgeService import WindowKnowledgeService
            from wmi import WMI

            serviceMap = self._registeredServices[OSTypes.Windows]
            serviceMap.setdefault(KnowledgeServiceBase, WindowKnowledgeService())
            serviceMap.setdefault(WMI, WMI())
