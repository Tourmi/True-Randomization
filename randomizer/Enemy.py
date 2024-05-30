from __future__ import annotations
from typing import Any, TypedDict

from .GlobalImports import *
from .Constants import *
from . import Data
from . import Utility
from . import Room

ActorPointer = TypedDict('ActorPointer', {'Name':str, 'File': str, 'Index': int})

_MAIN_RESISTANCES = [
    "ZAN",
    "DAG",
    "TOT",
    "FLA",
    "ICE",
    "LIG",
    "HOL",
    "DAR"
]

_STATUS_RESISTANCES = [
    "POI",
    "CUR",
    "STO",
    "SLO"
]

_STATIC_ENEMIES = [
    "N3090",
    "N3099",
    "N3025",
    "N2012",
    "N2013",
    "N0000"
]

_CAPPED_ENEMIES = [
    "N1011",
    "N2001"
]

_UNSIZABLE_ENEMIES = [
    "N3013",
    "N3014",
    "N3077",
    "N3076",
    "N3123",
    "N3100",
    "N3113",
    "N3116",
    "N3117"
]

_LARGES_ENEMIES = [
    "N3067",
    "N3030",
    "N3045",
    "N3016",
    "N3023",
    "N3028",
    "N3081",
    "N2003",
    "N3126"
]

_DEFAULT_ZANGETSU_EXP = {
    "N1001":          34,
    "N1011":          58,
    "N1003":         106,
    "N2004":         178,
    "N1005":         274,
    "N2001":         394,
    "N1006":         538,
    "N1012":         706,
    "N1002":         898,
    "N2014":        1114,
    "N2007":        1354,
    "N2006":        1618,
    "N1011_STRONG": 1906,
    "N1004":        2218,
    "N1008":        2554
}

_SPECIAL_ENEMY_REMOVAL = {
    "m01SIP_004_Enemy": [
        "Chr_N3006_1122"
    ],
    "m01SIP_011_Enemy": [
        "Chr_N3007",
        "Chr_N3008",
        "Chr_N3011"
    ],
    "m11UGD_013_Enemy": [
        "Chr_N3001_Lift4",
        "Chr_N3001_Lift5",
        "Chr_N3001_Lift6",
        "Chr_N3001_Lift8"
    ],
    "m10BIG_001_Enemy": [
        "Chr_N3005_895"
    ],
    "m10BIG_005_Enemy": [
        "Chr_N3005_895"
    ],
    "m10BIG_008_Enemy_Hard": [
        "Chr_N3019_1202",
        "Chr_N3020",
        "Chr_N3021",
        "Chr_N3022",
        "Chr_N3025",
        "Chr_N3026"
    ],
    "m10BIG_009_Enemy": [
        "Chr_N3017"
    ],
    "m10BIG_013_Enemy_Hard": [
        "Chr_N3019_1378",
        "Chr_N3020",
        "Chr_N3021",
        "Chr_N3022",
        "Chr_N3024"
    ],
    "m10BIG_014_Enemy": [
        "Chr_N3018",
        "Chr_N3020",
        "Chr_N3024",
        "Chr_N3026"
    ],
    "m10BIG_016_Enemy": [
        "Chr_N3020",
        "Chr_N3026"
    ],
    "m51EBT_000_Enemy": [
        "Chr_N3126_3612",
        "Chr_N3129_9474",
        "Chr_N3144_9920",
        "Chr_N3150_10960",
        "Chr_N3152",
        "Chr_N3153_3000",
        "Chr_N3155",
        "Chr_N3156"
    ]
}

_SPAWNER_TO_ADVANTAGEOUS_LOCATION = {
    "m01SIP_001_Enemy_Hard": {
        "N3003_Generator_3258":      ( 1890,    0,  120)
    },
    "m01SIP_001_Enemy_Normal": {
        "Chr_N3003_50":                             None
    },
    "m01SIP_003_Enemy": {
        "Chr_N3006_Generator_422":   ( 1200,    0,  300)
    },
    "m01SIP_004_Enemy": {
        "Chr_N3006_1122":                           None
    },
    "m01SIP_005_Enemy": {
        "Chr_N3003_562":                            None,
        "Chr_N3004_1365":            ( 1280,    0,  120)
    },
    "m01SIP_006_Enemy": {
        "Chr_N3006_1":               (  480,    0,  120),
        "Chr_N3006_2":                              None
    },
    "m01SIP_009_Enemy": {
        "Chr_N3003_834":             (  640,    0,  120),
        "Chr_N3004_1589":                           None,
        "Chr_N3005":                                None
    },
    "m01SIP_010_Enemy": {
        "Chr_N3006_2":                              None,
        "Chr_N3006_457":             (  320,    0,  260)
    },
    "m01SIP_011_Enemy": {
        "Chr_N3003_994":                            None,
        "Chr_N3004":                 ( 4400,    0,  120),
        "Chr_N3006_660":                            None,
        "Chr_N3009":                 ( 2220,    0, 1080)
    },
    "m01SIP_014_Enemy": {
        "Chr_N3003_1346":                           None,
        "Chr_N3004":                 (  820,    0,  120),
        "Chr_N3006_478":                            None
    },
    "m01SIP_016_Enemy": {
        "Chr_N1001_2":               (  520,    0,  780),
    },
    "m01SIP_017_Enemy": {
        "Chr_N3006_478":                            None
    },
    "m01SIP_017_Enemy_Hard": {
        "Chr_N3007_1000":            ( 2520,    0,  120)
    },
    "m01SIP_018_Enemy_Hard": {
        "N3090_Generator_50":        (  960,    0,  120)
    },
    "m01SIP_019_Enemy": {
        "Chr_N3006_Generator2_1825":                None,
        "Chr_N3006_Generator_422":   ( 1120,    0,  300)
    },
    "m02VIL_001_Enemy": {
        "Chr_N3003_2274":                           None,
        "Chr_N3003_3":               (  960,    0,  180)
    },
    "m02VIL_006_Enemy": {
        "Chr_N3003_1":               ( 2700,    0,  120),
        "Chr_N3003_2":                              None
    },
    "m03ENT_001_Enemy": {
        "Chr_N3003_68":                             None
    },
    "m03ENT_001_Enemy_Hard": {
        "N3003_Generator_3258":      ( 4980,    0,  120)
    },
    "m03ENT_001_Enemy_Normal": {
        "N3003_Generator_3258":      ( 4980,    0,  120)
    },
    "m03ENT_003_Enemy": {
        "Chr_N3003_68":                             None
    },
    "m03ENT_003_Enemy_Hard": {
        "N3003_Generator_3258":      ( 3880,    0,  120)
    },
    "m03ENT_003_Enemy_Normal": {
        "N3003_Generator_3258":      ( 3880,    0,  120)
    },
    "m03ENT_014_Enemy_Hard": {
        "N3090_Generator_81":        (  560,    0,  840)
    },
    "m03ENT_017_Enemy_Hard": {
        "N3003_Generator_899":       ( 1040,    0,  120)
    },
    "m05SAN_003_Enemy_Hard": {
        "N3090_Generator_95":        ( 2100,    0, 1380)
    },
    "m05SAN_016_Enemy_Hard": {
        "N3090_Generator_142":       ( 2180,    0, 1860)
    },
    "m05SAN_016_Enemy_Normal": {
        "N3090_Generator_142":       ( 2180,    0, 1860)
    },
    "m05SAN_019_Enemy_Normal": {
        "N3090_Generator_142":       (  680,    0, 3000)
    },
    "m05SAN_019_Enemy_Hard": {
        "N3090_Generator_142":       (  680,    0, 3000)
    },
    "m05SAN_020_Enemy_Hard": {
        "N3090_Generator_142":       ( 1920,    0,  780)
    },
    "m07LIB_029_Enemy_Hard": {
        "N3090_Generator_119":       ( 1860,    0,  180)
    },
    "m07LIB_012_Enemy_Hard": {
        "N3090_Generator_107":       (  340,    0, 1020)
    },
    "m07LIB_013_Enemy_Hard": {
        "N3090_Generator2_55":       ( 1080,    0,  240)
    },
    "m07LIB_013_Enemy_Normal": {
        "N3090_Generator2_55":       ( 1080,    0,  240)
    },
    "m07LIB_017_Enemy_Hard": {
        "N3090_Generator_92":        ( 1540,    0,  120)
    },
    "m07LIB_019_Enemy_Hard": {
        "N3090_Generator_86":        (  680,    0,  120)
    },
    "m07LIB_023_Enemy_Hard": {
        "N3090_Generator2_60":       (  600,    0,  120)
    },
    "m07LIB_023_Enemy_Normal": {
        "N3090_Generator2_60":       (  600,    0,  120)
    },
    "m07LIB_027_Enemy_Hard": {
        "N3090_Generator2_112":      (  300,    0,  120)
    },
    "m07LIB_027_Enemy_Normal": {
        "N3090_Generator_53":        (  300,    0,  120)
    },
    "m07LIB_029_Enemy_Normal": {
        "N3090_Generator_119":       ( 1860,    0,  180)
    },
    "m07LIB_032_Enemy_Hard": {
        "N3090_Generator_73":        (  840,    0,  120)
    },
    "m07LIB_035_Enemy_Hard": {
        "N3090_Generator_113":       (  960,    0,  120)
    },
    "m07LIB_035_Enemy_Normal": {
        "N3090_Generator_113":       (  960,    0,  120)
    },
    "m08TWR_005_Enemy_Hard": {
        "N3090_Generator_142":       ( 2200,    0,  120)
    },
    "m08TWR_005_Enemy_Normal": {
        "N3090_Generator_142":       ( 2200,    0,  120)
    },
    "m08TWR_006_Enemy": {
        "N3090_Generator_142":       ( 1080,    0,  300)
    },
    "m08TWR_006_Enemy_Hard": {
        "N3090_Generator2_112":      (  360,    0,  840)
    },
    "m08TWR_013_Enemy_Hard": {
        "N3090_Generator_142":       ( 1600,    0,  120)
    },
    "m08TWR_013_Enemy_Normal": {
        "N3090_Generator_142":       ( 1600,    0,  120)
    },
    "m08TWR_017_Enemy": {            
        "N3082_Generator_1445":      ( 3720, -720, 1640)
    },
    "m08TWR_018_Enemy": {            
        "N3082_Generator_509":       ( 3660,  680, 3660)
    },
    "m11UGD_000_Enemy_Hard": {
        "N3090_Generator_89":        (  500,    0,  120)
    },
    "m11UGD_006_Enemy_Hard": {
        "N3090_Generator_75":        (  180,    0,  940)
    },
    "m11UGD_013_Enemy_Hard": {
        "N3090_Generator2_44":                      None,
        "N3090_Generator3":                         None,
        "N3090_Generator_142":       ( 1600,    0, 1980)
    },
    "m11UGD_013_Enemy_Normal": {
        "N3090_Generator2_44":                      None,
        "N3090_Generator3":                         None,
        "N3090_Generator_142":       ( 1600,    0, 1980)
    },
    "m11UGD_031_Enemy_Hard": {
        "N3090_Generator_142":       ( 2700,    0, 1980)
    },
    "m11UGD_031_Enemy_Normal": {
        "N3090_Generator_142":       ( 2700,    0, 1980)
    },
    "m11UGD_037_Enemy_Hard": {
        "N3090_Generator_79":        (  960,    0, 2220)
    },
    "m11UGD_040_Enemy_Hard": {
        "N3090_Generator_99":        (  960,    0,  960)
    },
    "m14TAR_006_Enemy_Hard": {
        "N3090_Generator_107":       ( 1300,    0,  120)
    },
    "m20JRN_000_Enemy": {            
        "N3126_Generator5":          (10040,    0, 2160)
    },
    "m20JRN_001_Enemy": {            
        "N3126_Generator_119":       ( 7480,    0, 1080)
    },
    "m20JRN_002_Enemy": {            
        "N3126_Generator3_131":                     None,
        "N3126_Generator4":          ( 1980,    0,  300)
    },
    "m51EBT_000_Enemy": {            
        "Chr_N3122_Generator2":      (13820,    0,   20),
        "Chr_N3122_Generator3":      (10080,    0,   20),
        "Chr_N3122_Generator4":      ( 5680,    0,   20),
        "Chr_N3122_Generator_74":    ( 3160,    0,   20)
    }
}

class Enemy:
    @classmethod
    def init(cls):
        cls.current_portrait_pos = 0
        cls.enemy_replacement_invert = {}

    @classmethod
    def set_enemy_level_weight(cls, weight : int):
        cls.enemy_level_weight = WEIGHT_EXPONENTS[weight - 1]

    @classmethod
    def set_boss_level_weight(cls, weight : int):
        cls.boss_level_weight = WEIGHT_EXPONENTS[weight - 1]

    @classmethod
    def set_enemy_tolerance_weight(cls, weight : int):
        cls.enemy_tolerance_weight = WEIGHT_EXPONENTS[weight - 1]

    @classmethod
    def set_boss_tolerance_weight(cls, weight : int):
        cls.boss_tolerance_weight = WEIGHT_EXPONENTS[weight - 1]

    @classmethod
    def get_original_enemy_stats(cls):
        cls.original_enemy_stats : dict[str, dict[str, Any]] = {}
        #Store original enemy stats for convenience
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            cls.original_enemy_stats[entry] = {}
            cls.original_enemy_stats[entry]["Level"] = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]
            cls.original_enemy_stats[entry]["POI"]   = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["POI"]
            cls.original_enemy_stats[entry]["CUR"]   = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["CUR"]
            cls.original_enemy_stats[entry]["STO"]   = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["STO"]
            cls.original_enemy_stats[entry]["SLO"]   = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["SLO"]

    @classmethod
    def _convert_area_to_progress(cls):
        cls.area_to_progress = {}
        #Adapt the area order of Bloodless mode based on her starting position
        start_index = Data.constant["MapOrder"].index("m05SAN")
        for num in range(start_index -1, -1, -1):
            Data.constant["BloodlessModeMapOrder"].append(Data.constant["MapOrder"][num])
        for num in range(start_index +1, len(Data.constant["MapOrder"])):
            Data.constant["BloodlessModeMapOrder"].append(Data.constant["MapOrder"][num])
        #Convert area list to difficulty scale
        for suffix in ["", "Original", "BloodlessMode", "BloodlessModeOriginal"]:
            entry = suffix + "MapOrder"
            cls.area_to_progress[entry] = {}
            for num in range(len(Data.constant[entry])):
                cls.area_to_progress[entry][Data.constant[entry][num]] = num + 1.0
        #Handle in between areas with unique difficulty scale
        cls.area_to_progress["OriginalMapOrder"]["m04GDN_1"] = (cls.area_to_progress["OriginalMapOrder"]["m04GDN"] + cls.area_to_progress["OriginalMapOrder"]["m05SAN"])/2
        cls.area_to_progress["OriginalMapOrder"]["m05SAN_1"] = (cls.area_to_progress["OriginalMapOrder"]["m06KNG"])
        cls.area_to_progress["OriginalMapOrder"]["m07LIB_1"] = (cls.area_to_progress["OriginalMapOrder"]["m06KNG"])
        cls.area_to_progress["OriginalMapOrder"]["m08TWR_1"] = (cls.area_to_progress["OriginalMapOrder"]["m07LIB"] + cls.area_to_progress["OriginalMapOrder"]["m13ARC"])/2
        cls.area_to_progress["OriginalMapOrder"]["m11UGD_1"] = (cls.area_to_progress["OriginalMapOrder"]["m07LIB"] + cls.area_to_progress["OriginalMapOrder"]["m13ARC"])/2
        cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m04GDN_1"] = (cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m04GDN"])
        cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m05SAN_1"] = (cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m05SAN"])
        cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m07LIB_1"] = (cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m06KNG"])
        cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m08TWR_1"] = (cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m07LIB"] + cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m13ARC"])/2
        cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m11UGD_1"] = (cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m07LIB"] + cls.area_to_progress["BloodlessModeOriginalMapOrder"]["m13ARC"])/2
        for area in ["m04GDN", "m05SAN", "m07LIB", "m08TWR", "m11UGD"]:
            cls.area_to_progress["MapOrder"][area + "_1"]              = cls.area_to_progress["MapOrder"][area]
            cls.area_to_progress["BloodlessModeMapOrder"][area + "_1"] = cls.area_to_progress["BloodlessModeMapOrder"][area]
        #Change the order of progressive Zangetsu experience
        cls.zangetsu_exp = copy.deepcopy(_DEFAULT_ZANGETSU_EXP)
        new_boss_order = []
        for num in range(len(Data.constant["MapOrder"])):
            for enemy in cls.zangetsu_exp:
                current_area = Data.constant["EnemyInfo"][enemy]["AreaID"]
                if cls.area_to_progress["MapOrder"][current_area] == num + 1.0:
                    new_boss_order.append(enemy)
        if len(new_boss_order) != len(cls.zangetsu_exp):
            raise IndexError("New Zangetsu boss order mismatches original EXP order length")
        values = list(cls.zangetsu_exp.values())
        cls.zangetsu_exp.clear()
        cls.zangetsu_exp.update(dict(zip(new_boss_order, values)))

    @staticmethod
    def increase_starting_stats():
        #Random enemy levels can be rough at the start of the game so give the player a starting stat boost
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0000"]["MaxHP"]        += Data.datatable["PB_DT_CoordinateParameter"]["HpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0000"]["MaxMP"]        += Data.datatable["PB_DT_CoordinateParameter"]["MpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0000"]["MaxHP99Enemy"] += Data.datatable["PB_DT_CoordinateParameter"]["HpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0000"]["MaxMP99Enemy"] += Data.datatable["PB_DT_CoordinateParameter"]["MpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["MaxHP"]        += Data.datatable["PB_DT_CoordinateParameter"]["HpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["MaxMP"]        += Data.datatable["PB_DT_CoordinateParameter"]["MpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["MaxHP99Enemy"] += Data.datatable["PB_DT_CoordinateParameter"]["HpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["MaxMP99Enemy"] += Data.datatable["PB_DT_CoordinateParameter"]["MpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0006"]["MaxHP"]        += Data.datatable["PB_DT_CoordinateParameter"]["HpMaxUpLimit"]["Value"]/2
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0006"]["MaxMP"]        += Data.datatable["PB_DT_CoordinateParameter"]["MpMaxUpLimit"]["Value"]/2
        #Reduce the stats gained from upgrades in return
        Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["MaxHPUP"]["Parameter01"]             /= 2
        Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["MaxMPUP"]["Parameter01"]             /= 2
        Data.datatable["PB_DT_CoordinateParameter"]["BloodlessMainStoryModeMaxHpUpAmount"]["Value"] /= 2
        Data.datatable["PB_DT_CoordinateParameter"]["BloodlessMainStoryModeMaxMpUpAmount"]["Value"] /= 2
        #As well as the upgrade cap
        Data.datatable["PB_DT_CoordinateParameter"]["HpMaxUpLimit"]["Value"] /= 2
        Data.datatable["PB_DT_CoordinateParameter"]["MpMaxUpLimit"]["Value"] /= 2

    @staticmethod
    def set_zangetsu_progressive_level(nightmare : bool):
        #Progressive Zangetsu is all about using level ups for combat growth
        #Nightmare only lets you level up off of bosses so adapt the stats for that
        if nightmare:
            target_level = 16
            Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffHp"]["Value"]  = 0.0
            Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffMp"]["Value"]  = 0.0
            Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffStr"]["Value"] = 0.0
            Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffCon"]["Value"] = 0.0
            Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffInt"]["Value"] = 0.0
            Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffMnd"]["Value"] = 0.0
            Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffLuc"]["Value"] = 0.0
        else:
            target_level = 40
        Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffStr"]["Value"] += round(93/(target_level - 1), 3)
        Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffCon"]["Value"] += round(90/(target_level - 1), 3)
        Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffInt"]["Value"] += round(90/(target_level - 1), 3)
        Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffMnd"]["Value"] += round(87/(target_level - 1), 3)
        Data.datatable["PB_DT_CoordinateParameter"]["ZangetsuGrowthCoeffLuc"]["Value"] += round(45/(target_level - 1), 3)

    @staticmethod
    def set_zangetsu_nightmare_damage():
        #Progressive Zangetsu on nightmare has to be built over hard since the vanilla nightmare slot is hardcoded to not receive EXP
        #Update the hard mode damage multipliers to reflect nightmare
        Data.datatable["PB_DT_CoordinateParameter"]["HardEnemyAttackAdd"]["Value"]    = Data.datatable["PB_DT_CoordinateParameter"]["NightmareEnemyAttackAdd"]["Value"]
        Data.datatable["PB_DT_CoordinateParameter"]["HardEnemyDamageRate"]["Value"]   = Data.datatable["PB_DT_CoordinateParameter"]["NightmareEnemyDamageRate"]["Value"]
        Data.datatable["PB_DT_CoordinateParameter"]["HardBossAttackAdd"]["Value"]     = Data.datatable["PB_DT_CoordinateParameter"]["NightmareBossAttackAdd"]["Value"]
        Data.datatable["PB_DT_CoordinateParameter"]["HardBossDamageRate"]["Value"]    = Data.datatable["PB_DT_CoordinateParameter"]["NightmareBossDamageRate"]["Value"]
        Data.datatable["PB_DT_CoordinateParameter"]["HardGimmickDamageRate"]["Value"] = Data.datatable["PB_DT_CoordinateParameter"]["NightmareGimmickDamageRate"]["Value"]

    @classmethod
    def set_zangetsu_enemy_exp(cls):
        #On nightmare only bosses should give EXP
        #Make it so that each major boss gives exactly one level up if fought in order
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] == 0:
                continue
            if entry in cls.zangetsu_exp:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] = cls.zangetsu_exp[entry]
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]        = cls.zangetsu_exp[entry]
            elif entry[0:5] in cls.zangetsu_exp:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] = cls.zangetsu_exp[entry[0:5]]
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]        = cls.zangetsu_exp[entry[0:5]]
            else:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] = 0
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]        = 0

    @staticmethod
    def reset_zangetsu_starting_stats():
        #Zangetsu is very strong by default due to him weilding a late game weapon
        #Make all starting stats 0 to compensate
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["STR"]        = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["INT"]        = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["CON"]        = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["MND"]        = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["LUC"]        = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["STR99Enemy"] = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["INT99Enemy"] = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["CON99Enemy"] = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["MND99Enemy"] = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"]["P0001"]["LUC99Enemy"] = 0.0

    @staticmethod
    def update_brv_boss_speed(difficulty : str):
        #Update boss revenge bosses to have the animation speed of the chosen difficulty
        Data.datatable["PB_DT_CharacterParameterMaster"]["N1009_Enemy"]["AnimaionPlayRateNormal"]  = Data.datatable["PB_DT_CharacterParameterMaster"]["N1009_Enemy"]["AnimaionPlayRate" + difficulty]
        Data.datatable["PB_DT_CharacterParameterMaster"]["N1011_STRONG"]["AnimaionPlayRateNormal"] = Data.datatable["PB_DT_CharacterParameterMaster"]["N1011_STRONG"]["AnimaionPlayRate" + difficulty]
        Data.datatable["PB_DT_CharacterParameterMaster"]["N0000"]["AnimaionPlayRateNormal"]        = Data.datatable["PB_DT_CharacterParameterMaster"]["N0000"]["AnimaionPlayRate" + difficulty]

    @staticmethod
    def update_brv_damage(difficulty):
        #Rebalance boss revenge so that damage is canon with the main game
        #This also means that random resistances will now affect this mode
        if difficulty == "Normal":
            boss_attack_add  = 0.0
            boss_damage_rate = 1.0
        else:
            boss_attack_add  = Data.datatable["PB_DT_CoordinateParameter"][difficulty + "BossAttackAdd"]["Value"]
            boss_damage_rate = Data.datatable["PB_DT_CoordinateParameter"][difficulty + "BossDamageRate"]["Value"]
        for brv_entry in Data.datatable["PB_DT_BRVAttackDamage"]:
            #Getting enemy strength as if level 45
            target_level = 45
            if Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["Owner"] == "Zangetsu":
                base = Enemy.calculate_stat_with_level("N1011_STRONG", target_level, "STR")
            elif Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["Owner"] == "Dominique":
                base = Enemy.calculate_stat_with_level("N1009_Enemy", target_level, "STR")
            elif Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["Owner"] == "Miriam":
                base = Enemy.calculate_stat_with_level("N0000", target_level, "STR")
            #Multiplier for crits on Gremory
            critical = 2.5 if Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["IsZangetsutoAttack"] else 1.0
            #Getting attack multiplier and attributes from DamageMaster
            multiplier = 1.0
            attribute  = []
            #This brv_entry has a different name than the corresponding boss revenge one
            if brv_entry == "N1008_Moon_Attack_01_Burst":
                for attr in _MAIN_RESISTANCES:
                    if Data.datatable["PB_DT_DamageMaster"]["N1008_Moon_Attack_Screen"][attr]:
                        attribute.append(attr)
            #This brv_entry is shared for all of Zangetsu's Flying Vajra elemental versions in boss revenge so average its damage multiplier between the 3 elements
            elif brv_entry == "N1011_ATTACK_EXPLOSION":
                multiplier = (Data.datatable["PB_DT_DamageMaster"]["N1011_ATTACK_ICE_EXPLOSION"]["STR_Correction"] + Data.datatable["PB_DT_DamageMaster"]["N1011_ATTACK_FIRE_EXPLOSION"]["STR_Correction"])/2
            #Rest is straightforward
            else:
                for damage_entry in Data.datatable["PB_DT_DamageMaster"]:
                    if brv_entry in damage_entry:
                        multiplier = Data.datatable["PB_DT_DamageMaster"][damage_entry]["STR_Correction"]
                        if brv_entry == damage_entry:
                            for attr in _MAIN_RESISTANCES:
                                if Data.datatable["PB_DT_DamageMaster"][damage_entry][attr]:
                                    attribute.append(attr)
                            break
                if multiplier == 0.0:
                    continue
            #Getting enemy and player resistances
            andrealphus = 0.0
            bathin      = 0.0
            bloodless   = 0.0
            gremory     = 0.0
            zangetsu    = 0.0
            dominique   = 0.0
            miriam      = 0.0
            for attr in attribute:
                #Add up resistances into a multiplier and average out
                andrealphus += 1.0 - Data.datatable["PB_DT_CharacterParameterMaster"]["P0004"][attr]/100
                bathin      += 1.0 - Data.datatable["PB_DT_CharacterParameterMaster"]["P0005"][attr]/100
                bloodless   += 1.0 - Data.datatable["PB_DT_CharacterParameterMaster"]["P0006"][attr]/100
                gremory     += 1.0 - Data.datatable["PB_DT_CharacterParameterMaster"]["P0007"][attr]/100
                zangetsu    += 1.0 - Data.datatable["PB_DT_CharacterParameterMaster"]["N1011_STRONG"][attr]/100
                dominique   += 1.0 - Data.datatable["PB_DT_CharacterParameterMaster"]["N1009_Enemy"][attr]/100
                miriam      += 1.0 - Data.datatable["PB_DT_CharacterParameterMaster"]["N0000"][attr]/100
            if attribute:
                andrealphus /= len(attribute)
                bathin      /= len(attribute)
                bloodless   /= len(attribute)
                gremory     /= len(attribute)
                zangetsu    /= len(attribute)
                dominique   /= len(attribute)
                miriam      /= len(attribute)
            else:
                #If the attack has no attributes set every multiplier to 1 except for Gremory who is resistant to almost everything
                andrealphus = 1.0
                bathin      = 1.0
                bloodless   = 1.0
                gremory     = 0.75
                zangetsu    = 1.0
                dominique   = 1.0
                miriam      = 1.0
            #Calculating enemy damage
            if Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["ChanceAndrealphus"] == 100.0 and Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["ChanceBathin"] == 100.0 and Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["ChanceBloodless"] == 100.0 and Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["ChanceGremory"] == 100.0:
                Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["VsAndrealphus"] = float(int(max(max(base*multiplier - 40 + boss_attack_add, 1.0)*andrealphus     *boss_damage_rate, 1.0)))
                Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["VsBathin"]      = float(int(max(max(base*multiplier - 40 + boss_attack_add, 1.0)*bathin          *boss_damage_rate, 1.0)))
                Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["VsBloodless"]   = float(int(max(max(base*multiplier - 40 + boss_attack_add, 1.0)*bloodless       *boss_damage_rate, 1.0)))
                Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["VsGremory"]     = float(int(max(max(base*multiplier - 40 + boss_attack_add, 1.0)*gremory*critical*boss_damage_rate, 1.0)))
            #Calculating player damage
            if brv_entry in Data.constant["BossBase"]:
                Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["VsZangetsu"]    = float(int(max(Data.constant["BossBase"][brv_entry]*zangetsu , 1.0)))
                Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["VsDominique"]   = float(int(max(Data.constant["BossBase"][brv_entry]*dominique, 1.0)))
                Data.datatable["PB_DT_BRVAttackDamage"][brv_entry]["VsMiriam"]      = float(int(max(Data.constant["BossBase"][brv_entry]*miriam   , 1.0)))

    @classmethod
    def rebalance_enemies_to_map(cls):
        #If custom map is on then default enemy levels need to be rebalanced in order you encounter them
        cls._convert_area_to_progress()
        for enemy in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if not Enemy.is_enemy(enemy) or enemy in _STATIC_ENEMIES or Enemy.is_final_boss(enemy):
                continue
            for suffix in ["", "BloodlessMode"]:
                current_level = Data.datatable["PB_DT_CharacterParameterMaster"][enemy][suffix + "DefaultEnemyLevel"]
                if Enemy.is_main_enemy(enemy):
                    current_area = Data.constant["EnemyInfo"][enemy]["AreaID"]
                    #8 Bit Nightmare
                    if current_area == "m51EBT":
                        if cls.area_to_progress[suffix + "MapOrder"]["m06KNG"] - cls.area_to_progress[suffix + "OriginalMapOrder"]["m06KNG"] < -2:
                            current_level -= 10
                        if cls.area_to_progress[suffix + "MapOrder"]["m06KNG"] - cls.area_to_progress[suffix + "OriginalMapOrder"]["m06KNG"] < -5:
                            current_level -= 10
                    #Kingdom 2 Crowns
                    elif current_area == "m19K2C":
                        if cls.area_to_progress[suffix + "MapOrder"]["m09TRN"] - cls.area_to_progress[suffix + "OriginalMapOrder"]["m09TRN"] > 1:
                            current_level += 10
                        if cls.area_to_progress[suffix + "MapOrder"]["m09TRN"] - cls.area_to_progress[suffix + "OriginalMapOrder"]["m09TRN"] > 4:
                            current_level += 10
                    #Journey
                    elif current_area == "m20JRN":
                        new_area_progress = max(cls.area_to_progress[suffix + "MapOrder"]["m06KNG"]        , cls.area_to_progress[suffix + "MapOrder"]["m10BIG"]        , cls.area_to_progress[suffix + "MapOrder"]["m12SND"])
                        old_area_progress = max(cls.area_to_progress[suffix + "OriginalMapOrder"]["m06KNG"], cls.area_to_progress[suffix + "OriginalMapOrder"]["m10BIG"], cls.area_to_progress[suffix + "OriginalMapOrder"]["m12SND"])
                        if new_area_progress - old_area_progress < -4:
                            current_level -= 10
                        if new_area_progress - old_area_progress < -9:
                            current_level -= 10
                    #Other
                    elif current_area in cls.area_to_progress[suffix + "OriginalMapOrder"]:
                        current_level = round(current_level + (cls.area_to_progress[suffix + "MapOrder"][current_area] - cls.area_to_progress[suffix + "OriginalMapOrder"][current_area])*(40/17))
                        current_level = min(max(current_level, 1), 50)
                #Patch
                cls.patch_enemy_level(current_level, enemy, suffix)

    @classmethod
    def set_custom_enemy_level(cls, value):
        #If custom NG+ is chosen ignore random levels and assign a set value to all enemies
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if Enemy.is_enemy(entry):
                cls.patch_enemy_level(value, entry, "")
                cls.patch_enemy_level(value, entry, "BloodlessMode")

    @classmethod
    def randomize_enemy_levels(cls):
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if Enemy.is_enemy(entry) and not Enemy.is_boss_part(entry):
                cls._randomize_level_for(entry, cls.enemy_level_weight)

    @classmethod
    def randomize_boss_levels(cls):
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if Enemy.is_boss_part(entry):
                cls._randomize_level_for(entry, cls.boss_level_weight)

    @classmethod
    def _randomize_level_for(cls, entry, weight):
        for suffix in ["", "BloodlessMode"]:
            #Some bosses have a cap for either being too boring or having a time limit
            max_level = 50 if entry in _CAPPED_ENEMIES else 99
            #The final boss should be an average of 50 for both
            default_level = 50 if Enemy.is_final_boss(entry) else Data.datatable["PB_DT_CharacterParameterMaster"][entry][suffix + "DefaultEnemyLevel"]
            #Patch level
            cls.patch_enemy_level(Utility.random_weighted(default_level, 1, max_level, 1, weight), entry, suffix)

    @classmethod
    def randomize_enemy_tolerances(cls):
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if Enemy.is_enemy(entry) and not Enemy.is_boss_part(entry):
                Enemy._randomize_tolerances_for(entry, cls.enemy_tolerance_weight)

    @classmethod
    def randomize_boss_tolerances(cls):
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if Enemy.is_boss_part(entry):
                Enemy._randomize_tolerances_for(entry, cls.boss_tolerance_weight)

    @staticmethod
    def _randomize_tolerances_for(entry, weight):
        #Don't randomize entries that are meant to guard everything
        if (Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ZAN"] == 100.0 and 
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DAG"] == 100.0 and 
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["TOT"] == 100.0 and 
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["FLA"] == 100.0 and 
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ICE"] == 100.0 and 
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["LIG"] == 100.0 and 
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["HOL"] == 100.0 and 
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DAR"] == 100.0):
            return
        #Weak points
        if entry in ["N3015_HEAD", "N1001_HEAD", "N2001_HEAD"]:
            for attr in _MAIN_RESISTANCES:
                if Data.datatable["PB_DT_CharacterParameterMaster"][entry[0:5]][attr] < -20:
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = -100
                else:
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = Data.datatable["PB_DT_CharacterParameterMaster"][entry[0:5]][attr]-80
        #Strong parts
        elif entry in ["N3108_GUARD", "N2001_ARMOR"]:
            for attr in _MAIN_RESISTANCES:
                if Data.datatable["PB_DT_CharacterParameterMaster"][entry[0:5]][attr] > 20:
                        Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = 100
                else:
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = Data.datatable["PB_DT_CharacterParameterMaster"][entry[0:5]][attr]+80
        #Bael
        elif entry[0:5] == "N1013" and entry != "N1013_Bael" or entry == "N1009_Bael":
            for attr in _MAIN_RESISTANCES:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = Data.datatable["PB_DT_CharacterParameterMaster"]["N1013_Bael"][attr]
        #Greedling
        elif entry == "N3125":
            for attr in _MAIN_RESISTANCES:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = Data.datatable["PB_DT_CharacterParameterMaster"]["N2016"][attr]
        #Dullahammer EX
        elif entry == "N3127":
            for attr in _MAIN_RESISTANCES:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = Data.datatable["PB_DT_CharacterParameterMaster"]["N3015"][attr]
        #Main entry
        elif Enemy.is_main_enemy(entry):
            #Use the original resistances to create an average to base the random resistances off of
            average = 0
            for attr in _MAIN_RESISTANCES:
                average += Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr]
            average = average/len(_MAIN_RESISTANCES)
            for attr in _MAIN_RESISTANCES:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = Utility.random_weighted(round(average), -100, 100, 5, weight)
        #Sub entry
        else:
            for attr in _MAIN_RESISTANCES:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = Data.datatable["PB_DT_CharacterParameterMaster"][entry[0:5]][attr]

    @classmethod
    def randomize_enemy_locations(cls):
        """
        This needs to be done before item randomization so that the logic adapts\n
        Create a dict for enemy id to their class names
        """
        cls.enemy_id_to_class : dict[str, str] = {}
        for actor in Data.constant["ActorPointer"].keys():
            enemy_id = Data.constant["ActorPointer"][actor]["Name"]
            if enemy_id in cls.enemy_id_to_class:
                continue
            cls.enemy_id_to_class[enemy_id] = actor
        cls.enemy_id_to_class["N3099"] = cls.enemy_id_to_class["N3090"]
        #Gather portrait indexes
        cls.available_portrait_index = []
        for actor in Data.constant["ActorPointer"]:
            if "N3100" in actor:
                cls.available_portrait_index.append(int(actor.split("_")[2]))
        #Get enemy list
        old_enemy_slots : list[str] = []
        for enemy in Data.constant["EnemyInfo"]:
            if Data.constant["EnemyInfo"][enemy]["Type"] in ["Ground", "Air", "Spawner"]:
                old_enemy_slots.append(enemy)
        new_enemy_slots = copy.deepcopy(old_enemy_slots)
        #Shuffle enemies (special)
        cls.enemy_replacement : dict[str, str] = {}
        cls.enemy_replacement_invert : dict[str, str] = {}
        for enemy in copy.deepcopy(old_enemy_slots):
            chosen = random.choice(new_enemy_slots)
            #Prevent large enemies from ending up over the morte
            if enemy == "N3003":
                while Data.constant["EnemyInfo"][chosen]["Weight"] > Data.constant["EnemyInfo"][enemy]["Weight"]:
                    chosen = random.choice(new_enemy_slots)
            #Some enemies completely ignores any scale modifiers so prevent them from going over large enemies
            elif enemy in _LARGES_ENEMIES:
                while chosen in _UNSIZABLE_ENEMIES:
                    chosen = random.choice(new_enemy_slots)
            else:
                continue
            cls.enemy_replacement[enemy] = chosen
            new_enemy_slots.remove(chosen)
            old_enemy_slots.remove(enemy)
        #Shuffle enemies
        for enemy in old_enemy_slots:
            chosen = random.choice(new_enemy_slots)
            cls.enemy_replacement[enemy] = chosen
            new_enemy_slots.remove(chosen)
        for enemy in cls.enemy_replacement:
            cls.enemy_replacement_invert[cls.enemy_replacement[enemy]] = enemy
        #Remove the lone Seama in the early Galleon room since it is too weak to reflect its weight of 4
        if cls.enemy_replacement["N3006"] != "N3006":
            cls.remove_enemy_info("m01SIP_004", "N3006")
        #Update enemy location info
        for room in Data.constant["RoomRequirement"]:
            #Spawns in backer rooms don't change
            if room in ["m88BKR_002", "m88BKR_004"]:
                continue
            for door in Data.constant["RoomRequirement"][room]:
                for check in list(Data.constant["RoomRequirement"][room][door]):
                    enemy_profile = Utility.split_enemy_profile(check)
                    #Gusions in cages don't change
                    if room in ["m07LIB_001", "m13ARC_001"] and enemy_profile[0] == "N3035":
                        continue
                    #Check enemy
                    if enemy_profile[0] in cls.enemy_replacement:
                        if cls.enemy_replacement[enemy_profile[0]] == enemy_profile[0]:
                            continue
                        #Replace enemy
                        if enemy_profile[1]:
                            suffix = "_" + enemy_profile[1]
                        else:
                            suffix = enemy_profile[1]
                        #Scythe Mite and 8 Bit Zombie spawners seem to fail spawning anything in rooms of resistricted sizes
                        if not (Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"] < 2 and cls.enemy_replacement[enemy_profile[0]] in ["N3082", "N3121"]):
                            Data.constant["RoomRequirement"][room][door][cls.enemy_replacement[enemy_profile[0]] + suffix] = Data.constant["RoomRequirement"][room][door][check]
                        del Data.constant["RoomRequirement"][room][door][check]
        #Remove the Gusions from library and labs if they were scaled up
        if cls.enemy_replacement_invert["N3035"] in _LARGES_ENEMIES:
            cls.remove_enemy_info("m07LIB_001", "N3035")
            cls.remove_enemy_info("m13ARC_001", "N3035")

    @staticmethod
    def remove_enemy_info(room, enemy_id):
        for door in Data.constant["RoomRequirement"][room]:
            for check in list(Data.constant["RoomRequirement"][room][door]):
                enemy_profile = Utility.split_enemy_profile(check)
                if enemy_profile[0] == enemy_id:
                    del Data.constant["RoomRequirement"][room][door][check]

    @classmethod
    def update_enemy_locations(cls):
        #Actually do the removals mentioned above
        if cls.enemy_replacement_invert["N3035"] in _LARGES_ENEMIES:
            Room.remove_level_class("m07LIB_001_Gimmick", "Chr_N3035_C")
            Room.remove_level_class("m13ARC_001_Gimmick", "IncubatorGlass_BP_C")
        #Patch enemies in rooms
        for room in Data.constant["RoomRequirement"]:
            cls.change_room_enemies(room)

    @classmethod
    def change_room_enemies(cls, room):
        enemy_countdown = {}
        #Loop through all difficulties
        for difficulty in ["", "_Normal", "_Hard"]:
            filename = room + "_Enemy" + difficulty
            if not filename in Data.game_data:
                continue
            #Loop through all exports
            for export_index in range(len(Data.game_data[filename].Exports)):
                #Check if the export is an enemy
                export_name = str(Data.game_data[filename].Exports[export_index].ObjectName)
                if Data.game_data[filename].Exports[export_index].OuterIndex.Index == 0:
                    continue
                class_index = Data.game_data[filename].Exports[export_index].ClassIndex.Index
                if class_index >= 0:
                    continue
                old_class_name = str(Data.game_data[filename].Imports[abs(class_index) - 1].ObjectName)
                if not old_class_name in Data.constant["ActorPointer"]:
                    continue
                old_enemy_id = Data.constant["ActorPointer"][old_class_name]["Name"]
                if not Enemy.is_enemy(old_enemy_id):
                    continue
                #The village has unused moco weeds
                if room == "m02VIL_006" and old_enemy_id == "N3066":
                    continue
                #If it is a dulla head assume it's a Malediction
                if old_enemy_id == "N3090":
                    old_enemy_id = "N3099"
                #Get the old actor's properties
                location = FVector(0, 0, 0)
                rotation = FRotator(0, 0, 0)
                scale    = FVector(1, 1, 1)
                for data in Data.game_data[filename].Exports[export_index].Data:
                    #Change it back to a dulla head if the setting is there
                    if str(data.Name) == "SpawnIsN3099":
                        old_enemy_id = "N3090"
                    if str(data.Name) == "RootComponent":
                        root_index = int(str(data.Value)) - 1
                        for root_data in Data.game_data[filename].Exports[root_index].Data:
                            if str(root_data.Name) == "RelativeLocation":
                                location = root_data.Value[0].Value
                            if str(root_data.Name) == "RelativeRotation":
                                rotation = root_data.Value[0].Value
                            if str(root_data.Name) == "RelativeScale3D":
                                scale    = root_data.Value[0].Value
                if location.X < -500:
                    continue
                if not old_enemy_id in cls.enemy_replacement:
                    continue
                new_enemy_id = cls.enemy_replacement[old_enemy_id]
                if old_enemy_id == new_enemy_id:
                    continue
                #Remove the old enemy
                Room.remove_level_actor(filename, export_index)
                #Some enemies shouldn't get replaced and only deleted
                if filename in _SPECIAL_ENEMY_REMOVAL:
                    if export_name in _SPECIAL_ENEMY_REMOVAL[filename]:
                        continue
                #If non-spawner enemies are placed over spawner ones determine an advantageous location to avoid clipping into objects
                if filename in _SPAWNER_TO_ADVANTAGEOUS_LOCATION:
                    if export_name in _SPAWNER_TO_ADVANTAGEOUS_LOCATION[filename] and Data.constant["EnemyInfo"][new_enemy_id]["Type"] != "Spawner":
                        if _SPAWNER_TO_ADVANTAGEOUS_LOCATION[filename][export_name]:
                            location.X = _SPAWNER_TO_ADVANTAGEOUS_LOCATION[filename][export_name][0]
                            location.Y = _SPAWNER_TO_ADVANTAGEOUS_LOCATION[filename][export_name][1]
                            location.Z = _SPAWNER_TO_ADVANTAGEOUS_LOCATION[filename][export_name][2]
                        else:
                            continue
                #Balance enemy spawns around their weight
                old_weight = Data.constant["EnemyInfo"][old_enemy_id]["Weight"]
                new_weight = Data.constant["EnemyInfo"][new_enemy_id]["Weight"]
                if filename == "m01SIP_018_Enemy_Hard" and export_name == "N3090_Generator_50":
                    old_weight -= 1
                #If the new weight is higher only replace a portion of the enemy's instances
                if new_weight > old_weight:
                    enemy_num = 2**(new_weight - old_weight)
                    if new_enemy_id in enemy_countdown:
                        if enemy_countdown[new_enemy_id] == 0:
                            cls.add_level_enemy(filename, export_name, old_enemy_id, new_enemy_id, location, rotation, scale, 0, 0)
                            enemy_countdown[new_enemy_id] = enemy_num
                    else:
                        enemy_countdown[new_enemy_id] = enemy_num
                        cls.add_level_enemy(filename, export_name, old_enemy_id, new_enemy_id, location, rotation, scale, 0, 0)
                    enemy_countdown[new_enemy_id] -= 1
                #If the new weight is lower spawn more instances of the enemy with the old location as its center
                elif new_weight < old_weight:
                    enemy_num = 2**(old_weight - new_weight)
                    offset = 120*(1.5**(new_weight - 1))
                    if old_enemy_id in _LARGES_ENEMIES:
                        offset *= 1.5
                    for num in range(enemy_num):
                        horizontal_offset = -offset*(enemy_num - 1)/2 + offset*num
                        if "Air" in Data.constant["EnemyInfo"][new_enemy_id]["Type"] and not new_enemy_id in ["N3029", "N3030"]:
                            vertical_offset = random.uniform(-offset, offset)
                        else:
                            vertical_offset = 0
                        cls.add_level_enemy(filename, export_name, old_enemy_id, new_enemy_id, location, rotation, scale, horizontal_offset, vertical_offset)
                #If the new weight is identical then do a standard replacement
                else:
                    cls.add_level_enemy(filename, export_name, old_enemy_id, new_enemy_id, location, rotation, scale, 0, 0)

    @classmethod
    def add_level_enemy(cls, 
                        filename, 
                        export_name, 
                        old_enemy_id, 
                        new_enemy_id, 
                        location, 
                        rotation, 
                        scale, 
                        horizontal_offset, 
                        vertical_offset):
        room = filename.split("_Enemy")[0]
        room_width  = Data.datatable["PB_DT_RoomMaster"][room]["AreaWidthSize"]*1260
        room_height = Data.datatable["PB_DT_RoomMaster"][room]["AreaHeightSize"]*720
        hard_mode = "Hard" in filename
        location = FVector(location.X, location.Y, location.Z)
        rotation = FRotator(rotation.Pitch, rotation.Yaw, rotation.Roll)
        scale    = FVector(scale.X, scale.Y, scale.Z)
        #If the room is a rotating 3d one then use the forward vector to shift position
        if room in Room.ROTATING_ROOM_TO_CENTER:
            rotation.Yaw = -math.degrees(math.atan2(location.X - Room.ROTATING_ROOM_TO_CENTER[room][0], location.Y - Room.ROTATING_ROOM_TO_CENTER[room][1]))
            forward_vector = (math.sin(math.radians(rotation.Yaw))*(-1),      math.cos(math.radians(rotation.Yaw)))
            right_vector   = (math.sin(math.radians(rotation.Yaw - 90))*(-1), math.cos(math.radians(rotation.Yaw - 90)))
        else:
            rotation.Yaw = 0
            forward_vector = (0, 1)
            right_vector   = (1, 0)
            location.Y = 0
        #Apply offsets
        location.X += right_vector[0]*horizontal_offset
        location.Y += right_vector[1]*horizontal_offset
        location.Z += vertical_offset
        #If it is a portrait then cycle through each version
        if new_enemy_id == "N3100":
            new_class_name = "Chr_N3100_" + "{:03d}".format(cls.available_portrait_index[cls.current_portrait_pos]) + "_C"
            if cls.current_portrait_pos < len(cls.available_portrait_index) - 1:
                cls.current_portrait_pos += 1
            else:
                cls.current_portrait_pos = 0
        else:
            new_class_name = cls.enemy_id_to_class[new_enemy_id]
        #Adjust position when necessary
        if Data.constant["EnemyInfo"][old_enemy_id]["Type"] in ["Ground", "Spawner"] and Data.constant["EnemyInfo"][new_enemy_id]["Type"] == "Air":
            location.Z += 120
        if Data.constant["EnemyInfo"][old_enemy_id]["Type"] == "Air" and Data.constant["EnemyInfo"][new_enemy_id]["Type"] in ["Ground", "Spawner"]:
            location.Z -= 120
        if old_enemy_id in ["N3029", "N3030"] and room != "m03ENT_001":
            location.Z -= 200
        if new_enemy_id in ["N3028", "N3029", "N3030"]:
            location.Z += 120
        if new_enemy_id in ["N3089", "N3088"]:
            location.Z -= 60
        #Some enemies lie farther in the background
        if new_enemy_id == "N3100":
            location.X -= forward_vector[0]*270
            location.Y -= forward_vector[1]*270
        if new_enemy_id in ["N3070", "N3071"]:
            location.X -= forward_vector[0]*120
            location.Y -= forward_vector[1]*120
        if new_enemy_id in ["N3113", "N3116", "N3117"]:
            location.X -= forward_vector[0]*400
            location.Y -= forward_vector[1]*400
        #Some enemies are in inconvenient spots
        if filename == "m03ENT_023_Enemy" and export_name == "Chr_N3087_2":
            location.Z += 120
        if filename == "m04GDN_008_Enemy" and export_name == "Chr_N3091_2":
            location.X += 200
        if filename == "m05SAN_008_Enemy" and export_name == "Chr_N3055_2407":
            location.X += 340
        if filename == "m05SAN_008_Enemy_Hard" and export_name == "Chr_N3073_1952":
            location.X -= 260
        if filename == "m05SAN_021_Enemy" and export_name == "Chr_N3056_860":
            location.X += 220
        if filename == "m06KNG_002_Enemy" and export_name == "Chr_N3052_51":
            location.X += 260
        if filename == "m06KNG_014_Enemy_Hard" and export_name == "Chr_N3056_834":
            location.X += 300
        if filename == "m06KNG_017_Enemy_Hard" and export_name == "Chr_N3053_87":
            location.X += 260
        if filename == "m07LIB_025_Enemy" and export_name == "Chr_N3012_1157":
            location.X -= 520
            location.Z -= 180
        if filename == "m07LIB_025_Enemy" and export_name == "Chr_N3033_808":
            location.X -= 240
        if filename == "m07LIB_033_Enemy" and export_name == "Chr_N3086_1925":
            location.Z += 60
        if filename == "m07LIB_034_Enemy" and export_name == "Chr_210":
            location.X += 380
        if filename == "m10BIG_006_Enemy" and export_name in ["Chr_N3033", "Chr_N3034", "Chr_N3035", "Chr_N3036", "Chr_N3037"]:
            location.Z += 720
        if filename == "m10BIG_016_Enemy" and export_name == "Chr_N3039":
            location.X += 240
            location.Z += 520
        if filename == "m11UGD_004_Enemy" and export_name == "Chr_N3064_1":
            location.Z -= 340
        if filename == "m11UGD_017_Enemy_Hard" and export_name == "Chr_N3055_1042":
            location.X -= 310
        if filename == "m11UGD_032_Enemy":
            if export_name == "Chr_N3029_1122":
                location.X -= 290
                location.Z -= 100
            if export_name == "Chr_N3044_977":
                location.X += 270
                location.Z += 120
        if filename == "m12SND_020_Enemy" and export_name == "Chr_N3014_770":
            location.X -= 160
        if filename == "m17RVA_001_Enemy_Hard" and export_name == "Chr_N3123_2750":
            location.X += 90
        if filename == "m51EBT_000_Enemy" and export_name in ["Chr_N3136", "Chr_N3139_3"]:
            location.Z -= 90
        if filename == "m51EBT_000_Enemy" and export_name in ["Chr_N3143", "Chr_N3146"]:
            location.Z += 90
        #Swap some enemy positions
        if filename == "m08TWR_011_Enemy":
            if export_name == "Chr_N3100_008_58":
                location.X = 1080
            if export_name == "Chr_N3100_026_109":
                location.X = 1560
        if filename == "m11UGD_036_Enemy":
            if export_name == "Chr_N3078_566":
                location.X = 1380
            if export_name == "Chr_N3079":
                location.X = 3120
        if filename == "m13ARC_000_Enemy_Hard":
            if export_name == "Chr_N3026_1052":
                location.X = 660
                location.Z = 150
            if export_name == "Chr_N3027":
                location.X = 1980
                location.Z = 630
        if filename == "m15JPN_010_Enemy":
            if export_name == "Chr_N3035_1682":
                location.X = 2700
                location.Z = 145
            if export_name == "Chr_N3042":
                location.X = 2040
                location.Z = 1165
        if filename == "m15JPN_010_Enemy":
            if export_name == "Chr_N3054_2":
                location.X = 540
                location.Z = 580
            if export_name == "Chr_N3055":
                location.X = 2460
                location.Z = 1120
        #Avoid placing 8 bit zombies near the vertical edges of the room
        if new_enemy_id == "N3121" and room != "m19K2C_000":
            location.Z = max(min(location.Z, room_height - 360), 360)
        #The giant dulla head spawner requires to be scaled up to function properly
        if new_enemy_id == "N3126":
            scale.X = 32
            scale.Y = 1
            scale.Z = 32
        if old_enemy_id == "N3126":
            scale.X = 1
            scale.Y = 1
            scale.Z = 1
        #Make sure the enemy is never too close to the edge of the screen
        if not room in ["m12SND_025", "m19K2C_000"]:
            location.X = max(min(location.X, room_width  - 60), 60)
            location.Z = max(min(location.Z, room_height - 60), 60)
        #If the enemy is right next to an entrance do not add it
        if not room in Room.ROTATING_ROOM_TO_CENTER:
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),         "LEFT"]) in Room.map_connections[room] and location.X%1260 <   120 and 230   < location.Z%720 <  490:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),        "RIGHT"]) in Room.map_connections[room] and location.X%1260 >  1140 and 230   < location.Z%720 <  490:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),          "TOP"]) in Room.map_connections[room] and  500  < location.X%1260 <   760 and location.Z%720 >  420:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),       "BOTTOM"]) in Room.map_connections[room] and  500  < location.X%1260 <   760 and location.Z%720 <  360:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),     "LEFT_TOP"]) in Room.map_connections[room] and location.X%1260 <   120 and 460   < location.Z%720 <= 720:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),    "RIGHT_TOP"]) in Room.map_connections[room] and location.X%1260 >  1140 and 460   < location.Z%720 <= 720:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),     "TOP_LEFT"]) in Room.map_connections[room] and    0 <= location.X%1260 <   260 and location.Z%720 >  420:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),  "BOTTOM_LEFT"]) in Room.map_connections[room] and    0 <= location.X%1260 <   260 and location.Z%720 <  360:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),  "LEFT_BOTTOM"]) in Room.map_connections[room] and location.X%1260 <   120 and   0  <= location.Z%720 <  260:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)), "RIGHT_BOTTOM"]) in Room.map_connections[room] and location.X%1260 >  1140 and   0  <= location.Z%720 <  260:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)),    "TOP_RIGHT"]) in Room.map_connections[room] and 1000  < location.X%1260 <= 1260 and location.Z%720 >  420:
                return
            if "_".join([room[3:], str(int(location.X//1260)), str(int(location.Z//720)), "BOTTOM_RIGHT"]) in Room.map_connections[room] and 1000  < location.X%1260 <= 1260 and location.Z%720 <  360:
                return
        #One of the Journey rooms has a faulty persistent level export in its enemy file, so add in its bg file instead
        if room == "m20JRN_002":
            filename = "m20JRN_002_BG"
        #Setup the actor properties
        properties = {}
        if new_enemy_id == "N3003":
            if hard_mode:
                properties["MinSpawnInterval"] = 1.5
                properties["MaxSpawnInterval"] = 3.0
                properties["MaxSpawnCount"]    = 6
            else:
                properties["MinSpawnInterval"] = 2.0
                properties["MaxSpawnInterval"] = 4.0
                properties["MaxSpawnCount"]    = 4
            properties["RightSpawnRate"] = 0.5
        if new_enemy_id == "N3082":
            properties["MaxSpawnCount"]  = 3
            properties["RightSpawnRate"] = 0.5
        if new_enemy_id in ["N3090", "N3099"]:
            if hard_mode:
                properties["MinSpawnInterval"] = random.uniform(0.5, 1.5)
                properties["MaxSpawnInterval"] = random.uniform(1.5, 2.0)
                properties["MaxSpawnCount"]    = random.randint(4, 6)
            else:
                properties["MinSpawnInterval"] = random.uniform(1.5, 2.0)
                properties["MaxSpawnInterval"] = random.uniform(2.0, 3.0)
                properties["MaxSpawnCount"]    = random.randint(3, 4)
        if new_enemy_id == "N3099":
            properties["SpawnIsN3099"] = True
        if new_enemy_id == "N3121":
            properties["IntervalTime"] = random.uniform(1.0, 2.0)
            properties["MaxNum"]       = random.randint(4, 8)
        if new_enemy_id == "N3126":
            properties["MinSpawnInterval"] = random.uniform(2.0, 4.0)
            properties["MaxSpawnInterval"] = random.uniform(5.0, 8.0)
        if new_enemy_id == "N3067":
            properties["HiddenInRock"] = False
        if new_enemy_id == "N3053":
            properties["StandbyType"]        = FName(Data.game_data[filename], "EPBEnemyGargoyleStandbyType::Normal")
            properties["TargetNoticeRangeX"] = 1200.0
        if new_enemy_id == "N3063":
            properties["StandbyType"] = FName(Data.game_data[filename], "EPBEnemyDantalionEntryType::Floating")
        if new_enemy_id == "N3064":
            properties["ChainLength"] = 350.0
            properties["IsCeiling"]   = location.Y > room_height - 360
        if new_enemy_id == "N3087":
            properties["StandbyType"] = FName(Data.game_data[filename], "EPBEnemyCyhiraethStandbyType::Floating")
        if new_enemy_id == "N3122":
            properties["PlayerDistanceX"] = random.uniform( 90.0, 630.0)
            properties["PlayerDistanceZ"] = random.uniform(180.0, 360.0)
        #Add the new enemy
        Room.add_level_actor(filename, new_class_name, location, rotation, scale, properties)
        #If it is a cannon enemy then potentially add extra stacks
        if new_enemy_id == "N3005":
            stack_num = random.randint(1, 3)
            offset = 170
        elif new_enemy_id == "N3016" and old_enemy_id != "N3023":
            if room_height - location.Z < 480:
                return
            stack_num = random.randint(1, 2)
            offset = 360
        elif new_enemy_id == "N3124":
            stack_num = random.randint(1, 4)
            offset = 100
        else:
            return
        for num in range(stack_num - 1):
            location.Z += offset
            Room.add_level_actor(filename, new_class_name, location, rotation, scale, properties)

    @classmethod
    def restore_enemy_scaling(cls):
        #After randomizing enemies keep the difficulty progression the same by making them inherit original properties
        original_enemy_levels = {}
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if Enemy.is_enemy(entry):
                original_enemy_levels[entry] = {}
                original_enemy_levels[entry]["Miriam"]    = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]
                original_enemy_levels[entry]["Bloodless"] = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeDefaultEnemyLevel"]
        #Update enemy levels
        for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
            if not Enemy.is_enemy(entry):
                continue
            enemy_id = entry[0:5]
            if enemy_id in cls.enemy_replacement:
                cls.patch_enemy_level(original_enemy_levels[cls.enemy_replacement_invert[enemy_id]]["Miriam"], entry, "")
                cls.patch_enemy_level(original_enemy_levels[cls.enemy_replacement_invert[enemy_id]]["Bloodless"], entry, "BloodlessMode")
                #Den enemies that are placed in the overworld struggle to fit in most places so shrink them down a bit
                if enemy_id in _LARGES_ENEMIES and not cls.enemy_replacement_invert[enemy_id] in _LARGES_ENEMIES:
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["CapsuleRadius"]     /= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["CapsuleHeight"]     /= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MeshScaleX"]        /= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MeshScaleY"]        /= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MeshScaleZ"]        /= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP"]             *= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxMP"]             *= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]      *= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxMP99Enemy"]      *= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]        = round(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]*0.8125)
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] = round(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"]*0.8125)
                #On the other hand increase the size of overworld enemies placed in the Den
                if not enemy_id in _LARGES_ENEMIES and cls.enemy_replacement_invert[enemy_id] in _LARGES_ENEMIES:
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["CapsuleRadius"]     *= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["CapsuleHeight"]     *= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MeshScaleX"]        *= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MeshScaleY"]        *= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MeshScaleZ"]        *= 1.5
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP"]             /= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxMP"]             /= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]      /= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxMP99Enemy"]      /= 0.8125
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]        = round(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]/0.8125)
                    Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] = round(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"]/0.8125)
        #Update enemy area info
        enemy_id_to_archive = {}
        for entry in Data.datatable["PB_DT_ArchiveEnemyMaster"]:
            enemy_id_to_archive[Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["UniqueID"]] = entry
        for entry in Data.datatable["PB_DT_ArchiveEnemyMaster"]:
            enemy_id = Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["UniqueID"]
            if enemy_id in cls.enemy_replacement:
                if cls.enemy_replacement_invert[enemy_id] in enemy_id_to_archive:
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area1"] = Data.original_datatable["PB_DT_ArchiveEnemyMaster"][enemy_id_to_archive[cls.enemy_replacement_invert[enemy_id]]]["Area1"]
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area2"] = Data.original_datatable["PB_DT_ArchiveEnemyMaster"][enemy_id_to_archive[cls.enemy_replacement_invert[enemy_id]]]["Area2"]
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area3"] = Data.original_datatable["PB_DT_ArchiveEnemyMaster"][enemy_id_to_archive[cls.enemy_replacement_invert[enemy_id]]]["Area3"]
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area4"] = Data.original_datatable["PB_DT_ArchiveEnemyMaster"][enemy_id_to_archive[cls.enemy_replacement_invert[enemy_id]]]["Area4"]
                else:
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area1"] = "None"
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area2"] = "None"
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area3"] = "None"
                    Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["Area4"] = "None"

    @classmethod
    def patch_enemy_level(cls, value, entry, extra):
        #Make Zangetsu ally's level shared with Ultimate
        if entry == "N1011_COOP":
            Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"] = Data.datatable["PB_DT_CharacterParameterMaster"]["N1011_STRONG"][extra + "DefaultEnemyLevel"]
        #Make Dom's level be the inverse of the chosen value
        elif entry == "N1009_Enemy":
            Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"] = abs(value - 100)
        #Make it so that Bael and Dom's levels combined always equal 100
        #This ensures that the final fight is never too easy or too hard
        elif Enemy.is_final_boss(entry):
            Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"] = abs(Data.datatable["PB_DT_CharacterParameterMaster"]["N1009_Enemy"][extra + "DefaultEnemyLevel"] - 100)
        #Greedling is shared with Breeder despite having a completely different ID
        elif entry == "N3125":
            Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"] = Data.datatable["PB_DT_CharacterParameterMaster"]["N2016"][extra + "DefaultEnemyLevel"]
        #Main
        elif Enemy.is_main_enemy(entry):
            Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"] = value
        #Give sub entries the level of the main
        else:
            Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"] = Data.datatable["PB_DT_CharacterParameterMaster"][entry[0:5]][extra + "DefaultEnemyLevel"]
        
        #While physical and elemental resistances can be random status effect ones should scale with the enemy's level
        #Otherwise some enemies made strong could be easily one shot with petrifying weapons and whatnot
        #Ignore it for Bloodless mode though
        if not extra:
            cls.scale_status_resistances(entry)
        
        #Make level match in all difficulties
        Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "HardEnemyLevel"]      = Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"]
        Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "NightmareEnemyLevel"] = Data.datatable["PB_DT_CharacterParameterMaster"][entry][extra + "DefaultEnemyLevel"]

    @classmethod
    def scale_status_resistances(cls, entry : str):
        for attr in _STATUS_RESISTANCES:
            attr_num = cls.original_enemy_stats[entry][attr]
            #Bosses should always be immune to stone
            if attr == "STO" and Data.datatable["PB_DT_CharacterParameterMaster"][entry]["StoneType"] == "EPBStoneType::Boss":
                continue
            #If an enemy is by default immune to all status effects keep it that way
            if cls.original_enemy_stats[entry]["POI"] == 100.0 and cls.original_enemy_stats[entry]["CUR"] == 100.0 and cls.original_enemy_stats[entry]["STO"] >= 99.0 and cls.original_enemy_stats[entry]["SLO"] == 100.0:
                continue
            #Gain
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"] > cls.original_enemy_stats[entry]["Level"] + ((99 - cls.original_enemy_stats[entry]["Level"]) * 0.10):
                attr_num += 25.0
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"] > cls.original_enemy_stats[entry]["Level"] + ((99 - cls.original_enemy_stats[entry]["Level"]) * 0.55):
                attr_num += 25.0
            attr_num = min(attr_num, 99.99 if attr == "STO" else 100.0)
            #Loss
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"] < cls.original_enemy_stats[entry]["Level"] * 0.90:
                attr_num = math.ceil(attr_num - 25.0)
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"] < cls.original_enemy_stats[entry]["Level"] * 0.45:
                attr_num -= 25.0
            attr_num = max(attr_num, 50.0 if attr == "STO" else 25.0 if attr == "SLO" else 0.0)
            Data.datatable["PB_DT_CharacterParameterMaster"][entry][attr] = attr_num

    @staticmethod
    def update_special_properties():
        #Make sure Vepar has double health in Bloodless mode otherwise the fight is always too short
        for entry in ["N1001", "N1001_HEAD"]:
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeEnemyHPOverride"] = int(Enemy.calculate_stat_with_level(entry, Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeDefaultEnemyLevel"], "MaxHP")*2.0)
        #Update Gebel's health threshold for the red moon based on his level
        Data.datatable["PB_DT_CoordinateParameter"]["FakeMoon_ChangeHPThreshold"]["Value"] = int(Enemy.calculate_stat_with_level("N1012", Data.datatable["PB_DT_CharacterParameterMaster"]["N1012"]["DefaultEnemyLevel"], "MaxHP")*0.15)

    @staticmethod
    def add_enemy_to_archive(entry_index, enemy_id, area_ids, package_path, copy_from):
        last_id = int(list(Data.datatable["PB_DT_ArchiveEnemyMaster"])[-1].split("_")[-1])
        entry_id = "Enemy_" + "{:03d}".format(last_id + 1)
        for entry in Data.datatable["PB_DT_ArchiveEnemyMaster"]:
            if Data.datatable["PB_DT_ArchiveEnemyMaster"][entry]["UniqueID"] == copy_from:
                new_entry = copy.deepcopy(Data.datatable["PB_DT_ArchiveEnemyMaster"][entry])
                break
        Data.datatable["PB_DT_ArchiveEnemyMaster"][entry_id] = new_entry
        Data.datatable["PB_DT_ArchiveEnemyMaster"][entry_id]["UniqueID"] = enemy_id
        for index in range(4):
            Data.datatable["PB_DT_ArchiveEnemyMaster"][entry_id]["Area" + str(index + 1)] = "None"
        for index in range(len(area_ids)):
            Data.datatable["PB_DT_ArchiveEnemyMaster"][entry_id]["Area" + str(index + 1)] = area_ids[index]
        Data.datatable["PB_DT_ArchiveEnemyMaster"][entry_id]["AreaInputPath"] = package_path
        Data.datatable_entry_index["PB_DT_ArchiveEnemyMaster"][entry_id] = entry_index

    @staticmethod
    def add_hard_enemy_patterns():
        #Some major enemies in vanilla lack any form of patterns changes on harder difficulties making them feel underwhelming compared to the rest
        #However this needs to only be done if hard or nightmare is chosen within the mod since those properties would be shared between all difficulties in-game
        
        #Increase Bomber Morte explosion radius
        Data.datatable["PB_DT_BulletMaster"]["N3024_BOMB_BaudRideBlast"]["BeginEffectBeginScale"] *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N3024_BOMB_BaudRideBlast"]["BeginEffectEndScale"]   *= 2.0
        
        Data.datatable["PB_DT_CollisionMaster"]["N3024_EXPLOSION"]["R00"] *= 2.0
        Data.datatable["PB_DT_CollisionMaster"]["N3024_EXPLOSION"]["R01"] *= 2.0
        
        #Increase Millionaire melon explosion radius
        Data.datatable["PB_DT_BulletMaster"]["N3108_Bomb_Explosion"]["BeginEffectBeginScale"] *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N3108_Bomb_Explosion"]["BeginEffectEndScale"]   *= 1.5
        
        Data.datatable["PB_DT_CollisionMaster"]["N3108_BOMB_EXPLOSION"]["R00"] *= 1.5
        Data.datatable["PB_DT_CollisionMaster"]["N3108_BOMB_EXPLOSION"]["R01"] *= 1.5
        
        #Increase OD's fire sword explosion radius
        Data.datatable["PB_DT_BulletMaster"]["N2012_Magic_FireExplosion"]["BeginEffectBeginScale"] *= 4.0
        Data.datatable["PB_DT_BulletMaster"]["N2012_Magic_FireExplosion"]["BeginEffectEndScale"]   *= 4.0
        
        Data.datatable["PB_DT_CollisionMaster"]["N2012_Magic_FireExplosion"]["R00"] *= 4.0
        Data.datatable["PB_DT_CollisionMaster"]["N2012_Magic_FireExplosion"]["R01"] *= 4.0
        
        #Speeding up Bael's animation play rate doesn't work well so instead speed up and expand all of his projectiles
        Data.datatable["PB_DT_BallisticMaster"]["N1009_RAY"]["InitialSpeed"]        *= 2.0
        Data.datatable["PB_DT_BallisticMaster"]["N1013_TracerRay"]["InitialSpeed"]  *= 6.0
        Data.datatable["PB_DT_BallisticMaster"]["N1013_RingLasers"]["InitialSpeed"] *= 8.0
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull"]["EffectBeginScale"]      *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull"]["EffectEndScale"]        *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull"]["BeginEffectBeginScale"] *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull"]["BeginEffectEndScale"]   *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull"]["EndEffectBeginScale"]   *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull"]["EndEffectEndScale"]     *= 2.5
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles"]["EffectBeginScale"]      *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles"]["EffectEndScale"]        *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles"]["BeginEffectBeginScale"] *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles"]["BeginEffectEndScale"]   *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles"]["EndEffectBeginScale"]   *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles"]["EndEffectEndScale"]     *= 1.5
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasers"]["EffectBeginScale"]      *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasers"]["EffectEndScale"]        *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasers"]["BeginEffectBeginScale"] *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasers"]["BeginEffectEndScale"]   *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasers"]["EndEffectBeginScale"]   *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasers"]["EndEffectEndScale"]     *= 2.0
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_Screech"]["EffectBeginScale"]    *= 1.9
        Data.datatable["PB_DT_BulletMaster"]["N1013_Screech"]["EffectEndScale"]      *= 1.9
        Data.datatable["PB_DT_BulletMaster"]["N1013_Screech"]["EndEffectBeginScale"] *= 1.9
        Data.datatable["PB_DT_BulletMaster"]["N1013_Screech"]["EndEffectEndScale"]   *= 1.9
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Explosion"]["EffectBeginScale"]      *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Explosion"]["EffectEndScale"]        *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Explosion"]["BeginEffectBeginScale"] *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Explosion"]["BeginEffectEndScale"]   *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Explosion"]["EndEffectBeginScale"]   *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Explosion"]["EndEffectEndScale"]     *= 2.5
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Destroyed"]["EffectBeginScale"]      *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Destroyed"]["EffectEndScale"]        *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Destroyed"]["BeginEffectBeginScale"] *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Destroyed"]["BeginEffectEndScale"]   *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Destroyed"]["EndEffectBeginScale"]   *= 2.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_FlameSkull_Destroyed"]["EndEffectEndScale"]     *= 2.5
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles_Destroyed"]["EffectBeginScale"]      *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles_Destroyed"]["EffectEndScale"]        *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles_Destroyed"]["BeginEffectBeginScale"] *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles_Destroyed"]["BeginEffectEndScale"]   *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles_Destroyed"]["EndEffectBeginScale"]   *= 1.5
        Data.datatable["PB_DT_BulletMaster"]["N1013_Bubbles_Destroyed"]["EndEffectEndScale"]     *= 1.5
        
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasersImpact"]["EffectBeginScale"]      *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasersImpact"]["EffectEndScale"]        *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasersImpact"]["BeginEffectBeginScale"] *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasersImpact"]["BeginEffectEndScale"]   *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasersImpact"]["EndEffectBeginScale"]   *= 2.0
        Data.datatable["PB_DT_BulletMaster"]["N1013_RingLasersImpact"]["EndEffectEndScale"]     *= 2.0
        
        Data.datatable["PB_DT_CollisionMaster"]["N1013_FlameSkull"]["R00"] *= 2.5
        Data.datatable["PB_DT_CollisionMaster"]["N1013_FlameSkull"]["R01"] *= 2.5
        
        Data.datatable["PB_DT_CollisionMaster"]["N1013_FlameSkull_Explosion"]["R00"] *= 2.5
        Data.datatable["PB_DT_CollisionMaster"]["N1013_FlameSkull_Explosion"]["R01"] *= 2.5
        
        Data.datatable["PB_DT_CollisionMaster"]["N1013_Bubbles"]["R00"] *= 1.5
        Data.datatable["PB_DT_CollisionMaster"]["N1013_Bubbles"]["R01"] *= 1.5
        
        Data.datatable["PB_DT_CollisionMaster"]["N1013_RingLasers"]["R00"] *= 2.0
        Data.datatable["PB_DT_CollisionMaster"]["N1013_RingLasers"]["R01"] *= 2.0
        
        Data.datatable["PB_DT_CollisionMaster"]["N1013_Screech"]["R00"] *= 1.9
        Data.datatable["PB_DT_CollisionMaster"]["N1013_Screech"]["R01"] *= 1.9
        
        Data.datatable["PB_DT_DamageMaster"]["N1013_RingLasers"]["STR_Correction"] = 1.0
        Data.datatable["PB_DT_DamageMaster"]["N1013_RingLasers"]["INT_Correction"] = 1.0

    @staticmethod
    def calculate_stat_with_level(entry : str, level : int, stat_name : str):
        #Calculate a stat based on the enemy's level in a way nearly identical to how the game calculates it
        #Though sometimes it can be 1 unit off
        return int(((Data.datatable["PB_DT_CharacterParameterMaster"][entry][stat_name + "99Enemy"] - Data.datatable["PB_DT_CharacterParameterMaster"][entry][stat_name])/98)*(level-1) + Data.datatable["PB_DT_CharacterParameterMaster"][entry][stat_name])

    @staticmethod
    def is_enemy(character : str):
        if Enemy.is_main_enemy(character):
            return True
        if character[0:5] in Data.constant["EnemyInfo"]:
            return list(Data.datatable["PB_DT_CharacterParameterMaster"]).index("P0007") < list(Data.datatable["PB_DT_CharacterParameterMaster"]).index(character) < list(Data.datatable["PB_DT_CharacterParameterMaster"]).index("SubChar")
        return Enemy.is_final_boss(character)

    @staticmethod
    def is_main_enemy(character : str):
        return character in Data.constant["EnemyInfo"]

    @staticmethod
    def is_boss(character : str) -> bool:
        if Enemy.is_enemy(character):
            return Data.datatable["PB_DT_CharacterParameterMaster"][character]["IsBoss"] and character != "N2008_BOSS" or character[0:5] in ["N3106", "N3107", "N3108"]
        return False

    @staticmethod
    def is_boss_part(character : str):
        return Enemy.is_boss(character) or character in ["N1001_Tentacle", "N3125"]

    @staticmethod
    def is_final_boss(character : str):
        return character[0:5] in ["N1009", "N1013"]

    @classmethod
    def create_log(cls):
        log = {}
        for enemy in Data.constant["EnemyInfo"]:
            enemy_name = Data.translation["Enemy"][enemy]
            log[enemy_name] = {}
            log[enemy_name]["DefaultLevel"]   = Data.datatable["PB_DT_CharacterParameterMaster"][enemy]["DefaultEnemyLevel"]
            log[enemy_name]["BloodlessLevel"] = Data.datatable["PB_DT_CharacterParameterMaster"][enemy]["BloodlessModeDefaultEnemyLevel"]
            log[enemy_name]["Resistances"] = {}
            for attr in _MAIN_RESISTANCES:
                log[enemy_name]["Resistances"][attr] = int(Data.datatable["PB_DT_CharacterParameterMaster"][enemy][attr])
            for attr in _STATUS_RESISTANCES:
                log[enemy_name]["Resistances"][attr] = int(Data.datatable["PB_DT_CharacterParameterMaster"][enemy][attr])
            if enemy in cls.enemy_replacement:
                log[enemy_name]["Position"] = Data.translation["Enemy"][cls.enemy_replacement_invert[enemy]] if cls.enemy_replacement[enemy] != enemy else "Unchanged"
            else:
                log[enemy_name]["Position"] = "Unchanged"
            if enemy == "N0000":
                break
        return log
