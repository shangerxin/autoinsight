from dataclasses import dataclass

from .ShapeBase import ShapeBase


@dataclass
class Rectangle(ShapeBase):
    width: int
    height: int
