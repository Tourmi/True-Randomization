from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class StartWith(ConfigSection):
    section_name = "StartWith"

    items = ConfigOption[str](section_name, "sStartItem", "")