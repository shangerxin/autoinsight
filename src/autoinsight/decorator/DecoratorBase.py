from abc import abstractmethod
from functools import update_wrapper
from typing import Callable

from autoinsight.common.ObjectBase import ObjectBase


class DecoratorBase(ObjectBase):
    """
    The subclass will be used as decorator so keep the name in lower case.
    """
    def __init__(self, func: Callable, *args, **kwargs):
        self._func: Callable = func
        update_wrapper(self, func)

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass
