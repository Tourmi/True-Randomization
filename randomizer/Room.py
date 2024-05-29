from __future__ import annotations

from collections import OrderedDict

from .direction import Direction, opposite
from .GlobalImports import *
from .Constants import *
from .Door import Door
from . import Data
from . import FileType
from . import Utility

_C_CAT_ACTORS = [
    "PBEasyTreasureBox_BP_C",
    "PBEasyTreasureBox_BP_C(Gold)",
    "PBPureMiriamTreasureBox_BP_C",
    "PBBakkerDoor_BP_C",
    "Chr_N3016_C",
    "Chr_N3028_C",
    "Chr_N3066_C",
    "Chr_N3067_C",
    "Chr_N3124_C",
    "IncubatorGlass_BP_C"
]

_ROOM_TO_GIMMICK = {
    "m01SIP_007": "m01SIP_007_BG",
    "m20JRN_003": "m20JRN_003_Setting",
    "m20JRN_004": "m20JRN_004_BG"
}

_BOSS_DOOR_ROOMS = [
    "m03ENT_011",
    "m03ENT_014",
    "m05SAN_011",
    "m05SAN_022",
    "m07LIB_010",
    "m07LIB_037",
    "m07LIB_039",
    "m08TWR_019",
    "m13ARC_002",
    "m13ARC_006",
    "m14TAR_003",
    "m14TAR_005",
    "m15JPN_015",
    "m17RVA_007",
    "m17RVA_009",
    "m18ICE_002",
    "m18ICE_005",
    "m18ICE_010",
    "m18ICE_017",
    "m20JRN_002"
]

_BACKER_DOOR_ROOMS = [
    "m04GDN_006",
    "m06KNG_013",
    "m07LIB_036",
    "m15JPN_011"
]

_AREA_DOOR_ROOMS = [
    "m02VIL_012",
    "m03ENT_000",
    "m03ENT_007",
    "m03ENT_008",
    "m03ENT_016",
    "m03ENT_018",
    "m03ENT_019",
    "m04GDN_000",
    "m04GDN_003",
    "m04GDN_015",
    "m04GDN_016",
    "m04GDN_017",
    "m05SAN_000",
    "m05SAN_001",
    "m05SAN_003",
    "m05SAN_010",
    "m05SAN_021",
    "m05SAN_024",
    "m06KNG_000",
    "m06KNG_008",
    "m07LIB_000",
    "m07LIB_021",
    "m07LIB_039",
    "m08TWR_003",
    "m08TWR_017",
    "m09TRN_000",
    "m09TRN_005",
    "m10BIG_018",
    "m11UGD_000",
    "m11UGD_014",
    "m11UGD_026",
    "m11UGD_033",
    "m11UGD_036",
    "m11UGD_046",
    "m11UGD_055",
    "m11UGD_057",
    "m12SND_000",
    "m12SND_011",
    "m13ARC_000",
    "m14TAR_000",
    "m14TAR_009",
    "m15JPN_000",
    "m15JPN_007",
    "m17RVA_000",
    "m17RVA_014",
    "m18ICE_000"
]

_BOOKSHELF_ROOMS = [
    "m01SIP_005",
    "m01SIP_012",
    "m02VIL_007",
    "m03ENT_002",
    "m03ENT_004",
    "m03ENT_005",
    "m03ENT_011",
    "m03ENT_012",
    "m04GDN_005",
    "m04GDN_006",
    "m04GDN_011",
    "m05SAN_000",
    "m05SAN_003",
    "m05SAN_005",
    "m05SAN_009",
    "m05SAN_021",
    "m06KNG_003",
    "m06KNG_015",
    "m06KNG_018",
    "m07LIB_000",
    "m07LIB_010",
    "m07LIB_018",
    "m07LIB_036",
    "m08TWR_000",
    "m08TWR_003",
    "m08TWR_010",
    "m08TWR_014",
    "m09TRN_005",
    "m10BIG_009",
    "m11UGD_000",
    "m11UGD_006",
    "m11UGD_032",
    "m12SND_021",
    "m13ARC_002",
    "m13ARC_006",
    "m14TAR_001",
    "m15JPN_015",
    "m17RVA_007",
    "m18ICE_002"
]

_WALL_TO_GIMMICK_FLAG = {
    "SIP_006_0_0_RIGHT_BOTTOM": "SIP_006_DestructibleWall",
    "SIP_006_0_2_RIGHT":        "SIP_017_BreakWallCannon",
    "SIP_017_0_0_LEFT":         "SIP_017_BreakWallCannon",
    "VIL_006_3_0_BOTTOM":       "VIL_006_HardFloor1F",
    "VIL_009_0_0_LEFT_BOTTOM":  "VIL_009_DestructibleWall",
    "ENT_018_0_0_BOTTOM":       "ENT_018_DestructibleFloor",
    "GDN_013_0_0_LEFT":         "GDN_013_DestructibleWall",
    "SAN_019_1_0_BOTTOM":       "SAN_019_DestructibleFloor",
    "KNG_013_0_0_LEFT":         "KNG_013_DestructibleWall",
    "KNG_015_0_2_TOP":          "KNG_015_DestructibleRoof",
    "KNG_017_0_0_LEFT":         "KNG_017_DestructibleWall",
    "LIB_029_1_1_TOP":          "LIB_029_DestructibleCeil",
    "UGD_003_1_3_RIGHT":        "UGD_003_DestructibleWall1",
    "UGD_003_1_0_RIGHT":        "UGD_003_DestructibleWall2",
    "UGD_042_1_0_RIGHT":        "UGD_042_DestructibleWall",
    "SND_002_0_0_LEFT":         "SND_002_DestructibleWall",
    "ARC_003_0_0_RIGHT":        "ARC_002_DestructibleWall",
    "ARC_006_0_0_BOTTOM":       "ARC_006_DestructibleFloor",
    "JPN_003_0_0_LEFT":         "JPN_003_DestructibleWall",
    "RVA_003_1_0_RIGHT":        "RVA_003_DestructibleWall",
    "RVA_014_0_0_RIGHT":        "RVA_014_DestructibleWall"
}

_DOOR_SKIP = [
    "VIL_008_3_0_RIGHT",
    "VIL_008_3_0_BOTTOM_RIGHT",
    "VIL_011_5_0_RIGHT",
    "VIL_011_5_0_TOP_RIGHT",
    "SND_025_0_0_LEFT",
    "SND_026_0_0_LEFT",
    "SND_027_0_0_LEFT"
]

_ARCHED_DOORS = [
    "GDN_009_0_0_LEFT",
    "GDN_009_0_1_LEFT",
    "GDN_009_2_0_RIGHT",
    "SAN_015_0_0_LEFT",
    "SAN_015_1_0_RIGHT",
    "SAN_017_0_0_LEFT",
    "SAN_017_1_0_RIGHT",
    "SAN_018_0_0_LEFT",
    "SAN_018_1_0_RIGHT",
    "SAN_020_0_0_LEFT",
    "SAN_020_1_0_RIGHT",
    "SAN_020_0_1_LEFT",
    "SAN_020_1_1_RIGHT"
]

_FLOORLESS_DOORS = [
    "SIP_006_0_2_RIGHT",
    "SIP_017_0_0_LEFT",
    "VIL_000_1_0_RIGHT",
    "VIL_001_0_0_LEFT",
    "VIL_006_0_1_LEFT",
    "GDN_006_0_0_LEFT",
    "GDN_013_0_0_LEFT",
    "SAN_009_0_1_LEFT",
    "SAN_009_1_1_RIGHT",
    "SAN_019_0_3_LEFT",
    "SAN_021_0_1_LEFT",
    "SAN_021_1_1_RIGHT",
    "KNG_010_1_1_RIGHT",
    "KNG_013_0_0_LEFT",
    "KNG_017_0_0_LEFT",
    "LIB_003_0_1_RIGHT",
    "LIB_023_0_0_LEFT",
    "LIB_023_0_0_RIGHT",
    "UGD_006_0_2_LEFT",
    "UGD_009_1_0_RIGHT",
    "UGD_016_0_1_RIGHT",
    "UGD_019_0_2_LEFT",
    "UGD_019_1_2_RIGHT",
    "UGD_020_0_0_LEFT",
    "UGD_021_0_0_LEFT",
    "UGD_029_0_1_LEFT",
    "UGD_056_0_3_LEFT",
    "ARC_002_1_1_RIGHT",
    "ARC_003_0_0_RIGHT",
    "JPN_010_0_0_LEFT",
    "JPN_010_0_1_LEFT",
    "JPN_010_3_0_RIGHT",
    "JPN_011_0_0_RIGHT",
    "JPN_012_0_0_LEFT",
    "JPN_012_3_0_RIGHT",
    "JPN_014_0_0_LEFT",
    "JPN_014_3_0_RIGHT",
    "JPN_015_0_0_RIGHT",
    "JPN_015_0_1_LEFT",
    "JPN_015_0_1_RIGHT",
    "RVA_001_0_1_LEFT",
    "ICE_005_0_2_LEFT",
    "ICE_016_0_1_RIGHT"
]

_OPEN_TRANSITION_DOORS = [
    "LIB_008_0_1_RIGHT",
    "UGD_019_1_0_RIGHT",
    "UGD_021_0_0_LEFT",
    "UGD_022_1_0_RIGHT",
    "UGD_023_0_0_LEFT",
    "UGD_023_1_0_RIGHT",
    "UGD_024_0_2_LEFT",
    "UGD_024_1_1_RIGHT",
    "UGD_025_0_1_LEFT",
    "UGD_042_0_0_LEFT",
    "UGD_042_1_0_RIGHT",
    "UGD_044_0_0_LEFT",
    "UGD_045_0_0_LEFT",
    "UGD_045_1_0_RIGHT",
    "UGD_046_1_0_RIGHT"
]

_TRANSITIONLESS_DOORS = [
    "KNG_013_0_0_RIGHT",
    "TWR_009_0_10_RIGHT"
]

_ROOM_TO_BOSS = {
    "m03ENT_013": "N1011",
    "m05SAN_012": "N1003",
    "m07LIB_011": "N2004",
    "m13ARC_005": "N1006",
    "m07LIB_038": "N2008",
    "m05SAN_023": "N1002",
    "m14TAR_004": "N2007",
    "m17RVA_008": "N2006",
    "m15JPN_016": "N1011_STRONG",
    "m18ICE_004": "N2012",
    "m18ICE_018": "N1008",
    "m18ICE_019": "N1009_Enemy",
    "m20JRN_003": "N2017"
}

_ROOM_TO_BACKER = {
    "m88BKR_001": ("N3107", 2),
    "m88BKR_002": ("N3108", 3),
    "m88BKR_003": ( "None", 4),
    "m88BKR_004": ("N3106", 1)
}

_CUSTOM_ACTOR_PREFIX = "TR_"

class Room:
    ROTATING_ROOM_TO_CENTER = {
        "m02VIL_008": (2280, -2280),
        "m02VIL_011": (5218, -2310),
        "m08TWR_017": (2400,     0),
        "m08TWR_018": (2400,     0),
        "m08TWR_019": (2520,     0),
        "m09TRN_001": (2390, -2460),
        "m12SND_025": ( 120,  -450),
        "m12SND_026": ( 120,  -450),
        "m12SND_027": ( 120,  -450)
    }

    @classmethod
    def init(cls):
        cls.door_string_to_door : dict[str, Door] = {}
        cls.global_room_pickups : list[str] = []

    @classmethod
    def get_map_info(cls):
        cls.map_connections : dict[str, dict[str, list]] = {}
        #Keep track of every door connection for multi purpose
        for room in Data.datatable["PB_DT_RoomMaster"]:
            cls.map_connections[room] = {}
            doors = cls._convert_flag_to_door(room, Data.datatable["PB_DT_RoomMaster"][room]["DoorFlag"], Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"])
            for door in doors:
                door_string = "_".join([door.room[3:], str(door.x_block), str(door.z_block), door.direction_part.name])
                cls.door_string_to_door[door_string] = door
                cls.map_connections[room][door_string] = []
        for room_1 in Data.datatable["PB_DT_RoomMaster"]:
            for room_2 in Data.datatable["PB_DT_RoomMaster"]:
                cls._is_room_adjacent(room_1, room_2)

    @staticmethod
    def update_any_map():
        #Rooms with no traverse blocks only display properly based on their Y position below the origin
        #Shift those lists if the rooms are below 0
        for room in ["m08TWR_017", "m08TWR_018", "m08TWR_019", "m11UGD_013", "m11UGD_031"]:
            if Data.datatable["PB_DT_RoomMaster"][room]["OffsetZ"] < 0:
                multiplier = abs(int(Data.datatable["PB_DT_RoomMaster"][room]["OffsetZ"]/7.2)) - 1
                if multiplier > Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"] - 1:
                    multiplier = Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"] - 1
                for index in range(len(Data.datatable["PB_DT_RoomMaster"][room]["NoTraverse"])):
                    Data.datatable["PB_DT_RoomMaster"][room]["NoTraverse"][index] -= Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"]*multiplier

    @classmethod
    def update_custom_map(cls):
        #Remove the village locked door
        cls.remove_level_class("m02VIL_003_Gimmick", "BP_LookDoor_C")
        #Trigger a few events by default
        Data.datatable["PB_DT_GimmickFlagMaster"]["SIP_017_BreakWallCannon"]["Id"]  = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
        Data.datatable["PB_DT_GimmickFlagMaster"]["ENT_000_FallStatue"]["Id"]       = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
        Data.datatable["PB_DT_GimmickFlagMaster"]["ENT_007_ZangetuJump"]["Id"]      = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
        Data.datatable["PB_DT_GimmickFlagMaster"]["KNG_015_DestructibleRoof"]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
        Data.datatable["PB_DT_GimmickFlagMaster"]["LIB_029_DestructibleCeil"]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
        Data.datatable["PB_DT_GimmickFlagMaster"]["TRN_002_LeverDoor"]["Id"]        = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
        #Remove the few forced transitions that aren't necessary at all
        for room in ["m04GDN_006", "m06KNG_013", "m07LIB_036", "m15JPN_011", "m88BKR_001", "m88BKR_002", "m88BKR_003", "m88BKR_004"]:
            cls.remove_level_class(f"{room}_RV", "RoomChange_C")
        #Add a second lever to the right of the tower elevator so that it can be activated from either sides
        cls.add_level_actor("m08TWR_009_Gimmick", "TWR009_ElevatorLever_BP_C", FVector(1110, 0, 11040), FRotator(0, 0, 0), FVector(1, 1, 1), {})
        #Make Bathin's room enterable from the left without softlocking the boss
        cls._fix_bathin_left_entrance()
        #Each area has limitations as to where it can be displayed on the canvas
        #Change area IDs based on their X positions so that everything is always displayed
        for room in Data.datatable["PB_DT_RoomMaster"]:
            if   Data.datatable["PB_DT_RoomMaster"][room]["OffsetX"] < 214.2:
                Data.datatable["PB_DT_RoomMaster"][room]["AreaID"] = "EAreaID::m01SIP"
            elif Data.datatable["PB_DT_RoomMaster"][room]["OffsetX"] + Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"]*12.6 > 1108.8:
                Data.datatable["PB_DT_RoomMaster"][room]["AreaID"] = "EAreaID::m13ARC"
            else:
                Data.datatable["PB_DT_RoomMaster"][room]["AreaID"] = "EAreaID::m03ENT"

    @classmethod
    def update_map_doors(cls):
        #Place doors next to their corresponding transitions if the adjacent room is of a special type
        #Do this even for the default map as some rooms are missing boss doors
        #Boss doors
        #Remove originals
        for room in _BOSS_DOOR_ROOMS:
            cls.remove_level_class(Room._get_gimmick_filename(room), "PBBossDoor_BP_C")
        cls.remove_level_class("m20JRN_004_Setting", "PBBossDoor_BP_C")
        #Add new
        for room in _ROOM_TO_BOSS:
            for entrance in cls.map_connections[room]:
                for exit in cls.map_connections[room][entrance]:
                    if cls._cannot_add_actor_to_door(exit):
                        continue
                    #One of the Journey rooms has a faulty persistent level export in its gimmick file, so add in its bg file instead
                    filename = "m20JRN_002_BG" if cls.door_string_to_door[exit].room == "m20JRN_002" else cls._get_gimmick_filename(cls.door_string_to_door[exit].room)
                    #Offset the door for Journey
                    x_offset = 180 if cls.door_string_to_door[exit].room == "m20JRN_004" else -60 if "m20JRN" in cls.door_string_to_door[exit].room else 0
                    location = FVector(x_offset, 0, 0)
                    rotation = FRotator(0, 0, 0)
                    scale    = FVector(1, 3, 1)
                    properties = {}
                    properties["BossID"] = FName.FromString(Data.game_data[filename], _ROOM_TO_BOSS[room])
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT, Direction.LEFT_BOTTOM, Direction.LEFT_TOP]:
                        rotation.Yaw = -180
                        properties["IsRight"] = False
                        if exit in _ARCHED_DOORS:
                            rotation.Yaw += 15
                    if cls.door_string_to_door[exit].direction_part in [Direction.RIGHT, Direction.RIGHT_BOTTOM, Direction.RIGHT_TOP]:
                        location.X = Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["AreaWidthSize"]*1260 - x_offset
                        properties["IsRight"] = True
                        if exit in _ARCHED_DOORS:
                            rotation.Yaw -= 15
                    location.Z = cls.door_string_to_door[exit].z_block*720 + 240.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_BOTTOM, Direction.RIGHT_BOTTOM]:
                        location.Z -= 180.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_TOP, Direction.RIGHT_TOP]:
                        location.Z += 180.0
                    cls.add_level_actor(filename, "PBBossDoor_BP_C", location, rotation, scale, properties)
                    cls._clear_door_exit(exit, True)
        #Backer doors
        #Remove originals
        for room in _BACKER_DOOR_ROOMS:
            cls.remove_level_class(cls._get_gimmick_filename(room), "PBBakkerDoor_BP_C")
        #Add new
        for room in _ROOM_TO_BACKER:
            for entrance in cls.map_connections[room]:
                for exit in cls.map_connections[room][entrance]:
                    if cls._cannot_add_actor_to_door(exit):
                        continue
                    filename = cls._get_gimmick_filename(cls.door_string_to_door[exit].room)
                    location = FVector(0, 0, 0)
                    rotation = FRotator(0, 0, 0)
                    scale    = FVector(1, 3, 1)
                    properties = {}
                    properties["BossID"]     = FName.FromString(Data.game_data[filename], _ROOM_TO_BACKER[room][0])
                    properties["KeyItemID"]  = FName.FromString(Data.game_data[filename], "Keyofbacker" + str(_ROOM_TO_BACKER[room][1]))
                    properties["TutorialID"] = FName.FromString(Data.game_data[filename], "KeyDoor" + "{:02x}".format(_ROOM_TO_BACKER[room][1]))
                    if _ROOM_TO_BACKER[room][0] == "None":
                        properties["IsMusicBoxRoom"] =  True
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT, Direction.LEFT_BOTTOM, Direction.LEFT_TOP]:
                        rotation.Yaw = -180
                        if exit in _ARCHED_DOORS:
                            rotation.Yaw += 15
                    if cls.door_string_to_door[exit].direction_part in [Direction.RIGHT, Direction.RIGHT_BOTTOM, Direction.RIGHT_TOP]:
                        location.X = Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["AreaWidthSize"]*1260
                        if exit in _ARCHED_DOORS:
                            rotation.Yaw -= 15
                    location.Z = cls.door_string_to_door[exit].z_block*720 + 240.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_BOTTOM, Direction.RIGHT_BOTTOM]:
                        location.Z -= 180.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_TOP, Direction.RIGHT_TOP]:
                        location.Z += 180.0
                    cls.add_level_actor(filename, "PBBakkerDoor_BP_C", location, rotation, scale, properties)
                    cls._clear_door_exit(exit, True)
        #Area doors
        #Remove originals
        for room in _AREA_DOOR_ROOMS:
            cls.remove_level_class(cls._get_gimmick_filename(room), "BP_AreaDoor_C")
        #Add new
        doors_done = []
        for room in Data.datatable["PB_DT_RoomMaster"]:
            if Data.datatable["PB_DT_RoomMaster"][room]["RoomType"] != "ERoomType::Load" or room == "m03ENT_1200":
                continue
            for entrance in cls.map_connections[room]:
                for exit in cls.map_connections[room][entrance]:
                    if cls._cannot_add_actor_to_door(exit):
                        continue
                    if exit in doors_done or exit in _ARCHED_DOORS or exit in _TRANSITIONLESS_DOORS:
                        continue
                    #If the door is too close to a cutscene disable the event to prevent softlocks
                    if cls.door_string_to_door[exit].room == "m03ENT_006":
                        Data.datatable["PB_DT_EventFlagMaster"]["Event_05_001_0000"]["Id"] = Data.datatable["PB_DT_EventFlagMaster"]["Event_01_001_0000"]["Id"]
                    if exit == "ARC_001_0_0_LEFT":
                        Data.datatable["PB_DT_EventFlagMaster"]["Event_09_001_0000"]["Id"] = Data.datatable["PB_DT_EventFlagMaster"]["Event_01_001_0000"]["Id"]
                    if exit == "TAR_000_0_0_LEFT":
                        Data.datatable["PB_DT_EventFlagMaster"]["Event_12_001_0000"]["Id"] = Data.datatable["PB_DT_EventFlagMaster"]["Event_01_001_0000"]["Id"]
                    filename = cls._get_gimmick_filename(cls.door_string_to_door[exit].room)
                    x_offset = 40
                    location = FVector(x_offset, -180, 0)
                    rotation = FRotator(0, 0, 0)
                    scale    = FVector(1, 1, 1)
                    class_name = ""
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT, Direction.LEFT_BOTTOM, Direction.LEFT_TOP]:
                        class_name = "BP_AreaDoor_C(Left)"
                    if cls.door_string_to_door[exit].direction_part in [Direction.RIGHT, Direction.RIGHT_BOTTOM, Direction.RIGHT_TOP]:
                        location.X = Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["AreaWidthSize"]*1260 - x_offset
                        class_name = "BP_AreaDoor_C(Right)"
                    location.Z = cls.door_string_to_door[exit].z_block*720 + 240.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_BOTTOM, Direction.RIGHT_BOTTOM]:
                        location.Z -= 180.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_TOP, Direction.RIGHT_TOP]:
                        location.Z += 180.0
                    #If the door should remain open replace it with a regular event door
                    if exit in _OPEN_TRANSITION_DOORS:
                        scale.Y = 1/3
                        rotation.Yaw += -90 if "Left" in class_name else 90
                        lever_index = len(Data.game_data[filename].Exports) + 1
                        cls.add_level_actor(filename, "BP_SwitchDoor_C", location, rotation, scale, {"GimmickFlag": FName.FromString(Data.game_data[filename], "None")})
                        Data.game_data[filename].Exports[lever_index].Data[2].Value[0].Value = FVector(0, -600, 0)
                    else:
                        cls.add_level_actor(filename, class_name, location, rotation, scale, {"IsInvertingOpen": False})
                        #If the door is a breakable wall we don't want the area door to overlay it, so break it by default
                        if exit in _WALL_TO_GIMMICK_FLAG:
                            Data.datatable["PB_DT_GimmickFlagMaster"][_WALL_TO_GIMMICK_FLAG[exit]]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
                        #If the entrance has very little floor add a wooden platform to avoid softlocks
                        if exit in _FLOORLESS_DOORS:
                            platform_location = FVector(0, -250, location.Z - 20)
                            platform_rotation = FRotator(0, 0, 0)
                            platform_scale    = FVector(12/11, 1, 1)
                            platform_location.X = location.X + 35 if "Left" in class_name else location.X - 35 - 120*12/11
                            cls.add_level_actor(filename, "UGD_WeakPlatform_C", platform_location, platform_rotation, platform_scale, {"SecondsToDestroy": 9999.0})
                    cls._clear_door_exit(exit, True)
                    #Since transition rooms are double make sure that a door only gets added once
                    doors_done.append(exit)

    @classmethod
    def update_map_indicators(cls):
        #Place a bookshelf in front of every save and warp point to make map traversal easier
        #Only do it for custom maps as the default map already has bookshelves with text
        #Remove originals
        for room in _BOOKSHELF_ROOMS:
            cls.remove_level_class(cls._get_gimmick_filename(room), "ReadableBookShelf_C")
        #Add new
        doors_done = []
        for room in Data.datatable["PB_DT_RoomMaster"]:
            if Data.datatable["PB_DT_RoomMaster"][room]["RoomType"] != "ERoomType::Save" and Data.datatable["PB_DT_RoomMaster"][room]["RoomType"] != "ERoomType::Warp":
                continue
            for entrance in cls.map_connections[room]:
                for exit in cls.map_connections[room][entrance]:
                    if cls._cannot_add_actor_to_door(exit):
                        continue
                    if exit in ["VIL_005_0_0_RIGHT", "VIL_006_0_1_LEFT"]:
                        continue
                    filename = cls._get_gimmick_filename(cls.door_string_to_door[exit].room)
                    location = FVector(-80, -120, 0)
                    rotation = FRotator(0, 0, 0)
                    scale    = FVector(1, 1, 1)
                    properties = {}
                    properties["DiaryID"] = FName.FromString(Data.game_data[filename], "None")
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT, Direction.LEFT_BOTTOM, Direction.LEFT_TOP]:
                        rotation.Yaw = -30
                    if cls.door_string_to_door[exit].direction_part in [Direction.RIGHT, Direction.RIGHT_BOTTOM, Direction.RIGHT_TOP]:
                        location.X = Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["AreaWidthSize"]*1260 - 50
                        rotation.Yaw = 30
                    location.Z = cls.door_string_to_door[exit].z_block*720 + 240.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_BOTTOM, Direction.RIGHT_BOTTOM]:
                        location.Z -= 180.0
                    if cls.door_string_to_door[exit].direction_part in [Direction.LEFT_TOP, Direction.RIGHT_TOP]:
                        location.Z += 180.0
                    cls.add_level_actor(filename, "ReadableBookShelf_C", location, rotation, scale, properties)
                    cls._clear_door_exit(exit, False)
        #Fill empty entrances with an impassable door to prevent softlocks
        #Add new
        door_height = 240
        door_width = 44
        for room in cls.map_connections:
            for door in cls.map_connections[room]:
                if cls.map_connections[room][door]:
                    continue
                if cls._cannot_add_actor_to_door(door):
                    continue
                filename = cls._get_gimmick_filename(room)
                location = FVector(0, -360, 0)
                rotation = FRotator(0, 0, 0)
                scale    = FVector(1, 1, 1)
                #Global direction
                if cls.door_string_to_door[door].direction_part in [Direction.LEFT, Direction.LEFT_BOTTOM, Direction.LEFT_TOP]:
                    location.X = -18
                    location.Z = cls.door_string_to_door[door].z_block*720 + door_height
                    lever_offset = -360
                    if door in _ARCHED_DOORS:
                        rotation.Yaw += 20
                if cls.door_string_to_door[door].direction_part in [Direction.RIGHT, Direction.RIGHT_BOTTOM, Direction.RIGHT_TOP]:
                    location.X = Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"]*1260 + 18
                    location.Z = cls.door_string_to_door[door].z_block*720 + door_height
                    lever_offset = 360
                    if door in _ARCHED_DOORS:
                        rotation.Yaw -= 20
                if cls.door_string_to_door[door].direction_part in [Direction.TOP, Direction.TOP_LEFT, Direction.TOP_RIGHT]:
                    location.X = cls.door_string_to_door[door].x_block*1260 + 510.0
                    location.Z = Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"]*720 - 5
                    rotation.Pitch = -90
                    lever_offset = -360
                if cls.door_string_to_door[door].direction_part in [Direction.BOTTOM, Direction.BOTTOM_LEFT, Direction.BOTTOM_RIGHT]:
                    location.X = cls.door_string_to_door[door].x_block*1260 + 510.0
                    location.Z = 5
                    rotation.Pitch = -90
                    lever_offset = 360
                #Sub direction
                if cls.door_string_to_door[door].direction_part in [Direction.LEFT_BOTTOM, Direction.RIGHT_BOTTOM]:
                    if "m10BIG" in room:
                        location.Z -= door_height
                    elif "_".join([room[3:], str(cls.door_string_to_door[door].x_block), str(cls.door_string_to_door[door].z_block), cls.door_string_to_door[door].direction_part.name.split("_")[0]]) in cls.map_connections[room]:
                        location.Z -= door_height
                        scale.X = 4.25
                        scale.Z = 4.25
                        direction = -1 if cls.door_string_to_door[door].direction_part == Direction.LEFT_BOTTOM else 1
                        location.X += direction*((door_width*scale.Z - door_width)/2 - door_width)
                        location.Z -= door_height*scale.Z - door_height
                    else:
                        location.Z -= 180
                if cls.door_string_to_door[door].direction_part in [Direction.LEFT_TOP, Direction.RIGHT_TOP]:
                    if "m10BIG" in room:
                        location.Z += door_height
                    elif "_".join([room[3:], str(cls.door_string_to_door[door].x_block), str(cls.door_string_to_door[door].z_block), cls.door_string_to_door[door].direction_part.name.split("_")[0]]) in cls.map_connections[room]:
                        location.Z += door_height
                        scale.X = 4.25
                        scale.Z = 4.25
                        direction = -1 if cls.door_string_to_door[door].direction_part == Direction.LEFT_TOP else 1
                        location.X += direction*((door_width*scale.Z - door_width)/2 - door_width)
                    else:
                        location.Z += 180
                if cls.door_string_to_door[door].direction_part in [Direction.TOP_LEFT, Direction.BOTTOM_LEFT]:
                    location.X -= 510 if "m10BIG" in room else 370
                if cls.door_string_to_door[door].direction_part in [Direction.TOP_RIGHT, Direction.BOTTOM_RIGHT]:
                    location.X += 510 if "m10BIG" in room else 370
                lever_index = len(Data.game_data[filename].Exports) + 1
                Room.add_level_actor(filename, "BP_SwitchDoor_C", location, rotation, scale, {"GimmickFlag": FName.FromString(Data.game_data[filename], "None")})
                Data.game_data[filename].Exports[lever_index].Data[2].Value[0].Value = FVector(lever_offset, 360, 0)
                Room._clear_door_exit(door, False)

    @classmethod
    def _cannot_add_actor_to_door(cls, door):
        room = cls.door_string_to_door[door].room
        return door in _DOOR_SKIP or room in _ROOM_TO_BOSS or room in _ROOM_TO_BACKER or not room in Data.constant["RoomRequirement"]

    @staticmethod
    def _clear_door_exit(exit, heavy_door):
        #If the door is a breakable wall we don't want the backer door to overlay it, so break it by default
        if exit in _WALL_TO_GIMMICK_FLAG and heavy_door:
            Data.datatable["PB_DT_GimmickFlagMaster"][_WALL_TO_GIMMICK_FLAG[exit]]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
        #Remove the magic door in that one galleon room so that it never overlays with anything
        if exit == "SIP_002_0_0_RIGHT":
            Room.remove_level_class("m01SIP_002_Gimmick", "BP_MagicDoor_C")
    
    @classmethod
    def update_container_types(cls):
        for room in Data.constant["RoomRequirement"]:
            cls._update_room_containers(room)

    @classmethod
    def _update_room_containers(cls, room):
        filename = cls._get_gimmick_filename(room)
        if not filename in Data.game_data:
            return
        room_width = Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"]*1260
        for export_index in range(len(Data.game_data[filename].Exports)):
            old_class_name = str(Data.game_data[filename].Imports[abs(Data.game_data[filename].Exports[export_index].ClassIndex.Index) - 1].ObjectName)
            #Check if it is a golden chest
            if old_class_name == "PBEasyTreasureBox_BP_C" and str(Data.game_data[filename].Exports[export_index].Data[4].Name) == "IsAutoMaterial":
                old_class_name = "PBEasyTreasureBox_BP_C(Gold)"
            #Pure miriam is considered a different class but it's the same as regular chests
            if old_class_name == "PBPureMiriamTreasureBox_BP_C":
                old_class_name = "PBEasyTreasureBox_BP_C"
            if old_class_name in ["PBEasyTreasureBox_BP_C", "PBEasyTreasureBox_BP_C(Gold)", "HPMaxUp_C", "MPMaxUp_C", "BulletMaxUp_C"]:
                #Gather old actor properties
                location = FVector(0, 0, 0)
                rotation = FRotator(0, 0, 0)
                scale    = FVector(1, 1, 1)
                safety_chest = False
                gimmick_id = ""
                for data in Data.game_data[filename].Exports[export_index].Data:
                    if str(data.Name) in ["DropItemID", "DropRateID"]:
                        drop_id = str(data.Value)
                    if str(data.Name) == "IsRandomizerSafetyChest":
                        safety_chest = data.Value
                    if str(data.Name) == "OptionalGimmickID":
                        gimmick_id = str(data.Value)
                    if str(data.Name) == "RootComponent":
                        root_index = int(str(data.Value)) - 1
                        for root_data in Data.game_data[filename].Exports[root_index].Data:
                            if str(root_data.Name) == "RelativeLocation":
                                location = root_data.Value[0].Value
                            if str(root_data.Name) == "RelativeRotation":
                                rotation = root_data.Value[0].Value
                            if str(root_data.Name) == "RelativeScale3D":
                                scale    = root_data.Value[0].Value
                if not drop_id in Data.datatable["PB_DT_DropRateMaster"]:
                    continue
                if drop_id in cls.global_room_pickups:
                    continue
                if safety_chest:
                    continue
                if Data.datatable["PB_DT_DropRateMaster"][drop_id]["RareItemId"] == "MaxHPUP":
                    new_class_name = "HPMaxUp_C"
                elif Data.datatable["PB_DT_DropRateMaster"][drop_id]["RareItemId"] == "MaxMPUP":
                    new_class_name = "MPMaxUp_C"
                elif Data.datatable["PB_DT_DropRateMaster"][drop_id]["RareItemId"] == "MaxBulletUP":
                    new_class_name = "BulletMaxUp_C"
                elif Data.datatable["PB_DT_DropRateMaster"][drop_id]["RareItemId"] in KEY_ITEMS + ["Certificationboard"]:
                    new_class_name = "PBEasyTreasureBox_BP_C(Gold)"
                else:
                    new_class_name = "PBEasyTreasureBox_BP_C"
                #Check if container mismatches item type
                if old_class_name == new_class_name:
                    continue
                #Some upgrades in rotating rooms are on the wrong plane
                if room == "m02VIL_008":
                    location.X -= 50
                if drop_id == "Treasurebox_TWR017_6":
                    location.X -= 100
                #Correct container transform when necessary
                if "TreasureBox" in new_class_name and "MaxUp" in old_class_name or "MaxUp" in new_class_name and "TreasureBox" in old_class_name:
                    #If the room is a rotating 3d one then use the forward vector to shift position
                    if room in Room.ROTATING_ROOM_TO_CENTER and drop_id != "Treasurebox_TWR019_2":
                        rotation.Yaw = -math.degrees(math.atan2(location.X - Room.ROTATING_ROOM_TO_CENTER[room][0], location.Y - Room.ROTATING_ROOM_TO_CENTER[room][1]))
                        forward_vector = (math.sin(math.radians(rotation.Yaw))*(-1), math.cos(math.radians(rotation.Yaw)))
                        if "TreasureBox" in new_class_name:
                            location.X -= forward_vector[0]*120
                            location.Y -= forward_vector[1]*120
                        if "MaxUp" in new_class_name:
                            if drop_id in ["Treasurebox_TWR017_5", "Treasurebox_SND025_1"]:
                                location.X += forward_vector[0]*60
                                location.Y += forward_vector[1]*60
                            else:
                                location.X += forward_vector[0]*120
                                location.Y += forward_vector[1]*120
                    else:
                        if "TreasureBox" in new_class_name:
                            location.Y = -120
                            #Slightly rotate the chest to be facing the center of the room
                            if location.X < room_width*0.45:
                                rotation.Yaw = -30
                            elif location.X > room_width*0.55:
                                rotation.Yaw = 30
                            else:
                                rotation.Yaw = 0
                            #Drop chest down to the floor if it is in a bell
                            if drop_id == "Treasurebox_SAN003_4":
                                location.Z = 4080
                            if drop_id == "Treasurebox_SAN003_5":
                                location.Z = 6600
                            if drop_id == "Treasurebox_SAN019_3":
                                location.Z = 120
                            if drop_id == "Treasurebox_SAN021_4":
                                location.Z = 420
                        if "MaxUp" in new_class_name:
                            location.Y = 0
                            rotation.Yaw = 0
                            #If it used to be the chest under the bridge move it to Benjamin's room for the extra characters
                            if drop_id == "Treasurebox_JPN002_1":
                                location.X = 1860
                                location.Z = 60
                #Remove the old container
                Room.remove_level_actor(filename, export_index)
                #One of the Journey rooms has a faulty persistent level export in its gimmick file, so add in its bg file instead
                if room == "m20JRN_002":
                    filename = "m20JRN_002_BG"
                #Setup the actor properties
                properties = {}
                if "PBEasyTreasureBox_BP_C" in new_class_name:
                    properties["DropItemID"]   = FName.FromString(Data.game_data[filename], drop_id)
                    properties["ItemID"]       = FName.FromString(Data.game_data[filename], drop_id)
                    properties["TreasureFlag"] = FName.FromString(Data.game_data[filename], "EGameTreasureFlag::" + Utility.remove_inst_number(drop_id))
                    if gimmick_id:
                        properties["OptionalGimmickID"] = FName.FromString(Data.game_data[filename], gimmick_id)
                else:
                    properties["DropRateID"]   = FName.FromString(Data.game_data[filename], drop_id)
                Room.add_level_actor(filename, new_class_name, location, rotation, scale, properties)

    @classmethod
    def update_map_connections(cls):
        #The game map requires you to manually input a list of which rooms can be transitioned into from the current room
        #Doing this via the map editor would only add long load times upon saving a map so do it here instead
        #Fill same room field for rooms that are overlayed perfectly
        #Not sure if it serves any actual purpose in-game but it does help for the following adjacent room check
        for room_1 in Data.datatable["PB_DT_RoomMaster"]:
            Data.datatable["PB_DT_RoomMaster"][room_1]["SameRoom"] = "None"
            if Data.datatable["PB_DT_RoomMaster"][room_1]["OutOfMap"]:
                continue
            for room_2 in Data.datatable["PB_DT_RoomMaster"]:
                if Data.datatable["PB_DT_RoomMaster"][room_2]["OutOfMap"]:
                    continue
                if Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetX"] == Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetX"] and Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetZ"] == Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetZ"] and room_1 != room_2:
                    Data.datatable["PB_DT_RoomMaster"][room_1]["SameRoom"] = room_2
                    break
        is_vanilla_start = Data.datatable["PB_DT_RoomMaster"]["m03ENT_1200"]["SameRoom"] == "m02VIL_1200"
        #Fill adjacent room lists
        for room in Data.datatable["PB_DT_RoomMaster"]:
            Data.datatable["PB_DT_RoomMaster"][room]["AdjacentRoomName"].clear()
            open_doors = []
            for entrance in cls.map_connections[room]:
                for exit in cls.map_connections[room][entrance]:
                    #Transition rooms in Bloodstained come by pair, each belonging to an area
                    #Make it so that an area is only connected to its corresponding transition rooms when possible
                    #This avoids having the next area name tag show up within the transition
                    #With the exception of standalone transitions with no fallbacks as well as the first entrance transition fallback
                    if Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["RoomType"] == "ERoomType::Load" and cls.door_string_to_door[exit].room[0:6] != room[0:6] and Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["SameRoom"] != "None":
                        if is_vanilla_start or cls.door_string_to_door[exit].room != "m02VIL_1200" and Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["SameRoom"] != "m03ENT_1200":
                            continue
                    #The first entrance transition room is hardcoded to bring you back to the village regardless of its position on the canvas
                    #Ignore that room and don't connect it to anything
                    #Meanwhile the village version of that transition is always needed to trigger the curved effect of the following bridge room
                    #So ignore any other transitions overlayed on top of it
                    if not is_vanilla_start and (Data.datatable["PB_DT_RoomMaster"][cls.door_string_to_door[exit].room]["SameRoom"] == "m02VIL_1200" or cls.door_string_to_door[exit].room == "m03ENT_1200"):
                        continue
                    if not cls.door_string_to_door[exit].room in Data.datatable["PB_DT_RoomMaster"][room]["AdjacentRoomName"]:
                        Data.datatable["PB_DT_RoomMaster"][room]["AdjacentRoomName"].append(cls.door_string_to_door[exit].room)
                #Update door list
                if cls.map_connections[room][entrance]:
                    open_doors.append(cls.door_string_to_door[entrance])
            Data.datatable["PB_DT_RoomMaster"][room]["DoorFlag"] = cls._convert_door_to_flag(open_doors, Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"])
        #Some rooms need specific setups
        #Vepar room
        Data.datatable["PB_DT_RoomMaster"]["m01SIP_022"]["AdjacentRoomName"].append("m02VIL_000")
        #Tower rooms
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_000"]["AdjacentRoomName"].append("m08TWR_017")
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_005"]["AdjacentRoomName"].append("m08TWR_018")
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_006"]["AdjacentRoomName"].append("m08TWR_018")
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_016"]["AdjacentRoomName"].append("m08TWR_019")
        
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_017"]["AdjacentRoomName"].append("m08TWR_000")
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_018"]["AdjacentRoomName"].append("m08TWR_005")
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_018"]["AdjacentRoomName"].append("m08TWR_006")
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_019"]["AdjacentRoomName"].append("m08TWR_016")
        
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_000"]["DoorFlag"].insert(0, 1)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_000"]["DoorFlag"].insert(0, 1)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_005"]["DoorFlag"].append(4)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_005"]["DoorFlag"].append(4)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_006"]["DoorFlag"].insert(0, 1)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_006"]["DoorFlag"].insert(0, 1)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_016"]["DoorFlag"].insert(0, 4)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_016"]["DoorFlag"].insert(0, 2)
        
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_017"]["DoorFlag"].append(18)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_017"]["DoorFlag"].append(8)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_018"]["DoorFlag"].append(3)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_018"]["DoorFlag"].append(2)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_018"]["DoorFlag"].append(34)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_018"]["DoorFlag"].append(8)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_019"]["DoorFlag"].append(39)
        Data.datatable["PB_DT_RoomMaster"]["m08TWR_019"]["DoorFlag"].append(8)
        #Train rooms
        Data.datatable["PB_DT_RoomMaster"]["m09TRN_001"]["AdjacentRoomName"].append("m09TRN_002")
        Data.datatable["PB_DT_RoomMaster"]["m09TRN_002"]["AdjacentRoomName"].append("m09TRN_001")
        Data.datatable["PB_DT_RoomMaster"]["m09TRN_002"]["AdjacentRoomName"].append("m09TRN_003")
        Data.datatable["PB_DT_RoomMaster"]["m09TRN_003"]["AdjacentRoomName"].append("m09TRN_002")
        #Garden Den
        Data.datatable["PB_DT_RoomMaster"]["m04GDN_001"]["AdjacentRoomName"].append("m10BIG_000")
        Data.datatable["PB_DT_RoomMaster"]["m10BIG_000"]["AdjacentRoomName"].append("m04GDN_001")
        #Extra mode rooms
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_000"]["AdjacentRoomName"].append("m53BRV_001")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_001"]["AdjacentRoomName"].append("m53BRV_002")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_001"]["AdjacentRoomName"].append("m53BRV_022")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_002"]["AdjacentRoomName"].append("m53BRV_003")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_022"]["AdjacentRoomName"].append("m53BRV_003")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_003"]["AdjacentRoomName"].append("m53BRV_004")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_003"]["AdjacentRoomName"].append("m53BRV_024")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_004"]["AdjacentRoomName"].append("m53BRV_005")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_024"]["AdjacentRoomName"].append("m53BRV_005")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_005"]["AdjacentRoomName"].append("m53BRV_026")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_026"]["AdjacentRoomName"].append("m53BRV_101")
        Data.datatable["PB_DT_RoomMaster"]["m53BRV_026"]["AdjacentRoomName"].append("m53BRV_121")
        
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_000"]["AdjacentRoomName"].append("m50BRM_001")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_020"]["AdjacentRoomName"].append("m50BRM_001")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_001"]["AdjacentRoomName"].append("m50BRM_002")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_001"]["AdjacentRoomName"].append("m50BRM_022")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_002"]["AdjacentRoomName"].append("m50BRM_003")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_022"]["AdjacentRoomName"].append("m50BRM_003")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_003"]["AdjacentRoomName"].append("m50BRM_004")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_003"]["AdjacentRoomName"].append("m50BRM_024")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_004"]["AdjacentRoomName"].append("m50BRM_005")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_024"]["AdjacentRoomName"].append("m50BRM_005")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_005"]["AdjacentRoomName"].append("m50BRM_006")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_005"]["AdjacentRoomName"].append("m50BRM_026")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_006"]["AdjacentRoomName"].append("m50BRM_007")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_026"]["AdjacentRoomName"].append("m50BRM_007")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_007"]["AdjacentRoomName"].append("m50BRM_008")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_007"]["AdjacentRoomName"].append("m50BRM_028")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_008"]["AdjacentRoomName"].append("m50BRM_009")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_028"]["AdjacentRoomName"].append("m50BRM_009")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_009"]["AdjacentRoomName"].append("m50BRM_101")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_009"]["AdjacentRoomName"].append("m50BRM_121")
        
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_050"]["AdjacentRoomName"].append("m50BRM_051")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_070"]["AdjacentRoomName"].append("m50BRM_051")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_051"]["AdjacentRoomName"].append("m50BRM_052")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_051"]["AdjacentRoomName"].append("m50BRM_072")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_052"]["AdjacentRoomName"].append("m50BRM_053")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_072"]["AdjacentRoomName"].append("m50BRM_053")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_053"]["AdjacentRoomName"].append("m50BRM_054")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_053"]["AdjacentRoomName"].append("m50BRM_074")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_054"]["AdjacentRoomName"].append("m50BRM_055")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_074"]["AdjacentRoomName"].append("m50BRM_055")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_055"]["AdjacentRoomName"].append("m50BRM_056")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_055"]["AdjacentRoomName"].append("m50BRM_076")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_056"]["AdjacentRoomName"].append("m50BRM_057")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_076"]["AdjacentRoomName"].append("m50BRM_057")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_057"]["AdjacentRoomName"].append("m50BRM_058")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_057"]["AdjacentRoomName"].append("m50BRM_078")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_058"]["AdjacentRoomName"].append("m50BRM_059")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_078"]["AdjacentRoomName"].append("m50BRM_059")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_059"]["AdjacentRoomName"].append("m50BRM_151")
        Data.datatable["PB_DT_RoomMaster"]["m50BRM_059"]["AdjacentRoomName"].append("m50BRM_171")
        #Give overlayed rooms the same door flag as their counterparts
        Data.datatable["PB_DT_RoomMaster"]["m01SIP_022"]["DoorFlag"] = Data.datatable["PB_DT_RoomMaster"]["m02VIL_000"]["DoorFlag"]
        Data.datatable["PB_DT_RoomMaster"]["m18ICE_020"]["DoorFlag"] = Data.datatable["PB_DT_RoomMaster"]["m18ICE_019"]["DoorFlag"]
        #Update out of map based on accessible rooms
        for room in Data.datatable["PB_DT_RoomMaster"]:
            Data.datatable["PB_DT_RoomMaster"][room]["OutOfMap"] = True
        current_rooms = ["m01SIP_000"]
        while current_rooms:
            for room in current_rooms:
                Data.datatable["PB_DT_RoomMaster"][room]["OutOfMap"] = False
            current_rooms_copy = copy.deepcopy(current_rooms)
            for room_1 in current_rooms_copy:
                for room_2 in Data.datatable["PB_DT_RoomMaster"][room_1]["AdjacentRoomName"]:
                    if Data.datatable["PB_DT_RoomMaster"][room_2]["OutOfMap"]:
                        current_rooms.append(room_2)
                current_rooms.remove(room_1)
            current_rooms = list(dict.fromkeys(current_rooms))
        #Fix bad ending cutscene not transitioning to the village
        if not "m02VIL_099" in Data.datatable["PB_DT_RoomMaster"]["m06KNG_020"]["AdjacentRoomName"]:
            Data.datatable["PB_DT_RoomMaster"]["m06KNG_020"]["AdjacentRoomName"].append("m02VIL_099")
        #Fix good ending cutscene not transitioning to the village
        if not "m02VIL_099" in Data.datatable["PB_DT_RoomMaster"]["m18ICE_019"]["AdjacentRoomName"]:
            Data.datatable["PB_DT_RoomMaster"]["m18ICE_019"]["AdjacentRoomName"].append("m02VIL_099")

    @classmethod
    def _fix_bathin_left_entrance(cls):
        #If Bathin's intro event triggers when the player entered the room from the left they will be stuck in an endless walk cycle
        #To fix this add a special door to warp the player in the room's player start instead
        for door in cls.map_connections["m13ARC_005"]["ARC_005_0_0_LEFT"]:
            room = cls.door_string_to_door[door].room
            area_path = "ACT" + room[1:3] + "_" + room[3:6]
            new_file = UAsset(ASSETS_DIR + "\\" + Data.file_to_path["m02VIL_012_RV"] + "\\m02VIL_012_RV.umap", EngineVersion.VER_UE4_22)
            index = new_file.SearchNameReference(FString("m02VIL_012_RV"))
            new_file.SetNameReference(index, FString(room + "_RV"))
            index = new_file.SearchNameReference(FString("/Game/Core/Environment/ACT02_VIL/Level/m02VIL_012_RV"))
            new_file.SetNameReference(index, FString("/Game/Core/Environment/" + area_path + "/Level/" + room + "_RV"))
            new_file.Exports[9].Data[1].Value = FName.FromString(new_file, room)
            #Correct the room dimension settings
            new_file.Exports[0].Data[2].Value[0].Value  = FVector( 630*Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"],   0, 360*Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"])
            new_file.Exports[0].Data[3].Value[0].Value  = FVector(1260*Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"], 720, 720*Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"])
            new_file.Exports[12].Data[0].Value[0].Value = FVector(  21*Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"],  12,  12*Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"])
            #Change the door's properties
            new_file.Exports[2].Data[0].Value[0].Value  = FVector(1260*Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"], 0, 720*cls.door_string_to_door[door].z_block + 360)
            new_file.Exports[2].Data[1].Value[0].Value  = FRotator(0, 0, 0)
            new_file.Exports[8].Data[0].Value = FName.FromString(new_file, room[3:])
            new_file.Exports[8].Data[1].Value = FName.FromString(new_file, "dummy")
            new_file.Exports[8].Data[2].Value = FName.FromString(new_file, "dummy")
            new_file.Exports[8].Data[3].Value = FName.FromString(new_file, "m13ARC_005")
            new_file.Write(MOD_DIR + "\\Core\\Environment\\" + area_path + "\\Level\\" + room + "_RV.umap")
        adjacent_room = None
        #Get Bathin's adjacent room while prioritizing the same area
        for door in cls.map_connections["m13ARC_005"]["ARC_005_0_0_LEFT"]:
            room = cls.door_string_to_door[door].room
            adjacent_room = room
            if Data.datatable["PB_DT_RoomMaster"][room]["AreaID"] == Data.datatable["PB_DT_RoomMaster"]["m13ARC_005"]["AreaID"]:
                break
        #Add one more door in the boss room to have a proper transition
        if adjacent_room:
            room = "m13ARC_005"
            area_path = "ACT" + room[1:3] + "_" + room[3:6]
            new_file = UAsset(f"{ASSETS_DIR}\\" + Data.file_to_path["m02VIL_012_RV"] + "\\m02VIL_012_RV.umap", EngineVersion.VER_UE4_22)
            index = new_file.SearchNameReference(FString("m02VIL_012_RV"))
            new_file.SetNameReference(index, FString(f"{room}_RV"))
            index = new_file.SearchNameReference(FString("/Game/Core/Environment/ACT02_VIL/Level/m02VIL_012_RV"))
            new_file.SetNameReference(index, FString(f"/Game/Core/Environment/{area_path}/Level/{room}_RV"))
            new_file.Exports[9].Data[1].Value = FName.FromString(new_file, room)
            #Correct the room dimension settings
            new_file.Exports[0].Data[2].Value[0].Value  = FVector( 630*Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"],   0, 360*Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"])
            new_file.Exports[0].Data[3].Value[0].Value  = FVector(1260*Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"], 720, 720*Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"])
            new_file.Exports[12].Data[0].Value[0].Value = FVector(  21*Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"],  12,  12*Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"])
            #Change the door's properties
            new_file.Exports[2].Data[0].Value[0].Value  = FVector(0, 0, 360)
            new_file.Exports[2].Data[1].Value[0].Value  = FRotator(0, 0, 0)
            new_file.Exports[8].Data[0].Value = FName.FromString(new_file, "ARC_005")
            new_file.Exports[8].Data[1].Value = FName.FromString(new_file, adjacent_room[3:])
            new_file.Exports[8].Data[2].Value = FName.FromString(new_file, adjacent_room[3:])
            new_file.Exports[8].Data[3].Value = FName.FromString(new_file, adjacent_room)
            new_file.Write(f"{MOD_DIR}\\Core\\Environment\\{area_path}\\Level\\{room}_RV.umap")

    @classmethod
    def add_global_room_pickup(cls, room : str, drop_id : str):
        #Place an upgrade in a room at its origin
        room_width  = Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"]*1260
        room_height = Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"]*720
        filename = cls._get_gimmick_filename(room)
        actor_index = len(Data.game_data[filename].Exports)
        cls.add_level_actor(filename, "HPMaxUp_C", FVector(0, 0, 0), FRotator(0, 0, 0), FVector(1, 1, 1), {"DropRateID": FName.FromString(Data.game_data[filename], drop_id)})
        #Enlarge its hitbox considerably so that entering the room from anywhere will collect it
        struct = StructPropertyData(FName.FromString(Data.game_data[filename], "BoxExtent"), FName.FromString(Data.game_data[filename], "Vector"))
        sub_struct = VectorPropertyData(FName.FromString(Data.game_data[filename], "BoxExtent"))
        sub_struct.Value = FVector((room_width + 120)*4, 50, (room_height + 120)*4)
        struct.Value.Add(sub_struct)
        Data.game_data[filename].Exports[actor_index + 1].Data.Add(struct)
        #Keep it in mind to not update its container type
        cls.global_room_pickups.append(drop_id)

    @staticmethod
    def add_game_room(room):
        area_path = "ACT" + room[1:3] + "_" + room[3:6]
        new_file = UAsset(ASSETS_DIR + "\\" + Data.file_to_path["m01SIP_1000_RV"] + "\\m01SIP_1000_RV.umap", EngineVersion.VER_UE4_22)
        index = new_file.SearchNameReference(FString("m01SIP_1000_RV"))
        new_file.SetNameReference(index, FString(f"{room}_RV"))
        index = new_file.SearchNameReference(FString("/Game/Core/Environment/ACT01_SIP/Level/m01SIP_1000_RV"))
        new_file.SetNameReference(index, FString(f"/Game/Core/Environment/{area_path}/Level/{room}_RV"))
        new_file.Exports[5].Data[1].Value = FName.FromString(new_file, room)
        new_file.Write(f"{MOD_DIR}\\Core\\Environment\\{area_path}\\Level\\{room}_RV.umap")

    @staticmethod
    def add_level_actor(filename, actor_class, location, rotation, scale, properties):
        actor_index = len(Data.game_data[filename].Exports)
        #Name the new actor based on the class
        short_class = actor_class.replace(")", "").split("(")[0]
        short_class = short_class.split("_")
        if short_class[-1] == "C":
            short_class.pop()
        short_class = "_".join(short_class)
        actor_name = _CUSTOM_ACTOR_PREFIX + short_class
        snippet = UAssetSnippet(Data.game_data[Data.constant["ActorPointer"][actor_class]["File"]], Data.constant["ActorPointer"][actor_class]["Index"])
        snippet.AddToUAsset(Data.game_data[filename], actor_name)
        #Change class parameters
        for data in Data.game_data[filename].Exports[actor_index].Data:
            if str(data.Name) in properties:
                Utility.unreal_to_unreal_data(properties[str(data.Name)], data)
                del properties[str(data.Name)]
            if str(data.Name) == "ActorLabel":
                data.Value = FString(Utility.remove_inst_number(actor_name))
            if str(data.Name) == "RootComponent":
                root_index = int(str(data.Value)) - 1
                Data.game_data[filename].Exports[root_index].Data.Clear()
                if location.X != 0 or location.Y != 0 or location.Z != 0:
                    struct = StructPropertyData(FName.FromString(Data.game_data[filename], "RelativeLocation"), FName.FromString(Data.game_data[filename], "Vector"))
                    sub_struct = VectorPropertyData(FName.FromString(Data.game_data[filename], "RelativeLocation"))
                    sub_struct.Value = FVector(location.X, location.Y, location.Z)
                    struct.Value.Add(sub_struct)
                    Data.game_data[filename].Exports[root_index].Data.Add(struct)
                if rotation.Pitch != 0 or rotation.Yaw != 0 or rotation.Roll != 0:
                    struct = StructPropertyData(FName.FromString(Data.game_data[filename], "RelativeRotation"), FName.FromString(Data.game_data[filename], "Rotator"))
                    sub_struct = RotatorPropertyData(FName.FromString(Data.game_data[filename], "RelativeRotation"))
                    sub_struct.Value = FRotator(rotation.Pitch, rotation.Yaw, rotation.Roll)
                    struct.Value.Add(sub_struct)
                    Data.game_data[filename].Exports[root_index].Data.Add(struct)
                if scale.X != 1 or scale.Y != 1 or scale.Z != 1:
                    struct = StructPropertyData(FName.FromString(Data.game_data[filename], "RelativeScale3D"), FName.FromString(Data.game_data[filename], "Vector"))
                    sub_struct = VectorPropertyData(FName.FromString(Data.game_data[filename], "RelativeScale3D"))
                    sub_struct.Value = FVector(scale.X, scale.Y, scale.Z)
                    struct.Value.Add(sub_struct)
                    Data.game_data[filename].Exports[root_index].Data.Add(struct)
        #Add parameters that are missing
        for data in properties:
            if type(properties[data]) is bool:
                struct = BoolPropertyData(FName.FromString(Data.game_data[filename], data))
                struct.Value = properties[data]
            elif type(properties[data]) is int:
                struct = IntPropertyData(FName.FromString(Data.game_data[filename], data))
                struct.Value = properties[data]
            elif type(properties[data]) is float:
                struct = FloatPropertyData(FName.FromString(Data.game_data[filename], data))
                struct.Value = properties[data]
            elif "::" in str(properties[data]):
                struct = BytePropertyData(FName.FromString(Data.game_data[filename], data))
                struct.ByteType = BytePropertyType.FName
                struct.EnumType = FName.FromString(Data.game_data[filename], str(properties[data]).split("::")[0])
                struct.EnumValue = properties[data]
            else:
                struct = NamePropertyData(FName.FromString(Data.game_data[filename], data))
                struct.Value = properties[data]
            Data.game_data[filename].AddNameReference(struct.PropertyType)
            Data.game_data[filename].Exports[actor_index].Data.Add(struct)
        #Temporary Rocky fix
        if actor_class == "Chr_N3115_C":
            Room.remove_level_actor(filename, actor_index + 59)
            Data.game_data[filename].Exports[actor_index + 59].OuterIndex = FPackageIndex(actor_index + 43)

    @staticmethod
    def add_extra_mode_warp(filename, warp_1_location, warp_1_rotation, warp_2_location, warp_2_rotation):
        warp_1_index = len(Data.game_data[filename].Exports)
        Room.add_level_actor(filename, "ToriiWarp_BP_C", warp_1_location, warp_1_rotation, FVector(1, 1, 1), {})
        warp_2_index = int(str(Data.game_data[filename].Exports[warp_1_index].Data[12].Value)) - 1
        root_index = int(str(Data.game_data[filename].Exports[warp_2_index].Data[14].Value)) - 1
        Data.game_data[filename].Exports[root_index].Data.Clear()
        if warp_2_location.X != 0 or warp_2_location.Y != 0 or warp_2_location.Z != 0:
            struct = StructPropertyData(FName.FromString(Data.game_data[filename], "RelativeLocation"), FName.FromString(Data.game_data[filename], "Vector"))
            sub_struct = VectorPropertyData(FName.FromString(Data.game_data[filename], "RelativeLocation"))
            sub_struct.Value = warp_2_location
            struct.Value.Add(sub_struct)
            Data.game_data[filename].Exports[root_index].Data.Add(struct)
        if warp_2_rotation.Pitch != 0 or warp_2_rotation.Yaw != 0 or warp_2_rotation.Roll != 0:
            struct = StructPropertyData(FName.FromString(Data.game_data[filename], "RelativeRotation"), FName.FromString(Data.game_data[filename], "Rotator"))
            sub_struct = RotatorPropertyData(FName.FromString(Data.game_data[filename], "RelativeRotation"))
            sub_struct.Value = warp_2_rotation
            struct.Value.Add(sub_struct)
            Data.game_data[filename].Exports[root_index].Data.Add(struct)
        warp_1_event_index = int(str(Data.game_data[filename].Exports[warp_1_index].Data[3].Value)) - 1
        warp_2_event_index = int(str(Data.game_data[filename].Exports[warp_2_index].Data[3].Value)) - 1
        Data.game_data[filename].Exports[warp_1_event_index].Data[2].Value = Data.game_data[filename].Exports[warp_1_index].ObjectName
        Data.game_data[filename].Exports[warp_1_event_index].Data[3].Value = Data.game_data[filename].Exports[warp_2_index].ObjectName
        Data.game_data[filename].Exports[warp_2_event_index].Data[2].Value = Data.game_data[filename].Exports[warp_2_index].ObjectName
        Data.game_data[filename].Exports[warp_2_event_index].Data[3].Value = Data.game_data[filename].Exports[warp_1_index].ObjectName

    @staticmethod
    def remove_level_actor(filename, export_index):
        #Remove actor at index
        if Data.file_to_type[filename] != FileType.Level:
            raise TypeError("Input is not a level file")
        class_name = str(Data.game_data[filename].Imports[abs(Data.game_data[filename].Exports[export_index].ClassIndex.Index) - 1].ObjectName) # type: ignore
        #If the actor makes use of a c_cat class removing it will crash the game
        if class_name in _C_CAT_ACTORS or filename in ["m20JRN_002_Gimmick", "m20JRN_002_Enemy"]:
            for data in Data.game_data[filename].Exports[export_index].Data: # type: ignore
                if str(data.Name) in ["DropItemID", "ItemID"] and "TreasureBox" in class_name:
                    data.Value = FName.FromString(Data.game_data[filename], "AAAA_Shard")
                if str(data.Name) == "RootComponent":
                    root_index = int(str(data.Value)) - 1
            for data in Data.game_data[filename].Exports[root_index].Data:
                #Scale giant dulla spawner to 0 to remove it
                if class_name == "N3126_Generator_C":
                    if str(data.Name) == "RelativeScale3D":
                        data.Value[0].Value = FVector(0, 0, 0)
                #Otherwise move the actor off screen
                else:
                    if str(data.Name) == "RelativeLocation":
                        data.Value[0].Value = FVector(-999, 0, 0)
        else:
            Data.game_data[filename].Exports[export_index].OuterIndex = FPackageIndex(0) # type: ignore
            level_export = Data.get_export_by_name(filename, "PersistentLevel")
            level_export.Actors.Remove(FPackageIndex(export_index + 1))
            level_export.CreateBeforeSerializationDependencies.Remove(FPackageIndex(export_index + 1))

    @staticmethod
    def remove_level_class(filename, class_name):
        #Remove all actors of class in a level
        for export_index in range(len(Data.game_data[filename].Exports)):
            if str(Data.game_data[filename].Imports[abs(Data.game_data[filename].Exports[export_index].ClassIndex.Index) - 1].ObjectName) == class_name:
                Room.remove_level_actor(filename, export_index)

    @staticmethod
    def _convert_flag_to_door(room_name, door_flag, room_width) -> list[Door]:
        #Function by LagoLunatic
        door_list : list[Door] = []
        for index in range(0, len(door_flag), 2):
            tile_index = door_flag[index]
            direction = door_flag[index+1]
            tile_index -= 1
            if room_width == 0:
                x_block = tile_index
                z_block = 0
            else:
                x_block = tile_index % room_width
                z_block = tile_index // room_width
            for direction_part in Direction:
                if (direction & direction_part.value) != 0:
                    breakable = (direction & (direction_part.value << 16)) != 0
                    door = Door(room_name, x_block, z_block, direction_part, breakable)
                    door_list.append(door)
        return door_list

    @staticmethod
    def _convert_door_to_flag(door_list : list[Door], room_width):
        #Function by LagoLunatic
        door_flags_by_coords = OrderedDict()
        for door in door_list:
            coords = (door.x_block, door.z_block)
            if coords not in door_flags_by_coords:
                door_flags_by_coords[coords] = 0
                
            door_flags_by_coords[coords] |= door.direction_part.value
            if door.breakable:
                door_flags_by_coords[coords] |= (door.direction_part.value << 16)
            
        door_flag = []
        for (x, z), dir_flags in door_flags_by_coords.items():
            tile_index_in_room = z*room_width + x
            tile_index_in_room += 1
            door_flag.extend([tile_index_in_room, dir_flags])
        return door_flag

    @classmethod
    def _is_room_adjacent(cls, room_1, room_2):
        if Data.datatable["PB_DT_RoomMaster"][room_1]["OutOfMap"] != Data.datatable["PB_DT_RoomMaster"][room_2]["OutOfMap"]:
            return
        if cls._left_room_check(Data.datatable["PB_DT_RoomMaster"][room_1], Data.datatable["PB_DT_RoomMaster"][room_2]):
            cls._door_vertical_check(room_1, room_2, Direction.LEFT, Direction.LEFT_BOTTOM, Direction.LEFT_TOP)
        if cls._bottom_room_check(Data.datatable["PB_DT_RoomMaster"][room_1], Data.datatable["PB_DT_RoomMaster"][room_2]):
            cls._door_horizontal_check(room_1, room_2, Direction.BOTTOM, Direction.BOTTOM_RIGHT, Direction.BOTTOM_LEFT)
        if cls._right_room_check(Data.datatable["PB_DT_RoomMaster"][room_1], Data.datatable["PB_DT_RoomMaster"][room_2]):
            cls._door_vertical_check(room_1, room_2, Direction.RIGHT, Direction.RIGHT_BOTTOM, Direction.RIGHT_TOP)
        if cls._top_room_check(Data.datatable["PB_DT_RoomMaster"][room_1], Data.datatable["PB_DT_RoomMaster"][room_2]):
            cls._door_horizontal_check(room_1, room_2, Direction.TOP, Direction.TOP_LEFT, Direction.TOP_RIGHT)

    @staticmethod
    def _left_room_check(room_1, room_2):
        return bool(room_2["OffsetX"] == round(room_1["OffsetX"] - 12.6 * room_2["AreaWidthSize"], 1) and round(room_1["OffsetZ"] - 7.2 * (room_2["AreaHeightSize"] - 1), 1) <= room_2["OffsetZ"] <= round(room_1["OffsetZ"] + 7.2 * (room_1["AreaHeightSize"] - 1), 1))

    @staticmethod
    def _bottom_room_check(room_1, room_2):
        return bool(round(room_1["OffsetX"] - 12.6 * (room_2["AreaWidthSize"] - 1), 1) <= room_2["OffsetX"] <= round(room_1["OffsetX"] + 12.6 * (room_1["AreaWidthSize"] - 1), 1) and room_2["OffsetZ"] == round(room_1["OffsetZ"] - 7.2 * room_2["AreaHeightSize"], 1))

    @staticmethod
    def _right_room_check(room_1, room_2):
        return bool(room_2["OffsetX"] == round(room_1["OffsetX"] + 12.6 * room_1["AreaWidthSize"], 1) and round(room_1["OffsetZ"] - 7.2 * (room_2["AreaHeightSize"] - 1), 1) <= room_2["OffsetZ"] <= round(room_1["OffsetZ"] + 7.2 * (room_1["AreaHeightSize"] - 1), 1))

    @staticmethod
    def _top_room_check(room_1, room_2):
        return bool(round(room_1["OffsetX"] - 12.6 * (room_2["AreaWidthSize"] - 1), 1) <= room_2["OffsetX"] <= round(room_1["OffsetX"] + 12.6 * (room_1["AreaWidthSize"] - 1), 1) and room_2["OffsetZ"] == round(room_1["OffsetZ"] + 7.2 * room_1["AreaHeightSize"], 1))

    @classmethod
    def _door_vertical_check(cls, room_1, room_2, direction_1 : Direction, direction_2 : Direction, direction_3 : Direction):
        for door_1 in cls.map_connections[room_1]:
            if cls.door_string_to_door[door_1].direction_part == direction_1:
                for door_2 in cls.map_connections[room_2]:
                    if cls.door_string_to_door[door_2].direction_part == opposite(direction_1) and cls.door_string_to_door[door_1].z_block == (cls.door_string_to_door[door_2].z_block + round((Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetZ"] - Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetZ"])/7.2)):
                        cls.map_connections[room_1][door_1].append(door_2)
            if cls.door_string_to_door[door_1].direction_part == direction_2:
                for door_2 in cls.map_connections[room_2]:
                    if cls.door_string_to_door[door_2].direction_part == opposite(direction_2) and cls.door_string_to_door[door_1].z_block == (cls.door_string_to_door[door_2].z_block + round((Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetZ"] - Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetZ"])/7.2)):
                        cls.map_connections[room_1][door_1].append(door_2)
            if cls.door_string_to_door[door_1].direction_part == direction_3:
                for door_2 in cls.map_connections[room_2]:
                    if cls.door_string_to_door[door_2].direction_part == opposite(direction_3) and cls.door_string_to_door[door_1].z_block == (cls.door_string_to_door[door_2].z_block + round((Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetZ"] - Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetZ"])/7.2)):
                        cls.map_connections[room_1][door_1].append(door_2)

    @classmethod
    def _door_horizontal_check(cls, room_1, room_2, direction_1 : Direction, direction_2 : Direction, direction_3 : Direction):
        for door_1 in cls.map_connections[room_1]:
            if cls.door_string_to_door[door_1].direction_part == direction_1:
                for door_2 in cls.map_connections[room_2]:
                    if cls.door_string_to_door[door_2].direction_part == opposite(direction_1) and cls.door_string_to_door[door_1].x_block == (cls.door_string_to_door[door_2].x_block + round((Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetX"] - Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetX"])/12.6)):
                        cls.map_connections[room_1][door_1].append(door_2)
            if cls.door_string_to_door[door_1].direction_part == direction_2:
                for door_2 in cls.map_connections[room_2]:
                    if cls.door_string_to_door[door_2].direction_part == opposite(direction_2) and cls.door_string_to_door[door_1].x_block == (cls.door_string_to_door[door_2].x_block + round((Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetX"] - Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetX"])/12.6)):
                        cls.map_connections[room_1][door_1].append(door_2)
            if cls.door_string_to_door[door_1].direction_part == direction_3:
                for door_2 in cls.map_connections[room_2]:
                    if cls.door_string_to_door[door_2].direction_part == opposite(direction_3) and cls.door_string_to_door[door_1].x_block == (cls.door_string_to_door[door_2].x_block + round((Data.datatable["PB_DT_RoomMaster"][room_2]["OffsetX"] - Data.datatable["PB_DT_RoomMaster"][room_1]["OffsetX"])/12.6)):
                        cls.map_connections[room_1][door_1].append(door_2)

    @staticmethod
    def _get_gimmick_filename(room):
        if room in _ROOM_TO_GIMMICK:
            return _ROOM_TO_GIMMICK[room]
        return room + "_Gimmick"