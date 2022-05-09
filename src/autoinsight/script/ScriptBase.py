from abc import abstractmethod

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.services.ConfigurationService import ConfigurationService
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService


class ScriptBase(ObjectBase):
    @abstractmethod
    def __init__(self,
                 ioc: IoCService = IoCService(),
                 *args,
                 **kwargs):
        self._ioc: IoCService = ioc
        self._cms: ContextManagementService = ioc.getService(ContextManagementService)
        self._cs: ConfigurationService = ioc.getService(ConfigurationService)

    @property
    def steps(self):
        pass

    @property
    def config(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def save(self, path: str) -> bool:
        pass
