from typing import Generic, TypeVar

T = TypeVar('T')

class ConfigOption(Generic[T]):
    section_name : str
    option_key : str
    default_value : T

    def __init__(self, section_name : str, option_key : str, default_value : T = None):
        self.section_name = section_name
        self.option_key = option_key
        self.default_value = default_value

    def is_option(self, section : str, key : str):
        return (self.section_name, self.option_key) == (section, key)