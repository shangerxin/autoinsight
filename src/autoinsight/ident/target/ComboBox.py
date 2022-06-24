from random import sample
from typing import Callable, Optional, Sequence
from difflib import get_close_matches
from time import sleep

from .ControlBase import ControlBase
from autoinsight.decorator.Log import log, Log
from autoinsight.decorator.Step import step


class ComboBox(ControlBase):
    def __init__(self, query: str, *args, **kwargs):
        super().__init__(query, *args, **kwargs)

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    @property
    def values(self) -> Sequence[str]:
        if self.isExist():
            try:
                cb = self.automationInstance
                return cb.texts()
            except Exception as e:
                Log.logger.warning("Access values property failed with exception %s", e)
                return False

    @log
    def iterateValues(self, intervalSecond: int = 2,
                      callbackOnEachValue: Optional[Callable[[str], bool]] = None):
        if self.isExist():
            try:
                cb = self.automationInstance
                values = cb.texts()
                for value in values:
                    self.automationInstance.select(value)
                    if callbackOnEachValue:
                        callbackOnEachValue(value)
                    sleep(max(intervalSecond, 1))
                return True
            except Exception as e:
                Log.logger.warning("Iterate values failed with exception %s", e)
                return False

    @log
    @step
    def select(self, value: Optional[str] = None, index: int = -1) -> bool:
        if self.isExist():
            try:
                cb = self.automationInstance
                matches = get_close_matches(value, cb.texts())
                if matches:
                    self.automationInstance.select(matches[0])
                    return True
                else:
                    return False
            except Exception as e:
                Log.logger.warning("Select failed with exception %s", e)
                return False

    @log
    @step
    def randomSelect(self) -> bool:
        if self.isExist():
            try:
                cb = self.automationInstance
                values = cb.texts()
                if values:
                    self.automationInstance.select(sample([values], 1)[0])
                    return True
                else:
                    return False
            except Exception as e:
                Log.logger.warning("Random select failed with exception %s", e)
                return False

    @log
    @step
    def selectFirstValue(self) -> bool:
        if self.isExist():
            try:
                cb = self.automationInstance
                values = cb.texts()
                if values:
                    self.automationInstance.select(values[0])
                    return True
                else:
                    return False
            except Exception as e:
                Log.logger.warning("Select first value failed with exception %s", e)
                return False

    @log
    @step
    def selectLastValue(self) -> bool:
        if self.isExist():
            try:
                cb = self.automationInstance
                values = cb.texts()
                if values:
                    self.automationInstance.select(values[-1])
                    return True
                else:
                    return False
            except Exception as e:
                Log.logger.warning("Select last value failed with exception %s", e)
                return False
