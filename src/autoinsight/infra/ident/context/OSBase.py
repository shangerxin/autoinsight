from os import environ
from typing import Dict, Iterable
from abc import abstractmethod, abstractproperty

from .ContextBase import ContextBase


class OSContextBase(ContextBase):
    def __init__(self, *args, **kwargs):
        pass

    def launch(self, path):
        pass

    @abstractmethod
    def kill(self, processId: int, processName: str):
        pass

    @abstractmethod
    def terminate(self, processId: int, processName: str):
        pass

    def environ(self) -> Dict:
        return environ

    @abstractproperty
    def displays(self):
        pass

    @abstractproperty
    def systeminfo(self) -> str:
        pass

    @abstractproperty
    def version(self) -> str:
        pass

    @abstractproperty
    def drivers(self) -> Iterable[str]:
        pass

    @abstractproperty
    def SBIOS(self) -> str:
        pass

    @abstractproperty
    def VBIOS(self) -> str:
        pass

    @abstractmethod
    def updateDriver(self):
        pass
