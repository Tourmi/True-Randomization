import enum

class FileType(enum.Enum):
    DataTable   = 0
    StringTable = 1
    Blueprint   = 2
    Level       = 3
    Material    = 4
    Texture     = 5
    Sound       = 6