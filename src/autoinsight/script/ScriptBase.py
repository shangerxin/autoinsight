from abc import abstractmethod

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.services.ConfigurationService import ConfigurationService
from autoinsight.services.ContextManagementService import ContextManagementService


class ScriptBase(ObjectBase):
    @abstractmethod
    def __init__(self,
                 configurationService: ConfigurationService = ConfigurationService(),
                 contextManagementService: ContextManagementService = ContextManagementService(),
                 *args,
                 **kwargs):
        pass

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
