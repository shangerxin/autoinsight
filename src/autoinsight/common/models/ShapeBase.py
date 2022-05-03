from dataclasses import dataclass

from .ModelBase import ModelBase
from .Size import Size


@dataclass
class ShapeBase(ModelBase):
    left: int
    top: int

    @property
    def center(self):
        pass

    @property
    def size(self) -> Size:
        pass
