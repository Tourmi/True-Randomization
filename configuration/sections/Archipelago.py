from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Archipelago(ConfigSection):
    section_name = "Archipelago"
    
    enabled = ConfigOption[bool](section_name, "bEnable", False)
    name = ConfigOption[str](section_name, "sName", "Miriam{NUMBER}")
    progression = ConfigOption[int](section_name, "iProgression", 50)
    accessibility = ConfigOption[str](section_name, "sAccessibility", "items")
    death_link = ConfigOption[bool](section_name, "bDeathLink", False)