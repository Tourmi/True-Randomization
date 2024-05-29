from .GlobalImports import *
from .Constants import *
from . import Data
from . import Utility

_AVERAGE_POWER = 50
_AVERAGE_COST = 80
_CORRECTION = 0.2
_SPECIAL_CORRECTION = 0.4

_BUGGED_LIST = [
    "Shadowtracer",
    "Beastguard",
    "WildScratch",
    "Healing",
    "Sacredshade",
    "ChangeBunny"
]

_SPECIAL_LIST = [
    "Jackpot",
    "WildScratch",
    "ChangeBunny",
    "Voidlay",
    "Tornadoslicer",
    "Chiselbalage",
    "TissRosain",
    "FoldingTurb"
]

_SKIP_LIST = [
    "Bloodsteel",
    "SummonChair",
    "Demoniccapture",
    "Accelerator",
    "AccelWorld",
    "Beastguard",
    "Shadowtracer",
    "Sacredshade",
    "Reflectionray",
    "Aquastream",
    "Dimensionshift",
    "GoldBarrett",
    "Aimingshield",
    "CurseDray",
    "Petrey",
    "PetraBless",
    "Acidgouache",
    "Venomsmog"
]

class Shard:
    @classmethod
    def set_shard_power_weight(cls, weight : int):
        cls.shard_power_weight = WEIGHT_EXPONENTS[weight - 1]

    @classmethod
    def randomize_shard_power(cls, scale : bool):
        for entry in Data.constant["ShardBase"]:
            if entry in _SKIP_LIST + ["SummonBuell", "SummonBuChan", "LigaDoin"]:
                continue
            original_cost      = int(Data.datatable["PB_DT_ShardMaster"][entry]["useMP"])
            original_doin_cost = int(Data.datatable["PB_DT_ShardMaster"]["LigaDoin"]["useMP"])
            #Reduce the range for certain shards
            if   entry in _BUGGED_LIST:
                max_cost = 50
            elif entry in _SPECIAL_LIST:
                max_cost = 100
            else:
                max_cost = 300
            #Randomize magic cost first
            multiplier = Utility.random_weighted(original_cost, 1, max_cost, 1, cls.shard_power_weight)/original_cost
            Data.datatable["PB_DT_ShardMaster"][entry]["useMP"] = int(original_cost * multiplier)
            #Riga Doin explosion is shared with Riga Storeama
            if entry == "LigaStreyma":
                Data.datatable["PB_DT_ShardMaster"]["LigaDoin"]["useMP"] = int(original_doin_cost * multiplier)
            #Randomize power based on magic cost
            if scale:
                new_cost      = Data.datatable["PB_DT_ShardMaster"][entry]["useMP"]
                new_doin_cost = Data.datatable["PB_DT_ShardMaster"]["LigaDoin"]["useMP"]
            else:
                multiplier    = Utility.random_weighted(original_cost, 1, max_cost, 1, cls.shard_power_weight)/original_cost
                new_cost      = int(original_cost * multiplier)
                new_doin_cost = int(original_doin_cost * multiplier)
            new_base = new_cost * Data.constant["ShardBase"][entry]["Base"]
            #Prevent power from scaling too high or too low
            if   entry == "Healing":
                balance = 1.0
            elif entry in _SPECIAL_LIST:
                balance = (1/(multiplier**_SPECIAL_CORRECTION))*(_AVERAGE_POWER/new_base)**_CORRECTION
            else:
                balance = (_AVERAGE_COST/new_cost)**_CORRECTION
            Data.datatable["PB_DT_ShardMaster"][entry]["minGradeValue"] = round(new_base * balance, 3)
            Data.datatable["PB_DT_ShardMaster"][entry]["maxGradeValue"] = round(new_base * balance * Data.constant["ShardBase"][entry]["Grade"], 3)
            #Riga Doin explosion is shared with Riga Storeama
            if entry == "LigaStreyma":
                new_doin_base = new_doin_cost * Data.constant["ShardBase"]["LigaDoin"]["Base"]
                balance       = (_AVERAGE_COST/new_doin_cost)**_CORRECTION
                Data.datatable["PB_DT_ShardMaster"]["LigaDoin"]["minGradeValue"] = round(new_doin_base * balance, 3)
                Data.datatable["PB_DT_ShardMaster"]["LigaDoin"]["maxGradeValue"] = round(new_doin_base * balance * Data.constant["ShardBase"]["LigaDoin"]["Grade"], 3)

    @staticmethod
    def set_default_shard_power():
        #Recalculate default shard power in a more convenient way for balance
        for entry in Data.constant["ShardBase"]:
            base = Data.datatable["PB_DT_ShardMaster"][entry]["useMP"] * Data.constant["ShardBase"][entry]["Base"]
            if entry in _SKIP_LIST + ["Healing"]:
                balance = 1.0
            elif entry in _SPECIAL_LIST:
                balance = (_AVERAGE_POWER/base)**_CORRECTION
            else:
                balance = (_AVERAGE_COST/Data.datatable["PB_DT_ShardMaster"][entry]["useMP"])**_CORRECTION
            Data.datatable["PB_DT_ShardMaster"][entry]["minGradeValue"] = round(base * balance, 3)
            Data.datatable["PB_DT_ShardMaster"][entry]["maxGradeValue"] = round(base * balance * Data.constant["ShardBase"][entry]["Grade"], 3)

    @staticmethod
    def update_special_properties():
        """
        A few shards have a multiplier different than 1.0 in DamageMaster so update their shard power based on that
        """
        for data in ["minGradeValue", "maxGradeValue"]:
            Data.datatable["PB_DT_ShardMaster"]["DragonicRage"][data] = round(Data.datatable["PB_DT_ShardMaster"]["DragonicRage"][data] / 1.45, 3)
            Data.datatable["PB_DT_ShardMaster"]["SummonAme"][data]    = round(Data.datatable["PB_DT_ShardMaster"]["SummonAme"][data]    / 0.75, 3)

    @staticmethod
    def rescale_level_based_shards():
        """
        Money is Power and Red Rememberance only take starting stats and level up stats in account\n
        Considerably increase their multipliers to make them useful if level 1 capped
        """
        Data.datatable["PB_DT_CoordinateParameter"]["P0000_MONEYISPOWER_ATTACK_RATE_MAX"]["Value"] = 0.5
        #Unfortunately Red Rememberance seems to be capped at 1.0
        Data.datatable["PB_DT_ShardMaster"]["RedDowther"]["minGradeValue"] = 0.5
        Data.datatable["PB_DT_ShardMaster"]["RedDowther"]["maxGradeValue"] = 1.0