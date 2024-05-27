from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Library(ConfigSection):
    section_name = "LibraryRandomization"

    map_requirements = ConfigOption[bool](section_name, "bMapRequirements", False)
    map_requirements_weight = ConfigOption[int](section_name, "iMapRequirementsWeight", 2)
    tome_appearance = ConfigOption[bool](section_name, "bTomeAppearance", False)