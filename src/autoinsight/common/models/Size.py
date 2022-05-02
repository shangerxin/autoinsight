from dataclasses import dataclass

from .ModelBase import ModelBase


@dataclass
class Size(ModelBase):
    width: int
    height: int
