from abc import ABC, abstractmethod


class ObjectBase(ABC):
    """
    Autotest base object
    """
    @abstractmethod
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
