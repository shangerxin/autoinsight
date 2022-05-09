from autoinsight.ident.context.ContextBase import ContextBase


class DummyContext(ContextBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass

    def snapshot(self):
        pass
