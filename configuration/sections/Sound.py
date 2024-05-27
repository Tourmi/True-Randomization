from .ConfigSection import ConfigSection
from ..ConfigOption import ConfigOption

class Sound(ConfigSection):
    section_name = "SoundRandomization"

    dialogues = ConfigOption[bool](section_name, "bDialogues", False)
    dialogues_language = ConfigOption[int](section_name, "iDialoguesLanguage", 2)
    music = ConfigOption[bool](section_name, "bBackGroundMusic", False)
    