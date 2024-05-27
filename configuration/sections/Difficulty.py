from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Difficulty(ConfigSection):
    section_name = "GameDifficulty"
    
    normal = ConfigOption[bool](section_name, "bNormal", False)
    hard = ConfigOption[bool](section_name, "bHard", True)
    nightmare = ConfigOption[bool](section_name, "bNightmare", False)