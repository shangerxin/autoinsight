from abc import abstractmethod, abstractproperty

from autoinsight.common.ObjectBase import ObjectBase


class StepBase(ObjectBase):
    @abstractmethod
    def action(self):
        pass

    @abstractproperty
    def result(self):
        pass
