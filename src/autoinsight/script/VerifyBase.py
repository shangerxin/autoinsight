from abc import abstractmethod

from .Step import Step


class VerifyBase(Step):
    """
    Verify step for validate a specific condition
    """

    @abstractmethod
    def valid(self, condition, message):
        """
        If the condition is evaluated to false then an exception will be thrown
        """
