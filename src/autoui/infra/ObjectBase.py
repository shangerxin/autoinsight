from abc import ABC


class ObjectBase(ABC):
    """
    Autotest base object
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
