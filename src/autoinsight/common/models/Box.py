from dataclasses import dataclass

from .ModelBase import ModelBase


@dataclass
class Box(ModelBase):
    left: int
    top: int
    width: int
    height: int
