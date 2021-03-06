from abc import abstractmethod
from typing import Iterable

from autoinsight.common.CustomTyping import AutomationInstance
from autoinsight.common.models.Knowledge import Knowledge
from .ServiceBase import ServiceBase


class KnowledgeServiceBase(ServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._knowledge: Iterable[Knowledge] = []

    @abstractmethod
    def recognize(self, cmdline: str) -> AutomationInstance:
        pass

    @property
    def knowledge(self):
        return self._knowledge
