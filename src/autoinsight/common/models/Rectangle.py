from dataclasses import dataclass

from .Point import Point
from .ShapeBase import ShapeBase
from .Size import Size


@dataclass
class Rectangle(ShapeBase):
    width: int
    height: int

    @property
    def center(self) -> Point:
        return Point(x=self.left + self.width // 2, y=self.top + self.height // 2)

    @property
    def size(self) -> Size:
        return Size(width=self.width, height=self.height)
