from uuid import UUID

from autoinsight.common.Utils import GUID
from autoinsight.common.ObjectBase import ObjectBase


class IdentObjectBase(ObjectBase):
    def __init__(self, *args, **kwargs):
        self._id = GUID()

    @property
    def id(self) -> UUID:
        return self._id
