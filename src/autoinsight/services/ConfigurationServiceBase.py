import importlib.resources
import os.path as path
from typing import Optional, Dict

import yaml

import autoinsight.data
from .ServiceBase import ServiceBase


class ConfigurationServiceBase(ServiceBase):
    def __init__(self, *args, **kwargs):
        self._scriptConfig: Optional[Dict] = None
        self._userConfig: Optional[Dict] = None
        builtinConfigContent: str = importlib.resources.read_text(autoinsight.data, "autoinsight.yml")
        self._builtInConfig: Dict = self.load(builtinConfigContent)

        self._scriptConfigPath: Optional[str] = None

        self._config = None

    @property
    def config(self) -> Dict:
        if not self._config:
            self._config = self.loadAllConfigurations()

        return self._config

    @property
    def builtinConfig(self) -> Dict:
        return self._builtInConfig

    @classmethod
    def load(cls, configData: str) -> Optional[Dict]:
        """
        Load the yaml configuration file from the configData. It's either a file pat or the yaml content
        """
        if path.isfile(configData):
            return yaml.load(open(configData), yaml.Loader)
        elif configData:
            return yaml.load(configData, yaml.Loader)

    def loadAllConfigurations(self, *configs: str) -> Dict:
        """
        Reload the configuration file from default and custom location
        """
        configs = (self.load(c) for c in configs)
        config: Dict = self.merge(self.builtinConfig, self._userConfig, self._scriptConfig, *configs)
        return config

    def save(self):
        if self._scriptConfigPath:
            scriptConfig = self.load(self._scriptConfigPath)

    @classmethod
    def merge(cls, *configs: Dict) -> Dict:
        """
        Merge multiple levels of configurations into a single one. The later will
        overwrite the previous settings.
        """
        merged = {}
        for config in configs:
            merged.update(config)

        return merged

    @classmethod
    def assign(cls, config: Dict, *otherConfigs: Dict) -> Dict:
        pass
