from os import environ, path

from .ConfigurationServiceBase import ConfigurationServiceBase


class WindowConfigurationService(ConfigurationServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._userConfigPath: str = path.join(environ["userprofile"], self.configFileName)
        self._userConfig = self.load(self._userConfigPath)
