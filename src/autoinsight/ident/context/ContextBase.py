from autoinsight.ident.IdentObject import IdentObjectBase
from autoinsight.services.ContextManagementService import ContextManagementService


class ContextBase(IdentObjectBase):
    def __init__(self, contextManagementService: ContextManagementService = ContextManagementService(), *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self._cms: ContextManagementService = contextManagementService
        self._cms.registerContext(self)

    def __enter__(self):
        self.setCurrent()

    def __exit__(self):
        self.tearDown()

    def setCurrent(self):
        self._cms.currentContext = self

    def tearDown(self):
        self._cms.unregisterContext(self)
