from typing import Iterable, Optional

from PIL.Image import Image

from .FormBase import FormBase
from .WindowGUIContextBase import WindowGUIContextBase
from .ProcessBase import ProcessBase
from autoinsight.ident.target.TargetBase import TargetBase
from autoinsight.decorator.Log import log
from autoinsight.decorator.Step import step
from autoinsight.common.EnumTypes import ScrollAmountTypes, ScrollDirectionTypes


class WindowForm(FormBase, WindowGUIContextBase):

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def description(self) -> str:
        return f"form {self._title}"

    def __repr__(self):
        pass

    def __str__(self):
        pass

    @property
    def targets(self) -> Iterable[TargetBase]:
        pass

    @property
    def title(self) -> str:
        if self.automationInstance:
            return self.automationInstance.window_text()

    @log
    @step
    def snapshot(self) -> Optional[Image]:
        if self.automationInstance:
            try:
                return self.automationInstance.capture_as_image()
            except:
                return

    @log
    @step
    def scroll(self,
               direction: ScrollDirectionTypes = ScrollDirectionTypes.Down,
               amount: ScrollAmountTypes = ScrollAmountTypes.Lines,
               count: int = 1):

        if self.automationInstance:
            return self.automationInstance.scroll(direction, amount, count)

    @log
    @step
    def focus(self):
        if self.automationInstance:
            self.automationInstance.set_focus()

    @log
    @step
    def maximize(self):
        if self.automationInstance:
            self.automationInstance.maximize()

    @log
    @step
    def minimize(self):
        if self.automationInstance:
            self.automationInstance.minimize()

    @log
    @step
    def drag(self):
        pass

    @log
    @step
    def drop(self):
        pass

    @log
    @step
    def dragTo(self, x: int, y: int):
        pass

    @log
    @step
    def start(self) -> ProcessBase:
        """
        For will do noting for the start method
        """
        self.focus()
