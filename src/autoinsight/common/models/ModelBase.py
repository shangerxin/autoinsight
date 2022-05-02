
import dataclasses
from typing import Iterable, Any, Dict, Tuple

from autoinsight.common.ObjectBase import ObjectBase


@dataclasses.dataclass
class ModelBase(ObjectBase):
    """
    All the subclass inherit from ModelBase should be decorated with dataclass
    """
    def __iter__(self):
        pass

    def asTuple(self) -> Tuple:
        return dataclasses.astuple(self)

    def asDict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

    @property
    def values(self) -> Iterable[Any]:
        return (getattr(self, field.name) for field in self.fields)

    @property
    def fields(self) -> Iterable[dataclasses.Field]:
        return dataclasses.fields(self)

    @property
    def keys(self) -> Iterable[str]:
        return (field.name for field in self.fields)
