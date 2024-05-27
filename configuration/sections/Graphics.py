from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Graphics(ConfigSection):
    section_name = "GraphicRandomization"
    
    outfit_color = ConfigOption[bool](section_name, "bOutfitColor", False)
    backer_portraits = ConfigOption[bool](section_name, "bBackerPortraits", False)