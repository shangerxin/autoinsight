from abc import abstractmethod

from autoinsight.common.ObjectBase import ObjectBase


class ScriptBase(ObjectBase):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @property
    def steps(self):
        pass

    @property
    def config(self):
        pass
