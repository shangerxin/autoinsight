import importlib
import sys
import os.path as path
from typing import Optional, Dict, Union

import yaml

import autoinsight.data
from autoinsight.common.models.Configuration import Configuration
from .ServiceBase import ServiceBase
from ..common.CustomTyping import Serializable


class ConfigurationServiceBase(ServiceBase):
    _outputDirName = "output"
    def __init__(self, *args, **kwargs):
        self._configFilename: str = f"{autoinsight.__name__}.yml"
        self._scriptConfig: Optional[Dict] = None
        self._userConfig: Optional[Dict] = None
        builtinConfigContent: str = importlib.resources.read_text(autoinsight.data, self.configFileName)
        self._builtInConfig: Dict = self.load(builtinConfigContent)

        self._scriptConfigPath: Optional[str] = None
        self._config: Optional[Configuration] = None
        self._scriptRuntimeConfig: Optional[Dict[str, Serializable]] = None

    @property
    def configFileName(self) -> str:
        return self._configFilename

    @property
    def config(self) -> Configuration:
        if not self._config:
            self._config = Configuration(**self.loadAllConfigurations(self._scriptRuntimeConfig))

        return self._config

    @property
    def outputRoot(self) -> str:
        """
        If there is no output location specific by the configuration and the script then
        the default output location will be point to the entry point of the running process
        """
        if self.config.script.output_root:
            return self.config.script.output_root
        else:
            return path.join(path.dirname(sys.argv[0]), self._outputDirName)

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

    def loadAllConfigurations(self, *configInfo: Union[str, Dict]) -> Dict:
        """
        Reload the configuration file from default and custom location
        """
        configPaths, configs = [], []
        for c in configInfo:
            if isinstance(c, str):
                configPaths.append(c)
            else:
                configs.append(c)

        loadedConfigs = (self.load(c) for c in configPaths)
        config: Dict = self.merge(self.builtinConfig,
                                  self._userConfig,
                                  self._scriptConfig,
                                  *loadedConfigs,
                                  *configs)
        return config

    @classmethod
    def merge(cls, *configs: Optional[Dict]) -> Dict:
        """
        Merge multiple levels of configurations into a single one. The later will
        overwrite the previous settings.
        """
        merged = {}
        for config in configs:
            if config and isinstance(config, Dict):
                merged.update(config)

        return merged

    def updateConfig(self, script):
        """
        Update the configuration base on the provided script information
        """
        self._scriptConfigPath = path.join(script.location, f"{autoinsight.__name__}.yml")
        self._scriptConfig = self.load(self._scriptConfigPath)
        self._scriptRuntimeConfig: Optional[Dict[str, Serializable]] = script.runtimeConfig
        config = Configuration(**self.loadAllConfigurations(script.runtimeConfig))

        if not config.common.log_format:
            config.common.log_format = "%(asctime)s - %(levelname)s: %(message)s"

        if not config.script.output_root:
            config.script.output_root = path.join(script.location, self._outputDirName)

        self._config = config
