from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Item(ConfigSection):
    section_name = "ItemRandomization"

    
    overworld_pool = ConfigOption[bool](section_name, "bOverworldPool", False)
    overworld_pool_complexity = ConfigOption[int](section_name, "iOverworldPoolComplexity", 2)
    quest_pool = ConfigOption[bool](section_name, "bQuestPool", False)
    shop_pool = ConfigOption[bool](section_name, "bShopPool", False)
    shop_pool_weight = ConfigOption[int](section_name, "iShopPoolWeight", 2)
    quest_requirements = ConfigOption[bool](section_name, "bQuestRequirements", False)
    remove_infinites = ConfigOption[bool](section_name, "bRemoveInfinites", False)