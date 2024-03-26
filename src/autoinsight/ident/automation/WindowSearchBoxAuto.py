from pywinauto.keyboard import send_keys
from pywinauto.mouse import click

from .AutomationInstanceBase import AutomationBase


class WindowSearchBoxAuto(AutomationBase):
    def type(self, value: str):
        point = self._rectangle.center
        click(coords=(point.x, point.y))
        send_keys(value)
