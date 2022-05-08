from .ControlBase import ControlBase


class Button(ControlBase):
    def __repr__(self):
        return

    def __str__(self):
        pass

    def click(self) -> bool:
        if super().click():
            return True
        elif self.isToggleable():
            return self.toggle()
        else:
            return False

    def toggle(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.toggle()
                return True
            except:
                return False

    def isToggleable(self) -> bool:
        try:
            if not self.automationInstance:
                return False
            else:
                return not not self.automationInstance.iface_toggle
        except:
            return False
