from randomizer import Manager
from randomizer import Item
from randomizer import Shop
from randomizer import Library
from randomizer import Shard
from randomizer import Equipment
from randomizer import Enemy
from randomizer import Room
from randomizer import Sound
from randomizer import Bloodless
from randomizer import Graphic

from randomizer.DLCType import DLCType
from randomizer.Constants import MOD_DIR
from randomizer.Data import Data
from configuration import Config
from configuration import ConfigSections
from .Signaller import Signaller

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QProgressDialog

import os
import shutil
import glob
import random
import traceback

_CHEATS = {
    "BIGTOSS": Manager.set_bigtoss_mode
}

class Generate(QThread):
    def __init__(self, config : Config, progress_bar : QProgressDialog, selected_seed : str, selected_map, starting_items, owned_dlc):
        QThread.__init__(self)
        self.config = config
        self.signaller = Signaller()
        self.progress_bar = progress_bar
        self.selected_seed = selected_seed
        self.selected_map = selected_map
        self.starting_items = starting_items
        self.owned_dlc = owned_dlc
    
    def run(self):
        try:
            self.process()
        except Exception:
            self.signaller.error.emit(traceback.format_exc())

    def process(self):
        current = 0
        self.signaller.progress.emit(current)
        
        #Check DLCs
        
        if not DLCType.IGA in self.owned_dlc:
            for file in list(Data.file_to_path):
                if "DLC_0002" in Data.file_to_path[file]:
                    del Data.file_to_path[file]
                    del Data.file_to_type[file]
        
        #Mod directory
        
        if os.path.isdir(MOD_DIR):
            shutil.rmtree(MOD_DIR)
        for directory in list(Data.file_to_path.values()):
            if not os.path.isdir(f"{MOD_DIR}\\{directory}"):
                os.makedirs(f"{MOD_DIR}\\{directory}")
        if not os.path.isdir(f"{MOD_DIR}\\Core\\UI\\Dialog\\Data\\LipSync"):
            os.makedirs(f"{MOD_DIR}\\Core\\UI\\Dialog\\Data\\LipSync")
        
        #Log directory
        
        if os.path.isdir("Spoiler"):
            shutil.rmtree("Spoiler")
        os.makedirs("Spoiler")
        
        #Open files
        
        self.progress_bar.setLabelText("Loading data...")
        
        Data.reload_data()
        
        current += 1
        self.signaller.progress.emit(current)
        
        #Simplify data
        
        self.progress_bar.setLabelText("Processing data...")
        
        Data.table_complex_to_simple()
        #Manager.debug_output_datatables()
        current += 1
        self.signaller.progress.emit(current)
        
        self.progress_bar.setLabelText("Editing data...")
        
        #Init classes
        
        Item.init()
        Library.init()
        Enemy.init()
        Room.init()
        Bloodless.init()
        miriam_color = None
        zangetsu_color = None
        
        #Apply parameters
        
        Item.set_logic_complexity(self.config.getint(ConfigSections.item.overworld_pool_complexity))
        Item.set_shop_event_weight(self.config.getint(ConfigSections.item.shop_pool_weight))
        Shop.set_shop_price_weight(self.config.getint(ConfigSections.shop.item_values_weight))
        Library.set_requirement_weight(self.config.getint(ConfigSections.library.map_requirements_weight))
        Shard.set_shard_power_weight(self.config.getint(ConfigSections.shard.shard_power_and_cost_weight))
        Equipment.set_global_stat_weight(self.config.getint(ConfigSections.equipment.global_gear_stats_weight))
        Enemy.set_enemy_level_weight(self.config.getint(ConfigSections.enemy.enemy_levels_weight))
        Enemy.set_boss_level_weight(self.config.getint(ConfigSections.enemy.boss_levels_weight))
        Enemy.set_enemy_tolerance_weight(self.config.getint(ConfigSections.enemy.enemy_tolerances_weight))
        Enemy.set_boss_tolerance_weight(self.config.getint(ConfigSections.enemy.boss_tolerances_weight))
        Sound.set_voice_language(self.config.getint(ConfigSections.sound.dialogues_language))
        Bloodless.set_logic_complexity(self.config.getint(ConfigSections.extra.bloodless_candles_complexity))
        
        #Map
        
        random.seed(self.selected_seed)
        if not self.selected_map and self.config.getboolean(ConfigSections.map.room_layout):
            self.selected_map = random.choice(glob.glob("MapEdit\\Custom\\*.json")) if glob.glob("MapEdit\\Custom\\*.json") else ""
        Manager.load_map(self.selected_map)
        Room.get_map_info()
        Room.update_any_map()
        
        #Apply tweaks
        
        Manager.apply_default_tweaks()
        Shard.set_default_shard_power()
        Enemy.get_original_enemy_stats()
        
        #Apply cheats
        
        if type(self.selected_seed) is str:
            for code in _CHEATS:
                if code in self.selected_seed:
                    random.seed(self.selected_seed)
                    _CHEATS[code]()
        
        #Datatables
        
        has_risky_option = (self.config.getboolean(ConfigSections.enemy.enemy_levels) or self.config.getboolean(ConfigSections.enemy.boss_levels)) and not self.config.getboolean(ConfigSections.special_mode.custom_ng)
        
        if self.selected_map:
            Room.update_custom_map()
            Enemy.rebalance_enemies_to_map()
        
        if not self.config.getboolean(ConfigSections.difficulty.normal):
            Item.set_hard_mode()
        
        if not DLCType.IGA in self.owned_dlc:
            Item.del_iga_dlc()
        elif not self.config.getboolean(ConfigSections.misc.ignore_dlc):
            Item.add_iga_dlc()
        
        if not DLCType.Shantae in self.owned_dlc:
            Item.del_shantae_dlc()
        elif not self.config.getboolean(ConfigSections.misc.ignore_dlc):
            Item.add_shantae_dlc()
        
        if not DLCType.Succubus in self.owned_dlc:
            Item.del_succubus_dlc()
        elif not self.config.getboolean(ConfigSections.misc.ignore_dlc):
            Item.add_succubus_dlc()
        
        if not DLCType.MagicGirl in self.owned_dlc:
            Item.del_magicgirl_dlc()
        elif not self.config.getboolean(ConfigSections.misc.ignore_dlc):
            Item.add_magicgirl_dlc()
        
        if not DLCType.Japanese in self.owned_dlc:
            Item.del_japanese_dlc()
        elif not self.config.getboolean(ConfigSections.misc.ignore_dlc):
            Item.add_japanese_dlc()
        
        if self.config.getboolean(ConfigSections.enemy.enemy_locations):
            random.seed(self.selected_seed)
            Enemy.randomize_enemy_locations()
            Enemy.update_enemy_locations()
            Enemy.restore_enemy_scaling()
        
        Item.fill_enemy_to_room()
        
        if self.config.getboolean(ConfigSections.item.remove_infinites):
            Item.remove_infinite_items()
        
        for item in self.starting_items:
            if self.config.getboolean(ConfigSections.item.overworld_pool) and item == "Shortcut":
                continue
            Item.add_starting_item(item)
        
        if self.config.getboolean(ConfigSections.item.overworld_pool):
            random.seed(self.selected_seed)
            Item.unlock_all_quests()
            Item.add_all_hair_apparents_in_shop()
            Item.remove_all_keys_from_shop()
            Item.disable_shard_crafting()
            Item.add_starting_item("Shortcut")
            Item.randomize_overworld_keys()
            Item.randomize_overworld_items()
            Item.randomize_overworld_shards()
            Manager.set_randomizer_events()
        
        if has_risky_option:
            Item.add_pre_vepar_waystone()
        
        if self.config.getboolean(ConfigSections.item.overworld_pool):
            random.seed(self.selected_seed)
            Item.randomize_classic_mode_drops()
        
        if self.config.getboolean(ConfigSections.item.overworld_pool) or self.config.getboolean(ConfigSections.enemy.enemy_locations) or self.selected_map:
            Manager.remove_fire_shard_requirement()
        
        if self.config.getboolean(ConfigSections.extra.bloodless_candles):
            random.seed(self.selected_seed)
            Bloodless.randomize_bloodless_candles()
            if self.selected_map:
                Bloodless.remove_gremory_cutscene()
        
        if self.config.getboolean(ConfigSections.item.quest_pool):
            random.seed(self.selected_seed)
            Item.randomize_quest_rewards()
        
        if self.config.getboolean(ConfigSections.item.shop_pool):
            random.seed(self.selected_seed)
            Item.randomize_shop_items()
        
        if self.config.getboolean(ConfigSections.item.quest_requirements):
            random.seed(self.selected_seed)
            Item.randomize_quest_requirements()
            Item.update_catering_quest_info()
        
        if self.selected_map:
            Item.replace_silver_bromide()
            Item.remove_enemy_quest_icons()
        
        if self.config.getboolean(ConfigSections.shop.item_values):
            random.seed(self.selected_seed)
            Shop.randomize_shop_prices(self.config.getboolean(ConfigSections.shop.scale_selling_price_with_cost))
        
        if self.config.getboolean(ConfigSections.library.map_requirements):
            random.seed(self.selected_seed)
            Library.randomize_library_requirements()
        
        if self.config.getboolean(ConfigSections.library.tome_appearance):
            random.seed(self.selected_seed)
            Library.randomize_tome_appearance()
        
        if self.config.getboolean(ConfigSections.shard.randomize_shard_power_and_cost):
            random.seed(self.selected_seed)
            Shard.randomize_shard_power(self.config.getboolean(ConfigSections.shard.scale_cost_with_power))
        
        if self.config.getboolean(ConfigSections.equipment.global_gear_stats):
            random.seed(self.selected_seed)
            Equipment.randomize_equipment_stats()
            Equipment.randomize_weapon_power()
        
        if self.config.getboolean(ConfigSections.equipment.chest_gear_stats):
            random.seed(self.selected_seed)
            Equipment.randomize_cheat_equipment_stats()
            Equipment.randomize_cheat_weapon_power()
        
        if self.config.getboolean(ConfigSections.enemy.enemy_levels):
            random.seed(self.selected_seed)
            Enemy.randomize_enemy_levels()
        
        if self.config.getboolean(ConfigSections.enemy.boss_levels):
            random.seed(self.selected_seed)
            Enemy.randomize_boss_levels()
        
        if has_risky_option:
            Enemy.increase_starting_stats()
            #Bloodless.increase_starting_stats()
        
        if self.config.getboolean(ConfigSections.enemy.enemy_tolerances):
            random.seed(self.selected_seed)
            Enemy.randomize_enemy_tolerances()
        
        if self.config.getboolean(ConfigSections.enemy.boss_tolerances):
            random.seed(self.selected_seed)
            Enemy.randomize_boss_tolerances()
        
        if self.config.getboolean(ConfigSections.graphics.outfit_color):
            miriam_outfit_list = self.config.get(ConfigSections.outfit.miriam_outfits).split(",")
            random.seed(self.selected_seed)
            miriam_color = random.choice(miriam_outfit_list) if miriam_outfit_list else None
            zangetsu_outfit_list = self.config.get(ConfigSections.outfit.zangetsu_outfits).split(",")
            random.seed(self.selected_seed)
            zangetsu_color = random.choice(zangetsu_outfit_list) if zangetsu_outfit_list else None
            if miriam_color:
                Graphic.update_default_outfit_hsv(miriam_color)
        
        if self.config.getboolean(ConfigSections.graphics.backer_portraits):
            random.seed(self.selected_seed)
            Graphic.randomize_backer_portraits()
        
        if self.config.getboolean(ConfigSections.sound.dialogues):
            random.seed(self.selected_seed)
            Sound.randomize_dialogues()
        
        if self.config.getboolean(ConfigSections.sound.music):
            random.seed(self.selected_seed)
            Sound.randomize_music()
        
        #Change some in-game properties based on the difficulty chosen
        if self.config.getboolean(ConfigSections.difficulty.normal):
            Manager.set_single_difficulty("Normal")
            Enemy.update_brv_damage("Normal")
        elif self.config.getboolean(ConfigSections.difficulty.hard):
            Manager.set_single_difficulty("Hard")
            Manager.set_default_entry_name("NIGHTMARE")
            Enemy.add_hard_enemy_patterns()
            Enemy.update_brv_boss_speed("Hard")
            Enemy.update_brv_damage("Hard")
        elif self.config.getboolean(ConfigSections.difficulty.nightmare):
            Manager.set_single_difficulty("Nightmare")
            Manager.set_default_entry_name("NIGHTMARE")
            Enemy.add_hard_enemy_patterns()
            Enemy.update_brv_boss_speed("Nightmare")
            Enemy.update_brv_damage("Nightmare")
            Shard.rescale_level_based_shards()
        
        #Set custom NG+ levels
        if self.config.getboolean(ConfigSections.special_mode.custom_ng):
            Enemy.set_custom_enemy_level(self.config.getint(ConfigSections.special_mode.custom_ng_level))
        
        #Change some extra properties for Progressive Zangetsu mode
        if self.config.getboolean(ConfigSections.special_mode.progressive_z):
            if self.config.getboolean(ConfigSections.difficulty.nightmare):
                Manager.set_single_difficulty("Hard")
                Manager.Data.stringtable["PBSystemStringTable"]["SYS_SEN_Difficulty_Hard"] = "Nightmare"
                Enemy.set_zangetsu_enemy_exp()
                Enemy.set_zangetsu_nightmare_damage()
            Enemy.reset_zangetsu_starting_stats()
            Enemy.set_zangetsu_progressive_level(self.config.getboolean(ConfigSections.difficulty.nightmare))
            Equipment.reset_zangetsu_black_belt()
        
        #Update some things to reflect previous changes
        Item.ensure_drop_ids_unique()
        Room.update_container_types()
        Item.update_shard_candles()
        Bloodless.update_shard_candles()
        Shard.update_special_properties()
        Equipment.update_special_properties()
        Enemy.update_special_properties()
        Graphic.update_boss_crystal_color()
        Manager.update_item_descriptions()
        Room.update_map_connections()
        Room.update_map_doors()
        if self.selected_map:
            Room.update_map_indicators()
        
        #Display game version, mod version and seed on the title screen
        Manager.show_mod_stats(self.selected_seed, self.config.get(ConfigSections.misc.version))
        
        #Write the spoiler logs
        if self.config.getboolean(ConfigSections.extra.bloodless_candles):
            Manager.set_default_entry_name("BLOODLESS")
            Manager.write_log("KeyLocation", Bloodless.create_log(self.selected_seed, self.selected_map))
        elif self.config.getboolean(ConfigSections.item.overworld_pool):
            Manager.write_log("KeyLocation", Item.create_log(self.selected_seed, self.selected_map))
        
        if self.config.getboolean(ConfigSections.library.map_requirements) or self.config.getboolean(ConfigSections.library.tome_appearance):
            Manager.write_log("LibraryTomes", Library.create_log())
        
        if has_risky_option or self.config.getboolean(ConfigSections.enemy.enemy_locations) or self.config.getboolean(ConfigSections.enemy.enemy_tolerances) or self.config.getboolean(ConfigSections.enemy.boss_tolerances):
            Manager.write_log("EnemyProperties", Enemy.create_log())
        
        #Add and import any mesh files found in the mesh directory
        for directory in os.listdir("Data\\Mesh"):
            file_name, extension = os.path.splitext(directory)
            if extension == ".uasset":
                Graphic.import_mesh(file_name)
        
        #Add new armor references defined in the json
        for item in Data.constant["ArmorReference"]:
            Equipment.add_armor_reference(item)
        
        #Add and import any music files found in the music directory
        for directory in os.listdir("Data\\Music"):
            file_name = os.path.splitext(directory)[0]
            Sound.add_music_file(file_name)
        
        current += 1
        self.signaller.progress.emit(current)
        
        #Convert data
        
        self.progress_bar.setLabelText("Converting data...")
        
        Data.table_simple_to_complex()
        Data.update_datatable_order()
        current += 1
        self.signaller.progress.emit(current)
        
        #Write lip sync
        
        self.progress_bar.setLabelText("Writing lip sync...")
        
        Sound.update_lip_movement()
        current += 1
        self.signaller.progress.emit(current)
        
        #Write files
        
        self.progress_bar.setLabelText("Writing files...")
        
        Manager.write_files()
        
        #Edit the minimap outline to give an easy visual cue to tell if someone is using the mod or not and what difficulty they're on
        #This is especially useful on twitch as this difference is even visible from stream previews
        if self.config.getboolean(ConfigSections.difficulty.normal):
            shutil.copyfile("Data\\Texture\\Difficulty\\Normal\\WindowMinimap02.dds", "Data\\Texture\\WindowMinimap02.dds")
        elif self.config.getboolean(ConfigSections.difficulty.hard):
            shutil.copyfile("Data\\Texture\\Difficulty\\Hard\\WindowMinimap02.dds", "Data\\Texture\\WindowMinimap02.dds")
        elif self.config.getboolean(ConfigSections.difficulty.nightmare):
            shutil.copyfile("Data\\Texture\\Difficulty\\Nightmare\\WindowMinimap02.dds", "Data\\Texture\\WindowMinimap02.dds")
        Graphic.import_texture("WindowMinimap02")
        os.remove("Data\\Texture\\WindowMinimap02.dds")
        
        #Edit the file that contains all the icons in the game to give 8 bit weapons unique icons per rank
        #Otherwise it is almost impossible to tell which tier the weapon you're looking at actually is
        Graphic.import_texture("icon")
        
        #The textures used in the 8 Bit Nightmare area have inconsistent formats and mostly use block compression which butchers the pixel arts completely
        #An easy fix so include it here
        Graphic.import_texture("m51_EBT_BG")
        Graphic.import_texture("m51_EBT_BG_01")
        Graphic.import_texture("m51_EBT_Block")
        Graphic.import_texture("m51_EBT_Block_00")
        Graphic.import_texture("m51_EBT_Block_01")
        Graphic.import_texture("m51_EBT_Door")
        
        #Give the new dullahammer a unique color scheme
        Graphic.import_texture("T_N3127_Body_Color")
        Graphic.import_texture("T_N3127_Uni_Color")
        
        #Change the timestop shard in classic mode to have the same color as standstill
        Graphic.import_texture("time_shard_diffuse")
        Graphic.import_texture("ui_icon_pickup_timeShard")
        Graphic.import_texture("ui_icon_results_timeShard")
        #Also change the dagger icon to match the model
        Graphic.import_texture("ui_icon_pickup_dagger")
        Graphic.import_texture("ui_icon_results_dagger")
        
        #Most map icons have fixed positions on the canvas and will not adapt to the position of the rooms
        #Might be possible to edit them via a blueprint but that's not worth it so remove them if custom map is chosen
        if self.selected_map:
            Graphic.import_texture("icon_map_journey_")
            Graphic.import_texture("Map_Icon_Keyperson")
            Graphic.import_texture("Map_Icon_RootBox")
            Graphic.import_texture("Map_StartingPoint")
        if self.selected_map or self.config.getboolean(ConfigSections.item.overworld_pool):
            Graphic.import_texture("icon_8bitCrown")
        
        #Import chosen hues for Miriam and Zangetsu
        #While it is technically not necessary to first copy the textures out of the chosen folder we do it so that the random hue does not show up on the terminal
        if miriam_color:
            for texture in os.listdir(f"Data\\Texture\\Miriam\\{miriam_color}"):
                shutil.copyfile(f"Data\\Texture\\Miriam\\{miriam_color}\\{texture}", f"Data\\Texture\\{texture}")
            
            Graphic.import_texture("Face_Miriam")
            Graphic.import_texture("T_Pl01_Cloth_Bace")
            Graphic.import_texture("T_Body01_01_Color")
            
            for texture in os.listdir(f"Data\\Texture\\Miriam\\{miriam_color}"):
                os.remove(f"Data\\Texture\\{texture}")
        
        if zangetsu_color:
            for texture in os.listdir(f"Data\\Texture\\Zangetsu\\{zangetsu_color}"):
                shutil.copyfile(f"Data\\Texture\\Zangetsu\\{zangetsu_color}\\{texture}", f"Data\\Texture\\{texture}")
            
            Graphic.import_texture("Face_Zangetsu")
            Graphic.import_texture("T_N1011_body_color")
            Graphic.import_texture("T_N1011_face_color")
            Graphic.import_texture("T_N1011_weapon_color")
            Graphic.import_texture("T_Tknife05_Base")
            
            for texture in os.listdir(f"Data\\Texture\\Zangetsu\\{zangetsu_color}"):
                os.remove(f"Data\\Texture\\{texture}")
        
        Graphic.update_backer_portraits()
        
        #Clean up the mod folder
        
        Manager.remove_unchanged_files()
        current += 1
        self.signaller.progress.emit(current)
        
        #UnrealPak
        
        self.progress_bar.setLabelText("Packing files...")
        
        with open("Tools\\UnrealPak\\filelist.txt", "w") as file_writer:
            file_writer.write("\"Mod\\*.*\" \"..\\..\\..\\*.*\" \n")
        
        root = os.getcwd()
        os.chdir("Tools\\UnrealPak")
        os.system("cmd /c UnrealPak.exe \"Randomizer.pak\" -create=filelist.txt -compress")
        os.chdir(root)
        
        #Reset
        
        if os.path.isdir("Tools\\UE4 DDS Tools\\src\\__pycache__"):
            shutil.rmtree("Tools\\UE4 DDS Tools\\src\\__pycache__")
        shutil.rmtree("Tools\\UnrealPak\\Mod")
        os.remove("Tools\\UnrealPak\\filelist.txt")
        
        #Move
        
        if not os.path.isdir(self.config.get(ConfigSections.misc.game_path) + "\\BloodstainedRotN\\Content\\Paks\\~mods"):
            os.makedirs(self.config.get(ConfigSections.misc.game_path) + "\\BloodstainedRotN\\Content\\Paks\\~mods")
        shutil.move("Tools\\UnrealPak\\Randomizer.pak", self.config.get(ConfigSections.misc.game_path) + "\\BloodstainedRotN\\Content\\Paks\\~mods\\Randomizer.pak")
        
        #Copy UE4SS
        
        exe_directory = self.config.get(ConfigSections.misc.game_path) + "\\BloodstainedRotN\\Binaries\\Win64"
        if not os.path.isfile(f"{exe_directory}\\UE4SS.dll"):
            for item in os.listdir("Tools\\UE4SS"):
                if os.path.isfile(f"Tools\\UE4SS\\{item}"):
                    shutil.copyfile(f"Tools\\UE4SS\\{item}", f"{exe_directory}\\{item}")
                if os.path.isdir(f"Tools\\UE4SS\\{item}"):
                    shutil.copytree(f"Tools\\UE4SS\\{item}", f"{exe_directory}\\{item}", dirs_exist_ok=True)
        for directory in os.listdir("Data\\UE4SS"):
            shutil.copytree(f"Data\\UE4SS\\{directory}", f"{exe_directory}\\Mods\\{directory}", dirs_exist_ok=True)
            if not os.path.isfile(f"{exe_directory}\\Mods\\{directory}\\enabled.txt"): 
                open(f"{exe_directory}\\Mods\\{directory}\\enabled.txt", "w").close()
        
        #User randomly chosen mod
        
        if os.path.isdir("Data\\Mod"):
            for directory in os.listdir("Data\\Mod"):
                chosen_mod = random.choice(glob.glob(f"Data\\Mod\\{directory}\\*.pak"))
                shutil.copyfile(chosen_mod, self.config.get(ConfigSections.misc.game_path) + f"\\BloodstainedRotN\\Content\\Paks\\~mods\\{directory}.pak")
        
        current += 1
        self.signaller.progress.emit(current)
        
        self.progress_bar.setLabelText("Done")
        self.signaller.finished.emit()
