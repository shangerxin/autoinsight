import platform
from typing import Type, Optional

from autoinsight.common.EnumTypes import OSTypes
from .ConfigurationService import ConfigurationService
from .ContextManagementService import ContextManagementService
from .KnowledgeServiceBase import KnowledgeServiceBase
from .OCRServiceBase import OCRServiceBase
from .ServiceBase import ServiceBase
from .TesseractOCRService import TesseractOCRService
from .WindowKnowledgeService import WindowKnowledgeService


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
            OSTypes.Windows: {
                KnowledgeServiceBase: WindowKnowledgeService(),
            },
            OSTypes.Linux: {
            },
            OSTypes.MacOS: {
            }
        }

    def getService(self, serviceType: Type[ServiceBase]) -> Optional[ServiceBase]:
        try:
            rss = self._registeredServices
            if serviceType in rss[OSTypes.Any]:
                return rss[OSTypes.Any][serviceType]

            return rss[self.OSType][serviceType]
        except KeyError:
            return
