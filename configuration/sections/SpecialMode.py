from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class SpecialMode(ConfigSection):
    section_name = "SpecialMode"

    none = ConfigOption[bool](section_name, "bNone", True)
    custom_ng = ConfigOption[bool](section_name, "bCustomNG", False)
    custom_ng_level = ConfigOption[int](section_name, "iCustomNGLevel", 66)
    progressive_z = ConfigOption[bool](section_name, "bProgressiveZ", False)