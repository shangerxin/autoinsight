from dataclasses import dataclass

from .Rectangle import Rectangle
from .ModelBase import ModelBase


@dataclass
class IdentResult(ModelBase):
    rect: Rectangle
    confidence: float
    classnum: int

    def __str__(self):
        return f"rect: {self._rect}, confidence: {self._confidence}, class_num: {self._class_num}"
