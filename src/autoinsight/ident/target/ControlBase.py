from abc import ABC
from typing import Optional

from .TargetBase import TargetBase
from autoinsight.common.EnumTypes import ScrollDirectionTypes, ScrollAmountTypes
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.decorator.Log import log
from autoinsight.decorator.Step import step


class ControlBase(TargetBase, ABC):
    @property
    def next(self) -> Optional[IdentObjectBase]:
        pass

    @property
    def previous(self) -> Optional[IdentObjectBase]:
        pass

    @log
    @step
    def focus(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.set_focus()
                return True
            except:
                return False

    @log
    @step
    def scroll(self, direction: ScrollDirectionTypes = ScrollDirectionTypes.Down):
        if isinstance(direction, str):
            direction: ScrollDirectionTypes = ScrollDirectionTypes.fromStr(direction)

        if self.isScrollable():
            self.automationInstance.scroll(direction.Down.str, ScrollAmountTypes.Lines.str)
