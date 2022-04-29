from abc import abstractmethod

from autoinsight.infra.ObjectBase import ObjectBase
from autoinsight.infra.ident.context.NullContext import NullContext


class ScriptBase(ObjectBase):
    _currentContext = NullContext()

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @property
    def steps(self):
        pass
