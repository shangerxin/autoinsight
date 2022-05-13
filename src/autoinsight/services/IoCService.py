import platform
from typing import Type, Optional, Dict, Any

from autoinsight.common.EnumTypes import OSTypes
from .ConfigurationServiceBase import ConfigurationServiceBase
from .ContextManagementService import ContextManagementService
from .KnowledgeServiceBase import KnowledgeServiceBase
from .OCRServiceBase import OCRServiceBase
from .ServiceBase import ServiceBase
from .TesseractOCRService import TesseractOCRService
from .WindowConfigurationService import WindowConfigurationService


class IoCService(ServiceBase):
    OSType = OSTypes.fromStr(platform.system())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registeredServices: Dict[OSTypes, Dict[Any, Any]] = {
            OSTypes.Any: {
                OCRServiceBase: TesseractOCRService(),
                ContextManagementService: ContextManagementService()
            },
            OSTypes.Windows: {},
            OSTypes.Linux: {},
            OSTypes.MacOS: {}
        }
        self._registerWindowServices()

    def getService(self, serviceType: Type[ServiceBase]) -> Optional[Type[ServiceBase]]:
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
            serviceMap.setdefault(ConfigurationServiceBase, WindowConfigurationService())
            serviceMap.setdefault(WMI, WMI())
