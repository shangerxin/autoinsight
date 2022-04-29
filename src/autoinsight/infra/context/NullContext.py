from autoinsight.context.ContextBase import ContextBase


class NullContext(ContextBase):
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass
