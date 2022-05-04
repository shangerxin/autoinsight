from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable, Callable, Any, NewType, Tuple

from .ModelBase import ModelBase

AutomaticInstance = NewType("AutomaticInstance", Any)


@dataclass
class Knowledge(ModelBase):
    alias: Iterable[str]
    launch: Callable[[Knowledge], AutomaticInstance]
    arguments: Tuple[str] = field(default=tuple())
