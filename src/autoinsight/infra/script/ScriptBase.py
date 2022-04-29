from contextlib import contextmanager
from abc import abstractmethod

from autoinsight.infra.ObjectBase import ObjectBase
from autoinsight.context.NullContext import NullContext


@contextmanager
class ScriptBase(ObjectBase):
    _currentContext = NullContext()

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    @property
    def currentContext(cls):
        return cls._currentContext
