from time import sleep
from functools import wraps

from .DecoratorBase import DecoratorBase


# TODO add delay to the actions such as 1 second for each action
class Delay(DecoratorBase):
    def __init__(self, func, *args, **kwargs):
        pass


