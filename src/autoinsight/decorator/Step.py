from .DecoratorBase import DecoratorBase
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService


class step(DecoratorBase):
    _script = None
    """
    This decorator will automation create a step for base on the wrapped function
    """

    def __call__(self, *args, **kwargs):
        pass

    @classmethod
    @property
    def script(cls):
        if not cls._script:
            cms: ContextManagementService = IoCService().getService(ContextManagementService)
            cls._script = cms.script
        return cls.script
