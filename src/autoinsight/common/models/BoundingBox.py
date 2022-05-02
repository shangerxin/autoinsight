from dataclasses import dataclass

from .ModelBase import ModelBase
from .Box import Box


@dataclass
class BoundingBox(ModelBase):
    char: str
    box: Box
