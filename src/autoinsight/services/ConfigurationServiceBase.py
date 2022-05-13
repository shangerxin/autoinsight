import importlib
import os.path as path
from typing import Optional, Dict

import yaml

import autoinsight.data
from autoinsight.common.models.Configuration import Configuration
from .ServiceBase import ServiceBase


class ConfigurationServiceBase(ServiceBase):
    def __init__(self, *args, **kwargs):
        self._configFilename: str = f"{autoinsight.__name__}.yml"
        self._scriptConfig: Optional[Dict] = None
        self._userConfig: Optional[Dict] = None
        builtinConfigContent: str = importlib.resources.read_text(autoinsight.data, self.configFileName)
        self._builtInConfig: Dict = self.load(builtinConfigContent)

        self._scriptConfigPath: Optional[str] = None
        self._config: Optional[Configuration] = None

    @property
    def configFileName(self) -> str:
        return self._configFilename

    @property
    def config(self) -> Configuration:
        if not self._config:
            self._config = Configuration(**self.loadAllConfigurations())

        return self._config

    @property
    def builtinConfig(self) -> Dict:
        return self._builtInConfig

    @classmethod
    def load(cls, configData: str) -> Optional[Dict]:
        """
        Load the yaml configuration file from the configData. It's either a file pat or the yaml content
        """
        try:
            if path.isfile(configData):
                return yaml.load(open(configData), yaml.Loader)
            elif configData:
                return yaml.load(configData, yaml.Loader)
        except:
            return

    def loadAllConfigurations(self, *configs: str) -> Dict:
        """
        Reload the configuration file from default and custom location
        """
        configs = (self.load(c) for c in configs)
        config: Dict = self.merge(self.builtinConfig, self._userConfig, self._scriptConfig, *configs)
        return config

    @classmethod
    def merge(cls, *configs: Dict) -> Dict:
        """
        Merge multiple levels of configurations into a single one. The later will
        overwrite the previous settings.
        """
        merged = {}
        for config in configs:
            if config:
                merged.update(config)

        return merged

    def updateConfig(self, script):
        config = self._config
        if not config.common.log_format:
            config.common.log_format = ""

        if config.script.output_root == "script_root" or \
                not path.isdir(config.script.output_root):
            config.script.output_root = path.join(script.scriptRoot, "output")

        self._scriptConfigPath = path.join(script.location, autoinsight.__name__)
        self._scriptConfig = self.load(self._scriptConfigPath)
        self._config = Configuration(**self.loadAllConfigurations(script.runtimeConfig))
