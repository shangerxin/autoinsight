from dataclasses import dataclass

from .ModelBase import ModelBase


@dataclass
class Point(ModelBase):
    x: int
    y: int
