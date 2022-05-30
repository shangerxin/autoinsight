from time import sleep
from functools import wraps

from .DecoratorBase import DecoratorBase


class delay(DecoratorBase):
    def __init__(self, seconds: int = 1, *args, **kwargs):
        super().__init__(None, *args, **kwargs)
        self._delaySeconds = seconds

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
