from logging import Formatter
from typing import Literal, Optional

from pydantic import BaseModel

from .ModelBase import ModelBase


class ServiceConfig(BaseModel, ModelBase):
    pass


class IdentConfig(BaseModel, ModelBase):
    search_depth: int = 50
    search_width: int = 30
    wait_seconds_for_object: int = 30
    wait_seconds_for_window: int = 30
    wait_retry_interval_for_object: int = 3
    wait_retry_interval_for_window: int = 5
    highlight_wait_seconds: int = 10


class ScriptConfig(BaseModel, ModelBase):
    output_root: Optional[str] = None
    is_snapshot_before_action: bool = False
    action_delay_seconds: int = 0


class CommonConfig(BaseModel, ModelBase):
    log_format: Optional[str] = None
    log_level: Optional[Literal["critical", "error", "warning", "info", "debug"]] = "info"

    def __post_init__(self):
        if self.log_format:
            try:
                self._log_format: Formatter = Formatter(self.log_format)
            except ValueError:
                self.log_format = None


class Configuration(BaseModel, ModelBase):
    common: CommonConfig
    script: ScriptConfig
    ident: IdentConfig
    service: ServiceConfig
