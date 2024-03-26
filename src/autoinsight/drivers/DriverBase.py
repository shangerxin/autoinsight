from autoinsight.common.ObjectBase import ObjectBase


class DriverBase(ObjectBase):
    def __init__(self, *args, **kwargs):
        pass

    def wait(self, seconds: int):
        pass

    def find(self, *args, **kwargs):
        pass
