from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Enemy(ConfigSection):
    section_name = "EnemyRandomization"
    
    enemy_locations = ConfigOption[bool](section_name, "bEnemyLocations", False)
    enemy_levels = ConfigOption[bool](section_name, "bEnemyLevels", False)
    enemy_levels_weight = ConfigOption[int](section_name, "iEnemyLevelsWeight", 2)
    boss_levels = ConfigOption[bool](section_name, "bBossLevels", False)
    boss_levels_weight = ConfigOption[int](section_name, "iBossLevelsWeight", 2)
    enemy_tolerances = ConfigOption[bool](section_name, "bEnemyTolerances", False)
    enemy_tolerances_weight = ConfigOption[int](section_name, "iEnemyTolerancesWeight", 2)
    boss_tolerances = ConfigOption[bool](section_name, "bBossTolerances", False)
    boss_tolerances_weight = ConfigOption[int](section_name, "iBossTolerancesWeight", 2)