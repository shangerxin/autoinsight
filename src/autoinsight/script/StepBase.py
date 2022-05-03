from abc import abstractmethod

from autoinsight.common.ObjectBase import ObjectBase


class StepBase(ObjectBase):
    @abstractmethod
    def action(self):
        pass

    @property
    def result(self):
        pass
