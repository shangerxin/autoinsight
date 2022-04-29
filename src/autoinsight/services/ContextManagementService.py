from typing import Dict

from .ServiceBase import ServiceBase


class ContextManagementService(ServiceBase):
    def __init__(self, *args, **kwargs):
        self.contexts: Dict = {}
        self._currentContext = None

    @property
    def currentContext(self, context):
        return self._currentContext

    @currentContext.setter
    def currentContext(self, context):
        if self._currentContext != context:
            self._currentContext = context

    def registerContext(self, context):
        if context.id not in self.contexts:
            self.contexts[context.id] = context
