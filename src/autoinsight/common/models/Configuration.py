from dataclasses import dataclass, field
from typing import Literal, Optional

from pydantic import BaseModel, FilePath, DirectoryPath

from .ModelBase import ModelBase
from logging import Formatter


@dataclass
class ServiceConfig(BaseModel, ModelBase):
    user_config_path: FilePath


@dataclass
class IdentConfig(BaseModel, ModelBase):
    search_depth: int = field(default=50)
    search_width: int = field(default=30)
    wait_seconds_for_object: int = field(default=30)
    wait_seconds_for_window: int = field(default=30)
    wait_retry_interval_for_object: int = field(default=3)
    wait_retry_interval_for_window: int = field(default=5)
    highlight_wait_seconds: int = field(default=10)


@dataclass
class ScriptConfig(BaseModel, ModelBase):
    output_root: DirectoryPath
    script_config_name: str
    is_snapshot_before_action: bool


@dataclass
class CommonConfig(BaseModel, ModelBase):
    log_format: Optional[str]
    _log_format: Optional[Formatter] = field(init=False, default=None)
    log_level: Optional[Literal["critical", "error", "warning", "info", "debug"]] = field(default="info")

    def __post_init__(self):
        if self.log_format:
            try:
                self._log_format: Formatter = Formatter(self.log_format)
            except ValueError as e:
                pass


@dataclass
class Configuration(BaseModel, ModelBase):
    common: CommonConfig
    script: ScriptConfig
    ident: IdentConfig
    service: ServiceConfig
