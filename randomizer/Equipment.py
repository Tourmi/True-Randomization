from .GlobalImports import *
from .Constants import *
from .Data import *
from . import Utility

_MIN_VALUE_MULTIPLIER = 0.2
_LOW_BOUND_MULTIPLIER = 0.8
_HIGH_BOUND_MULTIPLIER = 1.2

_CHEAT_EQUIP = [
    "HumptyDumpty",
    "LoveOfBenki",
    "Plan9FOSpace",
    "Mega64Head",
    "HeyI’mGrump",
    "I’mNotSoGrump",
    "AKindaFunnyMask",
    "BigMustache",
    "PlagueDoctorFace",
    "The-BazMask"
]

_CHEAT_WEAPONS = [
    "ClockSowrd",
    "LoveOfPizza",
    "KongSword",
    "SwordOfTheMushroom",
    "PowerSword",
    "SilverAndBlackSword",
    "DungeonNightSword",
    "EvilTheSword"
]

_DLC_WEAPONS = [
    "Scythe",
    "MagicalScepter",
    "PirateSword",
    "PirateGun",
    "Wagasa"
]

_STAT_TO_PROPERTY = {
    "MeleeAttack":  "Attack",
    "MagicAttack":  "Attack",
    "MeleeDefense": "Defense",
    "MagicDefense": "Defense",
    "ZAN":          "Resist",
    "DAG":          "Resist",
    "TOT":          "Resist",
    "FLA":          "Resist",
    "ICE":          "Resist",
    "LIG":          "Resist",
    "HOL":          "Resist",
    "DAR":          "Resist",
    "POI":          "Status",
    "CUR":          "Status",
    "STO":          "Status",
    "STR":          "Stat",
    "CON":          "Stat",
    "INT":          "Stat",
    "MND":          "Stat",
    "LUC":          "Stat"
}

_WEAPON_TYPE_TO_MAX_VALUE = {
    "Boots":           45,
    "Knife":           50,
    "Rapir":           52,
    "ShortSword":      58,
    "Club":            58,
    "LargeSword":      84,
    "JapaneseSword":   52,
    "Spear":           58,
    "Whip":            52,
    "Gun":             32,
    "Scythe":          55,
    "MagicalGirlWand": 26
}

_EQUIPMENT_TYPE_TO_MAX_VALUE = {
    "Head": {
        "Attack":   0,
        "Defense": 20,
        "Resist":  10,
        "Status":  20,
        "Stat":     8
    },
    "Muffler": {
        "Attack":   0,
        "Defense":  7,
        "Resist":  10,
        "Status":  10,
        "Stat":     5
    },
    "Accessory1": {
        "Attack":   0,
        "Defense":  5,
        "Resist":  10,
        "Status":  20,
        "Stat":    10
    },
    "Body": {
        "Attack":   0,
        "Defense": 50,
        "Resist":  10,
        "Status":  10,
        "Stat":    10
    }
}

class Equipment:
    BIT_WEAPONS = [
        "CoolShoesOfMrNarita",
        "IceSlewShoes",
        "PoisonSpikeShoes",
        "CrystalSword",
        "ShieldWeapon",
        "XrossBrade",
        "BradeOfEU",
        "LightSaber",
        "JodoSwordLight",
        "SpearCutDownAside",
        "StickOfMagiGirl",
        "DeathBringer",
        "SacredSword",
        "ChargeWideEnd",
        "DrillWideEnd",
        "PetrifactionSword",
        "IcePillarSpear",
        "LoveOfFairyDragon",
        "WhipsOfLightDarkness",
        "TrustMusket"
    ]

    @classmethod
    def set_global_stat_weight(cls, weight):
        cls.global_stat_weight = WEIGHT_EXPONENTS[weight - 1]

    @staticmethod
    def reset_zangetsu_black_belt():
        #Playable Zangetsu has the Black Belt on by default giving him extra stats
        #In Progressive Zangetsu we want all his starting stats to be 0
        Data.datatable["PB_DT_ArmorMaster"]["Blackbelt"]["STR"] = 0
        Data.datatable["PB_DT_ArmorMaster"]["Blackbelt"]["CON"] = 0

    @classmethod
    def randomize_equipment_stats(cls):
        for entry in Data.datatable["PB_DT_ArmorMaster"]:
            #Only randomize equipment that has a description entry
            if not "ITEM_EXPLAIN_" + entry in Data.stringtable["PBMasterStringTable"]:
                continue
            #Some equipments have extreme stats that need to be evenly multiplied
            if cls._has_negative_stat(entry):
                list = []
                for stat in _STAT_TO_PROPERTY:
                    if Data.datatable["PB_DT_ArmorMaster"][entry][stat] == 0:
                        continue
                    list.append(abs(Data.datatable["PB_DT_ArmorMaster"][entry][stat]))
                multiplier = Utility.random_weighted(min(list), 1, int(min(list)*1.2), 1, cls.global_stat_weight)/min(list)
                for stat in _STAT_TO_PROPERTY:
                    if Data.datatable["PB_DT_ArmorMaster"][entry][stat] == 0:
                        continue
                    Data.datatable["PB_DT_ArmorMaster"][entry][stat] = round(Data.datatable["PB_DT_ArmorMaster"][entry][stat]*multiplier)
            #The rest can be semi-random
            else:
                for stat in _STAT_TO_PROPERTY:
                    if Data.datatable["PB_DT_ArmorMaster"][entry][stat] == 0:
                        continue
                    max_value = 20 if entry == "SkullNecklace" else _EQUIPMENT_TYPE_TO_MAX_VALUE[Data.datatable["PB_DT_ArmorMaster"][entry]["SlotType"].split("::")[1]][_STAT_TO_PROPERTY[stat]]
                    Data.datatable["PB_DT_ArmorMaster"][entry][stat] = Utility.random_weighted(Data.datatable["PB_DT_ArmorMaster"][entry][stat], 1, int(max_value*1.2), 1, cls.global_stat_weight)
        #Shovel Armor's attack
        max_value = _WEAPON_TYPE_TO_MAX_VALUE["LargeSword"]
        min_value = round(max_value*_MIN_VALUE_MULTIPLIER)
        Data.datatable["PB_DT_CoordinateParameter"]["ShovelArmorWeaponAtk"]["Value"] = Utility.random_weighted(int(Data.datatable["PB_DT_CoordinateParameter"]["ShovelArmorWeaponAtk"]["Value"]), int(min_value*_LOW_BOUND_MULTIPLIER), int(max_value*_HIGH_BOUND_MULTIPLIER), 1, cls.global_stat_weight)

    @classmethod
    def randomize_weapon_power(cls):
        for entry in Data.datatable["PB_DT_WeaponMaster"]:
            if Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"] == 0:
                continue
            max_value = _WEAPON_TYPE_TO_MAX_VALUE[Data.datatable["PB_DT_WeaponMaster"][entry]["WeaponType"].split("::")[1]]
            min_value = round(max_value*_MIN_VALUE_MULTIPLIER)
            reduction = cls._get_weapon_reduction(entry)
            weapon_tier = cls._get_weapon_tier(entry)
            if weapon_tier == 0:
                Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"] = Utility.random_weighted(Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"], int(min_value*_LOW_BOUND_MULTIPLIER*reduction), int(max_value*_HIGH_BOUND_MULTIPLIER*reduction), 1, cls.global_stat_weight)
            #Make progressive weapons retain their tier system
            if weapon_tier == 1:
                high_tier_name = (entry[:-1] if entry[-1].isnumeric() else entry) + str(3 if entry in cls.BIT_WEAPONS else 5 if "Pirate" in entry else 4)
                weapon_power = Utility.random_weighted(Data.datatable["PB_DT_WeaponMaster"][high_tier_name]["MeleeAttack"], int(min_value*_LOW_BOUND_MULTIPLIER*reduction), int(max_value*_HIGH_BOUND_MULTIPLIER*reduction), 1, cls.global_stat_weight)/3
                Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"] = int(weapon_power)
            if weapon_tier == 2:
                Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"] = int(weapon_power*2)
            if weapon_tier == 3:
                Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"] = int(weapon_power*3)
            #Update magic attack for weapons with elemental attributes
            if Data.datatable["PB_DT_WeaponMaster"][entry]["MagicAttack"] != 0:
                Data.datatable["PB_DT_WeaponMaster"][entry]["MagicAttack"] = Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"]

    @staticmethod
    def randomize_cheat_equipment_stats():
        #Cheat equipments stats are completely random
        #Gives them a chance to not be useless
        for entry in Data.datatable["PB_DT_ArmorMaster"]:
            if entry in _CHEAT_EQUIP:
                for stat in _STAT_TO_PROPERTY:
                    #Avoid having direct attack stats as this would favor rapid weapons over slow ones
                    if _STAT_TO_PROPERTY[stat] == "Attack":
                        continue
                    if random.random() < 0.25:
                        max_value = _EQUIPMENT_TYPE_TO_MAX_VALUE[Data.datatable["PB_DT_ArmorMaster"][entry]["SlotType"].split("::")[1]][_STAT_TO_PROPERTY[stat]]
                        if random.random() < 7/8:
                            Data.datatable["PB_DT_ArmorMaster"][entry][stat] =  random.randint(1, int(max_value*1.2))
                        else:
                            Data.datatable["PB_DT_ArmorMaster"][entry][stat] = -random.randint(1, int(max_value*1.2)*2)

    @staticmethod
    def randomize_cheat_weapon_power():
        #Cheat weapons stats are completely random
        #Gives them a chance to not be completely useless
        for entry in Data.datatable["PB_DT_WeaponMaster"]:
            if entry in _CHEAT_WEAPONS:
                max_value = _WEAPON_TYPE_TO_MAX_VALUE[Data.datatable["PB_DT_WeaponMaster"][entry]["WeaponType"].split("::")[1]]
                min_value = round(max_value*_MIN_VALUE_MULTIPLIER)
                reduction = Equipment._get_weapon_reduction(entry)
                Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"] = random.randint(int(min_value*_LOW_BOUND_MULTIPLIER*reduction), int(max_value*_HIGH_BOUND_MULTIPLIER*reduction))
                #Randomize special effect rate too
                if Data.datatable["PB_DT_WeaponMaster"][entry]["SpecialEffectDenominator"] != 0.0:
                    Data.datatable["PB_DT_WeaponMaster"][entry]["SpecialEffectDenominator"] = random.randint(1, 3)

    @staticmethod
    def update_special_properties():
        Data.datatable["PB_DT_CoordinateParameter"]["WeaponGrowMaxAtk_BloodBringer"]["Value"] = int(Data.datatable["PB_DT_WeaponMaster"]["BradBlingerLv1"]["MeleeAttack"]*2.3)
        Data.datatable["PB_DT_CoordinateParameter"]["WeaponGrowMaxAtk_RedbeastEdge"]["Value"] = Data.datatable["PB_DT_WeaponMaster"]["CrystalSword3"]["MeleeAttack"]
        Data.datatable["PB_DT_CoordinateParameter"]["WeaponGrowMaxAtk_Izayoi"]["Value"]       = int(Data.datatable["PB_DT_WeaponMaster"]["Truesixteenthnight"]["MeleeAttack"]*1.2)

    @staticmethod
    def add_armor_reference(armor_id):
        #Give a specific armor its own graphical asset pointer when equipped
        Data.datatable["PB_DT_ArmorMaster"][armor_id]["ReferencePath"] = f"/Game/Core/Item/Body/BDBP_{armor_id}.BDBP_{armor_id}"
        new_file = UAsset("\\".join([ASSETS_DIR, Data.file_to_path["BDBP_BodyValkyrie"], "BDBP_BodyValkyrie.uasset"]), EngineVersion.VER_UE4_22)
        index = new_file.SearchNameReference(FString("BDBP_BodyValkyrie_C"))
        new_file.SetNameReference(index, FString(f"BDBP_{armor_id}_C"))
        index = new_file.SearchNameReference(FString("Default__BDBP_BodyValkyrie_C"))
        new_file.SetNameReference(index, FString(f"Default__BDBP_{armor_id}_C"))
        default_body_mat          = Data.constant["ArmorReference"][armor_id]["DefaultBodyMat"]         + "." + Data.constant["ArmorReference"][armor_id]["DefaultBodyMat"].split("/")[-1]
        chroma_body_mat           = Data.constant["ArmorReference"][armor_id]["ChromaBodyMat"]          + "." + Data.constant["ArmorReference"][armor_id]["ChromaBodyMat"].split("/")[-1]
        default_skin_mat          = Data.constant["ArmorReference"][armor_id]["DefaultSkinMat"]         + "." + Data.constant["ArmorReference"][armor_id]["DefaultSkinMat"].split("/")[-1]
        chroma_skin_mat           = Data.constant["ArmorReference"][armor_id]["ChromaSkinMat"]          + "." + Data.constant["ArmorReference"][armor_id]["ChromaSkinMat"].split("/")[-1]
        dialogue_default_skin_mat = Data.constant["ArmorReference"][armor_id]["DialogueDefaultSkinMat"] + "." + Data.constant["ArmorReference"][armor_id]["DialogueDefaultSkinMat"].split("/")[-1]
        dialogue_chroma_skin_mat  = Data.constant["ArmorReference"][armor_id]["DialogueChromaSkinMat"]  + "." + Data.constant["ArmorReference"][armor_id]["DialogueChromaSkinMat"].split("/")[-1]
        new_file.Imports[18].ObjectName            = FName.FromString(new_file, Data.constant["ArmorReference"][armor_id]["Mesh"])
        new_file.Imports[27].ObjectName            = FName.FromString(new_file, Data.constant["ArmorReference"][armor_id]["Mesh"].split("/")[-1])
        new_file.Exports[1].Data[0].Value[0].Value = FSoftObjectPath(None, FName.FromString(new_file, chroma_body_mat), None) # type: ignore
        new_file.Exports[1].Data[1].Value[0].Value = FSoftObjectPath(None, FName.FromString(new_file, default_body_mat), None) # type: ignore
        new_file.Exports[1].Data[2].Value          = FSoftObjectPath(None, FName.FromString(new_file, chroma_skin_mat), None) # type: ignore
        sub_struct                                 = SoftObjectPropertyData()
        sub_struct.Value                           = FSoftObjectPath(None, FName.FromString(new_file, default_skin_mat), None) # type: ignore
        new_file.Exports[1].Data[3].Value          = [sub_struct]
        new_file.Exports[1].Data[4].Value          = FSoftObjectPath(None, FName.FromString(new_file, dialogue_chroma_skin_mat), None) # type: ignore
        new_file.Exports[1].Data[5].Value          = FSoftObjectPath(None, FName.FromString(new_file, dialogue_default_skin_mat), None) # type: ignore
        new_file.Exports[1].Data[9].Value          = False
        new_file.Exports[1].Data[10].Value         = 1
        new_file.Exports[1].Data[11].Value         = 0
        new_file.Write("\\".join([MOD_DIR, Data.file_to_path["BDBP_BodyValkyrie"], f"BDBP_{armor_id}.uasset"]))

    @staticmethod
    def _has_negative_stat(equipment):
        for stat in _STAT_TO_PROPERTY:
            if Data.datatable["PB_DT_ArmorMaster"][equipment][stat] < 0:
                return True
        return False

    @staticmethod
    def _get_weapon_tier(weapon):
        if weapon in Equipment.BIT_WEAPONS + _DLC_WEAPONS:
            return 1
        if weapon[:-1] in Equipment.BIT_WEAPONS:
            return int(weapon[-1])
        if weapon[:-1] in _DLC_WEAPONS:
            return (int(weapon[-1]) + (0 if "Pirate" in weapon else 1))//2 + 1
        return 0

    @staticmethod
    def _get_weapon_reduction(weapon):
        #Apply reductions to weapons with special properties to not make them super broken
        if "ShieldWeapon" in weapon or "Wagasa" in weapon:
            return 0.9
        if weapon == "Juwuse":
            return 0.85
        if weapon in ["KillerBoots", "Decapitator"]:
            return 0.9
        if weapon in ["Swordbreaker", "Adrastea"]:
            return 0.8
        if weapon in ["Liddyl", "SwordWhip", "BradBlingerLv1"]:
            return 23/_WEAPON_TYPE_TO_MAX_VALUE["ShortSword"]
        if weapon == "OutsiderKnightSword":
            return 13/32
        if weapon in ["RemoteDart", "OracleBlade"]:
            return 25/_WEAPON_TYPE_TO_MAX_VALUE["ShortSword"]
        if weapon in ["WalalSoulimo", "ValralAltar"]:
            return 12/_WEAPON_TYPE_TO_MAX_VALUE["ShortSword"]
        if weapon == "Truesixteenthnight":
            return 49/_WEAPON_TYPE_TO_MAX_VALUE["JapaneseSword"]
        if Data.datatable["PB_DT_WeaponMaster"][weapon]["FLA"]:
            return 0.9
        if Data.datatable["PB_DT_WeaponMaster"][weapon]["LIG"]:
            return 0.8
        if Data.datatable["PB_DT_WeaponMaster"][weapon]["UniqeValue"] != 0.0:
            return 0.9
        if Data.datatable["PB_DT_WeaponMaster"][weapon]["SpecialEffectId"] in ["Stone", "Slow"]:
            return 0.6
        if Data.datatable["PB_DT_WeaponMaster"][weapon]["SpecialEffectId"] != "None":
            return 0.8
        return 1.0