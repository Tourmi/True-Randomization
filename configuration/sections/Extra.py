from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Extra(ConfigSection):
    section_name = "ExtraRandomization"
    
    bloodless_candles = ConfigOption[bool](section_name, "bBloodlessCandles", False)
    bloodless_candles_complexity = ConfigOption[int](section_name, "iBloodlessCandlesComplexity", 2)