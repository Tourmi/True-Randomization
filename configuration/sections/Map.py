from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Map(ConfigSection):
    section_name = "MapRandomization"
    
    room_layout = ConfigOption[bool](section_name, "bRoomLayout", False)
    selected_map = ConfigOption[str](section_name, "sSelectedMap", "")