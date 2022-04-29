from autoinsight.infra.ident.context.ContextBase import ContextBase


class NullContext(ContextBase):
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def setCurrent(self):
        pass
