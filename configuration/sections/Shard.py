from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Shard(ConfigSection):
    section_name = "ShardRandomization"

    randomize_shard_power_and_cost = ConfigOption[bool](section_name, "bShardPowerAndMagicCost", False)
    shard_power_and_cost_weight = ConfigOption[int](section_name, "iShardPowerAndMagicCostWeight", 2)
    scale_cost_with_power = ConfigOption[bool](section_name, "bScaleMagicCostWithPower", False)