from autoinsight.ident.AutomationTyping import AutomationInstance
from autoinsight.ident.context.ContextBase import ContextBase


class DummyContext(ContextBase):
    def find(self, description: str, *args, **kwargs) -> AutomationInstance:
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def snapshot(self):
        pass
