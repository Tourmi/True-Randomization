from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Misc(ConfigSection):
    section_name = "Misc"

    window_size = ConfigOption[int](section_name, "iWindowSize", 0)
    game_path = ConfigOption[str](section_name, "sGamePath", "")
    seed = ConfigOption[str](section_name, "sSeed", "")
    ignore_dlc = ConfigOption[bool](section_name, "bIgnoreDLC", False)
    version = ConfigOption[str](section_name, "sVersion")