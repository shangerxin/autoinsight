from time import sleep

from autoinsight.script.Step import Step
from autoinsight.ident.IdentObjectBase import IdentObjectBase


class Wait(Step):
    def __init__(self, second: int, *args, **kwargs):
        self._second = second
        super().__init__('Wait', f"second {second}", IdentObjectBase(), IdentObjectBase())

    def execute(self, *args, **kwargs):
        sleep(self._second)
