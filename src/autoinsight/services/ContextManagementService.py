from typing import Dict

from .ServiceBase import ServiceBase


class ContextManagementService(ServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registeredContexts: Dict = {}
        self._currentContext = None
        self._contextQueue: list = []

    @property
    def currentContext(self, context):
        return self._currentContext

    @currentContext.setter
    def currentContext(self, context):
        pass

    def registerContext(self, context):
        if context.id not in self._registeredContexts:
            self._registeredContexts[context.id] = context

    def _updateContextQueue(self, context):
        self._contextQueue.remove(context)
        self._contextQueue.append(context)
