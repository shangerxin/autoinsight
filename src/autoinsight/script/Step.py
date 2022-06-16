from autoinsight.script.StepBase import StepBase
from autoinsight.decorator.Log import Log


class Step(StepBase):
    def __repr__(self) -> str:
        return f"step {self.name}, action:{self.action}, target:{self._target}, context:{self._context}"

    def __str__(self) -> str:
        return f"step {self.name}({self._target.description}) {self.action} in context: {self._context.description}"

    def execute(self, isPaused: bool = False):
        Log.logger.info("Execute %s", self)
        self._isExecuted = True
