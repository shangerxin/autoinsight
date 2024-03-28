from random import sample
from typing import Callable, Optional, Sequence, Iterable, Tuple
from time import sleep

from .ControlBase import ControlBase
from autoinsight.decorator.Log import log, Log
from autoinsight.decorator.Step import step
from autoinsight.common.Utils import matchScore


class ComboBox(ControlBase):
    def __init__(self, query: str, *args, **kwargs):
        super().__init__(query, *args, **kwargs)
        self._alias.extend(["combobox", "dropdown", "combo box", "drop down"])

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

    def _getTexts(self, cb) -> Iterable[str]:
        cb.set_focus()
        cb.expand()
        childList = cb.children(control_type="List")
        if childList:
            return [c.window_text() for c in childList[0].children()]
        else:
            return []

    # TODO: Move the finding logic into the context
    def _getMaxScoreIndex(self, values: Iterable[Tuple], texts: Iterable[str], value: str) -> int:
        if values:
            pairs = [(i, *scores) for i, scores in enumerate(values)]
            score, secondSore = 1, 2
            pairs.sort(key=lambda x: x[score], reverse=True)
            firstScore = pairs[0][score]
            pairs = [c for c in pairs if firstScore == c[score]]
            pairs.sort(key=lambda x: x[secondSore], reverse=True)
            if len(pairs) > 1:
                for pair in pairs:
                    i, score, secondScore = pair
                    if texts[i] == value:
                        return i

            return pairs[0][0]

    @property
    def selected(self):
        if self.isExist():
            return self.automationInstance.selected_text()

    @log
    @step
    def select(self, value: Optional[str] = None, index: int = -1) -> bool:
        if self.isExist():
            try:
                cb = self.automationInstance
                texts = self._getTexts(cb)
                matches = [matchScore(value, [text]) for text in texts]
                if matches:
                    index = self._getMaxScoreIndex(matches, texts, value)
                    text = texts[index]
                    self.automationInstance.select(text)
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
