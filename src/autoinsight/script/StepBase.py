from abc import abstractmethod
from typing import Any

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.ident.IdentObjectBase import IdentObjectBase


class StepBase(ObjectBase):
    def __init__(self,
                 name: str,
                 action: str,
                 target: IdentObjectBase,
                 context: IdentObjectBase,
                 description: str = "",
                 *args,
                 **kwargs):
        self._name = name
        self._action = action
        self._isExecuted = False
        self._result = None
        self._target: IdentObjectBase = target
        self._context: IdentObjectBase = context
        self._description = description

    @property
    def isExecuted(self):
        return self._isExecuted

    @property
    def result(self) -> Any:
        return self._result

    @property
    def name(self) -> str:
        return self._name

    @property
    def action(self) -> str:
        return self._action

    def reset(self):
        """
        Reset the step to init state
        """
        self._isExecuted = False

    @abstractmethod
    def execute(self, isPaused: bool = False):
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
