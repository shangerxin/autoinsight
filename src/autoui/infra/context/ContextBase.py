from abc import abstractmethod

from autoui.infra.ObjectBase import ObjectBase


class ContextBase(ObjectBase):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self):
        pass
