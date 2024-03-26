from .TargetBase import TargetBase
from autoinsight.decorator.Step import step
from autoinsight.common.EnumTypes import KnownContextQueries


class SearchBox(TargetBase):
    def __init__(self, query=KnownContextQueries.SearchBox, **kwargs):
        super().__init__(query, **kwargs)
        self._alias.extend(["search", "searchbox", "search_box", "edit"])

    @step
    def type(self, value: str) -> bool:
        if self.automationInstance:
            try:
                if hasattr(self.automationInstance, 'type'):
                    self.automationInstance.type(value)
                else:
                    # https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
                    self.automationInstance.type_keys(value, with_spaces=True)
                return True
            except:
                return False
