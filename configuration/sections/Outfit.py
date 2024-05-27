from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

DEFAULT_MIRIAM_OUTFITS = "H000,H030,H060,H090,H120,H150,H180,H210,H240,H270,H300,H330,S000V020,S000V080"
DEFAULT_ZANGETSU_OUTFITS = "H000,H030,H060,H090,H120,H150,H180,H210,H240,H270,H300,H330,S000V020,S000V080"

class Outfit(ConfigSection):
    section_name = "OutfitConfig"

    miriam_outfits = ConfigOption[str](section_name, "sMiriamList", DEFAULT_MIRIAM_OUTFITS)
    zangetsu_outfits = ConfigOption[str](section_name, "sZangetsuList", DEFAULT_ZANGETSU_OUTFITS)