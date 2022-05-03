from typing import Dict, Optional
from uuid import UUID

from autoinsight.ident.IdentObjectBase import IdentObjectBase
from .ServiceBase import ServiceBase


class ContextManagementService(ServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registeredContexts: Dict[UUID, IdentObjectBase] = {}
        self._currentContext: Optional[IdentObjectBase] = None
        self._contextQueue: list[IdentObjectBase] = []

    @property
    def currentContext(self) -> Optional[IdentObjectBase]:
        if not self._currentContext and self._contextQueue:
            self._currentContext = self._contextQueue[-1]
        return self._currentContext

    @currentContext.setter
    def currentContext(self, context: IdentObjectBase):
        if not context:
            self._currentContext = None

        if self._currentContext != context and context.id in self._registeredContexts:
            self._currentContext = context
            self._updateContextQueue(context)

    def registerContext(self, context: IdentObjectBase):
        if context.id not in self._registeredContexts:
            self._registeredContexts[context.id] = context
            self._contextQueue.append(context)

            if not self.currentContext:
                self.currentContext = context

    def _updateContextQueue(self, context: IdentObjectBase):
        if context.id in self._registeredContexts and self._contextQueue and self._contextQueue[-1] != context:
            self._contextQueue.remove(context)
            self._contextQueue.append(context)

    def unregisterContext(self, context: IdentObjectBase):
        if not context:
            return

        if context.id in self._registeredContexts:
            del self._registeredContexts[context.id]
            self._contextQueue.remove(context)

            if self.currentContext == context:
                self.currentContext = None

    def reset(self):
        """
        Clean all the registered contexts
        """
        self._registeredContexts.clear()
        self._contextQueue.clear()
        self._currentContext = None
