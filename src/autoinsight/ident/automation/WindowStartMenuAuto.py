from .AutomationInstanceBase import AutomationBase

from pywinauto.mouse import click


class WindowStartMenuAuto(AutomationBase):
    def toggle(self):
        point = self._rectangle.center
        click(coords=(point.x, point.y))
