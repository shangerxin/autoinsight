import sys
from abc import abstractmethod
from typing import Optional, Dict
from pathlib import Path

from autoinsight.common.ObjectBase import ObjectBase
from autoinsight.services.ConfigurationServiceBase import ConfigurationServiceBase
from autoinsight.services.ContextManagementService import ContextManagementService
from autoinsight.services.IoCService import IoCService
from autoinsight.common.CustomTyping import Serializable


class Script(ObjectBase):
    @abstractmethod
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
        self._location = scriptPath.parent
        self._name = scriptPath.stem
        self._cs.updateConfig(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return str(self._location)

    @property
    def steps(self):
        pass

    @property
    def config(self):
        return self._cs.config

    @property
    def runtimeConfig(self) -> Optional[Dict[str, Serializable]]:
        return self._runtimeConfig

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def save(self, path: str) -> bool:
        pass

    @abstractmethod
    def stop(self):
        """
        Will clean and close all the processes start by this script instance
        """
        pass
