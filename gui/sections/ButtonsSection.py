from __future__ import annotations

import glob
import os
import random
import vdf

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDialog

from configuration import Config
from configuration import ConfigSections
from randomizer import DLCType
from randomizer.Data import *
from randomizer.Constants import *
from randomizer import Data
from randomizer import Bloodless
from randomizer import Enemy
from randomizer import Item
from randomizer import Manager
from randomizer import Room
from randomizer import Utility
from ..dialogs import ArchipelagoDialog
from ..dialogs import SettingsDialog
from ..widgets import MessageBox
from ..widgets import ProgressBar
from ..widgets import CreditsBox
from ..threads import Generate
from ..threads import Import


class ButtonsSection(QWidget):
    def __init__(self, parent, size_multiplier : float, config : Config) -> None:
        super().__init__(parent)
        self.config = config
        self.size_multiplier = size_multiplier

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(int(self.size_multiplier*10))
        self.setLayout(layout)

        #Seed
        
        self.seed_window_layout = QVBoxLayout()
        seed_window_top = QHBoxLayout()
        self.seed_window_layout.addLayout(seed_window_top)
        seed_window_center = QHBoxLayout()
        self.seed_window_layout.addLayout(seed_window_center)
        seed_window_bottom = QHBoxLayout()
        self.seed_window_layout.addLayout(seed_window_bottom)
        
        self.seed_field = QLineEdit(self.config.get(ConfigSections.misc.seed))
        self.seed_field.setMaxLength(30)
        self.seed_field.textChanged.connect(self.seed_field_changed)
        seed_window_top.addWidget(self.seed_field)
        
        seed_new_button = QPushButton("New Seed")
        seed_new_button.clicked.connect(self.seed_new_button_clicked)
        seed_window_center.addWidget(seed_new_button)
        
        seed_test_button = QPushButton("Test Seed")
        seed_test_button.clicked.connect(self.seed_test_button_clicked)
        seed_window_center.addWidget(seed_test_button)
        
        seed_confirm_button = QPushButton("Confirm")
        seed_confirm_button.clicked.connect(self.seed_confirm_button_clicked)
        seed_window_center.addWidget(seed_confirm_button)

        self.dlc_check_box = QCheckBox("Ignore DLC")
        self.dlc_check_box.setToolTip("Make it so that any DLC that may be installed in\nyour game will be ignored by the randomization.")
        self.dlc_check_box.stateChanged.connect(self.dlc_check_box_changed)
        seed_window_bottom.addWidget(self.dlc_check_box)

        #Buttons
        
        setting_button = QPushButton("Settings")
        setting_button.setToolTip("Interface settings.")
        setting_button.setShortcut(Qt.Key.Key_S)
        setting_button.clicked.connect(self.setting_button_clicked)
        layout.addWidget(setting_button, 0, 0, 1, 1)
        
        import_asset_button = QPushButton("Import Assets")
        import_asset_button.setToolTip("Reimport and convert all base game assets used in this mod.\nUseful if the game updates or if one asset gets corrupted on\naccident.")
        import_asset_button.clicked.connect(self.import_asset_button_clicked)
        layout.addWidget(import_asset_button, 0, 1, 1, 1)
        
        archipelago_button = QPushButton("Coming Soon")
        archipelago_button.setToolTip("™")
        archipelago_button.clicked.connect(self.archipelago_button_clicked)
        layout.addWidget(archipelago_button, 0, 2, 1, 1)
        
        credit_button = QPushButton("Credits")
        credit_button.setToolTip("The people involved with this mod.")
        credit_button.clicked.connect(self.credit_button_clicked)
        layout.addWidget(credit_button, 0, 3, 1, 1)

        generate_button = QPushButton("Generate")
        generate_button.setToolTip("Generate the mod with the current settings.")
        generate_button.clicked.connect(self.generate_button_clicked)
        layout.addWidget(generate_button, 1, 0, 1, 4)

        # Config
        self.dlc_check_box.setChecked(self.config.getboolean(ConfigSections.misc.ignore_dlc))

    def setting_button_clicked(self):
        setting_window = SettingsDialog(self.parentWidget(), self.config, self.size_multiplier)
        setting_window.exec()
    
    
    def import_asset_button_clicked(self):
        #Check if path is valid
        
        if not self.is_game_path_valid():
            MessageBox.error(self, "Game path invalid, input the path to your game's data\n(...\\steamapps\\common\\Bloodstained Ritual of the Night).")
            return
        
        self.import_assets(list(Data.file_to_path), self.import_finished)

    def is_game_path_valid(self):
        return os.path.isdir(self.config.get(ConfigSections.misc.game_path)) and os.path.isfile(self.config.get(ConfigSections.misc.game_path) + "\\BloodstainedRotN.exe")
    
    def generate_button_clicked(self):
        #Check if path is valid
        
        if not self.is_game_path_valid():
            MessageBox.error(self.parentWidget(), "Game path invalid, input the path to your game's data\n(...\\steamapps\\common\\Bloodstained Ritual of the Night).")
            return
        
        #Check if starting items are valid
        
        self.starting_items = []
        for item in self.config.get(ConfigSections.start_with.items).split(","):
            if not item:
                continue
            simple_name = Utility.simplify_item_name(item)
            if not simple_name in Data.start_item_translation:
                MessageBox.error(self, "Starting item name invalid.")
                return
            item_name = Data.start_item_translation[simple_name]
            if "Skilled" in item_name:
                self.starting_items.append(item_name.replace("Skilled", ""))
            self.starting_items.append(item_name)
        self.starting_items = list(dict.fromkeys(self.starting_items))
        
        #Check DLC
        
        self.owned_dlc = self.get_dlc_info()
        
        #Prompt seed options
        
        if self.has_rando_options():
            self.seed_box = QDialog(self.parentWidget())
            self.seed_box.setLayout(self.seed_window_layout)
            self.seed_box.setWindowTitle("Seed")
            self.seed_box.exec()
        else:
            self.pre_generate()
    
    def has_rando_options(self):
        if self.config.getboolean(ConfigSections.item.overworld_pool):
            return True
        if self.config.getboolean(ConfigSections.item.shop_pool):
            return True
        if self.config.getboolean(ConfigSections.item.quest_pool):
            return True
        if self.config.getboolean(ConfigSections.item.quest_requirements):
            return True
        if self.config.getboolean(ConfigSections.shop.item_values):
            return True
        if self.config.getboolean(ConfigSections.library.map_requirements):
            return True
        if self.config.getboolean(ConfigSections.library.tome_appearance):
            return True
        if self.config.getboolean(ConfigSections.shard.randomize_shard_power_and_cost):
            return True
        if self.config.getboolean(ConfigSections.equipment.global_gear_stats):
            return True
        if self.config.getboolean(ConfigSections.equipment.chest_gear_stats):
            return True
        if self.config.getboolean(ConfigSections.enemy.enemy_locations):
            return True
        if self.config.getboolean(ConfigSections.enemy.enemy_levels):
            return True
        if self.config.getboolean(ConfigSections.enemy.boss_levels):
            return True
        if self.config.getboolean(ConfigSections.enemy.enemy_tolerances):
            return True
        if self.config.getboolean(ConfigSections.enemy.boss_tolerances):
            return True
        if self.config.getboolean(ConfigSections.map.room_layout):
            if not self.config.get(ConfigSections.map.selected_map):
                return True
        if self.config.getboolean(ConfigSections.graphics.outfit_color):
            if self.config.get(ConfigSections.outfit.miriam_outfits):
                return True
            if self.config.get(ConfigSections.outfit.zangetsu_outfits):
                return True
        if self.config.getboolean(ConfigSections.graphics.backer_portraits):
            return True
        if self.config.getboolean(ConfigSections.sound.dialogues):
            return True
        if self.config.getboolean(ConfigSections.sound.music):
            return True
        if self.config.getboolean(ConfigSections.extra.bloodless_candles):
            return True
        return False
    
    def pre_generate(self):
        #Check if every asset is already cached
        if os.path.isdir(ASSETS_DIR): 
            cached_assets = []
            for root, dirs, files in os.walk(ASSETS_DIR):
                for file in files:
                    name = os.path.splitext(file)[0]
                    cached_assets.append(name)
            cached_assets = list(dict.fromkeys(cached_assets))
            asset_list = []
            for file in Data.file_to_path:
                if not file in cached_assets:
                    asset_list.append(file)
        else:
            asset_list = list(Data.file_to_path)
        
        self.import_assets(asset_list, self.generate_pak) if asset_list else self.generate_pak()
    
    def import_assets(self, asset_list, finished):
        self.parentWidget().setEnabled(False)
        QApplication.processEvents()
        
        self.worker = Import(self.config, asset_list)
        self.progress_bar = ProgressBar(0, len(asset_list), self.parentWidget(), "Status")
        self.progress_bar.connect_to(self.worker.signaller)
        self.worker.signaller.finished.connect(finished)
        self.worker.start()

    def import_finished(self):
        self.parentWidget().setEnabled(True)
    
    def generate_pak(self):
        self.parentWidget().setEnabled(False)
        QApplication.processEvents()
        
        self.selected_seed = self.config.get(ConfigSections.misc.seed)
        self.selected_map = self.config.get(ConfigSections.map.selected_map) if self.config.getboolean(ConfigSections.map.room_layout) else ""
        self.progress_bar = ProgressBar(0, 7, self.parentWidget(), "Status")
        self.worker = Generate(self.config, self.selected_seed, self.selected_map, self.starting_items, self.owned_dlc)
        self.progress_bar.connect_to(self.worker.signaller)

        self.worker.signaller.finished.connect(self.generate_finished)
        self.worker.start()
    
    def generate_finished(self):
        self.progress_bar.close()
        self.parentWidget().setEnabled(True)
        MessageBox.success(self, "Pak file generated!")


    def seed_field_changed(self, text : str):
        if " " in text:
            self.seed_field.setText(text.replace(" ", ""))
        else:
            self.config.set(ConfigSections.misc.seed, text)

    def seed_new_button_clicked(self):
        self.seed_field.setText(str(random.randint(1000000000, 9999999999)))
    
    def seed_test_button_clicked(self):
        #Check seed
        if not self.config.get(ConfigSections.misc.seed):
            return
        
        self.selected_seed = self.config.get(ConfigSections.misc.seed)
        self.selected_map = self.config.get(ConfigSections.map.selected_map) if self.config.getboolean(ConfigSections.map.room_layout) else ""
        
        #Start
        Data.reload_data()
        
        Item.init()
        Enemy.init()
        Room.init()
        Bloodless.init()
        
        Item.set_logic_complexity(self.config.getint(ConfigSections.item.overworld_pool_complexity))
        Bloodless.set_logic_complexity(self.config.getint(ConfigSections.extra.bloodless_candles_complexity))
        
        random.seed(self.selected_seed)
        if not self.selected_map and self.config.getboolean(ConfigSections.map.room_layout):
            self.selected_map = random.choice(glob.glob("MapEdit\\Custom\\*.json")) if glob.glob("MapEdit\\Custom\\*.json") else ""
        Manager.load_map(self.selected_map)
        Room.get_map_info()
        
        if not self.config.getboolean(ConfigSections.difficulty.normal):
            Item.set_hard_mode()
        
        if DLCType.IGA in self.owned_dlc and not self.config.getboolean(ConfigSections.misc.ignore_dlc):
            Item.add_iga_dlc()
        
        if self.config.getboolean(ConfigSections.enemy.enemy_locations):
            random.seed(self.selected_seed)
            Enemy.randomize_enemy_locations()
        
        Item.fill_enemy_to_room()
        
        if self.config.getboolean(ConfigSections.item.overworld_pool):
            random.seed(self.selected_seed)
            Item.key_logic()
        
        if self.config.getboolean(ConfigSections.extra.bloodless_candles):
            random.seed(self.selected_seed)
            Bloodless.randomize_bloodless_candles()
        
        text = "No keys to randomize"
        if self.config.getboolean(ConfigSections.extra.bloodless_candles):
            text = Bloodless.create_log_string(self.selected_seed, self.selected_map)
        elif self.config.getboolean(ConfigSections.item.overworld_pool):
            text = Item.create_log_string(self.selected_seed, self.selected_map, Enemy.enemy_replacement_invert)
        MessageBox.success(self.parentWidget(), text, "Seed Test")

    
    def seed_confirm_button_clicked(self):
        if not self.config.get(ConfigSections.misc.seed):
            return
        self.seed_box.close()
        self.pre_generate()
    
    def dlc_check_box_changed(self):
        checked = self.dlc_check_box.isChecked()
        self.config.set(ConfigSections.misc.ignore_dlc, str(checked).lower())
    


    
    def get_dlc_info(self):
        #Shantae is on by default
        dlc_list = [DLCType.Shantae]
        #Steam
        if "steamapps" in self.config.get(ConfigSections.misc.game_path):
            steam_path = os.path.abspath(os.path.join(self.config.get(ConfigSections.misc.game_path), "../../.."))

            #Override the Steam path if the game path is on another drive
            library_config_path = f"{steam_path}\\libraryfolder.vdf"
            if os.path.isfile(library_config_path):
                with open(library_config_path, "r", encoding="utf8") as file_reader:
                    steam_exe_path = self.lowercase_vdf_dict(vdf.parse(file_reader))["libraryfolder"]["launcher"]
                    steam_path = os.path.split(steam_exe_path)[0]

            #Get user config
            user_config_path = f"{steam_path}\\config\\loginusers.vdf"
            if not os.path.isfile(user_config_path):
                self.dlc_failure()
                return dlc_list
            with open(f"{steam_path}\\config\\loginusers.vdf", "r", encoding="utf8") as file_reader:
                user_config = self.lowercase_vdf_dict(vdf.parse(file_reader))["users"]
            #Determine the Steam friend code based on their user ID
            steam_user = None
            for user in user_config:
                if user_config[user]["mostrecent"] == "1":
                    steam_user = int(user) - 76561197960265728
                    break
            #Get local config
            local_config_path = f"{steam_path}\\userdata\\{steam_user}\\config\\localconfig.vdf"
            if not os.path.isfile(local_config_path):
                self.dlc_failure()
                return dlc_list
            with open(local_config_path, "r", encoding="utf8") as file_reader:
                dlc_config = self.lowercase_vdf_dict(vdf.parse(file_reader))["userlocalconfigstore"]["apptickets"]
            #Check for DLC IDs in the config
            if "1041460" in dlc_config:
                dlc_list.append(DLCType.IGA)
            if "2380800" in dlc_config:
                dlc_list.append(DLCType.Succubus)
            if "2380801" in dlc_config:
                dlc_list.append(DLCType.MagicGirl)
            if "2380802" in dlc_config:
                dlc_list.append(DLCType.Japanese)
            return dlc_list
        #GOG
        if "GOG Games" in self.config.get(ConfigSections.misc.game_path):
            #List the DLC IDs in the game path
            dlc_id_list = []
            for file in glob.glob(self.config.get(ConfigSections.misc.game_path) + "\\*.hashdb"):
                file_name = os.path.split(os.path.splitext(file)[0])[-1]
                dlc_id_list.append(file_name.split("-")[-1])
            #Check for DLC IDs in the list
            if "2089941670" in dlc_id_list:
                dlc_list.append(DLCType.IGA)
            if "2021103941" in dlc_id_list:
                dlc_list.append(DLCType.Succubus)
            if "1841144430" in dlc_id_list:
                dlc_list.append(DLCType.MagicGirl)
            if "1255553972" in dlc_id_list:
                dlc_list.append(DLCType.Japanese)
            return dlc_list
        #Installation is unknown
        self.dlc_failure()
        return dlc_list
    
    def lowercase_vdf_dict(self, vdf_dict):
        new_dict = {}
        for key, value in vdf_dict.items():
            new_dict[key.lower()] = self.lowercase_vdf_dict(value) if type(value) is dict else value
        return new_dict
    
    def dlc_failure(self):
        MessageBox.warn(self, "Failed to retrieve DLC information from user installation. Proceeding without DLC.")
    
    def credit_button_clicked(self):
        self.credits = CreditsBox(self.parentWidget(), self.size_multiplier)
        self.credits.exec()
    
    def archipelago_button_clicked(self):
        self.archi_window = ArchipelagoDialog(self.parentWidget(), self.config, self.size_multiplier)
        self.archi_window.exec()
