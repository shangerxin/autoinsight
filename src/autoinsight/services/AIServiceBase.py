from abc import abstractmethod
from typing import Iterable

from .ServiceBase import ServiceBase
from autoinsight.common.models.IdentResult import IdentResult


class AIServiceBase(ServiceBase):
    @abstractmethod
    def predict(self, image) -> Iterable[IdentResult]:
        pass
