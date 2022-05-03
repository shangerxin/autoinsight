from dataclasses import dataclass, field
from typing import Iterable, Callable, Any, NewType, Optional, Tuple

from .ModelBase import ModelBase

AutomaticInstance = NewType("AutomaticInstance", Any)


@dataclass
class Knowledge(ModelBase):
    alias: Iterable[str]
    launch: Callable[[], AutomaticInstance]
    arguments: Tuple[str] = field(default=tuple())
