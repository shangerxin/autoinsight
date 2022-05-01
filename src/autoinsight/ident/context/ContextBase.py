from abc import abstractmethod

from autoinsight.ident.IdentObject import IdentObjectBase
from autoinsight.services.ContextManagementService import ContextManagementService


class ContextBase(IdentObjectBase):
    def __init__(self, contextManagementService: ContextManagementService = ContextManagementService(), *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._cms: ContextManagementService = contextManagementService
        self._cms.registerContext(self)

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self):
        pass

    @abstractmethod
    def setCurrent(self):
        self._cms.currentContext = self
