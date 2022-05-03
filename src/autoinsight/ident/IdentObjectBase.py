from uuid import UUID
from abc import abstractmethod

from autoinsight.common.Utils import GUID
from autoinsight.common.ObjectBase import ObjectBase


class IdentObjectBase(ObjectBase):
    def __init__(self, *args, **kwargs):
        self._id = GUID()
        self._repr = None
        self._str = None

    @property
    def id(self) -> UUID:
        return self._id

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
