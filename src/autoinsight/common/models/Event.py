from typing import Optional

from .ModelBase import ModelBase
from autoinsight.common.EnumTypes import EventTypes
from autoinsight.common.CustomTyping import Serializable


class Event(ModelBase):
    type: EventTypes
    args: Serializable
    error: Optional[BaseException]
