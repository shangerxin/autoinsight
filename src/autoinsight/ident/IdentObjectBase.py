from abc import abstractmethod
from uuid import UUID

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.common.Utils import GUID


class IdentObjectBase(ObjectBase):
    def __init__(self, *args, **kwargs):
        self._id = GUID()
        self._repr = None
        self._str = None

    @property
    def id(self) -> UUID:
        return self._id

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def snapshot(self):
        pass
