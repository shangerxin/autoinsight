from .Button import Button


class Checkbox(Button):

    def check(self) -> bool:
        return self.click()

    def isChecked(self) -> bool:
        return
