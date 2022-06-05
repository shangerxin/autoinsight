from autoinsight.script.StepBase import StepBase
from autoinsight.decorator.Log import Log


class Step(StepBase):
    def __repr__(self) -> str:
        return f"{super().__repr__()} {self.name}, {self.action}"

    def __str__(self) -> str:
        return f"step {self.name}({self._target.description}).{self.action} in context: {self._context.description}"

    def execute(self, isPaused: bool = False):
        Log.logger.info("Execute %s", self)
        self._isExecuted = True
