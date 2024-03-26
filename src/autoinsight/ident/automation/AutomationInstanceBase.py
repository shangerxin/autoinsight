from abc import ABC

from autoinsight.ident.IdentObjectBase import IdentObjectBase
from autoinsight.common.models.Rectangle import Rectangle


class AutomationBase(IdentObjectBase, ABC):
    def __init__(self, ioc, rectangle: Rectangle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ioc = ioc
        self._rectangle = rectangle
