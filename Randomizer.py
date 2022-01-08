#ImportSubclasses
import ClassBloodless
import ClassEnemy
import ClassEquipment
import ClassItem
import ClassLibrary
import ClassManagement
import ClassShard
import ClassSound
#ImportGUI
from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*
#ImportModules
import configparser
import sys
import os
import shutil
import random
import requests
import zipfile
import subprocess
import psutil
import glob

item_color = "#ff8080" 
shop_color = "#ffff80"
library_color = "#bf80ff"
shard_color = "#80ffff"
equip_color = "#80ff80"
enemy_color = "#80bfff"
map_color = "#ffbf80"
graphic_color = "#80ffbf"
sound_color = "#ff80ff"
extra_color = "#ff80bf"

checkbox_list = []
mod_directory = [
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Character\\N1011\\Texture",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Character\\P0000\\Texture\\Body",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\DataTable\\Character",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\DataTable\\Enemy",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\DataTable\\Item",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT01_SIP\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT02_VIL\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT03_ENT\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT04_GDN\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT05_SAN\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT06_KNG\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT07_LIB\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT08_TWR\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT10_BIG\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT11_UGD\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT12_SND\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT13_ARC\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT14_TAR\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT15_JPN\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT17_RVA\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT51_EBT\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT51_EBT\\Texture",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Environment\\ACT88_BKR\\Level",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Item\\Weapon\\Tknife\\Tknife05\\Texture",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\Sound\\bgm",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\System\\GameMode",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\UI\\HUD\\HUD_asset\\StateGauge\\0000",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\UI\\HUD\\HUD_asset\\StateGauge\\0001",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\UI\\K2C",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\UI\\Map\\Texture",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\Core\\UI\\UI_Pause\\Menu\\MainMenu\\Asset",
    "UnrealPak\\Mod\\BloodstainedRotN\\Content\\L10N\\en\\Core\\StringTable"
]

empty_preset = [
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False
]
trial_preset = [
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    False,
    False
]
race_preset = [
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False
]
meme_preset = [
    True,
    True,
    True,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    True,
    False,
    True,
    False,
    True,
    True,
    True,
    False,
    False
]
risk_preset = [
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False
]
blood_preset = [
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    True,
    False
]
    
map_num = len(glob.glob("MapEdit\\Custom\\*.json"))

datatable_files = [
    "PBMasterStringTable",
    "PBSystemStringTable",
    "PB_DT_AmmunitionMaster",
    "PB_DT_ArmorMaster",
    "PB_DT_ArtsCommandMaster",
    "PB_DT_BallisticMaster",
    "PB_DT_BloodlessAbilityData",
    "PB_DT_BookMaster",
    "PB_DT_BRVAttackDamage",
    "PB_DT_BRVCharacterParameters",
    "PB_DT_BulletMaster",
    "PB_DT_CharacterParameterMaster",
    "PB_DT_CharaUniqueParameterMaster",
    "PB_DT_CollisionMaster",
    "PB_DT_CoordinateParameter",
    "PB_DT_CraftMaster",
    "PB_DT_DamageMaster",
    "PB_DT_DropRateMaster",
    "PB_DT_EnchantParameterType",
    "PB_DT_ItemMaster",
    "PB_DT_RoomMaster",
    "PB_DT_ShardMaster",
    "PB_DT_SpecialEffectDefinitionMaster",
    "PB_DT_WeaponMaster",
    "~datatable"
]
ui_files = [
    "frameMiriam",
    "~ui"
]
texture_files = [
    "m51_EBT_BG",
    "m51_EBT_BG_01",
    "m51_EBT_Block",
    "m51_EBT_Block_00",
    "m51_EBT_Block_01",
    "m51_EBT_Door",
    "~texture"
]
sound_files = [
    "~sound"
]
blueprint_files = [
    "PBExtraModeInfo_BP",
    "mXXXXX_XXX_Gimmick",
    "~other"
]

write_json_param_list = []
write_log_param_list = []
copy_file_param_list = [
    ("PB_DT_AmmunitionMaster", "uasset", "Serializer", "Content\\Core\\DataTable"),
    ("PB_DT_ArtsCommandMaster", "uasset", "Serializer", "Content\\Core\\DataTable"),
    ("PB_DT_BloodlessAbilityData", "uasset", "Serializer", "Content\\Core\\DataTable"),
    ("PB_DT_BRVCharacterParameters", "uasset", "Serializer", "Content\\Core\\DataTable\\Character"),
    ("PB_DT_CharaUniqueParameterMaster", "uasset", "Serializer", "Content\\Core\\DataTable"),
    ("PB_DT_DamageMaster", "uasset", "Serializer", "Content\\Core\\DataTable"),
    ("PB_DT_EnchantParameterType", "uasset", "Serializer", "Content\\Core\\DataTable"),
    ("frameMiriam", "uasset", "Serializer\\Uasset", "Content\\Core\\UI\\HUD\\HUD_asset\\StateGauge\\0000"),
    ("m51_EBT_BG", "uasset", "Serializer\\Uasset", "Content\\Core\\Environment\\ACT51_EBT\\Texture"),
    ("m51_EBT_BG_01", "uasset", "Serializer\\Uasset", "Content\\Core\\Environment\\ACT51_EBT\\Texture"),
    ("m51_EBT_Block", "uasset", "Serializer\\Uasset", "Content\\Core\\Environment\\ACT51_EBT\\Texture"),
    ("m51_EBT_Block_00", "uasset", "Serializer\\Uasset", "Content\\Core\\Environment\\ACT51_EBT\\Texture"),
    ("m51_EBT_Block_01", "uasset", "Serializer\\Uasset", "Content\\Core\\Environment\\ACT51_EBT\\Texture"),
    ("m51_EBT_Door", "uasset", "Serializer\\Uasset", "Content\\Core\\Environment\\ACT51_EBT\\Texture"),
    ("m01SIP_001_Enemy_Hard", "umap", "UAssetGUI\\Umap", "Content\\Core\\Environment\\ACT01_SIP\\Level"),
    ("m03ENT_000_Gimmick", "umap", "UAssetGUI\\Umap", "Content\\Core\\Environment\\ACT03_ENT\\Level"),
    ("PBExtraModeInfo_BP", "uasset", "Serializer\\Uasset", "Content\\Core\\System\\GameMode")
]
json_list = []

#Config

config = configparser.ConfigParser()
config.optionxform = str
config.read("Data\\config.ini")

def writing():
    with open("Data\\config.ini", "w") as file_writer:
        config.write(file_writer)

def writing_and_exit():
    with open("Data\\config.ini", "w") as file_writer:
        config.write(file_writer)
    sys.exit()

#Threads

class Signaller(QObject):
    progress = Signal(int)
    finished = Signal()

class Generate(QThread):
    def __init__(self, string):
        QThread.__init__(self)
        self.signaller = Signaller()
        self.string = string

    def run(self):
        current = 0
        self.signaller.progress.emit(current)
        
        #FinalizeMap
        
        ClassManagement.room_final()
        current += 1
        self.signaller.progress.emit(current)
        
        #Copy
        
        for i in copy_file_param_list:
            ClassManagement.copy_file(i[0], i[1], i[2], i[3])
        
        #Serializer
        
        print("")
        for i in write_json_param_list:
            if i[0] == "MCANDLE":
                ClassManagement.write_miriam_candle()
            elif i[0] == "BCANDLE":
                ClassManagement.write_bloodless_candle(i[1])
            else:
                ClassManagement.write_json(i[0], i[1], i[2], i[3])
                print("")
            current += 1
            self.signaller.progress.emit(current)

        #UnrealPak
        
        root = os.getcwd()
        os.chdir("UnrealPak")
        os.system("cmd /c UnrealPak.exe \"Randomizer.pak\" -create=filelist.txt -compress Randomizer")
        os.chdir(root)
        
        current += 1
        self.signaller.progress.emit(current)
        
        #Reset
        
        for root, dirs, files in os.walk("UnrealPak\\Mod"):
            for file in os.listdir(root):
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        
        #Move
        
        if config.get("Misc", "sOutputPath"):
            shutil.move("UnrealPak\\Randomizer.pak", config.get("Misc", "sOutputPath") + "\\Randomizer.pak")
        else:
            shutil.move("UnrealPak\\Randomizer.pak", "Randomizer.pak")
        
        #Log
        
        for i in write_log_param_list:
            ClassManagement.write_log(i[0], i[1], i[2], i[3])
        
        self.signaller.finished.emit()

class Update(QThread):
    def __init__(self, progress_bar, api):
        QThread.__init__(self)
        self.signaller = Signaller()
        self.progress_bar = progress_bar
        self.api = api

    def run(self):
        current = 0
        self.signaller.progress.emit(current)
        
        #Download
        
        with open("True Randomization.zip", "wb") as file_writer:
            url = requests.get(self.api["assets"][0]["browser_download_url"], stream=True)
            for data in url.iter_content(chunk_size=4096):
                file_writer.write(data)
                current += len(data)
                self.signaller.progress.emit(current)
        
        self.progress_bar.setLabelText("Extracting...")
        
        #PurgeFolders
        
        shutil.rmtree("Data")
        shutil.rmtree("MapEdit\\Data")
        shutil.rmtree("Serializer")
        shutil.rmtree("UAssetGUI")
        shutil.rmtree("UnrealPak")
        
        #Extract
        
        os.rename("Randomizer.exe", "OldRandomizer.exe")
        with zipfile.ZipFile("True Randomization.zip", "r") as zip_ref:
            zip_ref.extractall("")
        os.remove("True Randomization.zip")
        
        #CarryPreviousConfig
        
        new_config = configparser.ConfigParser()
        new_config.optionxform = str
        new_config.read("Data\\config.ini")
        for each_section in new_config.sections():
            for (each_key, each_val) in new_config.items(each_section):
                if each_key == "sVersion":
                    continue
                try:
                    new_config.set(each_section, each_key, config.get(each_section, each_key))
                except (configparser.NoSectionError, configparser.NoOptionError):
                    continue
        with open("Data\\config.ini", "w") as file_writer:
            new_config.write(file_writer)
        
        #OpenNewEXE
        
        subprocess.Popen("Randomizer.exe")
        sys.exit()

class Convert(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.signaller = Signaller()

    def run(self):
        current = 0
        self.signaller.progress.emit(current)
        
        for i in json_list:
            if i == "PB_DT_RoomMaster":
                shutil.copyfile("MapEdit\\Data\\RoomMaster\\" + i + ".json", "Serializer\\" + i + ".json")
            else:
                shutil.copyfile("Serializer\\Json\\" + i + ".json", "Serializer\\" + i + ".json")
            root = os.getcwd()
            os.chdir("Serializer")
            if i == "PB_DT_RoomMaster":
                os.system("cmd /c UAsset2Json.exe -tobin -force " + i + ".json")
            else:
                os.system("cmd /c UAsset2Json.exe -tobin " + i + ".json")
            os.remove(i + ".uasset")
            os.rename(i + ".bin", i + ".uasset")
            os.remove(i + ".json")
            os.chdir(root)
            current += 1
            self.signaller.progress.emit(current)
        
        self.signaller.finished.emit()

#GUI

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setEnabled(False)
        self.initUI()
        self.check_for_updates()

    def initUI(self):
        
        self.first_time = False
        if config.getfloat("Misc", "fWindowSize") != 0.8 and config.getfloat("Misc", "fWindowSize") != 0.9 and config.getfloat("Misc", "fWindowSize") != 1.0:
            config.set("Misc", "fWindowSize", "1.0")
            self.first_time = True
        
        self.setStyleSheet("QWidget{background:transparent; color: #ffffff; font-family: Cambria; font-size: " + str(int(config.getfloat("Misc", "fWindowSize")*18)) + "px}"
        + "QComboBox{background-color: #21222e}"
        + "QMessageBox{background-color: #21222e}"
        + "QDialog{background-color: #21222e}"
        + "QProgressDialog{background-color: #21222e}"
        + "QPushButton{background-color: #21222e}"
        + "QSpinBox{background-color: #21222e}"
        + "QLineEdit{background-color: #21222e}"
        + "QMenu{background-color: #21222e}"
        + "QToolTip{border: 0px; background-color: #21222e; color: #ffffff; font-family: Cambria; font-size: " + str(int(config.getfloat("Misc", "fWindowSize")*18)) + "px}")
        self.string = ""
        
        #MainLayout
        
        grid = QGridLayout()
        grid.setSpacing(config.getfloat("Misc", "fWindowSize")*10)

        #Label

        label = QLabel()
        label.setStyleSheet("border: 1px solid white")
        label.setPixmap(QPixmap("Data\\artwork.png"))
        label.setScaledContents(True)
        label.setFixedSize(config.getfloat("Misc", "fWindowSize")*550, config.getfloat("Misc", "fWindowSize")*978)
        grid.addWidget(label, 0, 0, 10, 1)
        
        #Groupboxes

        box_1_grid = QGridLayout()
        self.box_1 = QGroupBox("Item Randomization")
        self.box_1.setLayout(box_1_grid)
        grid.addWidget(self.box_1, 0, 1, 2, 2)

        box_2_grid = QGridLayout()
        self.box_2 = QGroupBox("Shop Randomization")
        self.box_2.setLayout(box_2_grid)
        grid.addWidget(self.box_2, 2, 1, 1, 2)

        box_3_grid = QGridLayout()
        self.box_3 = QGroupBox("Library Randomization")
        self.box_3.setLayout(box_3_grid)
        grid.addWidget(self.box_3, 3, 1, 1, 2)

        box_4_grid = QGridLayout()
        self.box_4 = QGroupBox("Shard Randomization")
        self.box_4.setLayout(box_4_grid)
        grid.addWidget(self.box_4, 4, 1, 1, 2)

        box_5_grid = QGridLayout()
        self.box_5 = QGroupBox("Equipment Randomization")
        self.box_5.setLayout(box_5_grid)
        grid.addWidget(self.box_5, 5, 1, 1, 2)

        box_6_grid = QGridLayout()
        self.box_6 = QGroupBox("Enemy Randomization")
        self.box_6.setLayout(box_6_grid)
        grid.addWidget(self.box_6, 0, 3, 1, 2)

        box_7_grid = QGridLayout()
        self.box_7 = QGroupBox("Map Randomization")
        self.box_7.setLayout(box_7_grid)
        grid.addWidget(self.box_7, 1, 3, 1, 2)

        box_8_grid = QGridLayout()
        self.box_8 = QGroupBox("Graphic Randomization")
        self.box_8.setLayout(box_8_grid)
        grid.addWidget(self.box_8, 2, 3, 1, 2)

        box_9_grid = QGridLayout()
        self.box_9 = QGroupBox("Sound Randomization")
        self.box_9.setLayout(box_9_grid)
        grid.addWidget(self.box_9, 3, 3, 1, 2)
        
        box_10_left = QVBoxLayout()
        box_10_right = QVBoxLayout()
        box_10_box = QHBoxLayout()
        box_10_box.addLayout(box_10_left)
        box_10_box.addLayout(box_10_right)
        self.box_10 = QGroupBox("Extra Randomization")
        self.box_10.setLayout(box_10_box)
        grid.addWidget(self.box_10, 4, 3, 2, 2)
        
        box_11_grid = QGridLayout()
        box_11 = QGroupBox("Game Difficulty")
        box_11.setToolTip("Select the difficulty you'll be using in-game.")
        box_11.setLayout(box_11_grid)
        grid.addWidget(box_11, 6, 1, 1, 2)
        
        box_16_grid = QGridLayout()
        box_16 = QGroupBox("Start With")
        box_16.setToolTip("Select the shard you want to start the randomizer with.")
        box_16.setLayout(box_16_grid)
        grid.addWidget(box_16, 7, 1, 1, 2)
        
        box_13_grid = QGridLayout()
        box_13 = QGroupBox("Game Mode")
        box_13.setToolTip("Select the in-game mode this file is meant for.")
        box_13.setLayout(box_13_grid)
        grid.addWidget(box_13, 6, 3, 1, 2)
        
        box_17_grid = QGridLayout()
        box_17 = QGroupBox("Special Mode")
        box_17.setToolTip("Select from a few extra modes that this mod has to offer.")
        box_17.setLayout(box_17_grid)
        grid.addWidget(box_17, 7, 3, 1, 2)
        
        box_12_grid = QGridLayout()
        box_12 = QGroupBox("Presets")
        box_12.setLayout(box_12_grid)
        grid.addWidget(box_12, 8, 1, 1, 2)
        
        box_14_grid = QGridLayout()
        box_14 = QGroupBox("Output Path")
        box_14.setLayout(box_14_grid)
        grid.addWidget(box_14, 8, 3, 1, 2)
        
        box_15_left = QVBoxLayout()
        box_15_right = QVBoxLayout()
        box_15_box = QHBoxLayout()
        box_15_box.addLayout(box_15_left)
        box_15_box.addLayout(box_15_right)
        box_15 = QGroupBox()
        box_15.setLayout(box_15_box)
        box_15.setFixedSize(config.getfloat("Misc", "fWindowSize")*550, config.getfloat("Misc", "fWindowSize")*978)
        grid.addWidget(box_15, 0, 5, 10, 1)
        
        #TextLabel
        
        self.datatable_label = QLabel(self)
        self.label_change(datatable_files)
        box_15_left.addWidget(self.datatable_label)
        
        self.ui_label = QLabel(self)
        self.label_change(ui_files)
        box_15_left.addWidget(self.ui_label)
        
        self.texture_label = QLabel(self)
        self.label_change(texture_files)
        box_15_right.addWidget(self.texture_label)
        
        self.sound_label = QLabel(self)
        self.label_change(sound_files)
        box_15_right.addWidget(self.sound_label)
        
        self.blueprint_label = QLabel(self)
        self.label_change(blueprint_files)
        box_15_right.addWidget(self.blueprint_label)

        #Checkboxes

        self.check_box_1 = QCheckBox("Overworld Pool")
        self.check_box_1.setToolTip("Randomize all items and shards found in the overworld, now with\nnew improved logic. Everything you pick up will be 100% random\nso say goodbye to the endless sea of fried fish.")
        self.check_box_1.stateChanged.connect(self.check_box_1_changed)
        box_1_grid.addWidget(self.check_box_1, 0, 0)
        checkbox_list.append(self.check_box_1)

        self.check_box_2 = QCheckBox("Shop Pool")
        self.check_box_2.setToolTip("Randomize all items sold at the shop.")
        self.check_box_2.stateChanged.connect(self.check_box_2_changed)
        box_1_grid.addWidget(self.check_box_2, 1, 0)
        checkbox_list.append(self.check_box_2)

        self.check_box_16 = QCheckBox("Quest Pool")
        self.check_box_16.setToolTip("Randomize all quest rewards.")
        self.check_box_16.stateChanged.connect(self.check_box_16_changed)
        box_1_grid.addWidget(self.check_box_16, 2, 0)
        checkbox_list.append(self.check_box_16)

        self.check_box_17 = QCheckBox("Quest Requirements")
        self.check_box_17.setToolTip("Randomize the requirements for Susie, Abigail and Lindsay's quests.\nBenjamin will still ask you for waystones.")
        self.check_box_17.stateChanged.connect(self.check_box_17_changed)
        box_1_grid.addWidget(self.check_box_17, 3, 0)
        checkbox_list.append(self.check_box_17)

        self.check_box_18 = QCheckBox("Remove Infinites")
        self.check_box_18.setToolTip("Guarantee Gebel's Glasses and Recycle Hat to never appear.\nUseful for runs that favor magic and bullet management.")
        self.check_box_18.stateChanged.connect(self.check_box_18_changed)
        box_1_grid.addWidget(self.check_box_18, 4, 0)
        checkbox_list.append(self.check_box_18)

        self.check_box_3 = QCheckBox("Item Cost And Selling Price")
        self.check_box_3.setToolTip("Randomize the cost and selling price of every item in the shop.")
        self.check_box_3.stateChanged.connect(self.check_box_3_changed)
        box_2_grid.addWidget(self.check_box_3, 0, 0)
        checkbox_list.append(self.check_box_3)

        self.check_box_4 = QCheckBox("Scale Selling Price With Cost")
        self.check_box_4.setToolTip("Make the selling price scale with the item's random cost.")
        self.check_box_4.stateChanged.connect(self.check_box_4_changed)
        box_2_grid.addWidget(self.check_box_4, 1, 0)
        checkbox_list.append(self.check_box_4)

        self.check_box_5 = QCheckBox("Map Requirements")
        self.check_box_5.setToolTip("Randomize the completion requirement for each tome.")
        self.check_box_5.stateChanged.connect(self.check_box_5_changed)
        box_3_grid.addWidget(self.check_box_5, 0, 0)
        checkbox_list.append(self.check_box_5)

        self.check_box_6 = QCheckBox("Tome Appearance")
        self.check_box_6.setToolTip("Randomize which books are available in the game at all.\nDoes not affect Tome of Conquest.")
        self.check_box_6.stateChanged.connect(self.check_box_6_changed)
        box_3_grid.addWidget(self.check_box_6, 1, 0)
        checkbox_list.append(self.check_box_6)

        self.check_box_7 = QCheckBox("Shard Power And Magic Cost")
        self.check_box_7.setToolTip("Randomize the efficiency and MP cost of each shard.\nDoes not affect progression shards.")
        self.check_box_7.stateChanged.connect(self.check_box_7_changed)
        box_4_grid.addWidget(self.check_box_7, 0, 0)
        checkbox_list.append(self.check_box_7)

        self.check_box_8 = QCheckBox("Scale Magic Cost With Power")
        self.check_box_8.setToolTip("Make the MP cost scale with the shard's random power.")
        self.check_box_8.stateChanged.connect(self.check_box_8_changed)
        box_4_grid.addWidget(self.check_box_8, 1, 0)
        checkbox_list.append(self.check_box_8)

        self.check_box_23 = QCheckBox("Global Gear Stats")
        self.check_box_23.setToolTip("Slightly randomize the stats of all weapons and pieces of\nequipment with odds that still favor their original values.\nWARNING: Breaks the balance of playable Zangetsu !")
        self.check_box_23.stateChanged.connect(self.check_box_23_changed)
        box_5_grid.addWidget(self.check_box_23, 0, 0)
        checkbox_list.append(self.check_box_23)

        self.check_box_9 = QCheckBox("Cheat Gear Stats")
        self.check_box_9.setToolTip("Completely randomize the stats of the weapons, headgears\nand accessories that are originally obtained via cheatcodes.")
        self.check_box_9.stateChanged.connect(self.check_box_9_changed)
        box_5_grid.addWidget(self.check_box_9, 1, 0)
        checkbox_list.append(self.check_box_9)

        self.check_box_10 = QCheckBox("Enemy Levels")
        self.check_box_10.setToolTip("Randomize the level of every enemy. Stats that scale with\nlevel include HP, attack, defense, luck, EXP and expertise.\nPicking this option will give you more starting HP and MP\nand reduce their growth to compensate.\nWARNING: Only recommended for Miriam mode !")
        self.check_box_10.stateChanged.connect(self.check_box_10_changed)
        box_6_grid.addWidget(self.check_box_10, 0, 0)
        checkbox_list.append(self.check_box_10)

        self.check_box_11 = QCheckBox("Enemy Tolerances")
        self.check_box_11.setToolTip("Randomize the first 8 resistance/weakness attributes of every enemy.\nWARNING: Only recommended for Miriam mode !")
        self.check_box_11.stateChanged.connect(self.check_box_11_changed)
        box_6_grid.addWidget(self.check_box_11, 1, 0)
        checkbox_list.append(self.check_box_11)

        self.check_box_12 = QCheckBox("Room Layout")
        self.check_box_12.setToolTip("Randomly pick from a folder of map presets (" + str(map_num) + ").\nWARNING: Only recommended for Miriam mode !")
        self.check_box_12.stateChanged.connect(self.check_box_12_changed)
        box_7_grid.addWidget(self.check_box_12, 0, 0)
        checkbox_list.append(self.check_box_12)

        self.check_box_13 = QCheckBox("Miriam Color")
        self.check_box_13.setToolTip("Randomize the hue of Miriam's outfit.")
        self.check_box_13.stateChanged.connect(self.check_box_13_changed)
        box_8_grid.addWidget(self.check_box_13, 0, 0)
        checkbox_list.append(self.check_box_13)

        self.check_box_14 = QCheckBox("Zangetsu Color")
        self.check_box_14.setToolTip("Randomize the hue of Zangetsu's outfit.")
        self.check_box_14.stateChanged.connect(self.check_box_14_changed)
        box_8_grid.addWidget(self.check_box_14, 1, 0)
        checkbox_list.append(self.check_box_14)

        self.check_box_15 = QCheckBox("Dialogues")
        self.check_box_15.setToolTip("Randomize all conversation lines in the game. Characters\nwill still retain their actual voice (let's not get weird).")
        self.check_box_15.stateChanged.connect(self.check_box_15_changed)
        box_9_grid.addWidget(self.check_box_15, 0, 0)
        checkbox_list.append(self.check_box_15)

        self.check_box_21 = QCheckBox("Bloodless Candles")
        self.check_box_21.setToolTip("Randomize candle placement in Bloodless mode.")
        self.check_box_21.stateChanged.connect(self.check_box_21_changed)
        box_10_left.addWidget(self.check_box_21)
        checkbox_list.append(self.check_box_21)
        
        self.check_box_none = QCheckBox("None")
        self.check_box_none.setVisible(False)
        retain = self.check_box_none.sizePolicy()
        retain.setRetainSizeWhenHidden(True)
        self.check_box_none.setSizePolicy(retain)
        box_10_left.addWidget(self.check_box_none)

        self.check_box_22 = QCheckBox("Unknown")
        self.check_box_22.setToolTip("Analysis inconclusive, incompatible with current version.")
        #self.check_box_22.stateChanged.connect(self.check_box_22_changed)
        self.check_box_22.setEnabled(False)
        box_10_left.addWidget(self.check_box_22)
        checkbox_list.append(self.check_box_22)
        
        #RadioButtons
        
        self.radio_button_7 = QRadioButton("Full")
        self.radio_button_7.setToolTip("Shuffle every candle at random.")
        self.radio_button_7.toggled.connect(self.radio_button_group_3_checked)
        self.radio_button_7.setVisible(False)
        retain = self.radio_button_7.sizePolicy()
        retain.setRetainSizeWhenHidden(True)
        self.radio_button_7.setSizePolicy(retain)
        box_10_right.addWidget(self.radio_button_7)
        
        self.radio_button_8 = QRadioButton("Major-Minor")
        self.radio_button_8.setToolTip("Shuffle abilities and upgrades between themselves only.")
        self.radio_button_8.toggled.connect(self.radio_button_group_3_checked)
        self.radio_button_8.setVisible(False)
        retain = self.radio_button_8.sizePolicy()
        retain.setRetainSizeWhenHidden(True)
        self.radio_button_8.setSizePolicy(retain)
        box_10_right.addWidget(self.radio_button_8)
        
        self.radio_button_none = QRadioButton("None")
        self.radio_button_none.setVisible(False)
        retain = self.radio_button_none.sizePolicy()
        retain.setRetainSizeWhenHidden(True)
        self.radio_button_none.setSizePolicy(retain)
        box_10_right.addWidget(self.radio_button_none)
        
        self.radio_button_9 = QRadioButton("Full")
        self.radio_button_9.setToolTip("")
        #self.radio_button_9.toggled.connect(self.radio_button_group_4_checked)
        self.radio_button_9.setVisible(False)
        retain = self.radio_button_9.sizePolicy()
        retain.setRetainSizeWhenHidden(True)
        self.radio_button_9.setSizePolicy(retain)
        box_10_right.addWidget(self.radio_button_9)
        
        self.radio_button_10 = QRadioButton("Major-Minor")
        self.radio_button_10.setToolTip("")
        #self.radio_button_10.toggled.connect(self.radio_button_group_4_checked)
        self.radio_button_10.setVisible(False)
        retain = self.radio_button_10.sizePolicy()
        retain.setRetainSizeWhenHidden(True)
        self.radio_button_10.setSizePolicy(retain)
        box_10_right.addWidget(self.radio_button_10)
        
        self.radio_button_1 = QRadioButton("Normal")
        self.radio_button_1.setToolTip("More like easy mode.")
        self.radio_button_1.toggled.connect(self.radio_button_group_1_checked)
        box_11_grid.addWidget(self.radio_button_1, 0, 0)
        
        self.radio_button_2 = QRadioButton("Hard")
        self.radio_button_2.setToolTip("The real normal mode.")
        self.radio_button_2.toggled.connect(self.radio_button_group_1_checked)
        box_11_grid.addWidget(self.radio_button_2, 1, 0)
        
        self.radio_button_3 = QRadioButton("Nightmare")
        self.radio_button_3.setToolTip("Shit's gonna get real.")
        self.radio_button_3.toggled.connect(self.radio_button_group_1_checked)
        box_11_grid.addWidget(self.radio_button_3, 0, 1)
        
        self.radio_button_11 = QRadioButton("Nothing")
        self.radio_button_11.setToolTip("Start with no extra abilities.")
        self.radio_button_11.toggled.connect(self.radio_button_group_5_checked)
        box_16_grid.addWidget(self.radio_button_11, 0, 0)
        
        self.radio_button_12 = QRadioButton("Double Jump")
        self.radio_button_12.setToolTip("Start with the ability to double jump.")
        self.radio_button_12.toggled.connect(self.radio_button_group_5_checked)
        box_16_grid.addWidget(self.radio_button_12, 1, 0)
        
        self.radio_button_13 = QRadioButton("Accelerator")
        self.radio_button_13.setToolTip("Start with an accelerator shard.")
        self.radio_button_13.toggled.connect(self.radio_button_group_5_checked)
        box_16_grid.addWidget(self.radio_button_13, 0, 1)
        
        self.radio_button_4 = QRadioButton("Randomizer")
        self.radio_button_4.setToolTip("Adapt the file for randomizer mode.")
        self.radio_button_4.toggled.connect(self.radio_button_group_2_checked)
        box_13_grid.addWidget(self.radio_button_4, 0, 0)
        
        self.radio_button_6 = QRadioButton("Story")
        self.radio_button_6.setToolTip("Adapt the file for story mode.")
        self.radio_button_6.toggled.connect(self.radio_button_group_2_checked)
        box_13_grid.addWidget(self.radio_button_6, 1, 0)
        
        self.radio_button_14 = QRadioButton("None")
        self.radio_button_14.setToolTip("No special game mode.")
        self.radio_button_14.toggled.connect(self.radio_button_group_6_checked)
        box_17_grid.addWidget(self.radio_button_14, 0, 0)
        
        self.radio_button_5 = QRadioButton("Custom NG+")
        self.radio_button_5.setToolTip("Play through your NG+ files with a chosen level\nvalue for all enemies.")
        self.radio_button_5.toggled.connect(self.radio_button_group_6_checked)
        box_17_grid.addWidget(self.radio_button_5, 1, 0)
        
        self.radio_button_15 = QRadioButton("Progressive Z")
        self.radio_button_15.setToolTip("Play through a more balanced version of Zangetsu\nmode where his stats scale with progression.")
        self.radio_button_15.toggled.connect(self.radio_button_group_6_checked)
        box_17_grid.addWidget(self.radio_button_15, 0, 1)
        
        #SpinBoxes
        
        if config.getint("Misc", "iCustomLevel") < 1:
            config.set("Misc", "iCustomLevel", "1")
        if config.getint("Misc", "iCustomLevel") > 99:
            config.set("Misc", "iCustomLevel", "99")
        
        self.level_box = QSpinBox()
        self.level_box.setToolTip("Level of all enemies.")
        self.level_box.setRange(1, 99)
        self.level_box.setValue(config.getint("Misc", "iCustomLevel"))
        self.level_box.valueChanged.connect(self.new_level)
        self.level_box.setVisible(False)
        box_17_grid.addWidget(self.level_box, 1, 1)
        
        #DropDownLists
        
        self.preset_drop_down = QComboBox()
        self.preset_drop_down.setToolTip("EMPTY: Clear all options.\nTRIAL: To get started with this mod.\nRACE: Most fitting for a King of Speed.\nMEME: Time to break the game.\nRISK: Chaos awaits !\nBLOOD: She needs more blood.")
        self.preset_drop_down.addItem("Custom")
        self.preset_drop_down.addItem("Empty")
        self.preset_drop_down.addItem("Trial")
        self.preset_drop_down.addItem("Race")
        self.preset_drop_down.addItem("Meme")
        self.preset_drop_down.addItem("Risk")
        self.preset_drop_down.addItem("Blood")
        self.preset_drop_down.currentIndexChanged.connect(self.preset_drop_down_change)
        box_12_grid.addWidget(self.preset_drop_down, 0, 0)
        
        #Settings
        
        self.setting_layout = QGridLayout()
        
        size_box_grid = QGridLayout()
        size_box = QGroupBox("Window Size")
        size_box.setLayout(size_box_grid)
        self.setting_layout.addWidget(size_box, 0, 0, 1, 1)
        
        self.size_drop_down = QComboBox()
        self.size_drop_down.addItem("720p")
        self.size_drop_down.addItem("900p")
        self.size_drop_down.addItem("1080p and above")
        size_box_grid.addWidget(self.size_drop_down, 0, 0, 1, 1)
        
        setting_button = QPushButton("Apply")
        setting_button.clicked.connect(self.setting_button_clicked)
        self.setting_layout.addWidget(setting_button, 1, 0, 1, 1)
        
        #InitCheckboxes
        
        if config.getboolean("ItemRandomization", "bOverworldPool"):
            self.check_box_1.setChecked(True)
        if config.getboolean("ItemRandomization", "bShopPool"):
            self.check_box_2.setChecked(True)
        if config.getboolean("ItemRandomization", "bQuestPool"):
            self.check_box_16.setChecked(True)
        if config.getboolean("ItemRandomization", "bQuestRequirements"):
            self.check_box_17.setChecked(True)
        if config.getboolean("ItemRandomization", "bRemoveInfinites"):
            self.check_box_18.setChecked(True)
        if config.getboolean("ShopRandomization", "bItemCostAndSellingPrice"):
            self.check_box_3.setChecked(True)
        if config.getboolean("ShopRandomization", "bScaleSellingPriceWithCost"):
            self.check_box_4.setChecked(True)
        if config.getboolean("LibraryRandomization", "bMapRequirements"):
            self.check_box_5.setChecked(True)
        if config.getboolean("LibraryRandomization", "bTomeAppearance"):
            self.check_box_6.setChecked(True)
        if config.getboolean("ShardRandomization", "bShardPowerAndMagicCost"):
            self.check_box_7.setChecked(True)
        if config.getboolean("ShardRandomization", "bScaleMagicCostWithPower"):
            self.check_box_8.setChecked(True)
        if config.getboolean("EquipmentRandomization", "bGlobalGearStats"):
            self.check_box_23.setChecked(True)
        if config.getboolean("EquipmentRandomization", "bCheatGearStats"):
            self.check_box_9.setChecked(True)
        if config.getboolean("EnemyRandomization", "bEnemyLevels"):
            self.check_box_10.setChecked(True)
        if config.getboolean("EnemyRandomization", "bEnemyTolerances"):
            self.check_box_11.setChecked(True)
        if config.getboolean("MapRandomization", "bRoomLayout"):
            self.check_box_12.setChecked(True)
        if config.getboolean("GraphicRandomization", "bMiriamColor"):
            self.check_box_13.setChecked(True)
        if config.getboolean("GraphicRandomization", "bZangetsuColor"):
            self.check_box_14.setChecked(True)
        if config.getboolean("SoundRandomization", "bDialogues"):
            self.check_box_15.setChecked(True)
        if config.getboolean("ExtraRandomization", "bBloodlessCandles"):
            self.check_box_21.setChecked(True)
        else:
            self.check_box_21_changed()
        
        if config.getboolean("ExtraRandomization", "bBloodlessFull"):
            self.radio_button_7.setChecked(True)
        else:
            self.radio_button_8.setChecked(True)
        
        if config.getboolean("GameDifficulty", "bNormal"):
            self.radio_button_1.setChecked(True)
        elif config.getboolean("GameDifficulty", "bHard"):
            self.radio_button_2.setChecked(True)
        else:
            self.radio_button_3.setChecked(True)
        
        if config.getboolean("StartWith", "bNothing"):
            self.radio_button_11.setChecked(True)
        elif config.getboolean("StartWith", "bDoubleJump"):
            self.radio_button_12.setChecked(True)
        else:
            self.radio_button_13.setChecked(True)
        
        if config.getboolean("GameMode", "bRandomizer"):
            self.radio_button_4.setChecked(True)
        else:
            self.radio_button_6.setChecked(True)
        
        if config.getboolean("SpecialMode", "bNone"):
            self.radio_button_14.setChecked(True)
        elif config.getboolean("SpecialMode", "bCustom"):
            self.radio_button_5.setChecked(True)
        else:
            self.radio_button_15.setChecked(True)
        
        if config.getfloat("Misc", "fWindowSize") == 0.8:
            self.size_drop_down.setCurrentIndex(0)
        elif config.getfloat("Misc", "fWindowSize") == 0.9:
            self.size_drop_down.setCurrentIndex(1)
        elif config.getfloat("Misc", "fWindowSize") == 1.0:
            self.size_drop_down.setCurrentIndex(2)
        
        self.matches_preset()
        
        #TextField

        text_field = QLineEdit(config.get("Misc", "sOutputPath"))
        text_field.setToolTip("Use this field to link the path to your ~mods directory for a direct\ninstall.")
        text_field.textChanged[str].connect(self.new_text)
        box_14_grid.addWidget(text_field, 0, 0)

        #Buttons
        
        button_3 = QPushButton("Settings")
        button_3.setToolTip("Interface settings.")
        button_3.clicked.connect(self.button_3_clicked)
        grid.addWidget(button_3, 9, 1, 1, 1)

        button_4 = QPushButton("Pick Map")
        button_4.setToolTip("Manually pick a custom map to play on (overrides the random map selection).")
        button_4.clicked.connect(self.button_4_clicked)
        grid.addWidget(button_4, 9, 2, 1, 1)

        button_5 = QPushButton("Generate")
        button_5.setToolTip("Generate .pak file with current settings.")
        button_5.clicked.connect(self.button_5_clicked)
        grid.addWidget(button_5, 10, 1, 1, 4)
        
        button_6 = QPushButton("Auto Convert")
        button_6.setToolTip("Convert all the .json files from the Serializer\Json folder into .uasset\nautomatically. Only use this if you've made manual edits to those\ndatatables and want to apply them to this mod.")
        button_6.clicked.connect(self.button_6_clicked)
        grid.addWidget(button_6, 9, 3, 1, 1)
        
        button_7 = QPushButton("Credits")
        button_7.setToolTip("The people involved with this mod.")
        button_7.clicked.connect(self.button_7_clicked)
        grid.addWidget(button_7, 9, 4, 1, 1)
        
        #Window
        
        self.setLayout(grid)
        self.setFixedSize(config.getfloat("Misc", "fWindowSize")*1800, config.getfloat("Misc", "fWindowSize")*1000)
        self.setWindowTitle("Randomizer")
        self.setWindowIcon(QIcon("Data\\icon.png"))
        
        #Background
        
        background = QPixmap("MapEdit\\Data\\background.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, background)
        self.show()        
        self.setPalette(palette)
        
        #Position
        
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())
        
        QApplication.processEvents()

    def check_box_1_changed(self):
        self.matches_preset()
        if self.check_box_1.isChecked():
            config.set("ItemRandomization", "bOverworldPool", "true")
            self.check_box_1.setStyleSheet("color: " + item_color)
            if self.check_box_2.isChecked() and self.check_box_16.isChecked() and self.check_box_17.isChecked() and self.check_box_18.isChecked():
                self.box_1.setStyleSheet("color: " + item_color)
        else:
            config.set("ItemRandomization", "bOverworldPool", "false")
            self.check_box_1.setStyleSheet("color: #ffffff")
            self.box_1.setStyleSheet("color: #ffffff")

    def check_box_2_changed(self):
        self.matches_preset()
        if self.check_box_2.isChecked():
            config.set("ItemRandomization", "bShopPool", "true")
            self.check_box_2.setStyleSheet("color: " + item_color)
            if self.check_box_1.isChecked() and self.check_box_16.isChecked() and self.check_box_17.isChecked() and self.check_box_18.isChecked():
                self.box_1.setStyleSheet("color: " + item_color)
        else:
            config.set("ItemRandomization", "bShopPool", "false")
            self.check_box_2.setStyleSheet("color: #ffffff")
            self.box_1.setStyleSheet("color: #ffffff")

    def check_box_16_changed(self):
        self.matches_preset()
        if self.check_box_16.isChecked():
            config.set("ItemRandomization", "bQuestPool", "true")
            self.check_box_16.setStyleSheet("color: " + item_color)
            if self.check_box_1.isChecked() and self.check_box_2.isChecked() and self.check_box_17.isChecked() and self.check_box_18.isChecked():
                self.box_1.setStyleSheet("color: " + item_color)
        else:
            config.set("ItemRandomization", "bQuestPool", "false")
            self.check_box_16.setStyleSheet("color: #ffffff")
            self.box_1.setStyleSheet("color: #ffffff")

    def check_box_17_changed(self):
        self.matches_preset()
        if self.check_box_17.isChecked():
            config.set("ItemRandomization", "bQuestRequirements", "true")
            self.check_box_17.setStyleSheet("color: " + item_color)
            if self.check_box_1.isChecked() and self.check_box_2.isChecked() and self.check_box_16.isChecked() and self.check_box_18.isChecked():
                self.box_1.setStyleSheet("color: " + item_color)
            self.add_to_list(datatable_files, "PBScenarioStringTable", [])
        else:
            config.set("ItemRandomization", "bQuestRequirements", "false")
            self.check_box_17.setStyleSheet("color: #ffffff")
            self.box_1.setStyleSheet("color: #ffffff")
            self.remove_from_list(datatable_files, "PBScenarioStringTable", [])

    def check_box_18_changed(self):
        self.matches_preset()
        if self.check_box_18.isChecked():
            config.set("ItemRandomization", "bRemoveInfinites", "true")
            self.check_box_18.setStyleSheet("color: " + item_color)
            if self.check_box_1.isChecked() and self.check_box_2.isChecked() and self.check_box_16.isChecked() and self.check_box_17.isChecked():
                self.box_1.setStyleSheet("color: " + item_color)
        else:
            config.set("ItemRandomization", "bRemoveInfinites", "false")
            self.check_box_18.setStyleSheet("color: #ffffff")
            self.box_1.setStyleSheet("color: #ffffff")

    def check_box_3_changed(self):
        self.matches_preset()
        if self.check_box_3.isChecked():
            config.set("ShopRandomization", "bItemCostAndSellingPrice", "true")
            self.check_box_3.setStyleSheet("color: " + shop_color)
            if self.check_box_4.isChecked():
                self.box_2.setStyleSheet("color: " + shop_color)
        else:
            config.set("ShopRandomization", "bItemCostAndSellingPrice", "false")
            self.check_box_3.setStyleSheet("color: #ffffff")
            self.box_2.setStyleSheet("color: #ffffff")
            self.check_box_4.setChecked(False)

    def check_box_4_changed(self):
        self.matches_preset()
        if self.check_box_4.isChecked():
            config.set("ShopRandomization", "bScaleSellingPriceWithCost", "true")
            self.check_box_4.setStyleSheet("color: " + shop_color)
            if self.check_box_3.isChecked():
                self.box_2.setStyleSheet("color: " + shop_color)
            self.check_box_3.setChecked(True)
        else:
            config.set("ShopRandomization", "bScaleSellingPriceWithCost", "false")
            self.check_box_4.setStyleSheet("color: #ffffff")
            self.box_2.setStyleSheet("color: #ffffff")

    def check_box_5_changed(self):
        self.matches_preset()
        if self.check_box_5.isChecked():
            config.set("LibraryRandomization", "bMapRequirements", "true")
            self.check_box_5.setStyleSheet("color: " + library_color)
            if self.check_box_6.isChecked():
                self.box_3.setStyleSheet("color: " + library_color)
        else:
            config.set("LibraryRandomization", "bMapRequirements", "false")
            self.check_box_5.setStyleSheet("color: #ffffff")
            self.box_3.setStyleSheet("color: #ffffff")

    def check_box_6_changed(self):
        self.matches_preset()
        if self.check_box_6.isChecked():
            config.set("LibraryRandomization", "bTomeAppearance", "true")
            self.check_box_6.setStyleSheet("color: " + library_color)
            if self.check_box_5.isChecked():
                self.box_3.setStyleSheet("color: " + library_color)
        else:
            config.set("LibraryRandomization", "bTomeAppearance", "false")
            self.check_box_6.setStyleSheet("color: #ffffff")
            self.box_3.setStyleSheet("color: #ffffff")

    def check_box_7_changed(self):
        self.matches_preset()
        if self.check_box_7.isChecked():
            config.set("ShardRandomization", "bShardPowerAndMagicCost", "true")
            self.check_box_7.setStyleSheet("color: " + shard_color)
            if self.check_box_8.isChecked():
                self.box_4.setStyleSheet("color: " + shard_color)
        else:
            config.set("ShardRandomization", "bShardPowerAndMagicCost", "false")
            self.check_box_7.setStyleSheet("color: #ffffff")
            self.box_4.setStyleSheet("color: #ffffff")
            self.check_box_8.setChecked(False)

    def check_box_8_changed(self):
        self.matches_preset()
        if self.check_box_8.isChecked():
            config.set("ShardRandomization", "bScaleMagicCostWithPower", "true")
            self.check_box_8.setStyleSheet("color: " + shard_color)
            if self.check_box_7.isChecked():
                self.box_4.setStyleSheet("color: " + shard_color)
            self.check_box_7.setChecked(True)
        else:
            config.set("ShardRandomization", "bScaleMagicCostWithPower", "false")
            self.check_box_8.setStyleSheet("color: #ffffff")
            self.box_4.setStyleSheet("color: #ffffff")

    def check_box_23_changed(self):
        self.matches_preset()
        if self.check_box_23.isChecked():
            config.set("EquipmentRandomization", "bGlobalGearStats", "true")
            self.check_box_23.setStyleSheet("color: " + equip_color)
            if self.check_box_9.isChecked():
                self.box_5.setStyleSheet("color: " + equip_color)
        else:
            config.set("EquipmentRandomization", "bGlobalGearStats", "false")
            self.check_box_23.setStyleSheet("color: #ffffff")
            self.box_5.setStyleSheet("color: #ffffff")

    def check_box_9_changed(self):
        self.matches_preset()
        if self.check_box_9.isChecked():
            config.set("EquipmentRandomization", "bCheatGearStats", "true")
            self.check_box_9.setStyleSheet("color: " + equip_color)
            if self.check_box_23.isChecked():
                self.box_5.setStyleSheet("color: " + equip_color)
        else:
            config.set("EquipmentRandomization", "bCheatGearStats", "false")
            self.check_box_9.setStyleSheet("color: #ffffff")
            self.box_5.setStyleSheet("color: #ffffff")

    def check_box_10_changed(self):
        self.matches_preset()
        if self.check_box_10.isChecked():
            config.set("EnemyRandomization", "bEnemyLevels", "true")
            self.check_box_10.setStyleSheet("color: " + enemy_color)
            if self.check_box_11.isChecked():
                self.box_6.setStyleSheet("color: " + enemy_color)
        else:
            config.set("EnemyRandomization", "bEnemyLevels", "false")
            self.check_box_10.setStyleSheet("color: #ffffff")
            self.box_6.setStyleSheet("color: #ffffff")

    def check_box_11_changed(self):
        self.matches_preset()
        if self.check_box_11.isChecked():
            config.set("EnemyRandomization", "bEnemyTolerances", "true")
            self.check_box_11.setStyleSheet("color: " + enemy_color)
            if self.check_box_10.isChecked():
                self.box_6.setStyleSheet("color: " + enemy_color)
        else:
            config.set("EnemyRandomization", "bEnemyTolerances", "false")
            self.check_box_11.setStyleSheet("color: #ffffff")
            self.box_6.setStyleSheet("color: #ffffff")

    def check_box_12_changed(self):
        self.matches_preset()
        if self.check_box_12.isChecked():
            config.set("MapRandomization", "bRoomLayout", "true")
            self.check_box_12.setStyleSheet("color: " + map_color)
            self.box_7.setStyleSheet("color: " + map_color)
            if not self.string:
                self.add_to_list(datatable_files, "PB_DT_QuestMaster", [self.radio_button_4])
                self.add_to_list(ui_files, "icon_8bitCrown", [])
                self.add_to_list(ui_files, "Map_Icon_Keyperson", [])
                self.add_to_list(ui_files, "Map_Icon_RootBox", [])
                self.add_to_list(ui_files, "Map_StartingPoint", [])
        else:
            config.set("MapRandomization", "bRoomLayout", "false")
            self.check_box_12.setStyleSheet("color: #ffffff")
            self.box_7.setStyleSheet("color: #ffffff")
            if not self.string:
                self.remove_from_list(datatable_files, "PB_DT_QuestMaster", [self.radio_button_4])
                self.remove_from_list(ui_files, "icon_8bitCrown", [])
                self.remove_from_list(ui_files, "Map_Icon_Keyperson", [])
                self.remove_from_list(ui_files, "Map_Icon_RootBox", [])
                self.remove_from_list(ui_files, "Map_StartingPoint", [])

    def check_box_13_changed(self):
        self.matches_preset()
        if self.check_box_13.isChecked():
            config.set("GraphicRandomization", "bMiriamColor", "true")
            self.check_box_13.setStyleSheet("color: " + graphic_color)
            if self.check_box_14.isChecked():
                self.box_8.setStyleSheet("color: " + graphic_color)
            self.add_to_list(ui_files, "Face_Miriam", [])
            self.add_to_list(texture_files, "T_Body01_01_Color", [])
            self.add_to_list(texture_files, "T_Pl01_Cloth_Bace", [])
        else:
            config.set("GraphicRandomization", "bMiriamColor", "false")
            self.check_box_13.setStyleSheet("color: #ffffff")
            self.box_8.setStyleSheet("color: #ffffff")
            self.remove_from_list(ui_files, "Face_Miriam", [])
            self.remove_from_list(texture_files, "T_Body01_01_Color", [])
            self.remove_from_list(texture_files, "T_Pl01_Cloth_Bace", [])

    def check_box_14_changed(self):
        self.matches_preset()
        if self.check_box_14.isChecked():
            config.set("GraphicRandomization", "bZangetsuColor", "true")
            self.check_box_14.setStyleSheet("color: " + graphic_color)
            if self.check_box_13.isChecked():
                self.box_8.setStyleSheet("color: " + graphic_color)
            self.add_to_list(ui_files, "Face_Zangetsu", [])
            self.add_to_list(texture_files, "T_N1011_body_color", [])
            self.add_to_list(texture_files, "T_N1011_face_color", [])
            self.add_to_list(texture_files, "T_N1011_equip_color", [])
            self.add_to_list(texture_files, "T_Tknife05_Base", [])
        else:
            config.set("GraphicRandomization", "bZangetsuColor", "false")
            self.check_box_14.setStyleSheet("color: #ffffff")
            self.box_8.setStyleSheet("color: #ffffff")
            self.remove_from_list(ui_files, "Face_Zangetsu", [])
            self.remove_from_list(texture_files, "T_N1011_body_color", [])
            self.remove_from_list(texture_files, "T_N1011_face_color", [])
            self.remove_from_list(texture_files, "T_N1011_equip_color", [])
            self.remove_from_list(texture_files, "T_Tknife05_Base", [])

    def check_box_15_changed(self):
        self.matches_preset()
        if self.check_box_15.isChecked():
            config.set("SoundRandomization", "bDialogues", "true")
            self.check_box_15.setStyleSheet("color: " + sound_color)
            self.box_9.setStyleSheet("color: " + sound_color)
            self.add_to_list(datatable_files, "PB_DT_DialogueTableItems", [])
        else:
            config.set("SoundRandomization", "bDialogues", "false")
            self.check_box_15.setStyleSheet("color: #ffffff")
            self.box_9.setStyleSheet("color: #ffffff")
            self.remove_from_list(datatable_files, "PB_DT_DialogueTableItems", [])

    def check_box_21_changed(self):
        self.matches_preset()
        if self.check_box_21.isChecked():
            config.set("ExtraRandomization", "bBloodlessCandles", "true")
            self.check_box_21.setStyleSheet("color: " + extra_color)
            self.radio_button_7.setStyleSheet("color: " + extra_color)
            self.radio_button_8.setStyleSheet("color: " + extra_color)
            if self.check_box_22.isChecked():
                self.box_10.setStyleSheet("color: " + extra_color)
            self.remove_from_list(ui_files, "icon", [self.radio_button_15])
            self.remove_from_list(sound_files, "ACT50_BRM", [self.radio_button_15])
            self.radio_button_7.setVisible(True)
            self.radio_button_8.setVisible(True)
            #UncheckItem
            self.check_box_1.setChecked(False)
            self.check_box_2.setChecked(False)
            self.check_box_16.setChecked(False)
            self.check_box_17.setChecked(False)
            self.check_box_18.setChecked(False)
            #CheckStory
            self.radio_button_6.setChecked(True)
            #CheckSpecialNone
            self.radio_button_14.setChecked(True)
        else:
            config.set("ExtraRandomization", "bBloodlessCandles", "false")
            self.check_box_21.setStyleSheet("color: #ffffff")
            self.box_10.setStyleSheet("color: #ffffff")
            self.add_to_list(ui_files, "icon", [self.radio_button_15])
            self.add_to_list(sound_files, "ACT50_BRM", [self.radio_button_15])
            self.radio_button_7.setVisible(False)
            self.radio_button_8.setVisible(False)
    
    def radio_button_group_3_checked(self):
        if self.radio_button_7.isChecked():
            config.set("ExtraRandomization", "bBloodlessFull", "true")
            config.set("ExtraRandomization", "bBloodlessMajorMinor", "false")
        else:
            config.set("ExtraRandomization", "bBloodlessFull", "false")
            config.set("ExtraRandomization", "bBloodlessMajorMinor", "true")
    
    def radio_button_group_1_checked(self):
        if self.radio_button_1.isChecked():
            config.set("GameDifficulty", "bNormal", "true")
            config.set("GameDifficulty", "bHard", "false")
            config.set("GameDifficulty", "bNightmare", "false")
        elif self.radio_button_2.isChecked():
            config.set("GameDifficulty", "bNormal", "false")
            config.set("GameDifficulty", "bHard", "true")
            config.set("GameDifficulty", "bNightmare", "false")
        else:
            config.set("GameDifficulty", "bNormal", "false")
            config.set("GameDifficulty", "bHard", "false")
            config.set("GameDifficulty", "bNightmare", "true")
    
    def radio_button_group_5_checked(self):
        if self.radio_button_11.isChecked():
            config.set("StartWith", "bNothing", "true")
            config.set("StartWith", "bDoubleJump", "false")
            config.set("StartWith", "bAccelerator", "false")
        elif self.radio_button_12.isChecked():
            config.set("StartWith", "bNothing", "false")
            config.set("StartWith", "bDoubleJump", "true")
            config.set("StartWith", "bAccelerator", "false")
            #CheckRandomizer
            self.radio_button_4.setChecked(True)
        else:
            config.set("StartWith", "bNothing", "false")
            config.set("StartWith", "bDoubleJump", "false")
            config.set("StartWith", "bAccelerator", "true")
            #CheckRandomizer
            self.radio_button_4.setChecked(True)

    def radio_button_group_2_checked(self):
        if self.radio_button_4.isChecked():
            config.set("GameMode", "bRandomizer", "true")
            config.set("GameMode", "bStory", "false")
            if not self.string:
                self.add_to_list(datatable_files, "PB_DT_QuestMaster", [self.check_box_12])
            #UncheckExtra
            self.check_box_21.setChecked(False)
            self.check_box_22.setChecked(False)
            #CheckSpecialNone
            self.radio_button_14.setChecked(True)
        else:
            config.set("GameMode", "bRandomizer", "false")
            config.set("GameMode", "bStory", "true")
            if not self.string:
                self.remove_from_list(datatable_files, "PB_DT_QuestMaster", [self.check_box_12])
            #CheckStartNothing
            self.radio_button_11.setChecked(True)
    
    def radio_button_group_6_checked(self):
        if self.radio_button_14.isChecked():
            self.level_box.setVisible(False)
            config.set("SpecialMode", "bNone", "true")
            config.set("SpecialMode", "bCustom", "false")
            config.set("SpecialMode", "bProgressive", "false")
            self.add_to_list(ui_files, "icon", [self.check_box_21])
            self.add_to_list(sound_files, "ACT50_BRM", [self.check_box_21])
        elif self.radio_button_5.isChecked():
            self.level_box.setVisible(True)
            config.set("SpecialMode", "bNone", "false")
            config.set("SpecialMode", "bCustom", "true")
            config.set("SpecialMode", "bProgressive", "false")
            self.add_to_list(ui_files, "icon", [self.check_box_21])
            self.add_to_list(sound_files, "ACT50_BRM", [self.check_box_21])
            #UncheckItem
            self.check_box_1.setChecked(False)
            self.check_box_2.setChecked(False)
            self.check_box_16.setChecked(False)
            self.check_box_17.setChecked(False)
            self.check_box_18.setChecked(False)
            #CheckStory
            self.radio_button_6.setChecked(True)
            #UncheckExtra
            self.check_box_21.setChecked(False)
            self.check_box_22.setChecked(False)
        else:
            self.level_box.setVisible(False)
            config.set("SpecialMode", "bNone", "false")
            config.set("SpecialMode", "bCustom", "false")
            config.set("SpecialMode", "bProgressive", "true")
            self.remove_from_list(ui_files, "icon", [self.check_box_21])
            self.remove_from_list(sound_files, "ACT50_BRM", [self.check_box_21])
            #UncheckItem
            self.check_box_1.setChecked(False)
            self.check_box_2.setChecked(False)
            self.check_box_16.setChecked(False)
            self.check_box_17.setChecked(False)
            self.check_box_18.setChecked(False)
            #CheckStory
            self.radio_button_6.setChecked(True)
            #UncheckExtra
            self.check_box_21.setChecked(False)
            self.check_box_22.setChecked(False)
    
    def preset_drop_down_change(self, index):
        if index == 1:
            for i in range(len(checkbox_list)):
                checkbox_list[i].setChecked(empty_preset[i])
        elif index == 2:
            for i in range(len(checkbox_list)):
                checkbox_list[i].setChecked(trial_preset[i])
        elif index == 3:
            for i in range(len(checkbox_list)):
                checkbox_list[i].setChecked(race_preset[i])
        elif index == 4:
            for i in range(len(checkbox_list)):
                checkbox_list[i].setChecked(meme_preset[i])
        elif index == 5:
            for i in range(len(checkbox_list)):
                checkbox_list[i].setChecked(risk_preset[i])
        elif index == 6:
            for i in range(len(checkbox_list)):
                checkbox_list[i].setChecked(blood_preset[i])

    def matches_preset(self):
        is_preset_1 = True
        for i in range(len(checkbox_list)):
            if not(empty_preset[i] and checkbox_list[i].isChecked() or not empty_preset[i] and not checkbox_list[i].isChecked()):
                is_preset_1 = False
        if is_preset_1:
            self.preset_drop_down.setCurrentIndex(1)
            return
        
        is_preset_2 = True
        for i in range(len(checkbox_list)):
            if not(trial_preset[i] and checkbox_list[i].isChecked() or not trial_preset[i] and not checkbox_list[i].isChecked()):
                is_preset_2 = False
        if is_preset_2:
            self.preset_drop_down.setCurrentIndex(2)
            return
        
        is_preset_3 = True
        for i in range(len(checkbox_list)):
            if not(race_preset[i] and checkbox_list[i].isChecked() or not race_preset[i] and not checkbox_list[i].isChecked()):
                is_preset_3 = False
        if is_preset_3:
            self.preset_drop_down.setCurrentIndex(3)
            return
        
        is_preset_4 = True
        for i in range(len(checkbox_list)):
            if not(meme_preset[i] and checkbox_list[i].isChecked() or not meme_preset[i] and not checkbox_list[i].isChecked()):
                is_preset_4 = False
        if is_preset_4:
            self.preset_drop_down.setCurrentIndex(4)
            return
        
        is_preset_5 = True
        for i in range(len(checkbox_list)):
            if not(risk_preset[i] and checkbox_list[i].isChecked() or not risk_preset[i] and not checkbox_list[i].isChecked()):
                is_preset_5 = False
        if is_preset_5:
            self.preset_drop_down.setCurrentIndex(5)
            return
        
        is_preset_6 = True
        for i in range(len(checkbox_list)):
            if not(blood_preset[i] and checkbox_list[i].isChecked() or not blood_preset[i] and not checkbox_list[i].isChecked()):
                is_preset_6 = False
        if is_preset_6:
            self.preset_drop_down.setCurrentIndex(6)
            return
        
        self.preset_drop_down.setCurrentIndex(0)
    
    def new_level(self):
        config.set("Misc", "iCustomLevel", str(self.level_box.value()))
    
    def new_text(self, text):
        config.set("Misc", "sOutputPath", text)
    
    def add_to_list(self, list, file, checkboxes):
        change = True
        for i in checkboxes:
            if i.isChecked():
                change = False
        if change and not file in list:
            list.append(file)
            self.label_change(list)
    
    def remove_from_list(self, list, file, checkboxes):
        change = True
        for i in checkboxes:
            if i.isChecked():
                change = False
        if change and file in list:
            list.remove(file)
            self.label_change(list)
    
    def label_change(self, list):
        if list == datatable_files:
            string = "Modified DataTable:\n\n"
            label = self.datatable_label
        elif list == ui_files:
            string = "Modified UI:\n\n"
            label = self.ui_label
        elif list == texture_files:
            string = "Modified Texture:\n\n"
            label = self.texture_label
        elif list == sound_files:
            string = "Modified Sound:\n\n"
            label = self.sound_label
        elif list == blueprint_files:
            string = "Modified Blueprint:\n\n"
            label = self.blueprint_label
        list.sort()
        for i in range(len(list) - 1):
            string += list[i] + "\n"
        label.setText(string)
    
    def set_progress(self, progress):
        self.progress_bar.setValue(progress)
    
    def seed_finished(self):
        box = QMessageBox(self)
        box.setWindowTitle("Done")
        if config.getboolean("GameMode", "bRandomizer"):
            box.setText("Pak file generated !\n\nMake absolutely sure to use existing seed 17791 in the game randomizer for this to work !")
        else:
            box.setText("Pak file generated !")
        box.exec()
        writing_and_exit()
    
    def convert_finished(self):
        self.setEnabled(True)
    
    def setting_button_clicked(self):
        if config.getfloat("Misc", "fWindowSize") == 0.8 and self.size_drop_down.currentIndex() == 0 or config.getfloat("Misc", "fWindowSize") == 0.9 and self.size_drop_down.currentIndex() == 1 or config.getfloat("Misc", "fWindowSize") == 1.0 and self.size_drop_down.currentIndex() == 2:
            self.box.close()
        else:
            if self.size_drop_down.currentIndex() == 0:
                config.set("Misc", "fWindowSize", "0.8")
            elif self.size_drop_down.currentIndex() == 1:
                config.set("Misc", "fWindowSize", "0.9")
            elif self.size_drop_down.currentIndex() == 2:
                config.set("Misc", "fWindowSize", "1.0")
            writing()
            os.execl(sys.executable, sys.executable, *sys.argv)
    
    def button_3_clicked(self):
        self.box = QDialog(self)
        self.box.setLayout(self.setting_layout)
        self.box.setWindowTitle("Settings")
        self.box.exec()
        
        if config.getfloat("Misc", "fWindowSize") == 0.8:
            self.size_drop_down.setCurrentIndex(0)
        elif config.getfloat("Misc", "fWindowSize") == 0.9:
            self.size_drop_down.setCurrentIndex(1)
        elif config.getfloat("Misc", "fWindowSize") == 1.0:
            self.size_drop_down.setCurrentIndex(2)

    def button_4_clicked(self):
        path = QFileDialog.getOpenFileName(parent=self, caption="Open", dir="MapEdit//Custom", filter="*.json")[0]
        if path:
            self.string = path.replace("/", "\\")
            self.setWindowTitle("Randomizer (" + self.string + ")")
            self.add_to_list(datatable_files, "PB_DT_QuestMaster", [self.check_box_12, self.radio_button_4])
            self.add_to_list(ui_files, "icon_8bitCrown", [self.check_box_12])
            self.add_to_list(ui_files, "Map_Icon_Keyperson", [self.check_box_12])
            self.add_to_list(ui_files, "Map_Icon_RootBox", [self.check_box_12])
            self.add_to_list(ui_files, "Map_StartingPoint", [self.check_box_12])

    def button_5_clicked(self):
        self.setEnabled(False)
        QApplication.processEvents()
        
        #CheckIfPathExists
        
        if config.get("Misc", "sOutputPath") and not os.path.isdir(config.get("Misc", "sOutputPath")):
            self.no_path()
            self.setEnabled(True)
            return
        
        #CheckSerializerInstallRequirement
        
        try:
            subprocess.check_call("Serializer\\UAsset2Json.exe", shell=True)
        except subprocess.CalledProcessError as error:
            self.install_3()
            self.setEnabled(True)
            return
        
        #InitializeModDirectory
        
        for i in mod_directory:
            if not os.path.isdir(i):
                os.makedirs(i)
        
        #InitializeSpoilerLog
        
        if not os.path.isdir("SpoilerLog"):
            os.makedirs("SpoilerLog")
        if not os.path.isdir("MapEdit\\Key"):
            os.makedirs("MapEdit\\Key")
        
        for file in os.listdir("SpoilerLog"):
            file_path = os.path.join("SpoilerLog", file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        for file in os.listdir("MapEdit\\Key"):
            file_path = os.path.join("MapEdit\\Key", file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        open("SpoilerLog\\~debug.txt", "a").close()
        
        #OpenFiles
        
        ClassManagement.open_content()
        ClassManagement.open_data()
        ClassManagement.open_translation()
        
        #InitClasses
        
        ClassBloodless.init()
        ClassSound.init()
        ClassEnemy.init()
        ClassEquipment.init()
        ClassItem.init()
        ClassLibrary.init()
        ClassShard.init()
        
        #Hue
        
        miriam_hue = random.choice(os.listdir("Serializer\\Uasset\\Hue\\Miriam"))
        zangetsu_hue = random.choice(os.listdir("Serializer\\Uasset\\Hue\\Zangetsu"))
        
        #Map
        
        if not self.string and config.getboolean("MapRandomization", "bRoomLayout"):
            if glob.glob("MapEdit\\Custom\\*.json"):
                self.string = random.choice(glob.glob("MapEdit\\Custom\\*.json"))
        
        #Patch
        
        if self.string:
            ClassManagement.load_custom_map(self.string)
            ClassManagement.load_custom_logic(self.string)
            ClassManagement.load_custom_order(self.string)
            ClassItem.unused_room_check()
            ClassManagement.create_log(self.string)
            write_log_param_list.append(("MapSelection", "MapEdit\\Key", ClassManagement.log, False))
        
        if config.getboolean("GameDifficulty", "bHard") or config.getboolean("GameDifficulty", "bNightmare"):
            ClassItem.hard_enemy_logic()
        ClassItem.extra_logic()
        
        if config.getboolean("GameMode", "bRandomizer"):
            ClassItem.give_shortcut()
            ClassItem.give_eye()
            ClassShard.eye_max_range()
            ClassItem.unlock_all_quest()
            ClassItem.all_hair_in_shop()
            ClassEnemy.no_upgrade_cap()
        else:
            ClassItem.story_chest()
        
        if config.getboolean("StartWith", "bDoubleJump"):
            ClassItem.give_extra("Doublejump")
        elif config.getboolean("StartWith", "bAccelerator"):
            ClassItem.give_extra("Accelerator")
        
        if config.getboolean("LibraryRandomization", "bMapRequirements") or config.getboolean("LibraryRandomization", "bTomeAppearance"):
            ClassLibrary.rand_book(config.getboolean("LibraryRandomization", "bMapRequirements"), config.getboolean("LibraryRandomization", "bTomeAppearance"))
            write_log_param_list.append(("LibraryTomes", "SpoilerLog", ClassLibrary.get_log(), True))
        
        if config.getboolean("ItemRandomization", "bRemoveInfinites"):
            ClassItem.remove_infinite()
        
        if config.getboolean("ItemRandomization", "bOverworldPool"):
            ClassItem.no_key_in_shop()
            ClassItem.no_shard_craft()
            ClassItem.rand_overworld_key()
            if config.getboolean("EnemyRandomization", "bEnemyLevels") or config.getboolean("EnemyRandomization", "bEnemyTolerances"):
                ClassItem.rand_ship_waystone()
            ClassItem.rand_overworld_shard()
            ClassItem.rand_overworld_pool()
            write_log_param_list.append(("KeyLocation", "MapEdit\\Key", ClassItem.get_log(), True))
        
        if config.getboolean("ItemRandomization", "bQuestPool"):
            ClassItem.rand_quest_pool()
        
        if config.getboolean("ItemRandomization", "bShopPool"):
            ClassItem.rand_shop_pool()
        
        if config.getboolean("ItemRandomization", "bQuestRequirements"):
            ClassItem.rand_quest_requirement()
            ClassItem.catering_quest_info()
        
        if self.string:
            ClassItem.no_enemy_quest_icon()
        
        if config.getboolean("ShopRandomization", "bItemCostAndSellingPrice"):
            ClassItem.rand_shop_price(config.getboolean("ShopRandomization", "bScaleSellingPriceWithCost"))
        
        if config.getboolean("ShardRandomization", "bShardPowerAndMagicCost"):
            ClassShard.rand_shard(config.getboolean("ShardRandomization", "bScaleMagicCostWithPower"))
            write_log_param_list.append(("ShardPower", "SpoilerLog", ClassShard.get_log(), False))
        else:
            ClassShard.default_shard()
        
        if config.getboolean("EquipmentRandomization", "bGlobalGearStats"):
            ClassEquipment.rand_all_equip()
            ClassEquipment.rand_all_weapon()
        
        if config.getboolean("EquipmentRandomization", "bCheatGearStats"):
            ClassEquipment.rand_cheat_equip()
            write_log_param_list.append(("CheatEquipmentStats", "SpoilerLog", ClassEquipment.get_armor_log(), True))
            ClassEquipment.rand_cheat_weapon()
            write_log_param_list.append(("CheatWeaponStats", "SpoilerLog", ClassEquipment.get_weapon_log(), True))
        
        if config.getboolean("EnemyRandomization", "bEnemyLevels") or config.getboolean("EnemyRandomization", "bEnemyTolerances") or self.string or config.getboolean("SpecialMode", "bCustom"):
            ClassEnemy.enemy_property(config.getboolean("EnemyRandomization", "bEnemyLevels"), config.getboolean("EnemyRandomization", "bEnemyTolerances"), bool(self.string), config.getboolean("SpecialMode", "bCustom"), config.getint("Misc", "iCustomLevel"))
            if config.getboolean("EnemyRandomization", "bEnemyLevels") or config.getboolean("EnemyRandomization", "bEnemyTolerances"):
                write_log_param_list.append(("EnemyProperties", "SpoilerLog", ClassEnemy.get_log(), True))
        
        if config.getboolean("EnemyRandomization", "bEnemyLevels") and not config.getboolean("SpecialMode", "bCustom"):
            ClassEnemy.higher_HPMP()
            ClassEnemy.lower_HPMP_growth()
        
        if config.getboolean("SoundRandomization", "bDialogues"):
            ClassSound.rand_dialogue()
        
        if config.getboolean("ExtraRandomization", "bBloodlessCandles"):
            if config.getboolean("ExtraRandomization", "bBloodlessFull"):
                ClassBloodless.chaos_candle()
            ClassBloodless.candle_shuffle()
            ClassBloodless.create_log()
            ClassManagement.write_log("KeyLocation", "MapEdit\\Key", ClassBloodless.get_log(), True)
        
        if config.getboolean("GameDifficulty", "bNormal"):
            ClassEnemy.rename_difficulty("Normal", "???", "???")
            ClassEnemy.normal_bomber()
            ClassEnemy.normal_milli()
            ClassEnemy.normal_bael()
            ClassEnemy.brv_damage(1.0)
        elif config.getboolean("GameDifficulty", "bHard"):
            ClassEnemy.rename_difficulty("???", "Hard", "???")
            ClassEnemy.brv_speed("AnimaionPlayRateHard")
            ClassEnemy.brv_damage(ClassManagement.coordinate_content[9]["Value"]["Value"])
        elif config.getboolean("GameDifficulty", "bNightmare"):
            ClassEnemy.rename_difficulty("???", "???", "Nightmare")
            ClassEnemy.brv_speed("AnimaionPlayRateNightmare")
            ClassEnemy.brv_damage(ClassManagement.coordinate_content[14]["Value"]["Value"])
        
        if config.getboolean("SpecialMode", "bProgressive"):
            if config.getboolean("GameDifficulty", "bNightmare"):
                ClassEnemy.zangetsu_progress()
                ClassEnemy.nightmare_damage()
                ClassEnemy.rename_difficulty("???", "Nightmare", "???")
            ClassEnemy.zangetsu_no_stats()
            ClassEnemy.zangetsu_growth(config.getboolean("GameDifficulty", "bNightmare"))
            ClassEquipment.zangetsu_black_belt()
        
        #Write
        
        write_json_param_list.append(("PBSystemStringTable", "Content\\L10N\\en\\Core\\StringTable", ClassManagement.system_content, False))
        write_json_param_list.append(("PB_DT_BRVAttackDamage", "Content\\Core\\DataTable\\Character", ClassManagement.attack_content, True))
        write_json_param_list.append(("PB_DT_RoomMaster", "Content\\Core\\DataTable", ClassManagement.room_content, True))
        write_json_param_list.append(("PB_DT_ShardMaster", "Content\\Core\\DataTable", ClassManagement.shard_content, True))
        
        if self.string:
            copy_file_param_list.append(("icon_8bitCrown", "uasset", "Serializer\\Uasset", "Content\\Core\\UI\\K2C"))
            copy_file_param_list.append(("Map_Icon_Keyperson", "uasset", "Serializer\\Uasset", "Content\\Core\\UI\\Map\\Texture"))
            copy_file_param_list.append(("Map_Icon_RootBox", "uasset", "Serializer\\Uasset", "Content\\Core\\UI\\Map\\Texture"))
            copy_file_param_list.append(("Map_StartingPoint", "uasset", "Serializer\\Uasset", "Content\\Core\\UI\\Map\\Texture"))
        
        if config.getboolean("ItemRandomization", "bOverworldPool"):
            write_json_param_list.append(("PB_DT_CraftMaster", "Content\\Core\\DataTable", ClassManagement.craft_content, False))
            write_json_param_list.append(("MCANDLE",))
        else:
            copy_file_param_list.append(("PB_DT_CraftMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
        
        if config.getboolean("ItemRandomization", "bOverworldPool") or config.getboolean("GameMode", "bRandomizer") or config.getboolean("StartWith", "bDoubleJump") or config.getboolean("StartWith", "bAccelerator"):
            write_json_param_list.append(("PB_DT_DropRateMaster", "Content\\Core\\DataTable", ClassManagement.drop_content, False))
        else:
            copy_file_param_list.append(("PB_DT_DropRateMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
        
        if config.getboolean("ItemRandomization", "bQuestPool") or config.getboolean("ItemRandomization", "bQuestRequirements") or config.getboolean("GameMode", "bRandomizer") or self.string:
            write_json_param_list.append(("PB_DT_QuestMaster", "Content\\Core\\DataTable", ClassManagement.quest_content, False))
        
        if config.getboolean("ItemRandomization", "bShopPool") or config.getboolean("ShopRandomization", "bItemCostAndSellingPrice") or config.getboolean("GameMode", "bRandomizer"):
            write_json_param_list.append(("PB_DT_ItemMaster", "Content\\Core\\DataTable\\Item", ClassManagement.item_content, False))
        else:
            copy_file_param_list.append(("PB_DT_ItemMaster", "uasset", "Serializer", "Content\\Core\\DataTable\\Item"))
        
        if config.getboolean("ItemRandomization", "bQuestRequirements"):
            write_json_param_list.append(("PBScenarioStringTable", "Content\\L10N\\en\\Core\\StringTable", ClassManagement.scenario_content, False))
        
        if config.getboolean("LibraryRandomization", "bMapRequirements") or config.getboolean("LibraryRandomization", "bTomeAppearance"):
            write_json_param_list.append(("PB_DT_BookMaster", "Content\\Core\\DataTable", ClassManagement.book_content, True))
        else:
            copy_file_param_list.append(("PB_DT_BookMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
        
        if config.getboolean("EquipmentRandomization", "bGlobalGearStats") or config.getboolean("EquipmentRandomization", "bCheatGearStats"):
            write_json_param_list.append(("PB_DT_WeaponMaster", "Content\\Core\\DataTable", ClassManagement.weapon_content, True))
            write_json_param_list.append(("PBMasterStringTable", "Content\\L10N\\en\\Core\\StringTable", ClassManagement.master_content, False))
        else:
            copy_file_param_list.append(("PB_DT_WeaponMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
            copy_file_param_list.append(("PBMasterStringTable", "uasset", "Serializer", "Content\\L10N\\en\\Core\\StringTable"))
        
        if config.getboolean("EquipmentRandomization", "bGlobalGearStats") or config.getboolean("EquipmentRandomization", "bCheatGearStats") or config.getboolean("SpecialMode", "bProgressive"):
            write_json_param_list.append(("PB_DT_ArmorMaster", "Content\\Core\\DataTable", ClassManagement.armor_content, True))
        else:
            copy_file_param_list.append(("PB_DT_ArmorMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
        
        if config.getboolean("EnemyRandomization", "bEnemyLevels") or config.getboolean("EnemyRandomization", "bEnemyTolerances") or config.getboolean("GameDifficulty", "bHard") or config.getboolean("GameDifficulty", "bNightmare") or config.getboolean("SpecialMode", "bCustom") or config.getboolean("SpecialMode", "bProgressive"):
            write_json_param_list.append(("PB_DT_CharacterParameterMaster", "Content\\Core\\DataTable\\Enemy", ClassManagement.character_content, True))
        else:
            copy_file_param_list.append(("PB_DT_CharacterParameterMaster", "uasset", "Serializer", "Content\\Core\\DataTable\\Enemy"))
        
        if config.getboolean("EnemyRandomization", "bEnemyLevels") and not config.getboolean("SpecialMode", "bCustom"):
            write_json_param_list.append(("PB_DT_SpecialEffectDefinitionMaster", "Content\\Core\\DataTable", ClassManagement.effect_content, False))
        else:
            copy_file_param_list.append(("PB_DT_SpecialEffectDefinitionMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
        
        if config.getboolean("GraphicRandomization", "bMiriamColor"):
            copy_file_param_list.append(("T_Body01_01_Color", "uasset", "Serializer\\Uasset\\Hue\\Miriam\\" + miriam_hue, "Content\\Core\\Character\\P0000\\Texture\\Body"))
            copy_file_param_list.append(("T_Pl01_Cloth_Bace", "uasset", "Serializer\\Uasset\\Hue\\Miriam\\" + miriam_hue, "Content\\Core\\Character\\P0000\\Texture"))
            copy_file_param_list.append(("Face_Miriam", "uasset", "Serializer\\Uasset\\Hue\\Miriam\\" + miriam_hue, "Content\\Core\\UI\\HUD\\HUD_asset\\StateGauge\\0000"))
        
        if config.getboolean("GraphicRandomization", "bZangetsuColor"):
            copy_file_param_list.append(("T_N1011_body_color", "uasset", "Serializer\\Uasset\\Hue\\Zangetsu\\" + zangetsu_hue, "Content\\Core\\Character\\N1011\\Texture"))
            copy_file_param_list.append(("T_N1011_face_color", "uasset", "Serializer\\Uasset\\Hue\\Zangetsu\\" + zangetsu_hue, "Content\\Core\\Character\\N1011\\Texture"))
            copy_file_param_list.append(("T_N1011_weapon_color", "uasset", "Serializer\\Uasset\\Hue\\Zangetsu\\" + zangetsu_hue, "Content\\Core\\Character\\N1011\\Texture"))
            copy_file_param_list.append(("T_Tknife05_Base", "uasset", "Serializer\\Uasset\\Hue\\Zangetsu\\" + zangetsu_hue, "Content\\Core\\Item\\Weapon\\Tknife\\Tknife05\\Texture"))
            copy_file_param_list.append(("Face_Zangetsu", "uasset", "Serializer\\Uasset\\Hue\\Zangetsu\\" + zangetsu_hue, "Content\\Core\\UI\\HUD\\HUD_asset\\StateGauge\\0001"))
        
        if config.getboolean("SoundRandomization", "bDialogues"):
            write_json_param_list.append(("PB_DT_DialogueTableItems", "Content\\Core\\DataTable", ClassManagement.dialogue_content, True))
        
        if config.getboolean("ExtraRandomization", "bBloodlessCandles"):
            write_json_param_list.append(("BCANDLE", ClassBloodless.get_datatable()))
        
        if not config.getboolean("ExtraRandomization", "bBloodlessCandles") and not config.getboolean("SpecialMode", "bProgressive"):
            copy_file_param_list.append(("icon", "uasset", "Serializer\\Uasset", "Content\\Core\\UI\\UI_Pause\\Menu\\MainMenu\\Asset"))
            copy_file_param_list.append(("ACT50_BRM", "awb", "Serializer\\Awb", "Content\\Core\\Sound\\bgm"))

        if config.getboolean("GameDifficulty", "bNormal"):
            write_json_param_list.append(("PB_DT_BallisticMaster", "Content\\Core\\DataTable", ClassManagement.ballistic_content, True))
            write_json_param_list.append(("PB_DT_BulletMaster", "Content\\Core\\DataTable", ClassManagement.bullet_content, True))
            write_json_param_list.append(("PB_DT_CollisionMaster", "Content\\Core\\DataTable", ClassManagement.collision_content, True))
        else:
            copy_file_param_list.append(("PB_DT_BallisticMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
            copy_file_param_list.append(("PB_DT_BulletMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
            copy_file_param_list.append(("PB_DT_CollisionMaster", "uasset", "Serializer", "Content\\Core\\DataTable"))
        
        if config.getboolean("GameMode", "bRandomizer") or config.getboolean("SpecialMode", "bProgressive") or config.getboolean("EquipmentRandomization", "bGlobalGearStats") or config.getboolean("EnemyRandomization", "bEnemyLevels"):
            write_json_param_list.append(("PB_DT_CoordinateParameter", "Content\\Core\\DataTable", ClassManagement.coordinate_content, True))
        else:
            copy_file_param_list.append(("PB_DT_CoordinateParameter", "uasset", "Serializer", "Content\\Core\\DataTable"))
        
        #Process
        
        self.progress_bar = QProgressDialog("Generating...", None, 0, len(write_json_param_list) + 2, self)
        self.progress_bar.setWindowTitle("Status")
        self.progress_bar.setWindowModality(Qt.WindowModal)
        
        self.worker = Generate(self.string)
        self.worker.signaller.progress.connect(self.set_progress)
        self.worker.signaller.finished.connect(self.seed_finished)
        self.worker.start()
    
    def button_6_clicked(self):
        self.setEnabled(False)
        QApplication.processEvents()
        
        for i in os.listdir("Serializer\\Json"):
            name, extension = os.path.splitext(i)
            if os.path.getmtime("Serializer\\Json\\" + name + ".json") > os.path.getmtime("Serializer\\" + name + ".uasset"):
                json_list.append(name)
        if os.path.getmtime("MapEdit\\Data\\RoomMaster\\PB_DT_RoomMaster.json") > os.path.getmtime("Serializer\\PB_DT_RoomMaster.uasset"):
            json_list.append("PB_DT_RoomMaster")
        
        if json_list:
            self.progress_bar = QProgressDialog("Converting...", None, 0, len(json_list), self)
            self.progress_bar.setWindowTitle("Status")
            self.progress_bar.setWindowModality(Qt.WindowModal)
            
            self.worker = Convert()
            self.worker.signaller.progress.connect(self.set_progress)
            self.worker.signaller.finished.connect(self.convert_finished)
            self.worker.start()
        else:
            print("Nothing to convert")
            self.setEnabled(True)
    
    def button_7_clicked(self):
        label1_image = QLabel()
        label1_image.setPixmap(QPixmap("Data\\profile1.png"))
        label1_image.setScaledContents(True)
        label1_image.setFixedSize(config.getfloat("Misc", "fWindowSize")*60, config.getfloat("Misc", "fWindowSize")*60)
        label1_text = QLabel()
        label1_text.setText("<span style=\"font-weight: bold; color: #67aeff;\">Lakifume</span><br/>Author of True Randomization<br/><a href=\"https://github.com/Lakifume\"><font face=Cambria color=#67aeff>Github</font></a>")
        label1_text.setOpenExternalLinks(True)
        label2_image = QLabel()
        label2_image.setPixmap(QPixmap("Data\\profile2.png"))
        label2_image.setScaledContents(True)
        label2_image.setFixedSize(config.getfloat("Misc", "fWindowSize")*60, config.getfloat("Misc", "fWindowSize")*60)
        label2_text = QLabel()
        label2_text.setText("<span style=\"font-weight: bold; color: #e91e63;\">FatihG_</span><br/>Founder of Bloodstained Modding<br/><a href=\"http://discord.gg/b9XBH4f\"><font face=Cambria color=#e91e63>Discord</font></a>")
        label2_text.setOpenExternalLinks(True)
        label3_image = QLabel()
        label3_image.setPixmap(QPixmap("Data\\profile3.png"))
        label3_image.setScaledContents(True)
        label3_image.setFixedSize(config.getfloat("Misc", "fWindowSize")*60, config.getfloat("Misc", "fWindowSize")*60)
        label3_text = QLabel()
        label3_text.setText("<span style=\"font-weight: bold; color: #e6b31a;\">Joneirik</span><br/>Datatable researcher<br/><a href=\"http://wiki.omf2097.com/doku.php?id=joneirik:bs:start\"><font face=Cambria color=#e6b31a>Wiki</font></a>")
        label3_text.setOpenExternalLinks(True)
        label4_image = QLabel()
        label4_image.setPixmap(QPixmap("Data\\profile4.png"))
        label4_image.setScaledContents(True)
        label4_image.setFixedSize(config.getfloat("Misc", "fWindowSize")*60, config.getfloat("Misc", "fWindowSize")*60)
        label4_text = QLabel()
        label4_text.setText("<span style=\"font-weight: bold; color: #25c04e;\">BadmoonZ</span><br/>Randomizer researcher<br/><a href=\"https://github.com/BadmoonzZ/Bloodstained\"><font face=Cambria color=#25c04e>Github</font></a>")
        label4_text.setOpenExternalLinks(True)
        label5_image = QLabel()
        label5_image.setPixmap(QPixmap("Data\\profile5.png"))
        label5_image.setScaledContents(True)
        label5_image.setFixedSize(config.getfloat("Misc", "fWindowSize")*60, config.getfloat("Misc", "fWindowSize")*60)
        label5_text = QLabel()
        label5_text.setText("<span style=\"font-weight: bold; color: #7b9aff;\">Chrisaegrimm</span><br/>Testing and suffering<br/><a href=\"https://www.twitch.tv/chrisaegrimm\"><font face=Cambria color=#7b9aff>Twitch</font></a>")
        label5_text.setOpenExternalLinks(True)
        label6_image = QLabel()
        label6_image.setPixmap(QPixmap("Data\\profile6.png"))
        label6_image.setScaledContents(True)
        label6_image.setFixedSize(config.getfloat("Misc", "fWindowSize")*60, config.getfloat("Misc", "fWindowSize")*60)
        label6_text = QLabel()
        label6_text.setText("<span style=\"font-weight: bold; color: #ffa9a8;\">Giwayume</span><br/>Creator of Bloodstained Level Editor<br/><a href=\"https://github.com/Giwayume/BloodstainedLevelEditor\"><font face=Cambria color=#ffa9a8>Github</font></a>")
        label6_text.setOpenExternalLinks(True)
        label7_image = QLabel()
        label7_image.setPixmap(QPixmap("Data\\profile7.png"))
        label7_image.setScaledContents(True)
        label7_image.setFixedSize(config.getfloat("Misc", "fWindowSize")*60, config.getfloat("Misc", "fWindowSize")*60)
        label7_text = QLabel()
        label7_text.setText("<span style=\"font-weight: bold; color: #db1ee9;\">Atenfyr</span><br/>Creator of UAssetAPI<br/><a href=\"https://github.com/atenfyr/UAssetAPI\"><font face=Cambria color=#db1ee9>Github</font></a>")
        label7_text.setOpenExternalLinks(True)
        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(label1_image, 0, 0, 1, 1)
        layout.addWidget(label1_text, 0, 1, 1, 1)
        layout.addWidget(label2_image, 1, 0, 1, 1)
        layout.addWidget(label2_text, 1, 1, 1, 1)
        layout.addWidget(label3_image, 2, 0, 1, 1)
        layout.addWidget(label3_text, 2, 1, 1, 1)
        layout.addWidget(label4_image, 3, 0, 1, 1)
        layout.addWidget(label4_text, 3, 1, 1, 1)
        layout.addWidget(label6_image, 4, 0, 1, 1)
        layout.addWidget(label6_text, 4, 1, 1, 1)
        layout.addWidget(label7_image, 5, 0, 1, 1)
        layout.addWidget(label7_text, 5, 1, 1, 1)
        layout.addWidget(label5_image, 6, 0, 1, 1)
        layout.addWidget(label5_text, 6, 1, 1, 1)
        box = QDialog(self)
        box.setLayout(layout)
        box.setWindowTitle("Credits")
        box.exec()
    
    def install_3(self):
        label = QLabel()
        label.setText("<span style=\"font-weight: bold; color: #e06666;\">.NET Runtime 3.0 Preview 8</span> is currently not installed, it is required for datatable conversion:<br/><a href=\"https://dotnet.microsoft.com/download/thank-you/dotnet-runtime-3.0.0-preview8-windows-x64-installer\"><font face=Cambria color=#f6b26b>64bit Installer</font></a><br/><a href=\"https://dotnet.microsoft.com/download/thank-you/dotnet-runtime-3.0.0-preview8-windows-x86-installer\"><font face=Cambria color=#f6b26b>32bit Installer</font></a>")
        label.setOpenExternalLinks(True)
        layout = QVBoxLayout()
        layout.addWidget(label)
        box = QDialog(self)
        box.setLayout(layout)
        box.setWindowTitle("Install")
        box.exec()
    
    def no_path(self):
        box = QMessageBox(self)
        box.setWindowTitle("Error")
        box.setIcon(QMessageBox.Critical)
        box.setText("Output path invalid.")
        box.exec()
    
    def error(self):
        box = QMessageBox(self)
        box.setWindowTitle("Error")
        box.setIcon(QMessageBox.Critical)
        box.setText("MapEditor.exe is running, cannot overwrite.")
        box.exec()
    
    def check_for_updates(self):
        if os.path.isfile("OldRandomizer.exe"):
            os.remove("OldRandomizer.exe")
        try:
            api = requests.get("https://api.github.com/repos/Lakifume/True-Randomization/releases/latest").json()
        except requests.ConnectionError:
            self.check_for_resolution()
            return
        try:
            tag = api["tag_name"]
        except KeyError:
            self.check_for_resolution()
            return
        if tag != config.get("Misc", "sVersion"):
            choice = QMessageBox.question(self, "Auto Updater", "New version found:\n\n" + api["body"] + "\n\nUpdate ?", QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                if "MapEditor.exe" in (i.name() for i in psutil.process_iter()):
                    self.error()
                    self.check_for_resolution()
                    return
                
                self.progress_bar = QProgressDialog("Downloading...", None, 0, api["assets"][0]["size"], self)
                self.progress_bar.setWindowTitle("Status")
                self.progress_bar.setWindowModality(Qt.WindowModal)
                self.progress_bar.setAutoClose(False)
                self.progress_bar.setAutoReset(False)
                
                self.worker = Update(self.progress_bar, api)
                self.worker.signaller.progress.connect(self.set_progress)
                self.worker.start()
            else:
                self.check_for_resolution()
        else:
            self.check_for_resolution()
    
    def check_for_resolution(self):
        if self.first_time:
            self.button_3_clicked()
        self.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(writing_and_exit)
    main = Main()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()