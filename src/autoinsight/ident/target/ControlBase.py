from abc import ABC
from typing import Optional

from .TargetBase import TargetBase
from autoinsight.common.EnumTypes import ScrollDirectionTypes
from autoinsight.ident.IdentObjectBase import IdentObjectBase


class ControlBase(TargetBase, ABC):
    @property
    def next(self) -> Optional[IdentObjectBase]:
        pass

    @property
    def previous(self) -> Optional[IdentObjectBase]:
        pass

    def focus(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.set_focus()
                return True
            except:
                return False

    def scroll(self, direction: ScrollDirectionTypes = ScrollDirectionTypes.Down):
        if isinstance(direction, str):
            direction: ScrollDirectionTypes = ScrollDirectionTypes.fromStr(direction)

        if self.isScrollable():
            self.automationInstance.scroll(direction.Down.str, "line")
