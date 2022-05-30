import sys
from typing import Optional, Dict, Iterable
from pathlib import Path

from .StepBase import StepBase
from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService
from autoinsight.common.CustomTyping import Serializable


class Script(ObjectBase):

    def __init__(self,
                 scriptFile: str = sys.argv[0],
                 ioc: IoCService = IoCService(),
                 runtimeConfig: Optional[Dict[str, Serializable]] = None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._ioc: IoCService = ioc
        self._cms: ContextManagementService = ioc.getService(ContextManagementService)
        self._cs: ConfigurationServiceBase = ioc.getService(ConfigurationServiceBase)
        self._runtimeConfig: Optional[Dict[str, Serializable]] = runtimeConfig

        scriptPath = Path(scriptFile)
        self._location: Path = scriptPath.parent
        self._name = scriptPath.stem
        self._cs.updateConfig(self)
        self._steps: list[StepBase] = []

        # TODO changed to event
        self._isPaused = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return str(self._location)

    @property
    def steps(self) -> Iterable[StepBase]:
        pass

    def addStep(self, step: StepBase):
        self._steps.append(step)

    @property
    def config(self):
        return self._cs.config

    @property
    def runtimeConfig(self) -> Optional[Dict[str, Serializable]]:
        return self._runtimeConfig

    def run(self):
        for step in self.steps:
            if self._isPaused:
                break

            if not step.isExecuted:
                step.execute(self._isPaused)

    def load(self):
        pass

    def resume(self):
        self._isPaused = False

    def pause(self):
        self._isPaused = True

    def reset(self):
        for step in self.steps:
            step.reset()

    def save(self, path: str) -> bool:
        pass

    def stop(self):
        """
        Will clean and close all the processes start by this script instance
        """
        self.pause()
        self.reset()
