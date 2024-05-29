from __future__ import annotations
from enum import Enum

from .GlobalImports import *
from .Constants import *
from . import Enemy
from . import Data
from . import Utility
from . import Shop
from . import Room

_IMPORTANT_CHECK_RATIO = 2
_IMPORTANT_ENEMY_RATIO = 4
_COIN_TYPES = [1, 5, 10, 50, 100, 500, 1000]
_DEFAULT_SHOP_EVENT = "Event_01_001_0000"

_KEY_SHARDS = {
    "Doublejump":     4,
    "HighJump":       2,
    "Invert":         3,
    "Deepsinker":     2,
    "Dimensionshift": 1,
    "Reflectionray":  3,
    "Aquastream":     4,
    "Demoniccapture": 4,
    "Accelerator":    4,
    "Bloodsteel":     4
}

_ROOM_TO_AREA = {
    "SIP": "m01",
    "VIL": "m02",
    "ENT": "m03",
    "GDN": "m04",
    "SAN": "m05",
    "KNG": "m06",
    "LIB": "m07",
    "TWR": "m08",
    "TRN": "m09",
    "BIG": "m10",
    "UGD": "m11",
    "SND": "m12",
    "ARC": "m13",
    "TAR": "m14",
    "JPN": "m15",
    "RVA": "m17",
    "ICE": "m18",
    "K2C": "m19",
    "JRN": "m20",
    "EBT": "m51",
    "LBP": "m77",
    "BKR": "m88"
}

_KEYLESS_CHESTS = [
    "Treasurebox_SIP000_Tutorial",
    "Treasurebox_SIP020_1",
    "Treasurebox_VIL005_1",
    "N3106_1ST_Treasure",
    "N3106_2ND_Treasure"
]

_SPECIAL_CHEST_TO_ROOM = {
    "PotionMaterial":               "m02VIL_005",
    "Qu07_Last":                    "m02VIL_003",
    "Swordsman":                    "m15JPN_016",
    "Treasurebox_PureMiriam_Hair":  "m01SIP_003",
    "Treasurebox_PureMiriam_Tiare": "m10BIG_011",
    "Treasurebox_PureMiriam_Dress": "m08TWR_019",
    "Treasurebox_PureMiriam_Sword": "m08TWR_016",
    "N3106_1ST_Treasure":           "m88BKR_004",
    "N3106_2ND_Treasure":           "m88BKR_004"
}

_IMPORTANT_CHECKS = [
    "Qu07_Last",
    "Swordsman",
    "Treasurebox_LIB011_1",
    "Treasurebox_TWR019_1",
    "Treasurebox_TWR019_2",
    "Treasurebox_KNG021_1",
    "Treasurebox_JRN004_1"
]

_MACRO_TO_REQUIREMENTS = {
    "Height": ["Doublejump", "HighJump", "Invert", "Dimensionshift", "Reflectionray"],
    "Flight": ["HighJump", "Invert", "Dimensionshift"],
    "WaterM": ["Invert", "Deepsinker", "Aquastream"]
}

_CLASSIC_ITEM_TO_LEVEL = {
    "ItemCommonMoneyMedium":       "Stage_00",
    "ItemCommonMoneySmall":        "Stage_00",
    "ItemCommonMPLarge":           "Stage_00",
    "ItemCommonMPSmall":           "Stage_00",
    "ItemCommonWeaponDagger":      "Stage_00",
    "ItemCommonMagicKillAll":      "Stage_01",
    "ItemCommonMoneyLarge":        "Stage_01",
    "ItemCommonPotionInvisible":   "Stage_01",
    "ItemCommonWeaponBoneArc":     "Stage_01",
    "ItemCommonWeaponRuinousRood": "Stage_01",
    "ItemCommonWeaponUnholyFire":  "Stage_01",
    "ItemCommonMagicTimeShard":    "Stage_02",
    "ItemSecretCrown":             "Stage_02",
    "ItemSecretGoblet":            "Stage_03",
    "ItemSpecialExtraLife":        "Stage_03",
    "ItemTreasureChest":           "Stage_04",
    "ItemSecretLuckyCat":          "Stage_5A",
    "ItemSpecialFood":             "Stage_5B"
}

_BOSS_SHOP_EVENTS = [
    "Event_02_001_0000", #Vepar
    "Event_06_001_0000", #Zangetsu
    "Event_08_002_0000", #Glutton Train
    "Event_09_005_0000", #Bathin
    "Event_10_001_0000", #Gebel
    "Event_11_001_0000", #Alfred
    "Event_13_001_0000", #Ultimate Zangetsu
    "Event_15_001_0000", #Gremory
    "Event_20_001_0000", #Valefar
    "Event_24_001_0000"  #Bloodless
]

class CheckType(Enum):
    Door  = 0
    Chest = 1
    Enemy = 2

def init():
    #Declare variables
    global used_chests
    used_chests = [
        "PotionMaterial",
        "Qu07_Last",
        "Swordsman",
        "Treasurebox_SIP000_Tutorial",
        "Treasurebox_SIP002_1",
        "Treasurebox_SIP003_1",
        "Treasurebox_SIP004_1",
        "Treasurebox_SIP005_1",
        "Treasurebox_SIP005_2",
        "Treasurebox_SIP006_1",
        "Treasurebox_SIP007_1",
        "Treasurebox_SIP007_2",
        "Treasurebox_SIP009_1",
        "Treasurebox_SIP011_1",
        "Treasurebox_SIP011_2",
        "Treasurebox_SIP011_3",
        "Treasurebox_SIP011_4",
        "Treasurebox_SIP012_1",
        "Treasurebox_SIP013_1",
        "Treasurebox_SIP014_1",
        "Treasurebox_SIP015_1",
        "Treasurebox_SIP016_1",
        "Treasurebox_SIP017_1",
        "Treasurebox_SIP018_1",
        "Treasurebox_SIP019_1",
        "Treasurebox_SIP020_1",
        "Treasurebox_SIP021_2",
        "Treasurebox_SIP024_1",
        "Treasurebox_SIP024_2",
        "Treasurebox_SIP025_1",
        "Treasurebox_SIP025_2",
        "Treasurebox_SIP026_1",
        "Treasurebox_VIL001_1",
        "Treasurebox_VIL003_1",
        "Treasurebox_VIL005_1",
        "Treasurebox_VIL006_1",
        "Treasurebox_VIL006_2",
        "Treasurebox_VIL006_3",
        "Treasurebox_VIL006_4",
        "Treasurebox_VIL007_1",
        "Treasurebox_VIL008_1",
        "Treasurebox_VIL008_2",
        "Treasurebox_VIL010_1",
        "Treasurebox_ENT002_1",
        "Treasurebox_ENT002_2",
        "Treasurebox_ENT002_3",
        "Treasurebox_ENT004_1",
        "Treasurebox_ENT005_1",
        "Treasurebox_ENT005_2",
        "Treasurebox_ENT007_1",
        "Treasurebox_ENT007_2",
        "Treasurebox_ENT007_3",
        "Treasurebox_ENT009_1",
        "Treasurebox_ENT011_1",
        "Treasurebox_ENT014_1",
        "Treasurebox_ENT014_2",
        "Treasurebox_ENT014_3",
        "Treasurebox_ENT018_1",
        "Treasurebox_ENT018_2",
        "Treasurebox_ENT020_1",
        "Treasurebox_ENT020_2",
        "Treasurebox_ENT021_1",
        "Treasurebox_ENT022_1",
        "Treasurebox_ENT024_1",
        "Treasurebox_ENT024_2",
        "Treasurebox_ENT024_3",
        "Treasurebox_GDN002_1",
        "Treasurebox_GDN004_1",
        "Treasurebox_GDN006_1",
        "Treasurebox_GDN006_2",
        "Treasurebox_GDN006_3",
        "Treasurebox_GDN006_4",
        "Treasurebox_GDN006_5",
        "Treasurebox_GDN007_1",
        "Treasurebox_GDN009_1",
        "Treasurebox_GDN009_2",
        "Treasurebox_GDN010_1",
        "Treasurebox_GDN012_1",
        "Treasurebox_GDN012_2",
        "Treasurebox_GDN013_1",
        "Treasurebox_GDN013_2",
        "Treasurebox_GDN013_3",
        "Treasurebox_GDN013_4",
        "Treasurebox_GDN014_1",
        "Treasurebox_SAN003_1",
        "Treasurebox_SAN003_2",
        "Treasurebox_SAN003_3",
        "Treasurebox_SAN003_4",
        "Treasurebox_SAN003_5",
        "Treasurebox_SAN003_6",
        "Treasurebox_SAN003_7",
        "Treasurebox_SAN003_8",
        "Treasurebox_SAN005_1",
        "Treasurebox_SAN005_2",
        "Treasurebox_SAN009_1",
        "Treasurebox_SAN009_2",
        "Treasurebox_SAN013_1",
        "Treasurebox_SAN013_2",
        "Treasurebox_SAN014_1",
        "Treasurebox_SAN015_2",
        "Treasurebox_SAN015_3",
        "Treasurebox_SAN016_1",
        "Treasurebox_SAN016_2",
        "Treasurebox_SAN016_3",
        "Treasurebox_SAN016_4",
        "Treasurebox_SAN016_5",
        "Treasurebox_SAN017_1",
        "Treasurebox_SAN019_1",
        "Treasurebox_SAN019_2",
        "Treasurebox_SAN019_3",
        "Treasurebox_SAN020_1",
        "Treasurebox_SAN021_1",
        "Treasurebox_SAN021_2",
        "Treasurebox_SAN021_3",
        "Treasurebox_SAN021_4",
        "Treasurebox_SAN021_5",
        "Treasurebox_SAN024_1",
        "Treasurebox_TWR000_1",
        "Treasurebox_TWR003_1",
        "Treasurebox_TWR004_1",
        "Treasurebox_TWR005_1",
        "Treasurebox_TWR006_1",
        "Treasurebox_TWR008_1",
        "Treasurebox_TWR009_1",
        "Treasurebox_TWR010_1",
        "Treasurebox_TWR012_1",
        "Treasurebox_TWR013_1",
        "Treasurebox_TWR016_1",
        "Treasurebox_TWR017_1",
        "Treasurebox_TWR017_2",
        "Treasurebox_TWR017_3",
        "Treasurebox_TWR017_4",
        "Treasurebox_TWR017_5",
        "Treasurebox_TWR017_6",
        "Treasurebox_TWR017_7",
        "Treasurebox_TWR018_1",
        "Treasurebox_TWR018_2",
        "Treasurebox_TWR018_3",
        "Treasurebox_TWR018_4",
        "Treasurebox_TWR018_5",
        "Treasurebox_TWR018_6",
        "Treasurebox_TWR018_7",
        "Treasurebox_TWR018_8",
        "Treasurebox_TWR019_1",
        "Treasurebox_TWR019_2",
        "Treasurebox_TWR019_4",
        "Treasurebox_LIB001_1",
        "Treasurebox_LIB002_1",
        "Treasurebox_LIB007_1",
        "Treasurebox_LIB009_1",
        "Treasurebox_LIB009_2",
        "Treasurebox_LIB011_1",
        "Treasurebox_LIB012_1",
        "Treasurebox_LIB017_1",
        "Treasurebox_LIB019_1",
        "Treasurebox_LIB022_1",
        "Treasurebox_LIB030_1",
        "Treasurebox_LIB032_1",
        "Treasurebox_LIB033_1",
        "Treasurebox_LIB040_1",
        "Treasurebox_LIB043_1",
        "Treasurebox_TRN002_1",
        "Treasurebox_TRN002_2",
        "Treasurebox_TRN002_3",
        "Treasurebox_TRN002_4",
        "Treasurebox_TRN002_5",
        "Treasurebox_KNG002_1",
        "Treasurebox_KNG002_2",
        "Treasurebox_KNG003_1",
        "Treasurebox_KNG006_1",
        "Treasurebox_KNG010_1",
        "Treasurebox_KNG011_1",
        "Treasurebox_KNG012_1",
        "Treasurebox_KNG012_2",
        "Treasurebox_KNG016_1",
        "Treasurebox_KNG017_1",
        "Treasurebox_KNG017_2",
        "Treasurebox_KNG017_3",
        "Treasurebox_KNG017_4",
        "Treasurebox_KNG017_5",
        "Treasurebox_KNG018_2",
        "Treasurebox_KNG018_3",
        "Treasurebox_KNG018_4",
        "Treasurebox_KNG021_1",
        "Treasurebox_KNG022_1",
        "Treasurebox_UGD001_1",
        "Treasurebox_UGD003_1",
        "Treasurebox_UGD003_2",
        "Treasurebox_UGD003_3",
        "Treasurebox_UGD003_4",
        "Treasurebox_UGD005_1",
        "Treasurebox_UGD005_2",
        "Treasurebox_UGD007_1",
        "Treasurebox_UGD009_1",
        "Treasurebox_UGD009_2",
        "Treasurebox_UGD009_3",
        "Treasurebox_UGD009_4",
        "Treasurebox_UGD010_1",
        "Treasurebox_UGD011_1",
        "Treasurebox_UGD021_1",
        "Treasurebox_UGD024_1",
        "Treasurebox_UGD024_2",
        "Treasurebox_UGD024_3",
        "Treasurebox_UGD025_1",
        "Treasurebox_UGD025_2",
        "Treasurebox_UGD025_3",
        "Treasurebox_UGD027_1",
        "Treasurebox_UGD030_1",
        "Treasurebox_UGD031_1",
        "Treasurebox_UGD031_2",
        "Treasurebox_UGD036_1",
        "Treasurebox_UGD036_2",
        "Treasurebox_UGD038_1",
        "Treasurebox_UGD040_1",
        "Treasurebox_UGD041_1",
        "Treasurebox_UGD042_1",
        "Treasurebox_UGD044_1",
        "Treasurebox_UGD044_2",
        "Treasurebox_UGD046_1",
        "Treasurebox_UGD046_2",
        "Treasurebox_UGD047_2",
        "Treasurebox_UGD048_1",
        "Treasurebox_UGD050_1",
        "Treasurebox_UGD051_1",
        "Treasurebox_UGD052_1",
        "Treasurebox_UGD052_2",
        "Treasurebox_UGD053_1",
        "Treasurebox_UGD054_1",
        "Treasurebox_UGD056_1",
        "Treasurebox_SND002_1",
        "Treasurebox_SND003_1",
        "Treasurebox_SND004_1",
        "Treasurebox_SND006_1",
        "Treasurebox_SND008_1",
        "Treasurebox_SND008_2",
        "Treasurebox_SND009_1",
        "Treasurebox_SND010_1",
        "Treasurebox_SND010_2",
        "Treasurebox_SND013_1",
        "Treasurebox_SND015_1",
        "Treasurebox_SND016_1",
        "Treasurebox_SND017_1",
        "Treasurebox_SND018_1",
        "Treasurebox_SND019_1",
        "Treasurebox_SND020_1",
        "Treasurebox_SND024_1",
        "Treasurebox_SND025_1",
        "Treasurebox_ARC000_1",
        "Treasurebox_ARC002_1",
        "Treasurebox_ARC003_1",
        "Treasurebox_ARC004_1",
        "Treasurebox_ARC006_1",
        "Treasurebox_ARC006_2",
        "Treasurebox_ARC007_1",
        "Treasurebox_ARC007_2",
        "Treasurebox_TAR001_1",
        "Treasurebox_TAR002_1",
        "Treasurebox_TAR006_1",
        "Treasurebox_TAR007_1",
        "Treasurebox_TAR010_1",
        "Treasurebox_JPN002_1",
        "Treasurebox_JPN002_2",
        "Treasurebox_JPN004_1",
        "Treasurebox_JPN005_1",
        "Treasurebox_JPN009_1",
        "Treasurebox_JPN010_1",
        "Treasurebox_JPN010_2",
        "Treasurebox_JPN013_1",
        "Treasurebox_JPN015_1",
        "Treasurebox_JPN017_1",
        "Treasurebox_JPN018_1",
        "Treasurebox_RVA001_1",
        "Treasurebox_RVA001_2",
        "Treasurebox_RVA002_1",
        "Treasurebox_RVA004_1",
        "Treasurebox_RVA006_1",
        "Treasurebox_RVA010_1",
        "Treasurebox_RVA011_1",
        "Treasurebox_RVA011_2",
        "Treasurebox_RVA012_1",
        "Treasurebox_RVA015_1",
        "Treasurebox_BIG002_1",
        "Treasurebox_BIG005_1",
        "Treasurebox_BIG006_1",
        "Treasurebox_BIG006_2",
        "Treasurebox_BIG006_3",
        "Treasurebox_BIG006_4",
        "Treasurebox_BIG006_5",
        "Treasurebox_BIG006_6",
        "Treasurebox_BIG007_1",
        "Treasurebox_BIG008_1",
        "Treasurebox_BIG010_1",
        "Treasurebox_BIG011_1",
        "Treasurebox_BIG012_1",
        "Treasurebox_BIG012_2",
        "Treasurebox_BIG012_3",
        "Treasurebox_BIG013_1",
        "Treasurebox_BIG014_1",
        "Treasurebox_BIG016_1",
        "Treasurebox_BIG016_2",
        "Treasurebox_BIG016_3",
        "Treasurebox_ICE001_1",
        "Treasurebox_ICE001_2",
        "Treasurebox_ICE002_1",
        "Treasurebox_ICE003_1",
        "Treasurebox_ICE003_2",
        "Treasurebox_ICE006_1",
        "Treasurebox_ICE008_1",
        "Treasurebox_ICE008_2",
        "Treasurebox_ICE010_1",
        "Treasurebox_ICE011_1",
        "Treasurebox_ICE013_1",
        "Treasurebox_ICE014_1",
        "Treasurebox_PureMiriam_Hair",
        "Treasurebox_PureMiriam_Tiare",
        "Treasurebox_PureMiriam_Dress",
        "Treasurebox_PureMiriam_Sword",
        "Wall_SIP004_1",
        "Wall_SIP009_1",
        "Wall_SIP014_1",
        "Wall_SIP016_1",
        "Wall_ENT002_1",
        "Wall_ENT012_1",
        "Wall_GDN006_1",
        "Wall_SAN000_1",
        "Wall_SAN005_1",
        "Wall_SAN019_1",
        "Wall_KNG000_1",
        "Wall_KNG007_1",
        "Wall_LIB004_1",
        "Wall_LIB019_1",
        "Wall_LIB025_1",
        "Wall_TWR006_1",
        "Wall_TWR013_1",
        "Wall_TWR016_1",
        "Wall_TRN005_1",
        "Wall_UGD000_1",
        "Wall_UGD003_1",
        "Wall_UGD006_1",
        "Wall_UGD012_1",
        "Wall_UGD020_1",
        "Wall_UGD031_1",
        "Wall_UGD037_1",
        "Wall_UGD046_1",
        "Wall_UGD056_1",
        "Wall_SND001_1",
        "Wall_SND019_1",
        "Wall_TAR007_1",
        "Wall_JPN011_1",
        "Wall_JPN013_1",
        "Wall_RVA011_1",
        "Wall_BIG002_1",
        "Wall_BIG012_1",
        "Wall_BIG016_1",
        "Wall_ICE003_1",
        "Wall_ICE010_1",
        "Wall_ICE017_1",
        "N3106_1ST_Treasure",
        "N3106_2ND_Treasure",
        "Treasurebox_JRN001_1",
        "Treasurebox_JRN001_2",
        "Treasurebox_JRN001_3",
        "Treasurebox_JRN002_1",
        "Treasurebox_JRN004_1"
    ]
    global key_order
    key_order = []
    global key_item_to_location
    key_item_to_location = {}
    global key_shard_to_location
    key_shard_to_location = {}
    global all_keys
    all_keys = KEY_ITEMS + list(_KEY_SHARDS)
    global difficulty
    difficulty = "Normal"
    global previous_available_chests
    previous_available_chests = []
    global previous_available_enemies
    previous_available_enemies = []
    global current_available_doors
    current_available_doors = ["SIP_000_START"]
    global current_available_chests
    current_available_chests = []
    global current_available_enemies
    current_available_enemies = []
    global all_available_doors
    all_available_doors = []
    global all_available_chests
    all_available_chests = []
    global all_available_enemies
    all_available_enemies = []
    global check_to_requirement
    check_to_requirement = {}
    global special_check_to_door
    special_check_to_door = {}
    global special_check_to_requirement
    special_check_to_requirement = {
        "TO_BIG_000_START": den_portal_available,
        "TO_JRN_000_START": journey_area_available,
        "Qu07_Last":        last_benjamin_available,
        "N2012":            orlok_dracule_available,
        "N2013":            iga_dlc_boss_available
    }
    global enemy_to_room
    enemy_to_room = {}
    global enemy_skip_list
    enemy_skip_list = ["N2013"]
    #Pool
    global chest_type
    chest_type = []
    global green_chest_type
    green_chest_type = []
    global blue_chest_type
    blue_chest_type = []
    global enemy_type
    enemy_type = []
    global quest_type
    quest_type = []
    global area_pools
    area_pools = {}
    #Shop
    global shop_skip_list
    shop_skip_list = [
        "Potion",
        "Ether",
        "Waystone",
	    "SeedCorn",
	    "SeedRice",
	    "SeedPotato",
        "8BitCoin",
        "16BitCoin",
        "32BitCoin"
    ]
    Data.constant["ItemDrop"]["Potion"]["ShopRatio"]      -= 3
    Data.constant["ItemDrop"]["CookingMat"]["ShopRatio"]  -= 3
    Data.constant["ItemDrop"]["StandardMat"]["ShopRatio"] -= 3
    #Filling loot types
    for entry in Data.constant["ItemDrop"]:
        for _ in range(Data.constant["ItemDrop"][entry]["ChestRatio"]):
            chest_type.append(entry)
            if Data.constant["ItemDrop"][entry]["ChestColor"] == "Green":
                green_chest_type.append(entry)
            if Data.constant["ItemDrop"][entry]["ChestColor"] == "Blue":
                blue_chest_type.append(entry)
        for _ in range(Data.constant["ItemDrop"][entry]["QuestRatio"]):
            quest_type.append(entry)
    enemy_type = list(Data.constant["EnemyDrop"])

def set_logic_complexity(complexity : int):
    global logic_complexity
    logic_complexity = (complexity - 1)/2

def set_shop_event_weight(weight : int):
    global shop_event_weight
    shop_event_weight = 1/6 * 2**(weight - 1)

def set_hard_mode():
    global difficulty
    difficulty = "Hard"

def add_iga_dlc():
    enemy_skip_list.remove("N2013")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("SwordWhip")
    Data.constant["ShardDrop"]["ItemPool"].append("NeverSatisfied")
    Data.constant["QuestRequirement"]["Memento"]["ItemPool"].append("SwordWhip")

def del_iga_dlc():
    Data.datatable["PB_DT_ItemMaster"]["SwordWhip"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["NeverSatisfied"]["ItemType"] = "ECarriedCatalog::None"

def add_shantae_dlc():
    Data.constant["ItemDrop"]["Accessory"]["ItemPool"].append("ShantaeVest")
    Data.constant["ItemDrop"]["Accessory"]["ItemPool"].append("ShantaeTiara")
    Data.constant["ItemDrop"]["Headgear"]["ItemPool"].append("ShantaeBandana")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("ShantaeOutfit1")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("ShantaeOutfit3")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("ShantaeOutfit5")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("PirateGun1")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("PirateGun3")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("PirateGun5")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("PirateSword1")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("PirateSword3")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("PirateSword5")
    Data.constant["ShardDrop"]["ItemPool"].append("Fireball")

def del_shantae_dlc():
    Data.datatable["PB_DT_ItemMaster"]["ShantaeVest"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["ShantaeTiara"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["ShantaeBandana"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["ShantaeOutfit1"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["ShantaeOutfit3"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["ShantaeOutfit5"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["PirateGun1"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["PirateGun3"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["PirateGun5"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["PirateSword1"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["PirateSword3"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["PirateSword5"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Fireball"]["ItemType"] = "ECarriedCatalog::None"

def add_succubus_dlc():
    Data.constant["ItemDrop"]["Accessory"]["ItemPool"].append("VampiricWings")
    Data.constant["ItemDrop"]["Headgear"]["ItemPool"].append("AlluringHorns")
    Data.constant["ItemDrop"]["Scarf"]["ItemPool"].append("VampiricChoker")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("VampiricSkinsuit")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("VampiricSkinsuit2")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("VampiricSkinsuit4")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("Scythe")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("Scythe2")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("Scythe4")
    Data.constant["ShardDrop"]["ItemPool"].append("Dreamsteal")

def del_succubus_dlc():
    Data.datatable["PB_DT_ItemMaster"]["VampiricWings"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["AlluringHorns"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["VampiricChoker"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["VampiricSkinsuit"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["VampiricSkinsuit2"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["VampiricSkinsuit4"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Scythe"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Scythe2"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Scythe4"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Dreamsteal"]["ItemType"] = "ECarriedCatalog::None"

def add_magicgirl_dlc():
    Data.constant["ItemDrop"]["Accessory"]["ItemPool"].append("MagicalGirlAccessory")
    Data.constant["ItemDrop"]["Headgear"]["ItemPool"].append("MagicalGirlHead")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("MagicalGirlBody")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("MagicalGirlBody2")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("MagicalGirlBody4")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("MagicalScepter")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("MagicalScepter2")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("MagicalScepter4")
    Data.constant["ShardDrop"]["ItemPool"].append("SummonBuChan")
    Data.constant["ShardDrop"]["ItemPool"].append("FamiliaBuChan")

def del_magicgirl_dlc():
    Data.datatable["PB_DT_ItemMaster"]["MagicalGirlAccessory"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["MagicalGirlHead"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["MagicalGirlBody"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["MagicalGirlBody2"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["MagicalGirlBody4"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["MagicalScepter"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["MagicalScepter2"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["MagicalScepter4"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["SummonBuChan"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["FamiliaBuChan"]["ItemType"] = "ECarriedCatalog::None"

def add_japanese_dlc():
    Data.constant["ItemDrop"]["Accessory"]["ItemPool"].append("FestivalMask")
    Data.constant["ItemDrop"]["Accessory"]["ItemPool"].append("Sarashi")
    Data.constant["ItemDrop"]["Headgear"]["ItemPool"].append("Kanzashi")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("FestivalKimono")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("FestivalKimono2")
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("FestivalKimono4")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("Wagasa")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("Wagasa2")
    Data.constant["ItemDrop"]["Weapon"]["ItemPool"].append("Wagasa4")
    Data.constant["ShardDrop"]["ItemPool"].append("SakuraRain")

def del_japanese_dlc():
    Data.datatable["PB_DT_ItemMaster"]["FestivalMask"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Sarashi"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Kanzashi"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["FestivalKimono"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["FestivalKimono2"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["FestivalKimono4"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Wagasa"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Wagasa2"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["Wagasa4"]["ItemType"] = "ECarriedCatalog::None"
    Data.datatable["PB_DT_ItemMaster"]["SakuraRain"]["ItemType"] = "ECarriedCatalog::None"

def fill_enemy_to_room():
    #Gather a list of rooms per enemy
    for enemy in Data.constant["EnemyInfo"]:
        enemy_to_room[enemy] = []
    for room in Data.constant["RoomRequirement"]:
        for door in Data.constant["RoomRequirement"][room]:
            for check in Data.constant["RoomRequirement"][room][door]:
                if is_valid_enemy_check(check)[1]:
                    enemy_id = Utility.split_enemy_profile(check)[0]
                    if not room in enemy_to_room[enemy_id]:
                        enemy_to_room[enemy_id].append(room)

def chest_to_room(chest):
    if chest in _SPECIAL_CHEST_TO_ROOM:
        return _SPECIAL_CHEST_TO_ROOM[chest]
    return _ROOM_TO_AREA[chest.split("_")[1][:3]] + chest.split("_")[1][:3] + "_" + chest.split("_")[1][3:]

def enemy_shard_to_room(enemy):
    if enemy in ["N3090", "N3126"]:
        return enemy_to_room["N3090"] + enemy_to_room["N3126"]
    if enemy in ["N3015", "N3127"]:
        return enemy_to_room["N3015"] + enemy_to_room["N3127"]
    return enemy_to_room[enemy]

def remove_infinite_items():
    #These specific gears grant the player an infinite source of something which generally ends up defining the meta and dominating runs
    #If the player is up for variety and challenge remove those from the pool so that they can never be found
    while "Gebelsglasses" in Data.constant["ItemDrop"]["Accessory"]["ItemPool"]:
        Data.constant["ItemDrop"]["Accessory"]["ItemPool"].remove("Gebelsglasses")
    while "Gebelsglasses" in Data.constant["QuestRequirement"]["Memento"]["ItemPool"]:
        Data.constant["QuestRequirement"]["Memento"]["ItemPool"].remove("Gebelsglasses")
    while "Recyclehat" in Data.constant["ItemDrop"]["Headgear"]["ItemPool"]:
        Data.constant["ItemDrop"]["Headgear"]["ItemPool"].remove("Recyclehat")
    while "Recyclehat" in Data.constant["QuestRequirement"]["Memento"]["ItemPool"]:
        Data.constant["QuestRequirement"]["Memento"]["ItemPool"].remove("Recyclehat")

def add_starting_item(item : str):
    entry = f"Start_{item}"
    #Determine quantity based on item type
    quantity = None
    for string in ["Item", "Enemy"]:
        for data in Data.constant[f"{string}Drop"]:
            if item in Data.constant[f"{string}Drop"][data]["ItemPool"]:
                quantity = Data.constant[f"{string}Drop"][data]["ItemHighQuantity"]
    if not quantity:
        quantity = 7 if item == "Shortcut" else 1
    Data.datatable["PB_DT_DropRateMaster"][entry] = copy.deepcopy(Data.datatable["PB_DT_DropRateMaster"]["Tresurebox_SAN000_01"])
    Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemId"]       = item
    Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemQuantity"] = quantity
    Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemRate"]     = 100.0
    Room.add_global_room_pickup("m01SIP_000", entry)

def disable_shard_crafting():
    #If shards are randomized then disable the possiblity to manually craft shards so that they aren't always available
    #This is because there is currently no way to randomize which shards are craftable
    for entry in Data.datatable["PB_DT_CraftMaster"]:
        if Data.datatable["PB_DT_CraftMaster"][entry]["Type"] == "ECraftType::Craft" and Data.datatable["PB_DT_CraftMaster"][entry]["CraftItemId"] in Data.datatable["PB_DT_ShardMaster"]:
            Data.datatable["PB_DT_CraftMaster"][entry]["OpenKeyRecipeID"] = "Medal019"

def satisfies_requirement(requirement) -> bool:
    check = True
    for req in requirement:
        #AND
        if type(req) is list:
            for subreq in req:
                check = check_requirement(subreq)
                if not check:
                    break
            if check:
                break
        #OR  
        else:
            check = check_requirement(req)
            if check:
                break
    return check

def check_requirement(requirement) -> bool:
    if requirement in _MACRO_TO_REQUIREMENTS:
        return satisfies_requirement(_MACRO_TO_REQUIREMENTS[requirement])
    return requirement in key_order

def key_logic():
    #Logic that adapts to any map layout
    move_through_rooms()
    while True:
        #Place key item
        if check_to_requirement:
            #Weight checks
            requirement_list_list = []
            for check in check_to_requirement:
                requirement_list = check_to_requirement[check]
                if not requirement_list in requirement_list_list:
                    requirement_list_list.append(requirement_list)
            chosen_requirement_list = random.choice(requirement_list_list)
            #Weight requirements
            requirement_list = []
            for requirement in chosen_requirement_list:
                for num in range(get_requirement_weight(requirement)):
                    requirement_list.append(requirement)
            chosen_requirement = random.choice(requirement_list)
            #Choose requirement and key item
            if type(chosen_requirement) is list:
                for item in chosen_requirement:
                    if satisfies_requirement([item]):
                        continue
                    chosen_item = pick_next_key(item)
                    place_next_key(chosen_item)
            else:
                chosen_item = pick_next_key(chosen_requirement)
                place_next_key(chosen_item)
        #Place last unecessary keys
        elif all_keys:
            place_next_key(random.choice(all_keys))
        #Stop when all keys are placed and all doors are explored
        else:
            break

def move_through_rooms():
    #Move through each door
    while True:
        for door in copy.deepcopy(current_available_doors):
            current_available_doors.remove(door)
            room = get_door_room(door)
            if room in Data.constant["RoomRequirement"]:
                for check, requirement in Data.constant["RoomRequirement"][room][door].items():
                    #Don't automatically unlock certain checks
                    if check in special_check_to_requirement:
                        if not check in special_check_to_door:
                            special_check_to_door[check] = []
                        special_check_to_door[check].append(door)
                        continue
                    analyse_check(check, requirement)
            #Saves/warps/transitions
            else:
                for subdoor in Room.map_connections[room]:
                    if subdoor == door:
                        continue
                    analyse_check(subdoor, [])
        #Keep going until stuck
        if current_available_doors:
            continue
        #Check special requirements
        for special_check in special_check_to_requirement:
            if special_check in special_check_to_door and special_check_to_requirement[special_check]():
                for door in special_check_to_door[special_check]:
                    analyse_check(special_check, Data.constant["RoomRequirement"][get_door_room(door)][door][special_check])
                del special_check_to_door[special_check]
        #Stop if no more doors are found
        if not current_available_doors:
            break

def check_lifted_obstacles():
    for check in list(check_to_requirement):
        if not check in check_to_requirement:
            continue
        requirement = check_to_requirement[check]
        analyse_check(check, requirement)

def reset_available_checks():
    previous_available_chests.clear()
    previous_available_chests.extend(current_available_chests)
    current_available_chests.clear()
    previous_available_enemies.clear()
    previous_available_enemies.extend(current_available_enemies)
    current_available_enemies.clear()

def pick_next_key(chosen_requirement):
    if chosen_requirement in _MACRO_TO_REQUIREMENTS:
        requirement_list = []
        for requirement in _MACRO_TO_REQUIREMENTS[chosen_requirement]:
            for num in range(get_requirement_weight(requirement)):
                requirement_list.append(requirement)
        return random.choice(requirement_list)
    return chosen_requirement

def analyse_check(check, requirement):
    #If accessible remove it from the requirement list
    accessible = satisfies_requirement(requirement)
    if accessible:
        if check in check_to_requirement:
            del check_to_requirement[check]
    #Handle each check type differently
    check_type = get_check_type(check)
    match check_type:
        case CheckType.Door:
            if check in all_available_doors:
                return
        case CheckType.Chest:
            if check in all_available_chests:
                return
        case CheckType.Enemy:
            if not is_valid_enemy_check(check)[1]:
                return
            enemy_id = Utility.split_enemy_profile(check)[0]
            if enemy_id in all_available_enemies:
                return
    #Set check as available
    if accessible:
        match check_type:
            case CheckType.Door:
                all_available_doors.append(check)
                destination = get_door_destination(check)
                if destination:
                    current_available_doors.append(destination)
                    all_available_doors.append(destination)
                    if destination in check_to_requirement:
                        del check_to_requirement[destination]
            case CheckType.Chest:
                current_available_chests.append(check)
                all_available_chests.append(check)
            case CheckType.Enemy:
                current_available_enemies.append(enemy_id)
                all_available_enemies.append(enemy_id)
    #Add to requirement list
    else:
        if check in check_to_requirement:
            add_requirement_to_check(check, requirement)
        else:
            check_to_requirement[check] = requirement

def add_requirement_to_check(check, requirement):
    old_list = check_to_requirement[check] + requirement
    new_list = []
    for req in old_list:
        to_add = not req in new_list
        if type(req) is list:
            for subreq in old_list:
                if subreq in req:
                    to_add = False
        if to_add:
            new_list.append(req)
    check_to_requirement[check] = new_list

def get_check_type(check : str) -> CheckType:
    if check in used_chests:
        return CheckType.Chest
    if is_valid_enemy_check(check)[0]:
        return CheckType.Enemy
    return CheckType.Door

def is_valid_enemy_check(check : str) -> tuple[bool, bool]:
    enemy_profile = Utility.split_enemy_profile(check)
    is_enemy = enemy_profile[0] in Data.constant["EnemyInfo"]
    is_valid = is_enemy and (not enemy_profile[1] or enemy_profile[1] == difficulty)
    return (is_enemy, is_valid)

def get_requirement_weight(requirement):
    if type(requirement) is list:
        return 1
    elif requirement in _KEY_SHARDS:
        return _KEY_SHARDS[requirement]
    return 4

def place_next_key(chosen_item):
    #Item
    current_valid_chests = validate_chest_list(current_available_chests)
    previous_valid_chests = validate_chest_list(previous_available_chests)
    all_valid_chests = validate_chest_list(all_available_chests)
    if chosen_item in KEY_ITEMS:
        if should_place_key_in(current_valid_chests):
            try:
                chosen_chest = pick_key_chest(current_valid_chests)
            except IndexError:
                try:
                    chosen_chest = pick_key_chest(previous_valid_chests)
                except IndexError:
                    chosen_chest = pick_key_chest(all_valid_chests)
        elif should_place_key_in(previous_valid_chests):
            try:
                chosen_chest = pick_key_chest(previous_valid_chests)
            except IndexError:
                chosen_chest = pick_key_chest(all_valid_chests)
        else:
            chosen_chest = pick_key_chest(all_valid_chests)
        key_item_to_location[chosen_item] = chosen_chest
    #Shard
    current_valid_enemies = validate_enemy_list(current_available_enemies)
    previous_valid_enemies = validate_enemy_list(previous_available_enemies)
    all_valid_enemies = validate_enemy_list(all_available_enemies)
    if chosen_item in _KEY_SHARDS:
        if should_place_key_in(current_valid_enemies):
            try:
                chosen_enemy = pick_key_enemy(current_valid_enemies)
            except IndexError:
                try:
                    chosen_enemy = pick_key_enemy(previous_valid_enemies)
                except IndexError:
                    chosen_enemy = pick_key_enemy(all_valid_enemies)
        elif should_place_key_in(previous_valid_enemies):
            try:
                chosen_enemy = pick_key_enemy(previous_valid_enemies)
            except IndexError:
                chosen_enemy = pick_key_enemy(all_valid_enemies)
        else:
            chosen_enemy = pick_key_enemy(all_valid_enemies)
        key_shard_to_location[chosen_item] = chosen_enemy
    all_keys.remove(chosen_item)
    key_order.append(chosen_item)
    #Analyse the game again
    reset_available_checks()
    check_lifted_obstacles()
    move_through_rooms()

def should_place_key_in(list):
    return random.random() < (1 - 1/(1+len(list)))*logic_complexity

def validate_chest_list(available_chests):
    valid_chests = []
    for chest in available_chests:
        if not chest in list(key_item_to_location.values()) and not chest in _KEYLESS_CHESTS:
            valid_chests.append(chest)
    return valid_chests

def validate_enemy_list(available_enemies):
    #Giant dulla heads and Dullahammer EX share their drop with their early game counterpart
    available_enemies = ["N3090" if item == "N3126" else item for item in available_enemies]
    available_enemies = ["N3015" if item == "N3127" else item for item in available_enemies]
    valid_enemies = []
    for enemy in available_enemies:
        if not enemy in list(key_shard_to_location.values()) and not enemy in enemy_skip_list and Data.constant["EnemyInfo"][enemy]["HasShard"]:
            valid_enemies.append(enemy)
    return valid_enemies

def pick_key_chest(valid_chests):
    #Increase odds of important checks
    weighted_chests = []
    for chest in valid_chests:
        odds = 2**_IMPORTANT_CHECK_RATIO if chest in _IMPORTANT_CHECKS else 1
        for num in range(odds):
            weighted_chests.append(chest)
    return random.choice(weighted_chests)

def pick_key_enemy(valid_enemies):
    #Increase odds the more uncommon the enemy
    weighted_enemies = []
    for enemy in valid_enemies:
        odds = _IMPORTANT_ENEMY_RATIO - min(len(enemy_shard_to_room(enemy)), _IMPORTANT_ENEMY_RATIO)
        for num in range(2**odds):
            weighted_enemies.append(enemy)
    return random.choice(weighted_enemies)

def get_door_destination(door):
    if door in Room.door_string_to_door:
        if Room.map_connections[Room.door_string_to_door[door].room][door]:
            return Room.map_connections[Room.door_string_to_door[door].room][door][0]
        else:
            return None
    elif door.split("_")[0] == "TO":
        short_door = door.split("_")
        short_door.pop(0)
        return "_".join(short_door)
    else:
        return None

def get_door_room(door):
    short_door = door.split("_")
    return _ROOM_TO_AREA[short_door[0]] + "_".join([short_door[0], short_door[1]])

def den_portal_available():
    return "N1012" in all_available_enemies

def journey_area_available():
    return "BIG_000_START" in all_available_doors

def last_benjamin_available():
    return "VIL_004_1_0_RIGHT_BOTTOM" in all_available_doors and "ENT_015_0_0_LEFT" in all_available_doors and "UGD_049_0_0_LEFT" in all_available_doors and "Treasurebox_JPN002_1" in all_available_chests

def orlok_dracule_available():
    return "N1009_Enemy" in all_available_enemies

def iga_dlc_boss_available():
    return "N1009_Enemy" in all_available_enemies

def final_boss_available():
    return "N1013_Bael" in all_available_enemies

def randomize_overworld_keys():
    key_logic()
    #Key items
    for item in KEY_ITEMS:
        patch_key_item_entry(item, key_item_to_location[item])
    #Key shards
    for item in _KEY_SHARDS:
        patch_key_shard_entry(item, key_shard_to_location[item])

def randomize_overworld_items():
    create_area_pools()
    #Start chest
    patch_start_chest_entry()
    #Skip Vepar chest
    used_chests.remove("Treasurebox_SIP020_1")
    #Johannes mats
    patch_chest_entry(random.choice(blue_chest_type), "PotionMaterial")
    #100% chest
    patch_chest_entry(random.choice(green_chest_type), "Treasurebox_VIL005_1")
    #8 bit nightmare chest
    patch_chest_entry(random.choice(green_chest_type), "Treasurebox_KNG021_1")
    #Final Benjamin reward
    patch_chest_entry(random.choice(green_chest_type), "Qu07_Last")
    #Ultimate Zangetsu reward
    patch_chest_entry(random.choice(green_chest_type), "Swordsman")
    #Carpenter's first chest
    patch_chest_entry(random.choice(green_chest_type), "N3106_1ST_Treasure")
    #Carpenter's second chest
    patch_chest_entry(random.choice(green_chest_type), "N3106_2ND_Treasure")
    #Journey's last chest
    patch_chest_entry(random.choice(green_chest_type), "Treasurebox_JRN004_1")
    #Upgrades
    #Don't put any upgrades in areas that extra character can't access
    for num in range(30):
        chosen = random.choice(used_chests)
        while "JRN" in chosen:
            chosen = random.choice(used_chests)
        patch_key_item_entry("MaxHPUP", chosen)
    for num in range(30):
        chosen = random.choice(used_chests)
        while "JRN" in chosen:
            chosen = random.choice(used_chests)
        patch_key_item_entry("MaxMPUP", chosen)
    for num in range(24):
        chosen = random.choice(used_chests)
        while "JRN" in chosen:
            chosen = random.choice(used_chests)
        patch_key_item_entry("MaxBulletUP", chosen)
    #Item pool
    chest_pool = copy.deepcopy(used_chests)
    random.shuffle(chest_pool)
    for chest in chest_pool:
        patch_chest_entry(random.choice(chest_type), chest)
    #Enemy pool
    for entry in Data.datatable["PB_DT_DropRateMaster"]:
        if "Treasure" in entry:
            continue
        enemy_id = entry.split("_")[0]
        if not enemy_id in Data.constant["EnemyInfo"]:
            continue
        if not Data.constant["EnemyInfo"][enemy_id]["HasShard"]:
            continue
        if Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemRate"] == 0.0 and Data.datatable["PB_DT_DropRateMaster"][entry]["CommonRate"] == 0.0 and Data.datatable["PB_DT_DropRateMaster"][entry]["RareIngredientRate"] == 0.0 and Data.datatable["PB_DT_DropRateMaster"][entry]["CommonIngredientRate"] == 0.0:
            continue
        #Reduce dulla head drop rate
        drop_rate_multiplier = 0.5 if enemy_id in ["N3090", "N3099"] else 1.0
        #Assign drops
        if entry == enemy_id + "_Shard":
            patch_enemy_entry(random.choice(enemy_type), drop_rate_multiplier, entry)
        else:
            Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemId"]               = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["RareItemId"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemQuantity"]         = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["RareItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemRate"]             = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["RareItemRate"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["CommonItemId"]             = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["CommonItemId"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["CommonItemQuantity"]       = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["CommonItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["CommonRate"]               = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["CommonRate"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["RareIngredientId"]         = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["RareIngredientId"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["RareIngredientQuantity"]   = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["RareIngredientQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["RareIngredientRate"]       = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["RareIngredientRate"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["CommonIngredientId"]       = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["CommonIngredientId"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["CommonIngredientQuantity"] = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["CommonIngredientQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["CommonIngredientRate"]     = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["CommonIngredientRate"]

def randomize_overworld_shards():
    for entry in Data.datatable["PB_DT_DropRateMaster"]:
        #Check if the entry should be skipped
        if "Treasure" in entry:
            continue
        enemy_id = entry.split("_")[0]
        if not enemy_id in Data.constant["EnemyInfo"]:
            continue
        if not Data.constant["EnemyInfo"][enemy_id]["HasShard"]:
            continue
        if enemy_id in enemy_skip_list:
            continue
        if enemy_id in list(key_shard_to_location.values()):
            continue
        #Reduce dulla head drop rate
        drop_rate_multiplier = 0.5 if enemy_id in ["N3090", "N3099"] else 1.0
        #Assign shard
        if entry == enemy_id + "_Shard":
            Data.datatable["PB_DT_DropRateMaster"][entry]["ShardId"] = pick_and_remove(Data.constant["ShardDrop"]["ItemPool"], True, "None")
            if Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] < 100.0:
                Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] = Data.constant["ShardDrop"]["ItemRate"]*drop_rate_multiplier
        else:
            Data.datatable["PB_DT_DropRateMaster"][entry]["ShardId"]   = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["ShardId"]
            Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] = Data.datatable["PB_DT_DropRateMaster"][enemy_id + "_Shard"]["ShardRate"]

def randomize_classic_mode_drops():
    #Convert the drop dictionary to a weighted list
    classic_pool = []
    for item in Data.constant["ClassicDrop"]:
        for num in range(Data.constant["ClassicDrop"][item]):
            classic_pool.append(item)
    #Search for any instance of SpawnItemTypeClass and replace it with a random item
    for stage in ["Stage_00", "Stage_01", "Stage_02", "Stage_03", "Stage_04", "Stage_05A", "Stage_05B"]:
        filename = f"Classic_{stage}_Objects"
        for export in Data.game_data[filename].Exports:
            for data in export.Data:
                if str(data.Name) != "SpawnItemTypeClass":
                    continue
                item_name = "None" if int(str(data.Value)) == 0 else str(Data.game_data[filename].Imports[abs(int(str(data.Value))) - 1].ObjectName).split("_")[2]
                #Don't randomize the item if it isn't in the pool list
                if not item_name in classic_pool:
                    continue
                chosen_item = random.choice(classic_pool)
                data.Value = FPackageIndex(0) if chosen_item == "None" else Data.copy_asset_import(chosen_item, f"Classic_{_CLASSIC_ITEM_TO_LEVEL[chosen_item]}_Objects", filename)
                break

def add_pre_vepar_waystone():
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_SIP020_1"]["RareItemId"] = "Waystone"

def create_area_pools():
    #Set up material pools per area for blue chests
    for room_prefix in _ROOM_TO_AREA:
        area_id = _ROOM_TO_AREA[room_prefix] + room_prefix
        area_pools[area_id] = {}
        for item_type in blue_chest_type:
            area_pools[area_id][item_type] = []
            for num in range(4):
                chosen = pick_and_remove(Data.constant["ItemDrop"][item_type]["ItemPool"], Data.constant["ItemDrop"][item_type]["IsUnique"], item_type)
                while chosen in area_pools[area_id][item_type]:
                    chosen = pick_and_remove(Data.constant["ItemDrop"][item_type]["ItemPool"], Data.constant["ItemDrop"][item_type]["IsUnique"], item_type)
                area_pools[area_id][item_type].append(chosen)

def empty_drop_entry(container):
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"] = "None"
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"] = 0
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"] = 0.0
    Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemId"] = "None"
    Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemQuantity"] = 0
    Data.datatable["PB_DT_DropRateMaster"][container]["CommonRate"] = 0.0
    Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientId"] = "None"
    Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientQuantity"] = 0
    Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientRate"] = 0.0
    Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientId"] = "None"
    Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientQuantity"] = 0
    Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientRate"] = 0.0
    Data.datatable["PB_DT_DropRateMaster"][container]["CoinType"] = "EDropCoin::None"
    Data.datatable["PB_DT_DropRateMaster"][container]["CoinOverride"] = 0
    Data.datatable["PB_DT_DropRateMaster"][container]["CoinRate"] = 0.0
    Data.datatable["PB_DT_DropRateMaster"][container]["AreaChangeTreasureFlag"] = False

def patch_key_item_entry(item, container):
    empty_drop_entry(container)
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"] = item
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"] = 1
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"] = 100.0
    used_chests.remove(container)
    
def patch_key_shard_entry(shard, enemy):
    #Assign a key shard to an entry
    #Unlike regular shards those will be more likely to drop but can only be dropped once
    drop_rate_multiplier = 0.5 if enemy in ["N3090", "N3099"] else 1.0
    for entry in Data.datatable["PB_DT_DropRateMaster"]:
        if entry == enemy + "_Shard":
            Data.datatable["PB_DT_DropRateMaster"][entry]["DropSpecialFlags"] = "EDropSpecialFlag::DropShardOnce"
            Data.datatable["PB_DT_DropRateMaster"][entry]["ShardId"] = shard
            if Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] < 100.0:
                Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] = Data.constant["ShardDrop"]["ItemRate"]*3*drop_rate_multiplier
        elif entry.split("_")[0] == enemy:
            Data.datatable["PB_DT_DropRateMaster"][entry]["ShardId"] = "None"
            Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] = 0.0
    #If the key shard ends up in mutliple candles make them all disappear once one has been acquired
    if enemy == "Shortcut":
        for index in range(6):
            Data.datatable["PB_DT_GimmickFlagMaster"]["ShortcutLantarn" + "{:03d}".format(index + 2)]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["ShortcutLantarn001"]["Id"]
    if enemy == "FamiliaSilverKnight":
        for index in range(8):
            Data.datatable["PB_DT_GimmickFlagMaster"]["FamilierLantarn" + "{:03d}".format(index + 2)]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["FamilierLantarn001"]["Id"]

def patch_start_chest_entry():
    #Randomize the very first chest so that it is always a weapon
    container = "Treasurebox_SIP000_Tutorial"
    empty_drop_entry(container)
    start_weapon = pick_and_remove(Data.constant["ItemDrop"]["Weapon"]["ItemPool"], Data.constant["ItemDrop"]["Weapon"]["IsUnique"], "Weapon")
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"]       = start_weapon
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"] = Data.constant["ItemDrop"]["Weapon"]["ItemQuantity"]
    Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"]     = Data.constant["ItemDrop"]["Weapon"]["ItemRate"]
    #Give extra bullets if the starting weapon is a gun
    if Data.datatable["PB_DT_WeaponMaster"][start_weapon]["WeaponType"] == "EWeaponType::Gun":
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemId"]       = pick_and_remove(Data.constant["ItemDrop"]["Bullet"]["ItemPool"], Data.constant["ItemDrop"]["Bullet"]["IsUnique"], "Bullet")
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemQuantity"] = Data.constant["ItemDrop"]["Bullet"]["ItemHighQuantity"]
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonRate"]         = Data.constant["ItemDrop"]["Bullet"]["ItemRate"]
    used_chests.remove(container)

def patch_chest_entry(item_type, container):
    #Randomize chest items based on item types
    if not container in used_chests:
        return
    empty_drop_entry(container)
    if Data.constant["ItemDrop"][item_type]["ChestColor"] == "Blue":
        area_id = chest_to_room(container)[:6]
        Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"]               = area_pools[area_id][item_type][0]
        Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"]         = Data.constant["ItemDrop"][item_type]["ItemQuantity"]
        Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"]             = Data.constant["ItemDrop"][item_type]["ItemRate"]
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemId"]             = area_pools[area_id][item_type][1]
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemQuantity"]       = Data.constant["ItemDrop"][item_type]["ItemQuantity"]
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonRate"]               = Data.constant["ItemDrop"][item_type]["ItemRate"]
        Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientId"]         = area_pools[area_id][item_type][2]
        Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientQuantity"]   = Data.constant["ItemDrop"][item_type]["ItemQuantity"]
        Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientRate"]       = Data.constant["ItemDrop"][item_type]["ItemRate"]
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientId"]       = area_pools[area_id][item_type][3]
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientQuantity"] = Data.constant["ItemDrop"][item_type]["ItemQuantity"]
        Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientRate"]     = Data.constant["ItemDrop"][item_type]["ItemRate"]
        Data.datatable["PB_DT_DropRateMaster"][container]["CoinOverride"]             = random.choice(_COIN_TYPES)
        Data.datatable["PB_DT_DropRateMaster"][container]["CoinType"]                 = "EDropCoin::D" + str(Data.datatable["PB_DT_DropRateMaster"][container]["CoinOverride"])
        Data.datatable["PB_DT_DropRateMaster"][container]["AreaChangeTreasureFlag"]   = True
    elif Data.constant["ItemDrop"][item_type]["ChestColor"] == "Red":
        Data.datatable["PB_DT_DropRateMaster"][container]["CoinOverride"] = pick_and_remove(Data.constant["ItemDrop"][item_type]["ItemPool"], Data.constant["ItemDrop"][item_type]["IsUnique"], item_type)
        Data.datatable["PB_DT_DropRateMaster"][container]["CoinType"]     = "EDropCoin::D2000"
        Data.datatable["PB_DT_DropRateMaster"][container]["CoinRate"]     = Data.constant["ItemDrop"][item_type]["ItemRate"]
    else:
        Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"]       = pick_and_remove(Data.constant["ItemDrop"][item_type]["ItemPool"], Data.constant["ItemDrop"][item_type]["IsUnique"], item_type)
        Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"] = Data.constant["ItemDrop"][item_type]["ItemQuantity"]
        Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"]     = Data.constant["ItemDrop"][item_type]["ItemRate"]
    used_chests.remove(container)
    
def patch_enemy_entry(item_type, item_rate, container):
    #Randomize enemy drops in a varied fashion while slightly favouring one item type
    #Also randomize the amount of drops so that it isn't always 4 per enemy
    empty_drop_entry(container)
    if item_type == "CookingMat":
        if random.random() < 2/3 and Data.constant["ItemDrop"]["CookingMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"]       = pick_and_remove(Data.constant["ItemDrop"]["CookingMat"]["ItemPool"], Data.constant["EnemyDrop"]["CookingMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"] = Data.constant["EnemyDrop"]["CookingMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"]     = Data.constant["EnemyDrop"]["CookingMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["ItemDrop"]["StandardMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemId"]       = pick_and_remove(Data.constant["ItemDrop"]["StandardMat"]["ItemPool"], Data.constant["EnemyDrop"]["StandardMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemQuantity"] = Data.constant["EnemyDrop"]["StandardMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonRate"]         = Data.constant["EnemyDrop"]["StandardMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientId"]       = pick_and_remove(Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"], Data.constant["EnemyDrop"]["EnemyMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientQuantity"] = Data.constant["EnemyDrop"]["EnemyMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientRate"]     = Data.constant["EnemyDrop"]["EnemyMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["ItemDrop"]["CookingMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientId"]       = pick_and_remove(Data.constant["ItemDrop"]["CookingMat"]["ItemPool"], Data.constant["EnemyDrop"]["CookingMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientQuantity"] = Data.constant["EnemyDrop"]["CookingMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientRate"]     = Data.constant["EnemyDrop"]["CookingMat"]["ItemRate"]*item_rate
    elif item_type == "StandardMat":
        if random.random() < 2/3 and Data.constant["ItemDrop"]["StandardMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"]       = pick_and_remove(Data.constant["ItemDrop"]["StandardMat"]["ItemPool"], Data.constant["EnemyDrop"]["StandardMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"] = Data.constant["EnemyDrop"]["StandardMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"]     = Data.constant["EnemyDrop"]["StandardMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemId"]       = pick_and_remove(Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"], Data.constant["EnemyDrop"]["EnemyMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemQuantity"] = Data.constant["EnemyDrop"]["EnemyMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonRate"]         = Data.constant["EnemyDrop"]["EnemyMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["ItemDrop"]["CookingMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientId"]       = pick_and_remove(Data.constant["ItemDrop"]["CookingMat"]["ItemPool"], Data.constant["EnemyDrop"]["CookingMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientQuantity"] = Data.constant["EnemyDrop"]["CookingMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientRate"]     = Data.constant["EnemyDrop"]["CookingMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["ItemDrop"]["StandardMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientId"]       = pick_and_remove(Data.constant["ItemDrop"]["StandardMat"]["ItemPool"], Data.constant["EnemyDrop"]["StandardMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientQuantity"] = Data.constant["EnemyDrop"]["StandardMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientRate"]     = Data.constant["EnemyDrop"]["StandardMat"]["ItemRate"]*item_rate
    elif item_type == "EnemyMat":
        if random.random() < 2/3 and Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemId"]       = pick_and_remove(Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"], Data.constant["EnemyDrop"]["EnemyMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemQuantity"] = Data.constant["EnemyDrop"]["EnemyMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["RareItemRate"]     = Data.constant["EnemyDrop"]["EnemyMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["ItemDrop"]["CookingMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemId"]       = pick_and_remove(Data.constant["ItemDrop"]["CookingMat"]["ItemPool"], Data.constant["EnemyDrop"]["CookingMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonItemQuantity"] = Data.constant["EnemyDrop"]["CookingMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonRate"]         = Data.constant["EnemyDrop"]["CookingMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["ItemDrop"]["StandardMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientId"]       = pick_and_remove(Data.constant["ItemDrop"]["StandardMat"]["ItemPool"], Data.constant["EnemyDrop"]["StandardMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientQuantity"] = Data.constant["EnemyDrop"]["StandardMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["RareIngredientRate"]     = Data.constant["EnemyDrop"]["StandardMat"]["ItemRate"]*item_rate
        if random.random() < 2/3 and Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"]:
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientId"]       = pick_and_remove(Data.constant["EnemyDrop"]["EnemyMat"]["ItemPool"], Data.constant["EnemyDrop"]["EnemyMat"]["IsUnique"], item_type)
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientQuantity"] = Data.constant["EnemyDrop"]["EnemyMat"]["ItemQuantity"]
            Data.datatable["PB_DT_DropRateMaster"][container]["CommonIngredientRate"]     = Data.constant["EnemyDrop"]["EnemyMat"]["ItemRate"]*item_rate

def unlock_all_quests():
    #Make all quests available from the start
    #Note that picking a memento or catering quest commits you to that quest until you complete it
    for index in range(20):
        Data.datatable["PB_DT_QuestMaster"]["Quest_Enemy" + "{:02d}".format(index + 1)]["NeedQuestID"] = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Enemy" + "{:02d}".format(index + 1)]["NeedAreaID"]  = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Enemy" + "{:02d}".format(index + 1)]["NeedItemID"]  = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Enemy" + "{:02d}".format(index + 1)]["NeedBossID"]  = "None"
    for index in range(15):
        Data.datatable["PB_DT_QuestMaster"]["Quest_Memento" + "{:02d}".format(index + 1)]["NeedQuestID"] = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Memento" + "{:02d}".format(index + 1)]["NeedAreaID"]  = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Memento" + "{:02d}".format(index + 1)]["NeedItemID"]  = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Memento" + "{:02d}".format(index + 1)]["NeedBossID"]  = "None"
    for index in range(21):
        Data.datatable["PB_DT_QuestMaster"]["Quest_Catering" + "{:02d}".format(index + 1)]["NeedQuestID"] = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Catering" + "{:02d}".format(index + 1)]["NeedAreaID"]  = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Catering" + "{:02d}".format(index + 1)]["NeedItemID"]  = "None"
        Data.datatable["PB_DT_QuestMaster"]["Quest_Catering" + "{:02d}".format(index + 1)]["NeedBossID"]  = "None"

def randomize_quest_requirements():
    #Enemy quests
    all_enemies = list(Data.constant["EnemyInfo"])
    enemy_requirement = []
    for num in range(19):
        chosen = pick_and_remove(all_enemies, True, "None")
        #Don't pick Dom, Bael, IGA, Miriam, or shard candles
        while Enemy.is_final_boss(chosen) or chosen in ["N2013", "N0000"] or chosen in Data.datatable["PB_DT_ShardMaster"]:
            chosen = pick_and_remove(all_enemies, True, "None")
        enemy_requirement.append(chosen)
    #Order them by level, appending bosses at the end
    level_to_enemy = {}
    level_to_boss  = {}
    index = 0
    for enemy in enemy_requirement:
        if Enemy.is_boss(enemy):
            level_to_boss[Data.datatable["PB_DT_CharacterParameterMaster"][enemy]["DefaultEnemyLevel"]*100 + index] = enemy
        else:
            level_to_enemy[Data.datatable["PB_DT_CharacterParameterMaster"][enemy]["DefaultEnemyLevel"]*100 + index] = enemy
        index += 1
    level_to_enemy = dict(sorted(level_to_enemy.items()))
    level_to_boss  = dict(sorted(level_to_boss.items()))
    level_to_enemy.update(level_to_boss)
    #Update requirement
    for index in range(19):
        enemy = list(level_to_enemy.values())[index]
        quest_name = "Quest_Enemy" + "{:02d}".format(index + 1)
        Data.datatable["PB_DT_QuestMaster"][quest_name]["Enemy01"] = enemy
        Data.datatable["PB_DT_QuestMaster"][quest_name]["EnemyNum01"] = len(enemy_to_room[enemy])
        enemy_room_string = ""
        for room in enemy_to_room[enemy]:
            if not Data.datatable["PB_DT_RoomMaster"][room]["OutOfMap"]:
                enemy_room_string += room + ","
        Data.datatable["PB_DT_QuestMaster"][quest_name]["EnemySpawnLocations"] = enemy_room_string[:-1] if enemy_room_string else "none"
    #Memento quests
    for index in range(15):
        Data.datatable["PB_DT_QuestMaster"]["Quest_Memento" + "{:02d}".format(index + 1)]["Item01"] = pick_and_remove(Data.constant["QuestRequirement"]["Memento"]["ItemPool"], True, "None")
    #Catering quests
    for index in range(21):
        Data.datatable["PB_DT_QuestMaster"]["Quest_Catering" + "{:02d}".format(index + 1)]["Item01"] = pick_and_remove(Data.constant["QuestRequirement"]["Catering"]["ItemPool"], True, "None")

def remove_enemy_quest_icons():
    #The icons for enemy quests are not dynamic with room placement so remove them for custom maps
    for index in range(20):
        Data.datatable["PB_DT_QuestMaster"]["Quest_Enemy" + "{:02d}".format(index + 1)]["EnemySpawnLocations"] = "none"

def randomize_quest_rewards():
    #Randomize the rewards that quests give you
    #Quest rewards are meant to be higher tier than overworld items and come at greater quantities
    invert_ratio()
    for entry in Data.datatable["PB_DT_QuestMaster"]:
        item_type = random.choice(quest_type)
        if Data.constant["ItemDrop"][item_type]["ChestColor"] == "Blue":
            Data.datatable["PB_DT_QuestMaster"][entry]["RewardItem01"] = pick_and_remove(Data.constant["ItemDrop"][item_type]["ItemPool"], Data.constant["ItemDrop"][item_type]["IsUnique"], item_type)
            Data.datatable["PB_DT_QuestMaster"][entry]["RewardNum01"] = Data.constant["ItemDrop"][item_type]["ItemHighQuantity"]
        elif Data.constant["ItemDrop"][item_type]["ChestColor"] == "Red":
            Data.datatable["PB_DT_QuestMaster"][entry]["RewardItem01"] = "Money"
            Data.datatable["PB_DT_QuestMaster"][entry]["RewardNum01"] = pick_and_remove(Data.constant["ItemDrop"][item_type]["ItemPool"], Data.constant["ItemDrop"][item_type]["IsUnique"], item_type)
        else:
            Data.datatable["PB_DT_QuestMaster"][entry]["RewardItem01"] = pick_and_remove(Data.constant["ItemDrop"][item_type]["ItemPool"], Data.constant["ItemDrop"][item_type]["IsUnique"], item_type)
            Data.datatable["PB_DT_QuestMaster"][entry]["RewardNum01"] = Data.constant["ItemDrop"][item_type]["ItemHighQuantity"]
    invert_ratio()

def update_catering_quest_info():
    #Update catering quests descriptions so that it is possible to tell what Susie wants
    for index in range(21):
        Data.stringtable["PBScenarioStringTable"]["QST_Catering_Name" + "{:02d}".format(index + 1)]    = Data.translation["Item"][Data.datatable["PB_DT_QuestMaster"]["Quest_Catering" + "{:02d}".format(index + 1)]["Item01"]]
        Data.stringtable["PBScenarioStringTable"]["QST_Catering_Caption" + "{:02d}".format(index + 1)] = "She says she wants to eat until she explodes."

def add_all_hair_apparents_in_shop():
    #Add all hair apparents to the shop for 100G
    Data.datatable["PB_DT_ItemMaster"]["Worldfashionfirstissue"]["buyPrice"]  = 100
    Data.datatable["PB_DT_ItemMaster"]["Worldfashionfirstissue"]["Producted"] = "Event_01_001_0000"
    shop_skip_list.append("Worldfashionfirstissue")
    Shop.PRICE_SKIP_LIST.append("Worldfashionfirstissue")
    for index in range(11):
        Data.datatable["PB_DT_ItemMaster"]["WorldfashionNo" + "{:02d}".format(index + 2)]["buyPrice"]  = 100
        Data.datatable["PB_DT_ItemMaster"]["WorldfashionNo" + "{:02d}".format(index + 2)]["Producted"] = "Event_01_001_0000"
        shop_skip_list.append("WorldfashionNo" + "{:02d}".format(index + 2))
        Shop.PRICE_SKIP_LIST.append("WorldfashionNo" + "{:02d}".format(index + 2))

def remove_all_keys_from_shop():
    #Remove all key items from shop
    Data.datatable["PB_DT_ItemMaster"]["DiscountCard"]["buyPrice"]  = 0
    Data.datatable["PB_DT_ItemMaster"]["DiscountCard"]["sellPrice"] = 0
    Data.datatable["PB_DT_ItemMaster"]["MonarchCrown"]["buyPrice"]  = 0
    Data.datatable["PB_DT_ItemMaster"]["MonarchCrown"]["sellPrice"] = 0

def randomize_shop_items():
    #Reset shop event
    for entry in Data.datatable["PB_DT_ItemMaster"]:
        if entry in shop_skip_list:
            continue
        Data.datatable["PB_DT_ItemMaster"][entry]["Producted"] = "None"
    #Assign random events
    for entry in Data.constant["ItemDrop"]:
        for num in range(Data.constant["ItemDrop"][entry]["ShopRatio"]):
            if Data.constant["ItemDrop"][entry]["ItemPool"]:
                chosen = pick_and_remove(Data.constant["ItemDrop"][entry]["ItemPool"], True, "None")
                while Data.datatable["PB_DT_ItemMaster"][chosen]["buyPrice"] == 0 or chosen in shop_skip_list:
                    chosen = pick_and_remove(Data.constant["ItemDrop"][entry]["ItemPool"], True, "None")
                if random.random() < shop_event_weight:
                    Data.datatable["PB_DT_ItemMaster"][chosen]["Producted"] = random.choice(_BOSS_SHOP_EVENTS)
                else:
                    Data.datatable["PB_DT_ItemMaster"][chosen]["Producted"] = _DEFAULT_SHOP_EVENT

def replace_silver_bromide():
    #Find Silver Bromide and replace it by the Passplate
    for entry in Data.datatable["PB_DT_DropRateMaster"]:
        if Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemId"] == "Silverbromide":
            Data.datatable["PB_DT_DropRateMaster"][entry]["RareItemId"] = "Certificationboard"
    for entry in Data.datatable["PB_DT_QuestMaster"]:
        if Data.datatable["PB_DT_QuestMaster"][entry]["Item01"] == "Silverbromide":
            Data.datatable["PB_DT_QuestMaster"][entry]["Item01"] = "Certificationboard"

def ensure_drop_ids_unique():
    #Make sure that every id number in dropratemaster is unique
    used_ids = []
    for entry in Data.datatable["PB_DT_DropRateMaster"]:
        drop_id = Data.datatable["PB_DT_DropRateMaster"][entry]["Id"]
        while drop_id in used_ids:
            drop_id += 1
        used_ids.append(drop_id)
        Data.datatable["PB_DT_DropRateMaster"][entry]["Id"] = drop_id

def update_shard_candles():
    #While candle shards have entries in DropRateMaster they are completely ignored by the game
    #Instead those are read directly from the level files so they need to be updated to reflect the new shard drops
    for shard in ["Shortcut", "Deepsinker", "FamiliaSilverKnight", "Aquastream", "FamiliaIgniculus"]:
        for room in enemy_to_room[shard]:
            Data.search_and_replace_string(f"{room}_Gimmick", "BP_DM_BaseLantern_ShardChild2_C", "ShardID", shard, Data.datatable["PB_DT_DropRateMaster"][f"{shard}_Shard"]["ShardId"])

def add_game_item(index : int, 
                  item_id : str, 
                  item_type : str, 
                  item_subtype : str, 
                  icon_coord : tuple[int, int], 
                  name : str, 
                  description : str, 
                  price : int, 
                  craftable : bool):
    #Add a completely new item slot into the game
    if item_id in Data.datatable["PB_DT_ItemMaster"]:
        raise Exception("Item already exists.")
    #Edit ItemMaster
    icon_path                                                              = (icon_coord[1]//128)*32 + icon_coord[0]//128
    Data.datatable["PB_DT_ItemMaster"][item_id]                                 = copy.deepcopy(Data.datatable["PB_DT_ItemMaster"]["Potion"])
    Data.datatable["PB_DT_ItemMaster"][item_id]["IconPath"]                     = str(icon_path)
    Data.datatable["PB_DT_ItemMaster"][item_id]["NameStrKey"]                   = f"ITEM_NAME_{item_id}"
    Data.datatable["PB_DT_ItemMaster"][item_id]["DescriptionStrKey"]            = f"ITEM_EXPLAIN_{item_id}"
    Data.datatable["PB_DT_ItemMaster"][item_id]["buyPrice"]                     = price
    Data.datatable["PB_DT_ItemMaster"][item_id]["sellPrice"]                    = 1 if 0 < price < 100 else price//10
    Data.datatable["PB_DT_ItemMaster"][item_id]["Producted"]                    = "None"
    #Edit string entries                                                   
    Data.stringtable["PBMasterStringTable"][f"ITEM_NAME_{item_id}"]             = name
    Data.stringtable["PBMasterStringTable"][f"ITEM_EXPLAIN_{item_id}"]          = description
    #Edit case by case properties                                          
    if item_type == "Accessory":                                                
        Data.datatable["PB_DT_ItemMaster"][item_id]["ItemType"]                 = "ECarriedCatalog::Accessory1"
        Data.datatable["PB_DT_ItemMaster"][item_id]["max"]                      = 99
        Data.datatable["PB_DT_ItemMaster"][item_id]["CarryToBossRushMode"]      = True
        Data.datatable["PB_DT_ArmorMaster"][item_id]                            = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["EmptyAccesory"])
        Data.datatable["PB_DT_ArmorMaster"][item_id]["AttachPoint"]             = "EWeaponAttachPoint::None"
        Data.datatable["PB_DT_ArmorMaster"][item_id]["Category"]                = item_subtype
        if craftable:
            Data.datatable["PB_DT_CraftMaster"][item_id]                        = copy.deepcopy(Data.datatable["PB_DT_CraftMaster"]["Ring"])
            Data.datatable["PB_DT_CraftMaster"][item_id]["CraftItemId"]         = item_id
        Data.datatable_entry_index["PB_DT_ArmorMaster"][item_id]        = index
    if item_type == "Armor":                                                  
        Data.datatable["PB_DT_ItemMaster"][item_id]["ItemType"]                 = "ECarriedCatalog::Body"
        Data.datatable["PB_DT_ItemMaster"][item_id]["max"]                      = 99
        Data.datatable["PB_DT_ItemMaster"][item_id]["CarryToBossRushMode"]      = True
        Data.datatable["PB_DT_ArmorMaster"][item_id]                            = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["EmptyBody"])
        Data.datatable["PB_DT_ArmorMaster"][item_id]["AttachPoint"]             = "EWeaponAttachPoint::None"
        Data.datatable["PB_DT_ArmorMaster"][item_id]["Category"]                = item_subtype
        if craftable:
            Data.datatable["PB_DT_CraftMaster"][item_id]                        = copy.deepcopy(Data.datatable["PB_DT_CraftMaster"]["Tunic"])
            Data.datatable["PB_DT_CraftMaster"][item_id]["CraftItemId"]         = item_id
        Data.datatable_entry_index["PB_DT_ArmorMaster"][item_id]        = index
    if item_type == "Bullet":                                                 
        Data.datatable["PB_DT_ItemMaster"][item_id]["ItemType"]                 = "ECarriedCatalog::Bullet"
        Data.datatable["PB_DT_ItemMaster"][item_id]["max"]                      = 999
        Data.datatable["PB_DT_ItemMaster"][item_id]["CarryToBossRushMode"]      = True
        Data.datatable["PB_DT_AmmunitionMaster"][item_id]                       = copy.deepcopy(Data.datatable["PB_DT_AmmunitionMaster"]["Softpoint"])
        Data.datatable["PB_DT_AmmunitionMaster"][item_id]["BulletID"]           = item_id
        if craftable:
            Data.datatable["PB_DT_CraftMaster"][item_id]                        = copy.deepcopy(Data.datatable["PB_DT_CraftMaster"]["Softpoint"])
            Data.datatable["PB_DT_CraftMaster"][item_id]["CraftItemId"]         = item_id
        if not item_id in Data.datatable["PB_DT_BulletMaster"]:                 
            Data.datatable["PB_DT_BulletMaster"][item_id]                       = copy.deepcopy(Data.datatable["PB_DT_BulletMaster"]["Softpoint"])
            Data.datatable["PB_DT_BulletMaster"][item_id]["DamageId"]           = item_id
        if not item_id in Data.datatable["PB_DT_CollisionMaster"]:              
            Data.datatable["PB_DT_CollisionMaster"][item_id]                    = copy.deepcopy(Data.datatable["PB_DT_CollisionMaster"]["Softpoint"])
            Data.datatable["PB_DT_CollisionMaster"][item_id + "_EX"]            = copy.deepcopy(Data.datatable["PB_DT_CollisionMaster"]["Softpoint_EX"])
        if not item_id in Data.datatable["PB_DT_DamageMaster"]:                 
            Data.datatable["PB_DT_DamageMaster"][item_id]                       = copy.deepcopy(Data.datatable["PB_DT_DamageMaster"]["Softpoint"])
            Data.datatable["PB_DT_DamageMaster"][item_id + "_EX"]               = copy.deepcopy(Data.datatable["PB_DT_DamageMaster"]["Softpoint_EX"])
            Data.datatable["PB_DT_DamageMaster"][item_id + "_EX2"]              = copy.deepcopy(Data.datatable["PB_DT_DamageMaster"]["Softpoint_EX2"])
        Data.datatable_entry_index["PB_DT_AmmunitionMaster"][item_id]   = index
    if item_type == "Potion":                                                 
        Data.datatable["PB_DT_ItemMaster"][item_id]["ItemType"]                 = "ECarriedCatalog::Potion"
        Data.datatable["PB_DT_ItemMaster"][item_id]["max"]                      = 9
        Data.datatable["PB_DT_ConsumableMaster"][item_id]                       = copy.deepcopy(Data.datatable["PB_DT_ConsumableMaster"]["Potion"])
        Data.datatable["PB_DT_ConsumableMaster"][item_id]["SpecialEffectId"]    = item_id
        Data.datatable["PB_DT_SpecialEffectDefinitionMaster"][item_id]          = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["Potion"])
        Data.datatable["PB_DT_SpecialEffectDefinitionMaster"][item_id]["DefId"] = item_id
        Data.datatable["PB_DT_SpecialEffectGroupMaster"][item_id]               = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectGroupMaster"]["Potion"])
        Data.datatable["PB_DT_SpecialEffectGroupMaster"][item_id]["GroupId"]    = item_id
        Data.datatable["PB_DT_SpecialEffectGroupMaster"][item_id]["DefId"]      = item_id
        Data.datatable["PB_DT_SpecialEffectMaster"][item_id]                    = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectMaster"]["Potion"])
        Data.datatable["PB_DT_SpecialEffectMaster"][item_id]["Id"]              = item_id
        Data.datatable["PB_DT_SpecialEffectMaster"][item_id]["GroupId"]         = item_id
        if craftable:
            Data.datatable["PB_DT_CraftMaster"][item_id]                        = copy.deepcopy(Data.datatable["PB_DT_CraftMaster"]["Potion"])
            Data.datatable["PB_DT_CraftMaster"][item_id]["CraftItemId"]         = item_id
        Data.datatable_entry_index["PB_DT_ConsumableMaster"][item_id]   = index

def pick_and_remove(item_array, remove, item_type):
    #Function for picking and remove an item at random
    item = random.choice(item_array)
    if remove:
        if len(item_array) == 1:
            while item_type in chest_type:
                chest_type.remove(item_type)
            while item_type in blue_chest_type:
                blue_chest_type.remove(item_type)
            while item_type in green_chest_type:
                green_chest_type.remove(item_type)
            while item_type in enemy_type:
                enemy_type.remove(item_type)
            while item_type in quest_type:
                quest_type.remove(item_type)
        while item in item_array:
            item_array.remove(item)
    return item

def invert_ratio():
    #Complex function for inverting all item ratios in item drop dictionary
    for entry in Data.constant["ItemDrop"]:
        if Data.constant["ItemDrop"][entry]["IsUnique"]:
            continue
        ratio = []
        new_list = []
        duplicate = 1
        for index in range(len(Data.constant["ItemDrop"][entry]["ItemPool"]) - 1):
            previous = Data.constant["ItemDrop"][entry]["ItemPool"][index]
            current = Data.constant["ItemDrop"][entry]["ItemPool"][index + 1]
            if current == previous:
                duplicate += 1
            else:
                ratio.append(duplicate)
                duplicate = 1
            if index == len(Data.constant["ItemDrop"][entry]["ItemPool"]) - 2:
                ratio.append(duplicate)
            index += 1
        max_ratio = max(ratio)
        Data.constant["ItemDrop"][entry]["ItemPool"] = list(dict.fromkeys(Data.constant["ItemDrop"][entry]["ItemPool"]))
        for index in range(len(Data.constant["ItemDrop"][entry]["ItemPool"])):
            for odd in range(abs(ratio[index] - (max_ratio + 1))):
                new_list.append(Data.constant["ItemDrop"][entry]["ItemPool"][index])
        Data.constant["ItemDrop"][entry]["ItemPool"] = new_list

def create_log(seed, map):
    #Log compatible with the map editor to show key item locations
    file_name = os.path.split(os.path.splitext(map)[0])[-1]
    log = {}
    log["Seed"] = seed
    log["Map"]  = file_name
    log["Key"]  = {}
    for item in key_order:
        if item in KEY_ITEMS:
            log["Key"][Data.translation["Item"][item]] = [chest_to_room(key_item_to_location[item])]
        if item in _KEY_SHARDS:
            log["Key"][Data.translation["Shard"][item]] = enemy_shard_to_room(key_shard_to_location[item])
    log["Beatable"] = final_boss_available()
    return log

def create_log_string(seed : str, map : str, original_enemies):
    #Log string for quickly showing answer to a seed
    file_name = os.path.split(os.path.splitext(map)[0])[-1]
    map_name = file_name if file_name else "Default"
    log_string = ""
    log_string += f"Seed: {seed}\n"
    log_string += f"Map: {map_name}\n"
    log_string += "Key:\n"
    for item in key_order:
        if item in KEY_ITEMS:
            log_string += "  " + Data.translation["Item"][item] + ": " + key_item_to_location[item]
        if item in _KEY_SHARDS:
            log_string += "  " + Data.translation["Shard"][item] + ": " + Data.translation["Enemy"][key_shard_to_location[item]]
            if key_shard_to_location[item] in original_enemies:
                log_string += " (over " + Data.translation["Enemy"][original_enemies[key_shard_to_location[item]]] + ")"
        log_string += "\n"
    log_string += "Beatable: "
    log_string += "Yes" if final_boss_available() else "No"
    return log_string