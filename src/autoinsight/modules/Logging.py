import logging
from abc import abstractmethod
from logging import FileHandler, Handler, Logger, StreamHandler
from typing import Iterable


class LoggerBase:
    levelMaps = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG
    }

    def __init__(self, name: str, level: str, formatTemplate: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logLevel = self._toLogLevel(level)
        logging.basicConfig(format=formatTemplate,
                            level=logLevel)
        self._logger: Logger = logging.getLogger(name)

        for h in self._handlers():
            h.setLevel(logLevel)
            h.setFormatter(logging.Formatter(formatTemplate))
            self._logger.addHandler(h)

    @classmethod
    def _toLogLevel(cls, level: str) -> int:
        return cls.levelMaps.get(level.lower(), logging.WARNING)

    @abstractmethod
    def _handlers(self) -> Iterable[Handler]:
        pass

    def debug(self, *args, **kwargs):
        self._logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        self._logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self._logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        self._logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self._logger.critical(*args, **kwargs)

    @staticmethod
    def close():
        logging.shutdown()


class ConsoleLogger(LoggerBase):
    def _handlers(self) -> Iterable[Handler]:
        return (
            StreamHandler(),
        )


class ConsoleAndFileLogger(LoggerBase):
    def __init__(self, logPath: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logPath = logPath

    def _handlers(self) -> Iterable[Handler]:
        return (
            StreamHandler(),
            FileHandler(self._logPath, mode="w+")
        )
