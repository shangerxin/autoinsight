from .FormBase import FormBase


class WindowForm(FormBase):
    @property
    def title(self):
        pass

    def focus(self):
        pass

    def maximize(self):
        pass

    def minimize(self):
        pass

    def drag(self):
        pass

    def drop(self):
        pass

    def dragTo(self, x: int, y: int):
        pass
