import os.path
import time

from .DecoratorBase import DecoratorBase
from autoinsight.modules.Logging import ConsoleAndFileLogger
from autoinsight.services.IoCService import IoCService
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase


class log(DecoratorBase):
    """
    function log decorator
    """
    _logger = None

    @classmethod
    @property
    def logger(cls):
        if not cls._logger:
            cs: ConfigurationServiceBase = IoCService().getService(ConfigurationServiceBase)
            logPath = os.path.join(cs.config.script.output_root,
                                   time.strftime(f"{cs.scriptName}-%Y%m%d%H%M%S",
                                                 time.gmtime()))
            cls._logger = ConsoleAndFileLogger(logPath,
                                               "all",
                                               cs.config.common.log_level,
                                               cs.config.common.log_format)
        return cls._logger

    def __call__(self, *args, **kwargs):
        try:
            self._logger.debug("Call %s.%s with %s, %s",
                               self._func.__module__,
                               self._func.__name__,
                               args,
                               kwargs)
            ret = self._func(*args, **kwargs)
            self._logger.debug("%s.%s return %s",
                               self._func.__module__,
                               self._func.__name__,
                               ret)
            return ret
        except Exception as e:
            self.logger.error(f"Call function {self._func.__module__}.{self._func.__name__} with error {e}")
            raise e
