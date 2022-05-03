from dataclasses import dataclass

from .ShapeBase import ShapeBase


@dataclass
class Circle(ShapeBase):
    radius: int
