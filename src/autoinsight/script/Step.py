from autoinsight.script.StepBase import StepBase


class Step(StepBase):
    def execute(self, isPaused: bool):
        self._isExecuted = True
