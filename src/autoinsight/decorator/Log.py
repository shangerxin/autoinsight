import os.path
import time
from functools import wraps

from autoinsight.decorator.DecoratorBase import DecoratorBase
from autoinsight.modules.Logging import ConsoleAndFileLogger, LoggerBase, ConsoleLogger
from autoinsight.services.IoCService import IoCService
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase


class Log(DecoratorBase):
    """
    function log decorator
    """
    _logger: LoggerBase = None

    @classmethod
    @property
    def logger(cls) -> LoggerBase:
        if not cls._logger:
            cs: ConfigurationServiceBase = IoCService().getService(ConfigurationServiceBase)

            if cs.config.script and cs.config.script.output_root:
                logPath = os.path.join(cs.config.script.output_root,
                                       time.strftime(f"{cs.scriptName}-%Y%m%d%H%M%S",
                                                     time.gmtime()))
                cls._logger = ConsoleAndFileLogger(logPath,
                                                   "all",
                                                   cs.config.common.log_level,
                                                   cs.config.common.log_format)
            else:
                cls._logger = ConsoleLogger("all",
                                            cs.config.common.log_level,
                                            cs.config.common.log_format)
        return cls._logger

    def __call__(self, *args, **kwargs):
        try:
            func = self._func
            self.logger.debug("Call %s.%s with %s, %s",
                              self._func.__module__,
                              self._func.__name__,
                              args,
                              kwargs)
            ret = func(*args, **kwargs)
            self.logger.debug("%s.%s return %s",
                              self._func.__module__,
                              self._func.__name__,
                              ret)
            return ret
        except Exception as e:
            self.logger.error(f"Call function {self._func.__module__}.{self._func.__name__} with error {e}")
            raise e


def log(func):
    """
    logging decorator to a function and member function. When it is used with classmethod
    please add this decorator before the classmethod decorator.
    """
    @wraps(func)
    def __wrapper(*args, **kwargs):
        try:
            moduleName = func.__module__ if hasattr(func, "__module__") else ""
            funcName = func.__name__ if hasattr(func, "__name__") else ""
            Log.logger.debug("Call %s.%s with %s, %s",
                             moduleName,
                             funcName,
                             args,
                             kwargs)
            ret = func(*args, **kwargs)
            Log.logger.debug("%s.%s return %s",
                             moduleName,
                             funcName,
                             ret)
            return ret
        except Exception as e:
            Log.logger.error(f"Call function {func.__module__}.{func.__name__} with error {e}")
            raise e

    return __wrapper


# TODO: Add class level log wrapper
def logPublic(cls):
    pass
