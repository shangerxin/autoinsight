from autoinsight.script.StepBase import StepBase
from autoinsight.decorator.Log import Log, log


class Step(StepBase):
    def __repr__(self) -> str:
        return f"step {self.name}, action:{self.action}, target:{self._target}, context:{self._context}"

    def __str__(self) -> str:
        return f"step {self.name}({self._target.description}) {self.action} in context: {self._context.description}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.execute(*args, **kwargs)

    @log
    def execute(self, *args, **kwargs):
        Log.logger.info("Execute %s", self)
        self._isExecuted = True
