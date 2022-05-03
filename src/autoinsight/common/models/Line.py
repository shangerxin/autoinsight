from dataclasses import dataclass

from .Point import Point
from .ShapeBase import ShapeBase


@dataclass
class Line(ShapeBase):
    start: Point
    end: Point
