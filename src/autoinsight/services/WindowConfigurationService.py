from os import environ, path
from typing import Optional, Iterable

from .ConfigurationServiceBase import ConfigurationServiceBase


class WindowConfigurationService(ConfigurationServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._userConfigPath: Optional[Iterable[str]] = path.join(environ["userprofile"], ".autoinsight.yml")



