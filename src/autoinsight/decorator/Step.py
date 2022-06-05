from functools import wraps
from typing import Optional

from autoinsight.decorator.DecoratorBase import DecoratorBase
from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService
from autoinsight.script.Step import Step as ScriptStep
from autoinsight.script.Script import Script


class Step(DecoratorBase):
    _script: Optional[Script] = None
    """
    This decorator will automation create a step for base on the wrapped function

    The class decorator cannot be used with class member function.
    """

    def __call__(self, *args, **kwargs):
        if self.script and args and isinstance(args[0], IdentObjectBase):
            identObj: IdentObjectBase = args[0]
            s = ScriptStep(type(identObj).__name__,
                           self._func.__name__,
                           identObj,
                           identObj.parent)
            Step.script.addStep(s)
            s.execute()
            return self._func(*args, **kwargs)
        else:
            return self._func

    @classmethod
    @property
    def script(cls) -> Optional[Script]:
        if not cls._script:
            cms: ContextManagementService = IoCService().getService(ContextManagementService)
            cls._script = cms.script
        return cls._script


def step(func):
    """
    The decorator should be used with class member functions
    """

    @wraps(func)
    def __wrapper(*args, **kwargs):
        if args and isinstance(args[0], IdentObjectBase):
            identObj: IdentObjectBase = args[0]
            s = ScriptStep(type(identObj).__name__,
                           func.__name__,
                           identObj,
                           identObj.parent)

            if Step.script:
                Step.script.addStep(s)

            s.execute()
            return func(*args, **kwargs)
        else:
            return func

    return __wrapper
