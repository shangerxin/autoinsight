from abc import abstractmethod

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.common.Utils import GUID
from autoinsight.services.ContextManagementService import ContextManagementService


class ContextBase(ObjectBase):
    def __init__(self, contextManagementService: ContextManagementService = ContextManagementService(), *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._cms: ContextManagementService = contextManagementService
        self._cmd.registerContext(self)
        self._id = GUID()

    @property
    def id(self) -> int:
        return self._id

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self):
        pass

    @abstractmethod
    def setCurrent(self):
        self._cms.currentContext = self
