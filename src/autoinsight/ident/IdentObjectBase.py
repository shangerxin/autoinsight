from __future__ import annotations

from abc import abstractmethod
from uuid import UUID

from PIL.Image import Image

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.common.Utils import GUID


class IdentObjectBase(ObjectBase):
    def __init__(self, *args, **kwargs):
        self._id: UUID = GUID()
        self._repr: str = ""
        self._str: str = ""
        self._automationInstance = None

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def description(self) -> str:
        """
        A description that will unique locate the object within the context.

        TODO: The object should be able to rebuild base on the description
        """
        pass

    @property
    def parent(self) -> IdentObjectBase:
        pass

    @property
    def classname(self):
        """
        The control class name
        """
        return type(self).__name__

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def snapshot(self) -> Image:
        pass
