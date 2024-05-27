from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Equipment(ConfigSection):
    section_name = "EquipmentRandomization"
    
    global_gear_stats = ConfigOption[bool](section_name, "bGlobalGearStats", False)
    global_gear_stats_weight = ConfigOption[int](section_name, "iGlobalGearStatsWeight", 2)
    chest_gear_stats = ConfigOption[bool](section_name, "bCheatGearStats", False)