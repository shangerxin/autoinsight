from typing import Optional

from autoinsight.ident.AutomationTyping import AutomationInstance
from autoinsight.ident.context.ContextBase import ContextBase


class DummyContext(ContextBase):
    def find(self, query: str, *args, **kwargs) -> Optional[AutomationInstance]:
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def snapshot(self):
        pass
