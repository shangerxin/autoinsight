from typing import Iterable, Optional
from abc import abstractmethod

from .FormBase import FormBase
from .ProcessBase import ProcessBase


class GUIApplicationBase(ProcessBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._forms: Iterable[FormBase] = []
        self._currentForm: Optional[FormBase] = None

    @property
    def forms(self) -> Iterable[FormBase]:
        return self._forms

    @property
    def currentForm(self) -> FormBase:
        return self._currentForm

    @abstractmethod
    def focus(self):
        pass
