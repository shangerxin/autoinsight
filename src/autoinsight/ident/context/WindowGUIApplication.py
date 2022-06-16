from typing import Iterable, Optional

from PIL.Image import Image
from pywinauto import Application

from .FormBase import FormBase
from .GUIApplicationBase import GUIApplicationBase
from .ProcessBase import ProcessBase
from .WindowForm import WindowForm
from autoinsight.decorator.Log import log
from autoinsight.decorator.Step import step
from autoinsight.common.CustomTyping import AutomationInstance


class WindowGUIApplication(GUIApplicationBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._description = ""

    @classmethod
    def new(cls, *args, **kwargs) -> ProcessBase:
        return WindowGUIApplication(*args, **kwargs)

    @property
    def description(self) -> str:
        if not self._description:
            if self.processName:
                self._description += f"name:{self.processName}"
            elif self.processId:
                self._description += f"pid:{self.processId}"
            elif self._title:
                self._description += f"title:{self._title}"

        return self._description

    @property
    def forms(self) -> Optional[Iterable[WindowForm]]:
        return

    @property
    def currentForm(self) -> Optional[WindowForm]:
        if not self._currentForm and self.automationInstance:
            top = self.automationInstance.top_window()
            self._currentForm = WindowForm(automationInstance=top)

        return self._currentForm

    @log
    @step
    def focus(self) -> bool:
        if self.automationInstance:
            try:
                self.automationInstance.set_focus()
                return True
            except:
                return False

    @log
    @step
    def start(self) -> ProcessBase:
        super().start()
        self.automationInstance = Application.start(self._cmdline,
                                                    work_dir=self._workdir,
                                                    timeout=self._cs.config.ident.wait_seconds_for_window,
                                                    retry_interval=self._cs.config.ident.wait_retry_interval_for_window)

    @log
    @step
    def snapshot(self) -> Optional[Image]:
        if self.automationInstance:
            return self.automationInstance.capture_as_image()

    def _findForm(self, automationInstance: AutomationInstance) -> Optional[FormBase]:
        for form in self._forms:
            if form.automationInstance == automationInstance:
                return form
