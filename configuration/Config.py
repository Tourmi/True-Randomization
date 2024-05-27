from __future__ import annotations

import configparser
import sys

from .ConfigSections import ConfigSections
from .ConfigOption import ConfigOption

DEFAULT_CONFIG_PATH = "Data\\config.ini"

class Config:
    def __init__(self, config_path = DEFAULT_CONFIG_PATH):
        self._config = configparser.ConfigParser()
        self.config_path = config_path

        self._config.optionxform = str
        self._config.read(config_path)
    
    def write(self):
        """
        Saves the contents of the config to disk
        """
        with open(self.config_path, "w") as file_writer:
            self._config.write(file_writer)
            
    def write_and_exit(self):
        """
        Saves the contents of the config to disk then exit application
        """
        self.write()
        sys.exit()

    def populate_config(self, config : Config):
        """
        Populates the given config with the current values
        """
        for section in config._config.sections():
            for (key, _) in config._config.items(section):
                if ConfigSections.misc.version.is_option(section, key):
                    continue
                try:
                    config._config.set(section, key, self._config.get(section, key))
                except (configparser.NoSectionError, configparser.NoOptionError):
                    continue


    def get(self, option : ConfigOption[str]) -> str:
        return self._config.get(option.section_name, option.option_key, fallback= option.default_value)
    
    def getint(self, option : ConfigOption[int]) -> int:
        return self._config.getint(option.section_name, option.option_key, fallback= option.default_value)
    
    def getboolean(self, option : ConfigOption[bool]) -> bool:
        return self._config.getboolean(option.section_name, option.option_key, fallback= option.default_value)

    def getfloat(self, option : ConfigOption[float]) -> float:
        return self._config.getfloat(option.section_name, option.option_key, fallback= option.default_value)

    def set(self, option : ConfigOption, value : object):
        self._config.set(option.section_name, option.option_key, str(value))