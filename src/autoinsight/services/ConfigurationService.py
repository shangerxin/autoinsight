import yaml
import pathlib
import os

from .ServiceBase import ServiceBase


class ConfigurationService(ServiceBase):
    def __init__(self, *args, **kwargs):
        pass

    def load(self, configPath: str):
        pass

    def refreshConfig(self):
        pass

    def save(self):
        pass

    def _validate(self, yamlContent: str):
        """
        Validate configuration content base on the
        https://www.andrewvillazon.com/validate-yaml-python-schema/
        """
        pass
