from abc import abstractmethod
from typing import Optional

from TargetBase import TargetBase
from autoinsight.ident.IdentObjectBase import IdentObjectBase


class ControlBase(TargetBase):
    @abstractmethod
    def focus(self):
        pass

    @property
    def parent(self) -> Optional[IdentObjectBase]:
        pass

    @property
    def next(self) -> Optional[IdentObjectBase]:
        pass

    @property
    def previous(self) -> Optional[IdentObjectBase]:
        pass

    @abstractmethod
    def scrollIntoView(self):
        pass

    @abstractmethod
    def scroll(self):
        pass
