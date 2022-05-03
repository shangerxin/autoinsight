from abc import abstractmethod

from autoinsight.common.ObjectBase import ObjectBase


class MonitorBase(ObjectBase):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
