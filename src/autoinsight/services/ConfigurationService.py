import yaml
import pathlib
import os

from .ServiceBase import ServiceBase


class ConfigurationService(ServiceBase):
    def __init__(self, *args, **kwargs):
        pass

    def load(self, configFilePath: str):
        pass

    def parse(self, configContent: str):
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

    def merge(self, *configs, **kwargs):
        """
        Merge multiple levels of configurations into a single one. The later will
        overwrite the previous settings.
        """
        pass
