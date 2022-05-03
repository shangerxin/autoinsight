from dataclasses import dataclass
from uuid import UUID

from .ModelBase import ModelBase


@dataclass
class Context(ModelBase):
    id: UUID
