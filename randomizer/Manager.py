import filecmp
import shutil

from .GlobalImports import *
from .Constants import *
from .Utility import read_json, write_json
from . import Data
from . import FileType
from . import Item
from . import Equipment
from . import Enemy
from . import Room
from . import Graphic

STRING_ENTRY_EXCEPTIONS = [
    "ITEM_EXPLAIN_RolledOmelette",
    "ITEM_EXPLAIN_DiamondBullets"
]

def load_map(path):
    if not path:
        path = "MapEdit\\Data\\PB_DT_RoomMaster.json"
    json_file = read_json(path)
    if "PB_DT_RoomMaster" in Data.datatable:
        for room in json_file["MapData"]:
            if not room in Data.datatable["PB_DT_RoomMaster"]:
                area_save_room = json_file["MapData"][room]["AreaID"].split("::")[-1] + "_1000"
                Data.datatable["PB_DT_RoomMaster"][room] = copy.deepcopy(Data.datatable["PB_DT_RoomMaster"][area_save_room])
                Data.datatable["PB_DT_RoomMaster"][room]["LevelName"] = room
                Room.add_game_room(room)
            for data in json_file["MapData"][room]:
                Data.datatable["PB_DT_RoomMaster"][room][data] = json_file["MapData"][room][data]
    else:
        Data.datatable["PB_DT_RoomMaster"] = json_file["MapData"]
    Data.constant["MapOrder"] = json_file["AreaOrder"]
    Data.constant["OriginalMapOrder"] = [
      "m01SIP",
      "m02VIL",
      "m03ENT",
      "m04GDN",
      "m05SAN",
      "m08TWR",
      "m07LIB",
      "m09TRN",
      "m13ARC",
      "m06KNG",
      "m11UGD",
      "m12SND",
      "m14TAR",
      "m17RVA",
      "m15JPN",
      "m10BIG",
      "m18ICE"
    ]
    Data.constant["BloodlessModeMapOrder"] = ["m05SAN"]
    Data.constant["BloodlessModeOriginalMapOrder"] = [
      "m05SAN",
      "m03ENT",
      "m02VIL",
      "m01SIP",
      "m04GDN",
      "m08TWR",
      "m07LIB",
      "m09TRN",
      "m13ARC",
      "m06KNG",
      "m11UGD",
      "m12SND",
      "m14TAR",
      "m17RVA",
      "m15JPN",
      "m10BIG",
      "m18ICE"
    ]

def apply_default_tweaks():
    #Make levels identical in all modes
    #This needs to be done before applying the json tweaks so that exceptions can be patched over
    for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
        if not Enemy.is_enemy(entry):
            continue
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["HardEnemyLevel"]                       = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["NightmareEnemyLevel"]                  = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeDefaultEnemyLevel"]       = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeHardEnemyLevel"]          = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeNightmareEnemyLevel"]     = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeEnemyHPOverride"]         = 0.0
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeEnemyExperienceOverride"] = 0
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeEnemyStrIntMultiplier"]   = 1.0
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["BloodlessModeEnemyConMndMultiplier"]   = 1.0
    #Apply manual tweaks defined in the json
    for file in Data.constant["DefaultTweak"]:
        for entry in Data.constant["DefaultTweak"][file]:
            for data in Data.constant["DefaultTweak"][file][entry]:
                Data.datatable[file][entry][data] = Data.constant["DefaultTweak"][file][entry][data]
    #Loop through all enemies
    for entry in Data.datatable["PB_DT_CharacterParameterMaster"]:
        if not Enemy.is_enemy(entry):
            continue
        if Enemy.is_boss(entry):
            #Make boss health scale with level
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"] = round(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]*(99/Data.datatable["PB_DT_CharacterParameterMaster"][entry]["DefaultEnemyLevel"]))
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"] = round(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]/5)*5
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxMP99Enemy"] = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]
            #Make experience a portion of health
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] > 0:
                multiplier = (4/3)
                if entry[0:5] in Data.constant["ExpModifier"]:
                    multiplier *= Data.constant["ExpModifier"][entry[0:5]]
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] = int(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]*multiplier)
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]        = int(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"]/100) + 2
            #Expand expertise point range that scales with level
            #In vanilla the range is too small and barely makes a difference
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ArtsExperience99Enemy"] > 0:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ArtsExperience99Enemy"] = 15
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ArtsExperience"]        = 1
            #Set stone type
            #Some regular enemies are originally set to the boss stone type which doesn't work well when petrified
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["StoneType"] = "EPBStoneType::Boss"
        else:
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] > 0:
                multiplier = (2/3)
                if entry[0:5] in Data.constant["ExpModifier"]:
                    multiplier *= Data.constant["ExpModifier"][entry[0:5]]
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"] = int(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]*multiplier)
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience"]        = int(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["Experience99Enemy"]/100) + 2
            if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ArtsExperience99Enemy"] > 0:
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ArtsExperience99Enemy"] = 10
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["ArtsExperience"]        = 1
            if entry != "N2008_BOSS":
                Data.datatable["PB_DT_CharacterParameterMaster"][entry]["StoneType"] = "EPBStoneType::Mob"
        #Make level 1 health based off of level 99 health
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP"] = int(Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP99Enemy"]/100) + 2.0
        Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxMP"] = Data.datatable["PB_DT_CharacterParameterMaster"][entry]["MaxHP"]
        #Give all enemies a luck stat which reduces the chances of critting them
        #Originally only Gebel, Valefar and OD have one
        if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["LUC"] == 0 and entry != "N1008":
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["LUC"]        = 5.0
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["LUC99Enemy"] = 50.0
        #Allow Zangetsu to chain grab everyone
        #Whether he can grab or not is entirely based on the enemy's stone resistance
        #As long as it's not 100% resist the chain grab will connect so cap stone resistance at 99.99%
        if Data.datatable["PB_DT_CharacterParameterMaster"][entry]["STO"] >= 100.0:
            Data.datatable["PB_DT_CharacterParameterMaster"][entry]["STO"] = 99.99
    #Make up for the increased expertise range
    for entry in Data.datatable["PB_DT_ArtsCommandMaster"]:
        Data.datatable["PB_DT_ArtsCommandMaster"][entry]["Expertise"] = int(Data.datatable["PB_DT_ArtsCommandMaster"][entry]["Expertise"]*2.5)
    #Loop through 8 bit weapons
    for weapon in Equipment.BIT_WEAPONS:
        #Lock 8 bit weapons behind recipes so that they aren't always easily accessible
        Data.datatable["PB_DT_CraftMaster"][weapon]["OpenKeyRecipeID"]       = "ArmsRecipe018"
        Data.datatable["PB_DT_CraftMaster"][f"{weapon}2"]["OpenKeyRecipeID"] = "ArmsRecipe019"
        Data.datatable["PB_DT_CraftMaster"][f"{weapon}3"]["OpenKeyRecipeID"] = "ArmsRecipe020"
        #Update icon pointer of 8 bit weapons for the new icons
        #The icon texture was edited so that all new icons are evenly shifted from the original ones
        Data.datatable["PB_DT_ItemMaster"][f"{weapon}2"]["IconPath"] = str(int(Data.datatable["PB_DT_ItemMaster"][f"{weapon}2"]["IconPath"]) + 205)
        Data.datatable["PB_DT_ItemMaster"][f"{weapon}3"]["IconPath"] = str(int(Data.datatable["PB_DT_ItemMaster"][f"{weapon}3"]["IconPath"]) + 338)
    #Remove the minimal damage addition on attacks
    for entry in Data.datatable["PB_DT_DamageMaster"]:
        Data.datatable["PB_DT_DamageMaster"][entry]["FixedDamage"] = 0.0
    #Loop through drops
    for entry in Data.datatable["PB_DT_DropRateMaster"].keys():
        #Increase default drop rates
        if Data.datatable["PB_DT_DropRateMaster"][entry]["AreaChangeTreasureFlag"]:
            drop_rate = Data.constant["ItemDrop"]["StandardMat"]["ItemRate"]
        else:
            drop_rate = Data.constant["EnemyDrop"]["EnemyMat"]["ItemRate"]
        #Keep dulla head drops relatively low due to their spawn frequency
        drop_rate_multiplier = 0.5 if entry.split("_")[0] in ["N3090", "N3099"] else 1.0
        if 0.0 < Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] < 100.0:
            Data.datatable["PB_DT_DropRateMaster"][entry]["ShardRate"] = Data.constant["ShardDrop"]["ItemRate"]*drop_rate_multiplier
        for data in ["RareItemRate", "CommonRate", "RareIngredientRate", "CommonIngredientRate"]:
            if 0.0 < Data.datatable["PB_DT_DropRateMaster"][entry][data] < 100.0:
                Data.datatable["PB_DT_DropRateMaster"][entry][data] = drop_rate*drop_rate_multiplier
        #Make coin type match the amount
        if Data.datatable["PB_DT_DropRateMaster"][entry]["CoinOverride"] > 0:
            Data.datatable["PB_DT_DropRateMaster"][entry]["CoinType"] = "EDropCoin::D" + str(Data.datatable["PB_DT_DropRateMaster"][entry]["CoinOverride"])
    #Loop through all items
    for entry in Data.datatable["PB_DT_ItemMaster"]:
        #Remove dishes from shop to prevent heal spam
        #In vanilla you can easily stock up on an infinite amount of them which breaks the game completely
        #This change also makes regular potions more viable now
        if entry in Data.constant["ItemDrop"]["Dish"]["ItemPool"]:
            Data.datatable["PB_DT_ItemMaster"][entry]["max"]       = 1
            Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"]  = 0
            Data.datatable["PB_DT_ItemMaster"][entry]["sellPrice"] = 0
    #Loop through all shards
    for entry in Data.datatable["PB_DT_ShardMaster"]:
        #Make all shard colors match their type
        Data.datatable["PB_DT_ShardMaster"][entry]["ShardColorOverride"] = "EShardColor::None"
        #Make all shards ignore standstill
        Data.datatable["PB_DT_ShardMaster"][entry]["IsStopByAccelWorld"] = False
    #Give magic attack if a weapon has an elemental attribute
    for entry in Data.datatable["PB_DT_WeaponMaster"]:
        for data in ["FLA", "ICE", "LIG", "HOL", "DAR"]:
            if Data.datatable["PB_DT_WeaponMaster"][entry][data]:
                Data.datatable["PB_DT_WeaponMaster"][entry]["MagicAttack"] = Data.datatable["PB_DT_WeaponMaster"][entry]["MeleeAttack"]
                break
    #Rebalance boss rush mode a bit
    #Remove all consumables from inventory
    for data in Data.game_data["PBExtraModeInfo_BP"].Exports[1].Data[7].Value:
        data.Value[1].Value = 0
    #Start both stages at level 50
    for data in range(8, 14):
        Data.game_data["PBExtraModeInfo_BP"].Exports[1].Data[data].Value = 50
    #Give all bosses level 66
    for data in Data.game_data["PBExtraModeInfo_BP"].Exports[1].Data[14].Value:
        data.Value.Value = 66
    #Rename the second Zangetsu boss so that he isn't confused with the first
    Data.stringtable["PBMasterStringTable"]["ENEMY_NAME_N1011_STRONG"] = Data.translation["Enemy"]["N1011_STRONG"]
    Data.stringtable["PBMasterStringTable"]["ITEM_NAME_Medal013"]      = Data.translation["Enemy"]["N1011_STRONG"] + " Medal"
    Data.stringtable["PBMasterStringTable"]["ITEM_EXPLAIN_Medal013"]   = "Proof that you have triumphed over " + Data.translation["Enemy"]["N1011_STRONG"] + "."
    #Update Jinrai cost description
    Data.stringtable["PBMasterStringTable"]["ARTS_TXT_017_00"] += str(Data.datatable["PB_DT_ArtsCommandMaster"]["JSword_GodSpeed1"]["CostMP"])
    #Slightly change Igniculus' descriptions to match other familiar's
    Data.stringtable["PBMasterStringTable"]["SHARD_EFFECT_TXT_FamiliaIgniculus"] = Data.stringtable["PBMasterStringTable"]["SHARD_EFFECT_TXT_FamiliaArcher"]
    Data.stringtable["PBMasterStringTable"]["SHARD_NAME_FamiliaIgniculus"] = Data.translation["Shard"]["FamiliaIgniculus"]
    #Fix the archive Doppleganger outfit color to match Miriam's
    index = Data.game_data["M_Body06_06"].SearchNameReference(FString("/Game/Core/Character/P0000/Texture/Body/T_Body06_06_Color"))
    Data.game_data["M_Body06_06"].SetNameReference(index, FString("/Game/Core/Character/P0000/Texture/Body/T_Body01_01_Color"))
    index = Data.game_data["M_Body06_06"].SearchNameReference(FString("T_Body06_06_Color"))
    Data.game_data["M_Body06_06"].SetNameReference(index, FString("T_Body01_01_Color"))
    #Add DLCs to the enemy archives
    Enemy.add_enemy_to_archive(102, "N2016", [], None, "N2015")
    Data.stringtable["PBMasterStringTable"]["ENEMY_EXPLAIN_N2016"] = "A giant monster that takes part on the most powerful Greed waves."
    Enemy.add_enemy_to_archive(109, "N2017", [], None, "N2008")
    Data.stringtable["PBMasterStringTable"]["ENEMY_EXPLAIN_N2017"] = "An instrument of the war fought over the magical cloth that powered the world."
    #Give the new dullahammer a unique name and look
    Data.datatable["PB_DT_CharacterParameterMaster"]["N3127"]["NameStrKey"] = "ENEMY_NAME_N3127"
    Data.stringtable["PBMasterStringTable"]["ENEMY_NAME_N3127"] = Data.translation["Enemy"]["N3127"]
    Graphic.set_material_hsv("MI_N3127_Eye", "EmissiveColor" , (215, 100, 100))
    Graphic.set_material_hsv("MI_N3127_Eye", "HighlightColor", (215,  65, 100))
    #Give Guardian his own shard drop
    Data.datatable["PB_DT_CharacterMaster"]["N2017"]["ItemDrop"] = "N2017_Shard"
    Data.datatable["PB_DT_DropRateMaster"]["N2017_Shard"] = copy.deepcopy(Data.datatable["PB_DT_DropRateMaster"]["Deepsinker_Shard"])
    Data.datatable["PB_DT_DropRateMaster"]["N2017_Shard"]["ShardId"] = "TissRosain"
    Data.datatable["PB_DT_CraftMaster"]["TissRosain"]["OpenKeyRecipeID"] = "Medal019"
    #Make the second train gate a regular gate rather than a debug
    Data.game_data["m09TRN_004_Gimmick"].Exports[257].Data[18].Value = False
    #Move the Craftwork staircase closer to the edge of the screen so that Dimension Shift cannot pass
    Data.game_data["m07LIB_023_Gimmick"].Exports[57].Data[0].Value[0].Value = FVector(1160, 0, 2400)
    #Move the Alfred magical seal closer to the edge of the screen so that Dimension Shift cannot pass
    Data.game_data["m12SND_023_Gimmick"].Exports[7].Data[0].Value[0].Value = FVector(1200, 0, 2520)
    #Give the lever door in upper cathedral its own gimmick flag instead of being shared with the hall one
    Data.game_data["m05SAN_017_Gimmick"].Exports[1].Data[7].Value = FName.FromString(Data.game_data["m05SAN_017_Gimmick"], "SAN_017_LockDoor")
    Data.datatable["PB_DT_GimmickFlagMaster"]["SAN_017_LockDoor"] = {}
    Data.datatable["PB_DT_GimmickFlagMaster"]["SAN_017_LockDoor"]["Id"] = get_available_gimmick_flag()
    #Remove the breakable wall in m17RVA_003 that shares its drop id with the wall in m17RVA_011
    Data.datatable["PB_DT_GimmickFlagMaster"]["RVA_003_ItemWall"]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]
    #Add the missing gate warps for the extra characters
    #That way impassable obstacles are no longer a problem
    Room.add_extra_mode_warp("m04GDN_013_Gimmick", FVector(2460, 0, 2100), FRotator(180,   0,   0), FVector(3080, 0, 1800), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m05SAN_003_Gimmick", FVector( 220, 0, 5940), FRotator(  0,   0, 180), FVector(2300, 0, 6000), FRotator(  0, 180,   0))
    Room.add_extra_mode_warp("m05SAN_003_Gimmick", FVector(1400, 0,  900), FRotator(180,   0,   0), FVector(1400, 0,   60), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m07LIB_008_Gimmick", FVector(1200, 0,  960), FRotator(  0,   0,   0), FVector( 840, 0, 1380), FRotator(180,   0,   0))
    Room.add_extra_mode_warp("m07LIB_012_Gimmick", FVector(1080, 0,  480), FRotator(  0, 180,   0), FVector( 940, 0,  180), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m07LIB_014_Gimmick", FVector( 540, 0,  450), FRotator(-90, 180,   0), FVector(1080, 0,  240), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m07LIB_022_Gimmick", FVector( 420, 0,  720), FRotator(180,   0,   0), FVector( 520, 0,  600), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m07LIB_035_Gimmick", FVector( 420, 0, 1520), FRotator(-90, 180,   0), FVector( 540, 0, 1680), FRotator( 90, 180,   0))
    Room.add_extra_mode_warp("m08TWR_016_Gimmick", FVector( 600, 0,  240), FRotator(  0, 180,   0), FVector( 600, 0, -180), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m11UGD_025_Gimmick", FVector(1745, 0,  565), FRotator(  0, 180,   0), FVector(2205, 0,  630), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m11UGD_056_Gimmick", FVector( 880, 0, 2220), FRotator(180,   0,   0), FVector(1050, 0, 2400), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m11UGD_056_Gimmick", FVector( 600, 0, 1300), FRotator(-90, 180,   0), FVector( 660, 0, 1500), FRotator( 90, 180,   0))
    Room.add_extra_mode_warp("m12SND_006_Gimmick", FVector( 660, 0,   60), FRotator(  0,   0,   0), FVector( 420, 0,   60), FRotator(  0, 180,   0))
    Room.add_extra_mode_warp("m13ARC_006_Gimmick", FVector( 600, 0,  960), FRotator(  0,   0,   0), FVector( 420, 0,  960), FRotator(  0, 180,   0))
    Room.add_extra_mode_warp("m15JPN_002_Gimmick", FVector(1740, 0, 1260), FRotator(180,   0,   0), FVector(1200, 0,   75), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m17RVA_001_Gimmick", FVector( 800, 0, 2080), FRotator(  0,   0, 180), FVector( 540, 0, 1800), FRotator(  0, 180,   0))
    Room.add_extra_mode_warp("m17RVA_011_Gimmick", FVector(1900, 0, 2080), FRotator(180,   0,   0), FVector(2140, 0, 2080), FRotator(  0,   0, 180))
    Room.add_extra_mode_warp("m17RVA_012_Gimmick", FVector(2320, 0,  120), FRotator(  0, 180,   0), FVector(1640, 0,  120), FRotator(  0,   0,   0))
    Room.add_extra_mode_warp("m18ICE_008_Gimmick", FVector(1745, 0,  565), FRotator(  0, 180,   0), FVector(2205, 0,  630), FRotator(  0,   0,   0))
    #Make the garden iron maiden disappear in extra modes
    struct = BoolPropertyData(FName.FromString(Data.game_data["m04GDN_006_Gimmick"], "DeleteSpinoffCharacter"))
    struct.Value = True
    Data.game_data["m04GDN_006_Gimmick"].Exports[6].Data.Add(struct)
    #Add the missing Bloodless candle that was accidentally removed in a recent game update
    Room.add_level_actor("m07LIB_009_Gimmick", "BP_DM_BloodlessAbilityGimmick_C", FVector(720, -120, 1035), FRotator(0, 0, 0), FVector(1, 1, 1), {"UnlockAbilityType": FName.FromString(Data.game_data["m07LIB_009_Gimmick"], "EPBBloodlessAbilityType::BLD_ABILITY_INT_UP_5")})
    #Due to Focalor being scrapped the devs put aqua stream on a regular enemy instead but this can cause first playthroughs to miss out on the shard
    #Add a shard candle for it so that it becomes a guaranteed
    Room.add_level_actor("m11UGD_019_Gimmick", "BP_DM_BaseLantern_ShardChild2_C", FVector(1320, -60, 1845), FRotator(180, 0, 0), FVector(1, 1, 1), {"ShardID": FName.FromString(Data.game_data["m11UGD_019_Gimmick"], "Aquastream"), "GimmickFlag": FName.FromString(Data.game_data["m11UGD_019_Gimmick"], "AquastreamLantarn001")})
    Data.datatable["PB_DT_GimmickFlagMaster"]["AquastreamLantarn001"] = {}
    Data.datatable["PB_DT_GimmickFlagMaster"]["AquastreamLantarn001"]["Id"] = get_available_gimmick_flag()
    Data.datatable["PB_DT_DropRateMaster"]["Aquastream_Shard"] = copy.deepcopy(Data.datatable["PB_DT_DropRateMaster"]["Deepsinker_Shard"])
    Data.datatable["PB_DT_DropRateMaster"]["Aquastream_Shard"]["ShardId"] = "Aquastream"
    #Add a shard candle for Igniculus in Celeste's room
    #That way Celeste key becomes relevant and Igniculus can be obtained in story mode
    Room.add_level_actor("m88BKR_003_Gimmick", "BP_DM_BaseLantern_ShardChild2_C", FVector(660, -120, 315), FRotator(0, 0, 0), FVector(1, 1, 1), {"ShardID": FName.FromString(Data.game_data["m88BKR_003_Gimmick"], "FamiliaIgniculus"), "GimmickFlag": FName.FromString(Data.game_data["m88BKR_003_Gimmick"], "IgniculusLantarn001")})
    Data.datatable["PB_DT_GimmickFlagMaster"]["IgniculusLantarn001"] = {}
    Data.datatable["PB_DT_GimmickFlagMaster"]["IgniculusLantarn001"]["Id"] = get_available_gimmick_flag()
    Data.datatable["PB_DT_DropRateMaster"]["FamiliaIgniculus_Shard"] = copy.deepcopy(Data.datatable["PB_DT_DropRateMaster"]["FamiliaArcher_Shard"])
    Data.datatable["PB_DT_DropRateMaster"]["FamiliaIgniculus_Shard"]["ShardId"] = "FamiliaIgniculus"
    #The HavePatchPureMiriam gimmick flag triggers as soon as a Pure Miriam chest is loaded in a room
    #So place one in the first ship room for this flag to trigger as soon as the game starts
    Room.add_level_actor("m01SIP_000_Gimmick", "PBPureMiriamTreasureBox_BP_C", FVector(-999, 0, 0), FRotator(0, 0, 0), FVector(1, 1, 1), {"DropItemID": FName.FromString(Data.game_data["m01SIP_000_Gimmick"], "AAAA_Shard"), "ItemID": FName.FromString(Data.game_data["m01SIP_000_Gimmick"], "AAAA_Shard")})
    #Remove the Dullhammer in the first galleon room on hard to prevent rough starts
    #That way you can at least save once before the game truly starts
    Room.remove_level_class("m01SIP_001_Enemy_Hard", "Chr_N3015_C")
    #Remove the morte spawner that isn't an actual enemy actor
    Room.remove_level_class("m01SIP_011_Enemy", "PBCharacterGeneratorActor")
    #Remove the bone mortes from that one crowded room in galleon
    Room.remove_level_class("m01SIP_014_Enemy_Hard", "Chr_N3004_C")
    #Remove the giant rat in Den, was most likely a dev mistake
    Room.remove_level_class("m10BIG_008_Enemy", "Chr_N3051_C")
    #Remove the boss door duplicate in the room before Craftwork
    Room.remove_level_class("m05SAN_011_BG", "PBBossDoor_BP_C")
    #Fix that one Water Leaper in desert that falls through the floor by shifting its position upwards
    Data.game_data["m12SND_025_Enemy"].Exports[4].Data[5].Value[0].Value = FVector(-260, -700, 600)
    #Fix some of the giant cannon stacks clipping over each other
    Data.game_data["m10BIG_008_Enemy"].Exports[17].Data[5].Value[0].Value     = FVector(2220, 0, 3505)
    Data.game_data["m10BIG_008_Enemy_Hard"].Exports[0].Data[5].Value[0].Value = FVector(2220, 0, 3865)
    Data.game_data["m10BIG_008_Enemy_Hard"].Exports[1].Data[5].Value[0].Value = FVector(2220, 0, 4225)
    Data.game_data["m10BIG_008_Enemy"].Exports[18].Data[5].Value[0].Value     = FVector( 300, 0, 1345)
    Data.game_data["m10BIG_008_Enemy_Hard"].Exports[2].Data[5].Value[0].Value = FVector( 300, 0, 1705)
    Data.game_data["m10BIG_008_Enemy_Hard"].Exports[3].Data[5].Value[0].Value = FVector( 300, 0, 2065)
    Data.game_data["m10BIG_008_Enemy"].Exports[19].Data[5].Value[0].Value     = FVector(2220, 0,  505)
    Data.game_data["m10BIG_008_Enemy_Hard"].Exports[4].Data[5].Value[0].Value = FVector(2220, 0,  865)
    Data.game_data["m10BIG_008_Enemy_Hard"].Exports[5].Data[5].Value[0].Value = FVector(2220, 0, 1225)
    Data.game_data["m10BIG_013_Enemy"].Exports[5].Data[5].Value[0].Value      = FVector(1020, 0, 1585)
    Data.game_data["m10BIG_013_Enemy_Hard"].Exports[0].Data[5].Value[0].Value = FVector(1020, 0, 1945)
    Data.game_data["m10BIG_013_Enemy_Hard"].Exports[1].Data[5].Value[0].Value = FVector(1020, 0, 2305)
    Data.game_data["m10BIG_013_Enemy"].Exports[6].Data[5].Value[0].Value      = FVector(2040, 0, 2005)
    Data.game_data["m10BIG_013_Enemy_Hard"].Exports[2].Data[5].Value[0].Value = FVector(2040, 0, 2365)
    Data.game_data["m10BIG_013_Enemy"].Exports[7].Data[5].Value[0].Value      = FVector( 300, 0, 1105)
    Data.game_data["m10BIG_013_Enemy_Hard"].Exports[3].Data[5].Value[0].Value = FVector( 300, 0, 1465)
    Data.game_data["m10BIG_013_Enemy_Hard"].Exports[4].Data[5].Value[0].Value = FVector( 360, 0, 2065)
    Data.game_data["m10BIG_013_Enemy_Hard"].Exports[5].Data[5].Value[0].Value = FVector( 360, 0, 2425)
    #Remove the iron maidens that were added by the devs in an update in the tall entrance shaft
    Room.remove_level_class("m03ENT_000_Gimmick", "BP_IronMaiden_C")
    #Add magic doors instead to truly prevent tanking through
    Room.add_level_actor("m03ENT_000_Gimmick", "BP_MagicDoor_C", FVector(1260, -270, 7500), FRotator(  0, 0, 0), FVector(-1, 1, 1), {"CommonFlag": FName.FromString(Data.game_data["m03ENT_000_Gimmick"], "EGameCommonFlag::None")})
    Room.add_level_actor("m03ENT_000_Gimmick", "BP_MagicDoor_C", FVector(1260, -270, 9120), FRotator(180, 0, 0), FVector(-1, 1, 1), {"CommonFlag": FName.FromString(Data.game_data["m03ENT_000_Gimmick"], "EGameCommonFlag::None")})
    #Neutralize the golden chest interaction box transforms to prevent issues when copying
    Data.game_data["m08TWR_019_Gimmick"].Exports[1022].Data.Remove(Data.game_data["m08TWR_019_Gimmick"].Exports[1022].Data[5])
    Data.game_data["m08TWR_019_Gimmick"].Exports[1022].Data.Remove(Data.game_data["m08TWR_019_Gimmick"].Exports[1022].Data[5])
    #Change Dark Matter so that consuming it puts the player in OHKO mode until the next death
    Data.datatable["PB_DT_SpecialEffectMaster"]["DarkMatter"]["LifeTime"] = -1
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatter"]["Type"]                     = "EPBSpecialEffect::None"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatter"]["ParameterName"]            = "None"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatterTempDownMaxHP"]                = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["CurseTempDownMaxHP"])
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatterTempDownMaxHP"]["DefId"]       = "DarkMatterTempDownMaxHP"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatterTempDownMaxHP"]["Parameter01"] = 99.999
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatterTempDownMaxMP"]                = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["CurseTempDownMaxMP"])
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatterTempDownMaxMP"]["DefId"]       = "DarkMatterTempDownMaxMP"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DarkMatterTempDownMaxMP"]["Parameter01"] = 99.999
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DarkMatterHitPoint"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectGroupMaster"]["CurseHitPoint"])
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DarkMatterHitPoint"]["GroupId"] = "DarkMatter"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DarkMatterHitPoint"]["DefId"]   = "DarkMatterTempDownMaxHP"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DarkMatterMagicPoint"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectGroupMaster"]["CurseMagicPoint"])
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DarkMatterMagicPoint"]["GroupId"] = "DarkMatter"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DarkMatterMagicPoint"]["DefId"]   = "DarkMatterTempDownMaxMP"
    #Give primary stat debuffs their secondary stat too
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_STR_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["Id"]      = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_STR_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]["Id"]      = "DEBUFF_RATE_INT_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_INT_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_CON_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["Id"]      = "DEBUFF_RATE_DEF_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_DEF_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_CON_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]["Id"]      = "DEBUFF_RATE_MND_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_MND_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]                = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_STR_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["DefId"]       = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["Type"]        = "EPBSpecialEffect::None"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["Parameter01"] = 0
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["Parameter02"] = 0
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["Parameter03"] = 0
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]                = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_STR_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]["DefId"]       = "DEBUFF_RATE_INT_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]["Parameter01"] = 14
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]                = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_CON_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["DefId"]       = "DEBUFF_RATE_DEF_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["Type"]        = "EPBSpecialEffect::None"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["Parameter01"] = 0
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["Parameter02"] = 0
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["Parameter03"] = 0
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]                = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_CON_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]["DefId"]       = "DEBUFF_RATE_MND_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]["Parameter01"] = 15
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_STR_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_ATK_WITH_EFFECT"]["DefId"]   = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_STR_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_STR_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_INT_WITH_EFFECT"]["DefId"]   = "DEBUFF_RATE_INT_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_CON_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_DEF_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_DEF_WITH_EFFECT"]["DefId"]   = "DEBUFF_RATE_DEF_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_CON_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_DEF_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]            = copy.deepcopy(Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_CON_WITH_EFFECT"])
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]["GroupId"] = "DEBUFF_RATE_DEF_WITH_EFFECT"
    Data.datatable["PB_DT_SpecialEffectGroupMaster"]["DEBUFF_RATE_MND_WITH_EFFECT"]["DefId"]   = "DEBUFF_RATE_MND_WITH_EFFECT"
    Data.datatable["PB_DT_WeaponMaster"]["Swordbreaker"]["SpecialEffectId"]        = "DEBUFF_RATE_ATK_WITH_EFFECT"
    Data.datatable["PB_DT_DamageMaster"]["P0000_Jsword_Kabuto"]["SpecialEffectId"] = "DEBUFF_RATE_DEF_WITH_EFFECT"
    for suffix in ["", "_EX", "_EX2"]:
        Data.datatable["PB_DT_DamageMaster"]["WeaponbaneRounds" + suffix]["SpecialEffectId"] = "DEBUFF_RATE_ATK_WITH_EFFECT"
        Data.datatable["PB_DT_DamageMaster"]["ShieldbaneRounds" + suffix]["SpecialEffectId"] = "DEBUFF_RATE_DEF_WITH_EFFECT"
    #Add a special ring that buffs the katana parry techniques
    Item.add_game_item(106, "MightyRing", "Accessory", "Ring", (2048, 3200), Data.translation["Item"]["MightyRing"], "A symbol of great courage that amplifies the power of counterattacks.", 8080, False)
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt245"]                                                   = copy.deepcopy(Data.datatable["PB_DT_EnchantParameterType"]["DUMMY"])
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt245"]["Type_5_BF08F4064B9CF244C30C7788588CFDF5"]        = "EPBEquipSpecialAttribute::BuffParryArt"
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt245"]["EquipType_25_DEF1C32D420ACBA29D5AA0B5D0AE0D20"]  = "ECarriedCatalog::Accessory1"
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt245"]["ItemID_31_461716F74C5895124D82E0B3CA33B6B3"]     = "MightyRing"
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt245"]["EquipValue_28_5CFE97924D56254C9B62AF83698220FC"] = 1.5
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt246"]                                                   = copy.deepcopy(Data.datatable["PB_DT_EnchantParameterType"]["DUMMY"])
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt246"]["Type_5_BF08F4064B9CF244C30C7788588CFDF5"]        = "EPBEquipSpecialAttribute::BuffParryArt"
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt246"]["EquipType_25_DEF1C32D420ACBA29D5AA0B5D0AE0D20"]  = "ECarriedCatalog::Accessory2"
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt246"]["ItemID_31_461716F74C5895124D82E0B3CA33B6B3"]     = "MightyRing"
    Data.datatable["PB_DT_EnchantParameterType"]["BuffParryArt246"]["EquipValue_28_5CFE97924D56254C9B62AF83698220FC"] = 1.5
    Data.datatable["PB_DT_ArmorMaster"]["MightyRing"]["MeleeDefense"] = 3
    Data.datatable["PB_DT_ArmorMaster"]["MightyRing"]["DAG"]          = 5
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["RareItemId"]               = "MightyRing"
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["RareItemQuantity"]         = 1
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["RareItemRate"]             = 100.0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CommonItemId"]             = "None"
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CommonItemQuantity"]       = 0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CommonRate"]               = 0.0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["RareIngredientId"]         = "None"
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["RareIngredientQuantity"]   = 0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["RareIngredientRate"]       = 0.0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CommonIngredientId"]       = "None"
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CommonIngredientQuantity"] = 0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CommonIngredientRate"]     = 0.0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CoinType"]                 = "EDropCoin::None"
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["CoinOverride"]             = 0
    Data.datatable["PB_DT_DropRateMaster"]["Treasurebox_BIG010_1"]["AreaChangeTreasureFlag"]   = False
    Data.constant["ItemDrop"]["Accessory"]["ItemPool"].append("MightyRing")
    for num in range(4):
        Data.constant["QuestRequirement"]["Memento"]["ItemPool"].append("MightyRing")
    #Add an invisibility cloak into the game
    Item.add_game_item(151, "InvisibleCloak", "Armor", "None", (3840, 2944), Data.translation["Item"]["InvisibleCloak"], "A magical mantle that renders anything it covers fully invisible.", 22500, False)
    Data.datatable["PB_DT_ArmorMaster"]["InvisibleCloak"]["MeleeDefense"] = 11
    Data.datatable["PB_DT_ArmorMaster"]["InvisibleCloak"]["MagicDefense"] = 52
    Data.datatable["PB_DT_ArmorMaster"]["InvisibleCloak"]["HOL"]          = 5
    Data.datatable["PB_DT_ArmorMaster"]["InvisibleCloak"]["DAR"]          = 5
    Data.datatable["PB_DT_ArmorMaster"]["InvisibleCloak"]["INT"]          = 10
    Data.datatable["PB_DT_ArmorMaster"]["InvisibleCloak"]["MND"]          = 8
    Data.datatable["PB_DT_DropRateMaster"]["N3025_Shard"]["RareItemId"]       = "InvisibleCloak"
    Data.datatable["PB_DT_DropRateMaster"]["N3025_Shard"]["RareItemQuantity"] = 1
    Data.datatable["PB_DT_DropRateMaster"]["N3025_Shard"]["RareItemRate"]     = Data.constant["EnemyDrop"]["EnemyMat"]["ItemRate"]
    Data.constant["ItemDrop"]["Armor"]["ItemPool"].append("InvisibleCloak")
    for num in range(5):
        Data.constant["QuestRequirement"]["Memento"]["ItemPool"].append("InvisibleCloak")
    #Add staggering bullets into the game
    Item.add_game_item(8, "RagdollBullet", "Bullet", "None", (3456, 128), Data.translation["Item"]["RagdollBullet"], "Strange bullets that contort targets, leaving a lasting impact.", 0, True)
    Data.datatable["PB_DT_AmmunitionMaster"]["RagdollBullet"]["MeleeAttack"] = 40
    Data.datatable["PB_DT_CraftMaster"]["RagdollBullet"]["CraftValue"]       = 5
    Data.datatable["PB_DT_CraftMaster"]["RagdollBullet"]["Ingredient2Id"]    = "Silver"
    Data.datatable["PB_DT_CraftMaster"]["RagdollBullet"]["Ingredient3Id"]    = "HolyWater"
    Data.datatable["PB_DT_CraftMaster"]["RagdollBullet"]["Ingredient3Total"] = 1
    Data.datatable["PB_DT_CraftMaster"]["RagdollBullet"]["OpenKeyRecipeID"]  = "BalletRecipe002"
    for suffix in ["", "_EX", "_EX2"]:
        Data.datatable["PB_DT_DamageMaster"][f"RagdollBullet{suffix}"]["SA_Attack"] = 9999
    for num in range(5):
        Data.constant["ItemDrop"]["Bullet"]["ItemPool"].append("RagdollBullet")
    #Add a tonic that speeds up all of Miriam's movement for 15 seconds
    Item.add_game_item(9, "TimeTonic", "Potion", "None", (3840, 0), Data.translation["Item"]["TimeTonic"], "An ancient drink that grants the ability to view the world at a slower pace.", 2000, True)
    Data.datatable["PB_DT_ItemMaster"]["TimeTonic"]["max"] = 5
    Data.datatable["PB_DT_CraftMaster"]["TimeTonic"]["Ingredient1Id"] = "MonsterBirdTears"
    Data.datatable["PB_DT_CraftMaster"]["TimeTonic"]["Ingredient2Id"] = "SeekerEye"
    Data.datatable["PB_DT_CraftMaster"]["TimeTonic"]["Alkhahest"]     = 4
    Data.datatable["PB_DT_ConsumableMaster"]["TimeTonic"]["IsAutoUse"] = False
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["TimeTonic"]["Type"]        = "EPBSpecialEffect::TimeRate"
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["TimeTonic"]["Parameter01"] = 1.5
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["TimeTonic"]["Parameter02"] = 1.0
    Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]["TimeTonic"]["Parameter03"] = 20.0
    Data.datatable["PB_DT_SpecialEffectMaster"]["TimeTonic"]["LifeTime"] = 15.0
    for num in range(2):
        Data.constant["ItemDrop"]["Potion"]["ItemPool"].append("TimeTonic")
    #Make DLC armors inherit the stats of their higher level counterpart to reflect the simplified tier system
    Data.datatable["PB_DT_ArmorMaster"]["VampiricSkinsuit"]  = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["VampiricSkinsuit1"])
    Data.datatable["PB_DT_ArmorMaster"]["VampiricSkinsuit2"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["VampiricSkinsuit3"])
    Data.datatable["PB_DT_ArmorMaster"]["VampiricSkinsuit4"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["VampiricSkinsuit5"])
    Data.datatable["PB_DT_ArmorMaster"]["MagicalGirlBody"]  = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["MagicalGirlBody1"])
    Data.datatable["PB_DT_ArmorMaster"]["MagicalGirlBody2"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["MagicalGirlBody3"])
    Data.datatable["PB_DT_ArmorMaster"]["MagicalGirlBody4"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["MagicalGirlBody5"])
    Data.datatable["PB_DT_ArmorMaster"]["ShantaeOutfit1"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["ShantaeOutfit2"])
    Data.datatable["PB_DT_ArmorMaster"]["ShantaeOutfit3"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["ShantaeOutfit4"])
    Data.datatable["PB_DT_ArmorMaster"]["ShantaeOutfit5"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["ShantaeOutfit6"])
    Data.datatable["PB_DT_ArmorMaster"]["FestivalKimono"]  = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["FestivalKimono1"])
    Data.datatable["PB_DT_ArmorMaster"]["FestivalKimono2"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["FestivalKimono3"])
    Data.datatable["PB_DT_ArmorMaster"]["FestivalKimono4"] = copy.deepcopy(Data.datatable["PB_DT_ArmorMaster"]["FestivalKimono5"])
    #Give the Valkyrie set a luck bonus if both are equipped
    Data.datatable["PB_DT_SetBonus"]["Valkyriedress"] = copy.deepcopy(Data.datatable["PB_DT_SetBonus"]["COL_Au15_Dress"])
    Data.datatable["PB_DT_SetBonus"]["Valkyriedress"]["FaceIcon"] = "EIconType::Default"
    Data.datatable["PB_DT_SetBonus"]["Valkyriedress"]["Head"] = "ValkyrieTiara"
    Data.datatable["PB_DT_SetBonus"]["Valkyriedress"]["Body"] = "Valkyriedress"
    Data.datatable["PB_DT_SetBonus"]["Valkyriedress"]["LCK"] = 10
    #With this mod vanilla rando is pointless and obselete so remove its widget
    #Also prevent going online with this mod active
    remove_unwanted_modes()

def set_randomizer_events():
    #Some events need to be triggered by default to avoid conflicts or tedium
    #First ship door
    Room.remove_level_class("m01SIP_000_Gimmick", "BP_EventDoor_C")
    #Librarian easter egg
    Data.datatable["PB_DT_GimmickFlagMaster"]["LIB_009_PushUpOD_Second"]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["LIB_009_PushUpOD_First"]["Id"]
    #Tower cutscene/garden red moon removal
    Data.datatable["PB_DT_EventFlagMaster"]["Event_07_001_0000"]["Id"] = Data.datatable["PB_DT_EventFlagMaster"]["Event_01_001_0000"]["Id"]
    Data.datatable["PB_DT_EventFlagMaster"]["Event_19_001_0000"]["Id"] = Data.datatable["PB_DT_EventFlagMaster"]["Event_01_001_0000"]["Id"]

def remove_fire_shard_requirement():
    #Break galleon cannon wall
    Data.datatable["PB_DT_GimmickFlagMaster"]["SIP_008_BreakWallCannon"]["Id"] = Data.datatable["PB_DT_GimmickFlagMaster"]["HavePatchPureMiriam"]["Id"]

def update_item_descriptions():
    #Add magical stats to descriptions
    for entry in Data.datatable["PB_DT_ArmorMaster"]:
        if not f"ITEM_EXPLAIN_{entry}" in Data.stringtable["PBMasterStringTable"]:
            continue
        if Data.datatable["PB_DT_ArmorMaster"][entry]["MagicAttack"] != 0:
            append_string_entry("PBMasterStringTable", f"ITEM_EXPLAIN_{entry}", "<span color=\"#ff8000\">mATK " + str(Data.datatable["PB_DT_ArmorMaster"][entry]["MagicAttack"]) + "</>")
        if Data.datatable["PB_DT_ArmorMaster"][entry]["MagicDefense"] != 0:
            append_string_entry("PBMasterStringTable", f"ITEM_EXPLAIN_{entry}", "<span color=\"#ff00ff\">mDEF " + str(Data.datatable["PB_DT_ArmorMaster"][entry]["MagicDefense"]) + "</>")
    #Add restoration amount to descriptions
    for entry in Data.datatable["PB_DT_SpecialEffectDefinitionMaster"]:
        if not f"ITEM_EXPLAIN_{entry}" in Data.stringtable["PBMasterStringTable"]:
            continue
        if Data.datatable["PB_DT_SpecialEffectDefinitionMaster"][entry]["Type"] == "EPBSpecialEffect::ChangeHP":
            append_string_entry("PBMasterStringTable", f"ITEM_EXPLAIN_{entry}", "<span color=\"#00ff00\">HP " + str(int(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"][entry]["Parameter01"])) + "</>")
        if Data.datatable["PB_DT_SpecialEffectDefinitionMaster"][entry]["Type"] == "EPBSpecialEffect::ChangeMP":
            append_string_entry("PBMasterStringTable", f"ITEM_EXPLAIN_{entry}", "<span color=\"#00bfff\">MP " + str(int(Data.datatable["PB_DT_SpecialEffectDefinitionMaster"][entry]["Parameter01"])) + "</>")
    for entry in Data.datatable["PB_DT_AmmunitionMaster"]:
        if not f"ITEM_EXPLAIN_{entry}" in Data.stringtable["PBMasterStringTable"]:
            continue
        append_string_entry("PBMasterStringTable", f"ITEM_EXPLAIN_{entry}", "<span color=\"#ff0000\">ATK " + str(Data.datatable["PB_DT_AmmunitionMaster"][entry]["MeleeAttack"]) + "</>")
    #Add Shovel Armor's attack stat to its description
    append_string_entry("PBMasterStringTable", "ITEM_EXPLAIN_Shovelarmorsarmor", "<span color=\"#ff0000\">wATK " + str(int(Data.datatable["PB_DT_CoordinateParameter"]["ShovelArmorWeaponAtk"]["Value"])) + "</>")

def remove_unwanted_modes():
    for index in [293, 294]:
        new_list = []
        count = 0
        for data in Data.game_data["TitleExtraMenu"].Exports[index].Data[0].Value:
            if not count in [2, 5, 6]:
                new_list.append(data)
            count += 1
        Data.game_data["TitleExtraMenu"].Exports[index].Data[0].Value = new_list
    Data.stringtable["PBSystemStringTable"]["SYS_SEN_ModeRogueDungeon"] = "DELETED"
    Data.stringtable["PBSystemStringTable"]["SYS_MSG_OpenRogueDungeonMode"] = "Story Mode completed."

def show_mod_stats(seed : str, mod_version : str):
    game_version = str(Data.game_data["VersionNumber"].Exports[6].Data[0].CultureInvariantString)
    mod_stats = f"Bloodstained {game_version}\r\nTrue Randomization v{mod_version}"
    mod_stats += f"\r\nSeed # {seed}" if seed else ""
    height = 0.66 if seed else 0.4
    for num in range(2):
        Data.game_data["VersionNumber"].Exports[4 + num].Data[0].Value[2].Value[0].X = 19
        Data.game_data["VersionNumber"].Exports[4 + num].Data[0].Value[2].Value[0].Y = height
        Data.game_data["VersionNumber"].Exports[6 + num].Data[0].CultureInvariantString = FString(mod_stats)
        Data.game_data["VersionNumber"].Exports[6 + num].Data[1].Value[2].Value = 16
        Data.game_data["VersionNumber"].Exports[6 + num].Data[2].EnumValue = FName.FromString(Data.game_data["VersionNumber"], "ETextJustify::Left")
        struct = struct = FloatPropertyData(FName.FromString(Data.game_data["VersionNumber"], "LineHeightPercentage"))
        struct.Value = 0.6
        Data.game_data["VersionNumber"].Exports[6 + num].Data.Add(struct)

def set_single_difficulty(difficulty):
    #Ensure that in game difficulty never mismatches the mod's
    new_list = []
    sub_struct = BytePropertyData()
    sub_struct.ByteType = BytePropertyType.FName
    sub_struct.EnumValue = FName.FromString(Data.game_data["DifficultSelecter"], f"EPBGameLevel::{difficulty}")
    new_list = [sub_struct]
    Data.game_data["DifficultSelecter"].Exports[2].Data[1].Value = new_list

def set_default_entry_name(name):
    #Change the default in-game file name
    Data.game_data["EntryNameSetter"].Exports[110].Data[0].CultureInvariantString = FString(name)
    Data.game_data["EntryNameSetter"].Exports[110].Data[1].CultureInvariantString = FString(name)
    Data.game_data["EntryNameSetter"].Exports[111].Data[2].CultureInvariantString = FString(name)
    Data.game_data["EntryNameSetter"].Exports[111].Data[3].CultureInvariantString = FString(name)

def set_bigtoss_mode():
    #Greatly increase the knockback from enemy attacks and randomize the impulse angle
    enemy_attack_ranges = [
        range(302, 783),
        range(814, 835),
        range(848, 862)
    ]
    for index_range in enemy_attack_ranges:
        for index in index_range:
            entry = list(Data.datatable["PB_DT_DamageMaster"])[index]
            if "P000" in entry or "P000" in Data.datatable["PB_DT_DamageMaster"][entry]["GroupId"]:
                continue
            if "FAMILIA" in entry or "FAMILIA" in Data.datatable["PB_DT_DamageMaster"][entry]["GroupId"]:
                continue
            if entry.split("_")[-1] == "BRV" or Data.datatable["PB_DT_DamageMaster"][entry]["GroupId"].split("_")[-1] == "BRV":
                continue
            if entry == "N2008_BackStep":
                continue
            Data.datatable["PB_DT_DamageMaster"][entry]["KnockBackDistance"] += 20.0
            Data.datatable["PB_DT_DamageMaster"][entry]["KnockBackLimitAngleMin"] = float(random.randint(-180, 180))
            Data.datatable["PB_DT_DamageMaster"][entry]["KnockBackLimitAngleMax"] = float(random.randint(-180, 180))

def write_log(filename, log):
    write_json(f"Spoiler\\{filename}.json", log)

def write_files():
    #Dump all uasset objects to files
    for file in Data.game_data:
        extension = ".umap" if Data.file_to_type[file] == FileType.Level else ".uasset"
        Data.game_data[file].Write(MOD_DIR + "\\" + Data.file_to_path[file] + "\\" + file.split("(")[0] + extension)

def debug_output_datatables():
    if os.path.isdir("Debug"):
        shutil.rmtree("Debug")
    os.makedirs("Debug")
    for file, value in Data.datatable.items():
        write_json(f"Debug\\{file}.json", value)

def remove_unchanged_files():
    #Since uasset objects cannot be compared successfully we need to compare the files after they've been written
    #That way unchanged files get removed from the pak
    for file, path in Data.file_to_path.items():
        remove = True
        for sub_file in os.listdir(f"{MOD_DIR}\\{path}"):
            name, _ = os.path.splitext(sub_file)
            if name == file:
                if not filecmp.cmp(f"{MOD_DIR}\\{path}\\{sub_file}", f"{ASSETS_DIR}\\{path}\\{sub_file}", shallow=False):
                    remove = False
                    break
        if remove:
            for sub_file in os.listdir(f"{MOD_DIR}\\{path}"):
                name, _ = os.path.splitext(sub_file)
                if name == file:
                    os.remove(f"{MOD_DIR}\\{path}\\{sub_file}")

def append_string_entry(file, entry, text):
    #Make sure the text never exceeds two lines
    prefix = " " if "\r\n" in Data.stringtable[file][entry] or len(Data.stringtable[file][entry]) > 60 or entry in STRING_ENTRY_EXCEPTIONS else "\r\n"
    Data.stringtable[file][entry] += prefix + text

def get_available_gimmick_flag():
    index = -1
    while abs(index) <= len(Data.datatable["PB_DT_GimmickFlagMaster"]):
        dict = Data.datatable["PB_DT_GimmickFlagMaster"][list(Data.datatable["PB_DT_GimmickFlagMaster"])[index]]
        if "Id" in dict:
            return dict["Id"] + 1
        index -= 1
    return 1
