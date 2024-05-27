from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Shop(ConfigSection):
    section_name = "ShopRandomization"

    item_values = ConfigOption[bool](section_name, "bItemCostAndSellingPrice", False)
    item_values_weight = ConfigOption[int](section_name, "iItemCostAndSellingPriceWeight", 2)
    scale_selling_price_with_cost = ConfigOption[bool](section_name, "bScaleSellingPriceWithCost", False)