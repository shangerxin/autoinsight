import logging
from logging import FileHandler
from logging.handlers import SysLogHandler

import autoinsight
from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase
from autoinsight.services.IoCService import IoCService


class LoggerBase(ObjectBase):
    levelMaps = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG
    }

    def __init__(self, ioc: IoCService = IoCService()):
        super().__init__()
        self.cs: ConfigurationServiceBase = ioc.getService(ConfigurationServiceBase)
        logging.basicConfig(format=self.cs.config.common.log_format,
                            level=self._toLogLevel(self.cs.config.common.log_level))

    @classmethod
    def _toLogLevel(cls, level: str):
        cls.levelMaps.get(level.lower(), logging.WARNING)

    @classmethod
    def _handlers(cls):
        pass


class ScriptLogger(LoggerBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger("script")

    @classmethod
    def _handlers(cls):
        return (
            FileHandler
        )


class AutoInsightLogger(LoggerBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger(autoinsight.__name__)


class OverallLogger(LoggerBase):
    pass


class SystemLogHandler(LoggerBase):
    pass
