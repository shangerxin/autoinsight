from .ControlBase import ControlBase
from autoinsight.decorator.Log import log
from autoinsight.decorator.Step import step


class Button(ControlBase):
    def __init__(self, query: str, *args, **kwargs):
        super().__init__(query, *args, **kwargs)
        self._alias.extend(["hyperlink", "link", "button", "toggle", "checkbutton"])

    def __repr__(self):
        return

    def __str__(self):
        pass

    @step
    def click(self) -> bool:
        if super().click():
            return True
        elif self.isToggleable():
            return self.toggle()
        else:
            return False

    @step
    def toggle(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.toggle()
                return True
            except:
                return False

    @log
    def isToggleable(self) -> bool:
        try:
            if not self.automationInstance:
                return False
            else:
                return not not self.automationInstance.iface_toggle
        except:
            return False
