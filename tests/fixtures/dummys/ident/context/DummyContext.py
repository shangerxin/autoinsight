from autoinsight.ident.context.WindowGUIContextBase import WindowGUIContextBase


class DummyContext(WindowGUIContextBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def snapshot(self):
        pass
