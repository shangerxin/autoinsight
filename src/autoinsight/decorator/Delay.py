from time import sleep
from functools import wraps

from autoinsight.decorator.DecoratorBase import DecoratorBase
from autoinsight.services.IoCService import IoCService
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase


class Delay(DecoratorBase):
    _delaySeconds: int = 0

    def __init__(self, seconds: int = 1, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self._delaySeconds = seconds

    @classmethod
    @property
    def delaySeconds(cls) -> int:
        if cls._delaySeconds <= 0:
            cs: ConfigurationServiceBase = IoCService().getService(ConfigurationServiceBase)
            cls._delaySeconds = max(cs.config.script.action_delay_seconds, 0)

        return cls._delaySeconds

    def __call__(self, func, *args, **kwargs):
        self._func = func

        if self._delaySeconds > 0:

            @wraps(func)
            def __wrapper(*args, **kwargs):
                sleep(self._delaySeconds)
                return func(*args, **kwargs)

            return __wrapper

        else:
            return func


def delay(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        if Delay.delaySeconds > 0:
            sleep(Delay.delaySeconds)
            return func(*args, **kwargs)
        else:
            return func

    return __wrapper
