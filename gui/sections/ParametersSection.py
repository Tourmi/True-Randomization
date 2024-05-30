from __future__ import annotations

import glob

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QRadioButton
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QDialog

from . import ModifiedFilesSection
from randomizer.Constants import *
from configuration import Config
from configuration import ConfigSections

map_num = len(glob.glob("MapEdit\\Custom\\*.json"))

preset_to_bytes = {
    "Empty": 0x000000,
    "Trial": 0x3807FF,
    "Race":  0x5806EF,
    "Meme":  0x7F3AAF,
    "Risk":  0x7FFFFF,
    "Blood": 0x980001
}
bytes_to_preset = {value: key for key, value in preset_to_bytes.items()}

main_param_length = 6
sub_param_length = 6
main_widget_to_param : dict[QCheckBox, int] = {}
sub_widget_to_param : dict[QPushButton, int] = {}
spin_index_to_shift = {1: 0, 2: 2, 3: 1}
shift_to_spin_index = {value: key for key, value in spin_index_to_shift.items()}

item_color    = "#ff8080"
shop_color    = "#ffff80"
library_color = "#bf80ff"
shard_color   = "#80ffff"
equip_color   = "#80ff80"
enemy_color   = "#80bfff"
map_color     = "#ffbf80"
graphic_color = "#80ffbf"
sound_color   = "#ff80ff"
extra_color   = "#ff80bf"

class ParametersSection(QWidget):
    def __init__(self, parent : QWidget, config : Config, size_multiplier : float, modified_files : ModifiedFilesSection) -> None:
        super().__init__(parent)
        self.config = config
        self.size_multiplier = size_multiplier
        self.modified_files = modified_files

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setVerticalSpacing(int(self.size_multiplier*10))
        self.setLayout(layout)
        
        #Groupboxes
        center_box_1_layout = QGridLayout()
        self.center_box_1 = QGroupBox("Item Randomization")
        self.center_box_1.setLayout(center_box_1_layout)
        layout.addWidget(self.center_box_1, 0, 0, 2, 2)

        center_box_2_layout = QGridLayout()
        self.center_box_2 = QGroupBox("Shop Randomization")
        self.center_box_2.setLayout(center_box_2_layout)
        layout.addWidget(self.center_box_2, 2, 0, 1, 2)

        center_box_3_layout = QGridLayout()
        self.center_box_3 = QGroupBox("Library Randomization")
        self.center_box_3.setLayout(center_box_3_layout)
        layout.addWidget(self.center_box_3, 3, 0, 1, 2)

        center_box_4_layout = QGridLayout()
        self.center_box_4 = QGroupBox("Shard Randomization")
        self.center_box_4.setLayout(center_box_4_layout)
        layout.addWidget(self.center_box_4, 4, 0, 1, 2)

        center_box_5_layout = QGridLayout()
        self.center_box_5 = QGroupBox("Equipment Randomization")
        self.center_box_5.setLayout(center_box_5_layout)
        layout.addWidget(self.center_box_5, 5, 0, 1, 2)

        center_box_6_layout = QGridLayout()
        self.center_box_6 = QGroupBox("Enemy Randomization")
        self.center_box_6.setLayout(center_box_6_layout)
        layout.addWidget(self.center_box_6, 0, 2, 2, 2)

        center_box_7_layout = QGridLayout()
        self.center_box_7 = QGroupBox("Map Randomization")
        self.center_box_7.setLayout(center_box_7_layout)
        layout.addWidget(self.center_box_7, 2, 2, 1, 2)

        center_box_8_layout = QGridLayout()
        self.center_box_8 = QGroupBox("Graphic Randomization")
        self.center_box_8.setLayout(center_box_8_layout)
        layout.addWidget(self.center_box_8, 3, 2, 1, 2)

        center_box_9_layout = QGridLayout()
        self.center_box_9 = QGroupBox("Sound Randomization")
        self.center_box_9.setLayout(center_box_9_layout)
        layout.addWidget(self.center_box_9, 4, 2, 1, 2)
        
        center_box_10_layout = QGridLayout()
        self.center_box_10 = QGroupBox("Extra Randomization")
        self.center_box_10.setLayout(center_box_10_layout)
        layout.addWidget(self.center_box_10, 5, 2, 1, 2)
        
        center_box_16_layout = QGridLayout()
        center_box_16 = QGroupBox("Start With")
        center_box_16.setLayout(center_box_16_layout)
        layout.addWidget(center_box_16, 7, 0, 1, 2)
        
        center_box_11_layout = QGridLayout()
        center_box_11 = QGroupBox("Game Difficulty")
        center_box_11.setLayout(center_box_11_layout)
        layout.addWidget(center_box_11, 6, 0, 1, 2)
        
        center_box_17_layout = QGridLayout()
        center_box_17 = QGroupBox("Special Mode")
        center_box_17.setLayout(center_box_17_layout)
        layout.addWidget(center_box_17, 6, 2, 1, 2)
        
        
        center_box_13_layout = QGridLayout()
        center_box_13 = QGroupBox("Parameter String")
        center_box_13.setLayout(center_box_13_layout)
        layout.addWidget(center_box_13, 7, 2, 1, 2)
        
        center_box_12_layout = QGridLayout()
        center_box_12 = QGroupBox("Presets")
        center_box_12.setLayout(center_box_12_layout)
        layout.addWidget(center_box_12, 8, 0, 1, 2)
        
        center_box_14_layout = QGridLayout()
        self.center_box_14 = QGroupBox("Game Path")
        self.center_box_14.setLayout(center_box_14_layout)
        layout.addWidget(self.center_box_14, 8, 2, 1, 2)

        
        #Checkboxes
        self.check_box_1 = QCheckBox("Overworld Pool")
        self.check_box_1.setToolTip("Randomize all items and shards found in the overworld, now with\nnew improved logic. Everything you pick up will be 100% random\nso say goodbye to the endless sea of fried fish.")
        self.check_box_1.stateChanged.connect(self.check_box_1_changed)
        center_box_1_layout.addWidget(self.check_box_1, 0, 0)
        main_widget_to_param[self.check_box_1] = 0x000001

        self.check_box_16 = QCheckBox("Quest Pool")
        self.check_box_16.setToolTip("Randomize all quest rewards.")
        self.check_box_16.stateChanged.connect(self.check_box_16_changed)
        center_box_1_layout.addWidget(self.check_box_16, 1, 0)
        main_widget_to_param[self.check_box_16] = 0x000002

        self.check_box_2 = QCheckBox("Shop Pool")
        self.check_box_2.setToolTip("Randomize all items sold at the shop.")
        self.check_box_2.stateChanged.connect(self.check_box_2_changed)
        center_box_1_layout.addWidget(self.check_box_2, 2, 0)
        main_widget_to_param[self.check_box_2] = 0x000004

        self.check_box_17 = QCheckBox("Quest Requirements")
        self.check_box_17.setToolTip("Randomize the requirements for Susie, Abigail and Lindsay's quests.\nBenjamin will still ask you for waystones.")
        self.check_box_17.stateChanged.connect(self.check_box_17_changed)
        center_box_1_layout.addWidget(self.check_box_17, 3, 0)
        main_widget_to_param[self.check_box_17] = 0x000008

        self.check_box_18 = QCheckBox("Remove Infinites")
        self.check_box_18.setToolTip("Guarantee Gebel's Glasses and Recycle Hat to never appear.\nUseful for runs that favor magic and bullet management.")
        self.check_box_18.stateChanged.connect(self.check_box_18_changed)
        center_box_1_layout.addWidget(self.check_box_18, 4, 0)
        main_widget_to_param[self.check_box_18] = 0x000010

        self.check_box_3 = QCheckBox("Item Cost And Selling Price")
        self.check_box_3.setToolTip("Randomize the cost and selling price of every item in the shop.")
        self.check_box_3.stateChanged.connect(self.check_box_3_changed)
        center_box_2_layout.addWidget(self.check_box_3, 0, 0)
        main_widget_to_param[self.check_box_3] = 0x000020

        self.check_box_4 = QCheckBox("Scale Selling Price With Cost")
        self.check_box_4.setToolTip("Make the selling price scale with the item's random cost.")
        self.check_box_4.stateChanged.connect(self.check_box_4_changed)
        center_box_2_layout.addWidget(self.check_box_4, 1, 0)
        main_widget_to_param[self.check_box_4] = 0x000040

        self.check_box_5 = QCheckBox("Map Requirements")
        self.check_box_5.setToolTip("Randomize the completion requirement for each tome.")
        self.check_box_5.stateChanged.connect(self.check_box_5_changed)
        center_box_3_layout.addWidget(self.check_box_5, 0, 0)
        main_widget_to_param[self.check_box_5] = 0x000080

        self.check_box_6 = QCheckBox("Tome Appearance")
        self.check_box_6.setToolTip("Randomize which books are available in the game at all.\nDoes not affect Tome of Conquest.")
        self.check_box_6.stateChanged.connect(self.check_box_6_changed)
        center_box_3_layout.addWidget(self.check_box_6, 1, 0)
        main_widget_to_param[self.check_box_6] = 0x000100

        self.check_box_7 = QCheckBox("Shard Power And Magic Cost")
        self.check_box_7.setToolTip("Randomize the efficiency and MP cost of each shard.\nDoes not affect progression shards.")
        self.check_box_7.stateChanged.connect(self.check_box_7_changed)
        center_box_4_layout.addWidget(self.check_box_7, 0, 0)
        main_widget_to_param[self.check_box_7] = 0x000200

        self.check_box_8 = QCheckBox("Scale Magic Cost With Power")
        self.check_box_8.setToolTip("Make the MP cost scale with the shard's random power.")
        self.check_box_8.stateChanged.connect(self.check_box_8_changed)
        center_box_4_layout.addWidget(self.check_box_8, 1, 0)
        main_widget_to_param[self.check_box_8] = 0x000400

        self.check_box_23 = QCheckBox("Global Gear Stats")
        self.check_box_23.setToolTip("Slightly randomize the stats of all weapons and pieces of\nequipment with odds that still favor their original values.")
        self.check_box_23.stateChanged.connect(self.check_box_23_changed)
        center_box_5_layout.addWidget(self.check_box_23, 0, 0)
        main_widget_to_param[self.check_box_23] = 0x000800

        self.check_box_9 = QCheckBox("Cheat Gear Stats")
        self.check_box_9.setToolTip("Completely randomize the stats of the weapons, headgears\nand accessories that are originally obtained via cheatcodes.")
        self.check_box_9.stateChanged.connect(self.check_box_9_changed)
        center_box_5_layout.addWidget(self.check_box_9, 1, 0)
        main_widget_to_param[self.check_box_9] = 0x001000

        self.check_box_25 = QCheckBox("Enemy Locations")
        self.check_box_25.setToolTip("Randomize which enemies appear where.")
        self.check_box_25.stateChanged.connect(self.check_box_25_changed)
        center_box_6_layout.addWidget(self.check_box_25, 0, 0)
        main_widget_to_param[self.check_box_25] = 0x002000

        self.check_box_10 = QCheckBox("Enemy Levels")
        self.check_box_10.setToolTip("Randomize the level of every enemy. Stats that scale with\nlevel include HP, attack, defense, luck, EXP and expertise.\nPicking this option will give you more starting HP and MP\nand reduce their growth to compensate.")
        self.check_box_10.stateChanged.connect(self.check_box_10_changed)
        center_box_6_layout.addWidget(self.check_box_10, 1, 0)
        main_widget_to_param[self.check_box_10] = 0x004000

        self.check_box_26 = QCheckBox("Boss Levels")
        self.check_box_26.setToolTip("Only recommended for Miriam mode.")
        self.check_box_26.stateChanged.connect(self.check_box_26_changed)
        center_box_6_layout.addWidget(self.check_box_26, 2, 0)
        main_widget_to_param[self.check_box_26] = 0x008000

        self.check_box_11 = QCheckBox("Enemy Tolerances")
        self.check_box_11.setToolTip("Randomize the first 8 resistance/weakness attributes of every enemy.")
        self.check_box_11.stateChanged.connect(self.check_box_11_changed)
        center_box_6_layout.addWidget(self.check_box_11, 3, 0)
        main_widget_to_param[self.check_box_11] = 0x010000

        self.check_box_27 = QCheckBox("Boss Tolerances")
        self.check_box_27.setToolTip("Only recommended for Miriam mode.")
        self.check_box_27.stateChanged.connect(self.check_box_27_changed)
        center_box_6_layout.addWidget(self.check_box_27, 4, 0)
        main_widget_to_param[self.check_box_27] = 0x020000

        self.check_box_12 = QCheckBox("Room Layout")
        self.check_box_12.setToolTip(f"Randomly pick from a folder of map presets ({map_num}).")
        self.check_box_12.stateChanged.connect(self.check_box_12_changed)
        center_box_7_layout.addWidget(self.check_box_12, 0, 0)
        main_widget_to_param[self.check_box_12] = 0x040000

        self.check_box_13 = QCheckBox("Outfit Color")
        self.check_box_13.setToolTip("Randomize the color of Miriam's and Zangetsu's outfits.")
        self.check_box_13.stateChanged.connect(self.check_box_13_changed)
        center_box_8_layout.addWidget(self.check_box_13, 0, 0)
        main_widget_to_param[self.check_box_13] = 0x080000

        self.check_box_24 = QCheckBox("Backer Portraits")
        self.check_box_24.setToolTip("Shuffle backer paintings.")
        self.check_box_24.stateChanged.connect(self.check_box_24_changed)
        center_box_8_layout.addWidget(self.check_box_24, 1, 0)
        main_widget_to_param[self.check_box_24] = 0x100000

        self.check_box_15 = QCheckBox("Dialogues")
        self.check_box_15.setToolTip("Randomize all conversation lines in the game. Characters\nwill still retain their actual voice (let's not get weird).")
        self.check_box_15.stateChanged.connect(self.check_box_15_changed)
        center_box_9_layout.addWidget(self.check_box_15, 0, 0)
        main_widget_to_param[self.check_box_15] = 0x200000

        self.check_box_14 = QCheckBox("Background Music")
        self.check_box_14.setToolTip("Randomize the music tracks that play in different areas.")
        self.check_box_14.stateChanged.connect(self.check_box_14_changed)
        center_box_9_layout.addWidget(self.check_box_14, 1, 0)
        main_widget_to_param[self.check_box_14] = 0x400000

        self.check_box_21 = QCheckBox("Bloodless Candles")
        self.check_box_21.setToolTip("Randomize candle placement in Bloodless mode.")
        self.check_box_21.stateChanged.connect(self.check_box_21_changed)
        center_box_10_layout.addWidget(self.check_box_21, 0, 0)
        main_widget_to_param[self.check_box_21] = 0x800000
        
        #SpinButtons
        
        self.spin_button_1 = QPushButton()
        self.spin_button_1.setAccessibleName("spin_button_1")
        self.spin_button_1.setToolTip("Logic complexity. Higher values usually follow a\nprogression chain.")
        self.spin_button_1.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_1.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_1.clicked.connect(self.spin_button_1_clicked)
        self.spin_button_1.setVisible(False)
        center_box_1_layout.addWidget(self.spin_button_1, 0, 1)
        sub_widget_to_param[self.spin_button_1] = 0x001
        
        self.spin_button_2 = QPushButton()
        self.spin_button_2.setAccessibleName("spin_button_2")
        self.spin_button_2.setToolTip("Weight of shop items locked behind events.")
        self.spin_button_2.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_2.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_2.clicked.connect(self.spin_button_2_clicked)
        self.spin_button_2.setVisible(False)
        center_box_1_layout.addWidget(self.spin_button_2, 2, 1)
        sub_widget_to_param[self.spin_button_2] = 0x002
        
        self.spin_button_3 = QPushButton()
        self.spin_button_3.setAccessibleName("spin_button_3")
        self.spin_button_3.setToolTip("Price weight. The higher the value the more extreme\nthe price differences.")
        self.spin_button_3.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_3.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_3.clicked.connect(self.spin_button_3_clicked)
        self.spin_button_3.setVisible(False)
        center_box_2_layout.addWidget(self.spin_button_3, 0, 1)
        sub_widget_to_param[self.spin_button_3] = 0x004
        
        self.spin_button_4 = QPushButton()
        self.spin_button_4.setAccessibleName("spin_button_4")
        self.spin_button_4.setToolTip("Requirement weight. 2 is linear, 1 and 3 favor early and\nlate map completion respectively.")
        self.spin_button_4.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_4.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_4.clicked.connect(self.spin_button_4_clicked)
        self.spin_button_4.setVisible(False)
        center_box_3_layout.addWidget(self.spin_button_4, 0, 1)
        sub_widget_to_param[self.spin_button_4] = 0x008
        
        self.spin_button_5 = QPushButton()
        self.spin_button_5.setAccessibleName("spin_button_5")
        self.spin_button_5.setToolTip("Power weight. The higher the value the more extreme\nthe power differences.")
        self.spin_button_5.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_5.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_5.clicked.connect(self.spin_button_5_clicked)
        self.spin_button_5.setVisible(False)
        center_box_4_layout.addWidget(self.spin_button_5, 0, 1)
        sub_widget_to_param[self.spin_button_5] = 0x010
        
        self.spin_button_6 = QPushButton()
        self.spin_button_6.setAccessibleName("spin_button_6")
        self.spin_button_6.setToolTip("Stat weight. The higher the value the more extreme\nthe stat differences.")
        self.spin_button_6.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_6.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_6.clicked.connect(self.spin_button_6_clicked)
        self.spin_button_6.setVisible(False)
        center_box_5_layout.addWidget(self.spin_button_6, 0, 1)
        sub_widget_to_param[self.spin_button_6] = 0x020
        
        self.spin_button_8 = QPushButton()
        self.spin_button_8.setAccessibleName("spin_button_8")
        self.spin_button_8.setToolTip("Level weight. The higher the value the more extreme\nthe level differences.")
        self.spin_button_8.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_8.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_8.clicked.connect(self.spin_button_8_clicked)
        self.spin_button_8.setVisible(False)
        center_box_6_layout.addWidget(self.spin_button_8, 1, 1)
        sub_widget_to_param[self.spin_button_8] = 0x040
        
        self.spin_button_9 = QPushButton()
        self.spin_button_9.setAccessibleName("spin_button_9")
        self.spin_button_9.setToolTip("Level weight. The higher the value the more extreme\nthe level differences.")
        self.spin_button_9.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_9.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_9.clicked.connect(self.spin_button_9_clicked)
        self.spin_button_9.setVisible(False)
        center_box_6_layout.addWidget(self.spin_button_9, 2, 1)
        sub_widget_to_param[self.spin_button_9] = 0x080
        
        self.spin_button_10 = QPushButton()
        self.spin_button_10.setAccessibleName("spin_button_10")
        self.spin_button_10.setToolTip("Tolerance weight. The higher the value the more extreme\nthe tolerance differences.")
        self.spin_button_10.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_10.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_10.clicked.connect(self.spin_button_10_clicked)
        self.spin_button_10.setVisible(False)
        center_box_6_layout.addWidget(self.spin_button_10, 3, 1)
        sub_widget_to_param[self.spin_button_10] = 0x100
        
        self.spin_button_11 = QPushButton()
        self.spin_button_11.setAccessibleName("spin_button_11")
        self.spin_button_11.setToolTip("Tolerance weight. The higher the value the more extreme\nthe tolerance differences.")
        self.spin_button_11.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_11.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_11.clicked.connect(self.spin_button_11_clicked)
        self.spin_button_11.setVisible(False)
        center_box_6_layout.addWidget(self.spin_button_11, 4, 1)
        sub_widget_to_param[self.spin_button_11] = 0x200
        
        self.browse_map_button = QPushButton()
        self.browse_map_button.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.browse_map_button.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.browse_map_button.clicked.connect(self.browse_map_button_clicked)
        self.browse_map_button.setVisible(False)
        center_box_7_layout.addWidget(self.browse_map_button, 0, 1)
        
        self.outfit_config_button = QPushButton()
        self.outfit_config_button.setIcon(QPixmap("Data\\config.png"))
        self.outfit_config_button.setToolTip("Configure which outfit colors can be chosen.")
        self.outfit_config_button.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.outfit_config_button.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.outfit_config_button.clicked.connect(self.outfit_config_button_clicked)
        self.outfit_config_button.setVisible(False)
        center_box_8_layout.addWidget(self.outfit_config_button, 0, 1)
        
        self.language_sequence = "JE"
        self.spin_button_12 = QPushButton()
        self.spin_button_12.setAccessibleName("spin_button_12")
        self.spin_button_12.setToolTip("Voice language")
        self.spin_button_12.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_12.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_12.clicked.connect(self.spin_button_12_clicked)
        self.spin_button_12.setVisible(False)
        center_box_9_layout.addWidget(self.spin_button_12, 0, 1)
        sub_widget_to_param[self.spin_button_12] = 0x400
        
        self.spin_button_13 = QPushButton()
        self.spin_button_13.setAccessibleName("spin_button_13")
        self.spin_button_13.setToolTip("Logic complexity. Higher values usually follow a\nprogression chain.")
        self.spin_button_13.setStyleSheet("QPushButton{color: #ffffff; font-family: Impact}" + "QToolTip{color: #ffffff; font-family: Cambria}")
        self.spin_button_13.setFixedSize(int(self.size_multiplier*28), int(self.size_multiplier*24))
        self.spin_button_13.clicked.connect(self.spin_button_13_clicked)
        self.spin_button_13.setVisible(False)
        center_box_10_layout.addWidget(self.spin_button_13, 0, 1)
        sub_widget_to_param[self.spin_button_13] = 0x800
        
        #RadioButtons
        
        self.radio_button_1 = QRadioButton("Normal")
        self.radio_button_1.setToolTip("More like easy mode.")
        self.radio_button_1.toggled.connect(self.radio_button_group_1_checked)
        center_box_11_layout.addWidget(self.radio_button_1, 0, 0)
        
        self.radio_button_2 = QRadioButton("Hard")
        self.radio_button_2.setToolTip("The real normal mode.")
        self.radio_button_2.toggled.connect(self.radio_button_group_1_checked)
        center_box_11_layout.addWidget(self.radio_button_2, 1, 0)
        
        self.radio_button_3 = QRadioButton("Nightmare")
        self.radio_button_3.setToolTip("Shit's gonna get real.")
        self.radio_button_3.toggled.connect(self.radio_button_group_1_checked)
        center_box_11_layout.addWidget(self.radio_button_3, 0, 1)
        
        self.radio_button_4 = QRadioButton("None")
        self.radio_button_4.setToolTip("No special game mode.")
        self.radio_button_4.toggled.connect(self.radio_button_group_2_checked)
        center_box_17_layout.addWidget(self.radio_button_4, 0, 0)
        
        self.radio_button_5 = QRadioButton("Custom NG+")
        self.radio_button_5.setToolTip("Play through your NG+ files with a chosen level\nvalue for all enemies.")
        self.radio_button_5.toggled.connect(self.radio_button_group_2_checked)
        center_box_17_layout.addWidget(self.radio_button_5, 1, 0)
        
        self.radio_button_6 = QRadioButton("Progressive Z")
        self.radio_button_6.setToolTip("Play through a more balanced version of Zangetsu\nmode where his stats scale with progression.")
        self.radio_button_6.toggled.connect(self.radio_button_group_2_checked)
        center_box_17_layout.addWidget(self.radio_button_6, 0, 1)
        
        #Spin boxes
        
        self.config.set(ConfigSections.special_mode.custom_ng_level, str(min(max(self.config.getint(ConfigSections.special_mode.custom_ng_level), 1), 99)))
        
        self.custom_level_field = QSpinBox()
        self.custom_level_field.setToolTip("Level of all enemies.")
        self.custom_level_field.setRange(1, 99)
        self.custom_level_field.setValue(self.config.getint(ConfigSections.special_mode.custom_ng_level))
        self.custom_level_field.valueChanged.connect(self.custom_level_field_changed)
        self.custom_level_field.setVisible(False)
        center_box_17_layout.addWidget(self.custom_level_field, 1, 1)
        
        #Dropdown lists
        
        self.preset_drop_down = QComboBox()
        self.preset_drop_down.setToolTip("EMPTY: Clear all options.\nTRIAL: To get started with this mod.\nRACE: Most fitting for a King of Speed.\nMEME: Time to break the game.\nRISK: Chaos awaits !\nBLOOD: She needs more blood.")
        self.preset_drop_down.addItem("Custom")
        for preset in preset_to_bytes:
            self.preset_drop_down.addItem(preset)
        self.preset_drop_down.currentIndexChanged.connect(self.preset_drop_down_changed)
        center_box_12_layout.addWidget(self.preset_drop_down, 0, 0)
        
        
        #Text field
        
        self.starting_items_field = QLineEdit(self.config.get(ConfigSections.start_with.items))
        self.starting_items_field.setToolTip("Items to start with. Input their english names with\ncommas as separators. If unsure refer to the files\nin Data\\Translation for item names.")
        self.starting_items_field.textChanged.connect(self.starting_items_field_changed)
        center_box_16_layout.addWidget(self.starting_items_field, 0, 0)
        
        self.param_string_format = "{:0" + str(main_param_length + sub_param_length) + "x}"
        self.param_string_field = QLineEdit(self.param_string_format.format(0).upper())
        self.param_string_field.setMaxLength(main_param_length + sub_param_length)
        self.param_string_field.setToolTip("Simplified string containing all the randomization settings.")
        self.param_string_field.textChanged.connect(self.param_string_field_changed)
        center_box_13_layout.addWidget(self.param_string_field, 0, 0)
        
        self.game_path_field = QLineEdit(self.config.get(ConfigSections.misc.game_path))
        self.game_path_field.setToolTip("Path to your game's data (...\\steamapps\\common\\Bloodstained Ritual of the Night).")
        self.game_path_field.textChanged.connect(self.game_path_field_changed)
        center_box_14_layout.addWidget(self.game_path_field, 0, 0)
        
        browse_game_path_button = QPushButton()
        browse_game_path_button.setIcon(QPixmap("Data\\browse.png"))
        browse_game_path_button.clicked.connect(self.browse_game_path_button_clicked)
        center_box_14_layout.addWidget(browse_game_path_button, 0, 1)
        
        #Init checkboxes
        
        self.check_box_1.setChecked(self.config.getboolean(ConfigSections.item.overworld_pool))
        self.check_box_2.setChecked(self.config.getboolean(ConfigSections.item.shop_pool))
        self.check_box_16.setChecked(self.config.getboolean(ConfigSections.item.quest_pool))
        self.check_box_17.setChecked(self.config.getboolean(ConfigSections.item.quest_requirements))
        self.check_box_18.setChecked(self.config.getboolean(ConfigSections.item.remove_infinites))
        self.check_box_3.setChecked(self.config.getboolean(ConfigSections.shop.item_values))
        self.check_box_4.setChecked(self.config.getboolean(ConfigSections.shop.scale_selling_price_with_cost))
        self.check_box_5.setChecked(self.config.getboolean(ConfigSections.library.map_requirements))
        self.check_box_6.setChecked(self.config.getboolean(ConfigSections.library.tome_appearance))
        self.check_box_7.setChecked(self.config.getboolean(ConfigSections.shard.randomize_shard_power_and_cost))
        self.check_box_8.setChecked(self.config.getboolean(ConfigSections.shard.scale_cost_with_power))
        self.check_box_23.setChecked(self.config.getboolean(ConfigSections.equipment.global_gear_stats))
        self.check_box_9.setChecked(self.config.getboolean(ConfigSections.equipment.chest_gear_stats))
        self.check_box_25.setChecked(self.config.getboolean(ConfigSections.enemy.enemy_locations))
        self.check_box_10.setChecked(self.config.getboolean(ConfigSections.enemy.enemy_levels))
        self.check_box_26.setChecked(self.config.getboolean(ConfigSections.enemy.boss_levels))
        self.check_box_11.setChecked(self.config.getboolean(ConfigSections.enemy.enemy_tolerances))
        self.check_box_27.setChecked(self.config.getboolean(ConfigSections.enemy.boss_tolerances))
        self.check_box_12.setChecked(self.config.getboolean(ConfigSections.map.room_layout))
        self.check_box_13.setChecked(self.config.getboolean(ConfigSections.graphics.outfit_color))
        self.check_box_24.setChecked(self.config.getboolean(ConfigSections.graphics.backer_portraits))
        self.check_box_15.setChecked(self.config.getboolean(ConfigSections.sound.dialogues))
        self.check_box_14.setChecked(self.config.getboolean(ConfigSections.sound.music))
        self.check_box_21.setChecked(self.config.getboolean(ConfigSections.extra.bloodless_candles))
        
        self.spin_button_1_set_index(self.config.getint(ConfigSections.item.overworld_pool_complexity))
        self.spin_button_2_set_index(self.config.getint(ConfigSections.item.shop_pool_weight))
        self.spin_button_3_set_index(self.config.getint(ConfigSections.shop.item_values_weight))
        self.spin_button_4_set_index(self.config.getint(ConfigSections.library.map_requirements_weight))
        self.spin_button_5_set_index(self.config.getint(ConfigSections.shard.shard_power_and_cost_weight))
        self.spin_button_6_set_index(self.config.getint(ConfigSections.equipment.global_gear_stats_weight))
        self.spin_button_8_set_index(self.config.getint(ConfigSections.enemy.enemy_levels_weight))
        self.spin_button_9_set_index(self.config.getint(ConfigSections.enemy.boss_levels_weight))
        self.spin_button_10_set_index(self.config.getint(ConfigSections.enemy.enemy_tolerances_weight))
        self.spin_button_11_set_index(self.config.getint(ConfigSections.enemy.boss_tolerances_weight))
        self.spin_button_12_set_index(self.config.getint(ConfigSections.sound.dialogues_language))
        self.spin_button_13_set_index(self.config.getint(ConfigSections.extra.bloodless_candles_complexity))
        
        self.radio_button_1.setChecked(self.config.getboolean(ConfigSections.difficulty.normal))
        self.radio_button_2.setChecked(self.config.getboolean(ConfigSections.difficulty.hard))
        self.radio_button_3.setChecked(self.config.getboolean(ConfigSections.difficulty.nightmare))
        
        self.radio_button_4.setChecked(self.config.getboolean(ConfigSections.special_mode.none))
        self.radio_button_5.setChecked(self.config.getboolean(ConfigSections.special_mode.custom_ng))
        self.radio_button_6.setChecked(self.config.getboolean(ConfigSections.special_mode.progressive_z))

        
        #Outfit config
        
        self.outfit_window_layout = QVBoxLayout()
        outfit_window_top = QHBoxLayout()
        self.outfit_window_layout.addLayout(outfit_window_top)
        outfit_window_center = QHBoxLayout()
        self.outfit_window_layout.addLayout(outfit_window_center)
        outfit_window_bottom = QHBoxLayout()
        self.outfit_window_layout.addLayout(outfit_window_bottom)
        
        outfit_instruction_label = QLabel()
        outfit_instruction_label.setText("Select none for vanilla or select multiple for a random\nchoice. Outfits are named after their HSV component.")
        outfit_window_top.addWidget(outfit_instruction_label)
        
        miriam_outfit_box_layout = QVBoxLayout()
        miriam_outfit_box = QGroupBox("Miriam")
        miriam_outfit_box.setLayout(miriam_outfit_box_layout)
        outfit_window_center.addWidget(miriam_outfit_box)
        
        self.miriam_outfit_list = QListWidget()
        self.miriam_outfit_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        miriam_outfit_box_layout.addWidget(self.miriam_outfit_list)
        for folder in os.listdir("Data\\Texture\\Miriam"):
            if os.path.isdir(f"Data\\Texture\\Miriam\\{folder}"):
                self.miriam_outfit_list.addItem(folder)
        
        zangetsu_outfit_box_layout = QVBoxLayout()
        zangetsu_outfit_box = QGroupBox("Zangetsu")
        zangetsu_outfit_box.setLayout(zangetsu_outfit_box_layout)
        outfit_window_center.addWidget(zangetsu_outfit_box)
        
        self.zangetsu_outfit_list = QListWidget()
        self.zangetsu_outfit_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        zangetsu_outfit_box_layout.addWidget(self.zangetsu_outfit_list)
        for folder in os.listdir("Data\\Texture\\Zangetsu"):
            if os.path.isdir(f"Data\\Texture\\Zangetsu\\{folder}"):
                self.zangetsu_outfit_list.addItem(folder)
        
        outfit_confirm_button = QPushButton("Confirm")
        outfit_confirm_button.clicked.connect(self.outfit_confirm_button_clicked)
        outfit_window_bottom.addStretch(1)
        outfit_window_bottom.addWidget(outfit_confirm_button)

        
        self.matches_preset()
        self.reset_selected_map_state()





    def check_box_1_changed(self):
        checked = self.check_box_1.isChecked()
        self.config.set(ConfigSections.item.overworld_pool, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_1)
            self.check_box_1.setStyleSheet(f"color: {item_color}")
            if self.check_box_2.isChecked() and self.check_box_16.isChecked() and self.check_box_17.isChecked() and self.check_box_18.isChecked():
                self.center_box_1.setStyleSheet(f"color: {item_color}")
        else:
            self.remove_main_param(self.check_box_1)
            self.check_box_1.setStyleSheet("color: #ffffff")
            self.center_box_1.setStyleSheet("color: #ffffff")
            self.check_box_16.setChecked(False)
            self.check_box_2.setChecked(False)
        self.spin_button_1.setVisible(checked)
        self.matches_preset()

    def check_box_16_changed(self):
        checked = self.check_box_16.isChecked()
        self.config.set(ConfigSections.item.quest_pool, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_16)
            self.check_box_16.setStyleSheet(f"color: {item_color}")
            if self.check_box_1.isChecked() and self.check_box_2.isChecked() and self.check_box_17.isChecked() and self.check_box_18.isChecked():
                self.center_box_1.setStyleSheet(f"color: {item_color}")
            self.check_box_1.setChecked(True)
        else:
            self.remove_main_param(self.check_box_16)
            self.check_box_16.setStyleSheet("color: #ffffff")
            self.center_box_1.setStyleSheet("color: #ffffff")
            self.check_box_2.setChecked(False)
        self.matches_preset()

    def check_box_2_changed(self):
        checked = self.check_box_2.isChecked()
        self.config.set(ConfigSections.item.shop_pool, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_2)
            self.check_box_2.setStyleSheet(f"color: {item_color}")
            if self.check_box_1.isChecked() and self.check_box_16.isChecked() and self.check_box_17.isChecked() and self.check_box_18.isChecked():
                self.center_box_1.setStyleSheet(f"color: {item_color}")
            self.check_box_1.setChecked(True)
            self.check_box_16.setChecked(True)
        else:
            self.remove_main_param(self.check_box_2)
            self.check_box_2.setStyleSheet("color: #ffffff")
            self.center_box_1.setStyleSheet("color: #ffffff")
        self.spin_button_2.setVisible(checked)
        self.matches_preset()

    def check_box_17_changed(self):
        checked = self.check_box_17.isChecked()
        self.config.set(ConfigSections.item.quest_requirements, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_17)
            self.check_box_17.setStyleSheet(f"color: {item_color}")
            if self.check_box_1.isChecked() and self.check_box_2.isChecked() and self.check_box_16.isChecked() and self.check_box_18.isChecked():
                self.center_box_1.setStyleSheet(f"color: {item_color}")
        else:
            self.remove_main_param(self.check_box_17)
            self.check_box_17.setStyleSheet("color: #ffffff")
            self.center_box_1.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_18_changed(self):
        checked = self.check_box_18.isChecked()
        self.config.set(ConfigSections.item.remove_infinites, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_18)
            self.check_box_18.setStyleSheet(f"color: {item_color}")
            if self.check_box_1.isChecked() and self.check_box_2.isChecked() and self.check_box_16.isChecked() and self.check_box_17.isChecked():
                self.center_box_1.setStyleSheet(f"color: {item_color}")
        else:
            self.remove_main_param(self.check_box_18)
            self.check_box_18.setStyleSheet("color: #ffffff")
            self.center_box_1.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_3_changed(self):
        checked = self.check_box_3.isChecked()
        self.config.set(ConfigSections.shop.item_values, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_3)
            self.check_box_3.setStyleSheet(f"color: {shop_color}")
            if self.check_box_4.isChecked():
                self.center_box_2.setStyleSheet(f"color: {shop_color}")
        else:
            self.remove_main_param(self.check_box_3)
            self.check_box_3.setStyleSheet("color: #ffffff")
            self.center_box_2.setStyleSheet("color: #ffffff")
            self.check_box_4.setChecked(False)
        self.spin_button_3.setVisible(checked)
        self.matches_preset()

    def check_box_4_changed(self):
        checked = self.check_box_4.isChecked()
        self.config.set(ConfigSections.shop.scale_selling_price_with_cost, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_4)
            self.check_box_4.setStyleSheet(f"color: {shop_color}")
            if self.check_box_3.isChecked():
                self.center_box_2.setStyleSheet(f"color: {shop_color}")
            self.check_box_3.setChecked(True)
        else:
            self.remove_main_param(self.check_box_4)
            self.check_box_4.setStyleSheet("color: #ffffff")
            self.center_box_2.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_5_changed(self):
        checked = self.check_box_5.isChecked()
        self.config.set(ConfigSections.library.map_requirements, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_5)
            self.check_box_5.setStyleSheet(f"color: {library_color}")
            if self.check_box_6.isChecked():
                self.center_box_3.setStyleSheet(f"color: {library_color}")
        else:
            self.remove_main_param(self.check_box_5)
            self.check_box_5.setStyleSheet("color: #ffffff")
            self.center_box_3.setStyleSheet("color: #ffffff")
        self.spin_button_4.setVisible(checked)
        self.matches_preset()

    def check_box_6_changed(self):
        checked = self.check_box_6.isChecked()
        self.config.set(ConfigSections.library.tome_appearance, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_6)
            self.check_box_6.setStyleSheet(f"color: {library_color}")
            if self.check_box_5.isChecked():
                self.center_box_3.setStyleSheet(f"color: {library_color}")
        else:
            self.remove_main_param(self.check_box_6)
            self.check_box_6.setStyleSheet("color: #ffffff")
            self.center_box_3.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_7_changed(self):
        checked = self.check_box_7.isChecked()
        self.config.set(ConfigSections.shard.randomize_shard_power_and_cost, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_7)
            self.check_box_7.setStyleSheet(f"color: {shard_color}")
            if self.check_box_8.isChecked():
                self.center_box_4.setStyleSheet(f"color: {shard_color}")
        else:
            self.remove_main_param(self.check_box_7)
            self.check_box_7.setStyleSheet("color: #ffffff")
            self.center_box_4.setStyleSheet("color: #ffffff")
            self.check_box_8.setChecked(False)
        self.spin_button_5.setVisible(checked)
        self.matches_preset()

    def check_box_8_changed(self):
        checked = self.check_box_8.isChecked()
        self.config.set(ConfigSections.shard.scale_cost_with_power, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_8)
            self.check_box_8.setStyleSheet(f"color: {shard_color}")
            if self.check_box_7.isChecked():
                self.center_box_4.setStyleSheet(f"color: {shard_color}")
            self.check_box_7.setChecked(True)
        else:
            self.remove_main_param(self.check_box_8)
            self.check_box_8.setStyleSheet("color: #ffffff")
            self.center_box_4.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_23_changed(self):
        checked = self.check_box_23.isChecked()
        self.config.set(ConfigSections.equipment.global_gear_stats, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_23)
            self.check_box_23.setStyleSheet(f"color: {equip_color}")
            if self.check_box_9.isChecked():
                self.center_box_5.setStyleSheet(f"color: {equip_color}")
        else:
            self.remove_main_param(self.check_box_23)
            self.check_box_23.setStyleSheet("color: #ffffff")
            self.center_box_5.setStyleSheet("color: #ffffff")
        self.spin_button_6.setVisible(checked)
        self.matches_preset()

    def check_box_9_changed(self):
        checked = self.check_box_9.isChecked()
        self.config.set(ConfigSections.equipment.chest_gear_stats, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_9)
            self.check_box_9.setStyleSheet(f"color: {equip_color}")
            if self.check_box_23.isChecked():
                self.center_box_5.setStyleSheet(f"color: {equip_color}")
        else:
            self.remove_main_param(self.check_box_9)
            self.check_box_9.setStyleSheet("color: #ffffff")
            self.center_box_5.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_25_changed(self):
        checked = self.check_box_25.isChecked()
        self.config.set(ConfigSections.enemy.enemy_locations, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_25)
            self.check_box_25.setStyleSheet(f"color: {enemy_color}")
            if self.check_box_10.isChecked() and self.check_box_26.isChecked() and self.check_box_11.isChecked() and self.check_box_27.isChecked():
                self.center_box_6.setStyleSheet(f"color: {enemy_color}")
        else:
            self.remove_main_param(self.check_box_25)
            self.check_box_25.setStyleSheet("color: #ffffff")
            self.center_box_6.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_10_changed(self):
        checked = self.check_box_10.isChecked()
        self.config.set(ConfigSections.enemy.enemy_levels, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_10)
            self.check_box_10.setStyleSheet(f"color: {enemy_color}")
            if self.check_box_25.isChecked() and self.check_box_26.isChecked() and self.check_box_11.isChecked() and self.check_box_27.isChecked():
                self.center_box_6.setStyleSheet(f"color: {enemy_color}")
        else:
            self.remove_main_param(self.check_box_10)
            self.check_box_10.setStyleSheet("color: #ffffff")
            self.center_box_6.setStyleSheet("color: #ffffff")
        self.spin_button_8.setVisible(checked)
        self.matches_preset()

    def check_box_26_changed(self):
        checked = self.check_box_26.isChecked()
        self.config.set(ConfigSections.enemy.boss_levels, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_26)
            self.check_box_26.setStyleSheet(f"color: {enemy_color}")
            if self.check_box_25.isChecked() and self.check_box_10.isChecked() and self.check_box_11.isChecked() and self.check_box_27.isChecked():
                self.center_box_6.setStyleSheet(f"color: {enemy_color}")
        else:
            self.remove_main_param(self.check_box_26)
            self.check_box_26.setStyleSheet("color: #ffffff")
            self.center_box_6.setStyleSheet("color: #ffffff")
        self.spin_button_9.setVisible(checked)
        self.matches_preset()

    def check_box_11_changed(self):
        checked = self.check_box_11.isChecked()
        self.config.set(ConfigSections.enemy.enemy_tolerances, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_11)
            self.check_box_11.setStyleSheet(f"color: {enemy_color}")
            if self.check_box_25.isChecked() and self.check_box_10.isChecked() and self.check_box_26.isChecked() and self.check_box_27.isChecked():
                self.center_box_6.setStyleSheet(f"color: {enemy_color}")
        else:
            self.remove_main_param(self.check_box_11)
            self.check_box_11.setStyleSheet("color: #ffffff")
            self.center_box_6.setStyleSheet("color: #ffffff")
        self.spin_button_10.setVisible(checked)
        self.matches_preset()

    def check_box_27_changed(self):
        checked = self.check_box_27.isChecked()
        self.config.set(ConfigSections.enemy.boss_tolerances, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_27)
            self.check_box_27.setStyleSheet(f"color: {enemy_color}")
            if self.check_box_25.isChecked() and self.check_box_10.isChecked() and self.check_box_26.isChecked() and self.check_box_11.isChecked():
                self.center_box_6.setStyleSheet(f"color: {enemy_color}")
        else:
            self.remove_main_param(self.check_box_27)
            self.check_box_27.setStyleSheet("color: #ffffff")
            self.center_box_6.setStyleSheet("color: #ffffff")
        self.spin_button_11.setVisible(checked)
        self.matches_preset()

    def check_box_12_changed(self):
        checked = self.check_box_12.isChecked()
        self.config.set(ConfigSections.map.room_layout, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_12)
            self.check_box_12.setStyleSheet(f"color: {map_color}")
            self.center_box_7.setStyleSheet(f"color: {map_color}")
            self.add_to_modified_files("UI", "icon_8bitCrown")
            self.add_to_modified_files("UI", "Map_Icon_Keyperson")
            self.add_to_modified_files("UI", "Map_Icon_RootBox")
            self.add_to_modified_files("UI", "Map_StartingPoint")
        else:
            self.remove_main_param(self.check_box_12)
            self.check_box_12.setStyleSheet("color: #ffffff")
            self.center_box_7.setStyleSheet("color: #ffffff")
            self.remove_from_modified_files("UI", "icon_8bitCrown")
            self.remove_from_modified_files("UI", "Map_Icon_Keyperson")
            self.remove_from_modified_files("UI", "Map_Icon_RootBox")
            self.remove_from_modified_files("UI", "Map_StartingPoint")
        self.reset_selected_map_state()
        self.browse_map_button.setVisible(checked)
        self.matches_preset()

    def check_box_13_changed(self):
        checked = self.check_box_13.isChecked()
        self.config.set(ConfigSections.graphics.outfit_color, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_13)
            self.check_box_13.setStyleSheet(f"color: {graphic_color}")
            if self.check_box_24.isChecked():
                self.center_box_8.setStyleSheet(f"color: {graphic_color}")
        else:
            self.remove_main_param(self.check_box_13)
            self.check_box_13.setStyleSheet("color: #ffffff")
            self.center_box_8.setStyleSheet("color: #ffffff")
        self.update_modified_files_for_outfit()
        self.outfit_config_button.setVisible(checked)
        self.matches_preset()

    def check_box_24_changed(self):
        checked = self.check_box_24.isChecked()
        self.config.set(ConfigSections.graphics.backer_portraits, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_24)
            self.check_box_24.setStyleSheet(f"color: {graphic_color}")
            if self.check_box_13.isChecked():
                self.center_box_8.setStyleSheet(f"color: {graphic_color}")
        else:
            self.remove_main_param(self.check_box_24)
            self.check_box_24.setStyleSheet("color: #ffffff")
            self.center_box_8.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_15_changed(self):
        checked = self.check_box_15.isChecked()
        self.config.set(ConfigSections.sound.dialogues, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_15)
            self.check_box_15.setStyleSheet(f"color: {sound_color}")
            if self.check_box_14.isChecked():
                self.center_box_9.setStyleSheet(f"color: {sound_color}")
        else:
            self.remove_main_param(self.check_box_15)
            self.check_box_15.setStyleSheet("color: #ffffff")
            self.center_box_9.setStyleSheet("color: #ffffff")
        self.spin_button_12.setVisible(checked)
        self.matches_preset()

    def check_box_14_changed(self):
        checked = self.check_box_14.isChecked()
        self.config.set(ConfigSections.sound.music, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_14)
            self.check_box_14.setStyleSheet(f"color: {sound_color}")
            if self.check_box_15.isChecked():
                self.center_box_9.setStyleSheet(f"color: {sound_color}")
        else:
            self.remove_main_param(self.check_box_14)
            self.check_box_14.setStyleSheet("color: #ffffff")
            self.center_box_9.setStyleSheet("color: #ffffff")
        self.matches_preset()

    def check_box_21_changed(self):
        checked = self.check_box_21.isChecked()
        self.config.set(ConfigSections.extra.bloodless_candles, str(checked).lower())
        if checked:
            self.add_main_param(self.check_box_21)
            self.check_box_21.setStyleSheet(f"color: {extra_color}")
            self.center_box_10.setStyleSheet(f"color: {extra_color}")
        else:
            self.remove_main_param(self.check_box_21)
            self.check_box_21.setStyleSheet("color: #ffffff")
            self.center_box_10.setStyleSheet("color: #ffffff")
        self.spin_button_13.setVisible(checked)
        self.matches_preset()

    def spin_button_1_clicked(self):
        num = self.spin_button_1_get_index()
        num = num % 3 + 1
        self.spin_button_1_set_index(num)

    def spin_button_1_get_index(self):
        if self.spin_button_1.text():
            return int(self.spin_button_1.text())
        return 0

    def spin_button_1_set_index(self, index):
        self.spin_button_1.setText(str(index))
        self.config.set(ConfigSections.item.overworld_pool_complexity, str(index))
        self.change_sub_param(self.spin_button_1, index)
        return True

    def spin_button_2_clicked(self):
        num = self.spin_button_2_get_index()
        num = num % 3 + 1
        self.spin_button_2_set_index(num)

    def spin_button_2_get_index(self):
        if self.spin_button_2.text():
            return int(self.spin_button_2.text())
        return 0

    def spin_button_2_set_index(self, index):
        self.spin_button_2.setText(str(index))
        self.config.set(ConfigSections.item.shop_pool_weight, str(index))
        self.change_sub_param(self.spin_button_2, index)
        return True

    def spin_button_3_clicked(self):
        num = self.spin_button_3_get_index()
        num = num % 3 + 1
        self.spin_button_3_set_index(num)

    def spin_button_3_get_index(self):
        if self.spin_button_3.text():
            return int(self.spin_button_3.text())
        return 0

    def spin_button_3_set_index(self, index):
        self.spin_button_3.setText(str(index))
        self.config.set(ConfigSections.shop.item_values_weight, str(index))
        self.change_sub_param(self.spin_button_3, index)
        return True

    def spin_button_4_clicked(self):
        num = self.spin_button_4_get_index()
        num = num % 3 + 1
        self.spin_button_4_set_index(num)

    def spin_button_4_get_index(self):
        if self.spin_button_4.text():
            return int(self.spin_button_4.text())
        return 0

    def spin_button_4_set_index(self, index):
        self.spin_button_4.setText(str(index))
        self.config.set(ConfigSections.library.map_requirements_weight, str(index))
        self.change_sub_param(self.spin_button_4, index)
        return True

    def spin_button_5_clicked(self):
        num = self.spin_button_5_get_index()
        num = num % 3 + 1
        self.spin_button_5_set_index(num)

    def spin_button_5_get_index(self):
        if self.spin_button_5.text():
            return int(self.spin_button_5.text())
        return 0

    def spin_button_5_set_index(self, index):
        self.spin_button_5.setText(str(index))
        self.config.set(ConfigSections.shard.shard_power_and_cost_weight, str(index))
        self.change_sub_param(self.spin_button_5, index)
        return True

    def spin_button_6_clicked(self):
        num = self.spin_button_6_get_index()
        num = num % 3 + 1
        self.spin_button_6_set_index(num)

    def spin_button_6_get_index(self):
        if self.spin_button_6.text():
            return int(self.spin_button_6.text())
        return 0

    def spin_button_6_set_index(self, index):
        self.spin_button_6.setText(str(index))
        self.config.set(ConfigSections.equipment.global_gear_stats_weight, str(index))
        self.change_sub_param(self.spin_button_6, index)
        return True

    def spin_button_8_clicked(self):
        num = self.spin_button_8_get_index()
        num = num % 3 + 1
        self.spin_button_8_set_index(num)

    def spin_button_8_get_index(self):
        if self.spin_button_8.text():
            return int(self.spin_button_8.text())
        return 0

    def spin_button_8_set_index(self, index):
        self.spin_button_8.setText(str(index))
        self.config.set(ConfigSections.enemy.enemy_levels_weight, str(index))
        self.change_sub_param(self.spin_button_8, index)
        return True

    def spin_button_9_clicked(self):
        num = self.spin_button_9_get_index()
        num = num % 3 + 1
        self.spin_button_9_set_index(num)

    def spin_button_9_get_index(self):
        if self.spin_button_9.text():
            return int(self.spin_button_9.text())
        return 0

    def spin_button_9_set_index(self, index):
        self.spin_button_9.setText(str(index))
        self.config.set(ConfigSections.enemy.boss_levels_weight, str(index))
        self.change_sub_param(self.spin_button_9, index)
        return True

    def spin_button_10_clicked(self):
        num = self.spin_button_10_get_index()
        num = num % 3 + 1
        self.spin_button_10_set_index(num)

    def spin_button_10_get_index(self):
        if self.spin_button_10.text():
            return int(self.spin_button_10.text())
        return 0

    def spin_button_10_set_index(self, index):
        self.spin_button_10.setText(str(index))
        self.config.set(ConfigSections.enemy.enemy_tolerances_weight, str(index))
        self.change_sub_param(self.spin_button_10, index)
        return True

    def spin_button_11_clicked(self):
        num = self.spin_button_11_get_index()
        num = num % 3 + 1
        self.spin_button_11_set_index(num)

    def spin_button_11_get_index(self):
        if self.spin_button_11.text():
            return int(self.spin_button_11.text())
        return 0

    def spin_button_11_set_index(self, index):
        self.spin_button_11.setText(str(index))
        self.config.set(ConfigSections.enemy.boss_tolerances_weight, str(index))
        self.change_sub_param(self.spin_button_11, index)
        return True

    def spin_button_12_clicked(self):
        num = self.spin_button_12_get_index()
        num = num % len(self.language_sequence) + 1
        self.spin_button_12_set_index(num)

    def spin_button_12_get_index(self):
        if self.spin_button_12.text():
            return self.language_sequence.index(self.spin_button_12.text()) + 1
        return 0

    def spin_button_12_set_index(self, index):
        if index <= len(self.language_sequence):
            self.spin_button_12.setText(self.language_sequence[index - 1])
            self.config.set(ConfigSections.sound.dialogues_language, str(index))
            self.change_sub_param(self.spin_button_12, index)
            return True
        return False

    def spin_button_13_clicked(self):
        num = self.spin_button_13_get_index()
        num = num % 3 + 1
        self.spin_button_13_set_index(num)

    def spin_button_13_get_index(self):
        if self.spin_button_13.text():
            return int(self.spin_button_13.text())
        return 0

    def spin_button_13_set_index(self, index):
        self.spin_button_13.setText(str(index))
        self.config.set(ConfigSections.extra.bloodless_candles_complexity, index)
        self.change_sub_param(self.spin_button_13, index)
        return True
    
    def radio_button_group_1_checked(self):
        checked_1 = self.radio_button_1.isChecked()
        checked_2 = self.radio_button_2.isChecked()
        checked_3 = self.radio_button_3.isChecked()
        self.config.set(ConfigSections.difficulty.normal, str(checked_1).lower())
        self.config.set(ConfigSections.difficulty.hard, str(checked_2).lower())
        self.config.set(ConfigSections.difficulty.nightmare, str(checked_3).lower())
    
    def radio_button_group_2_checked(self):
        checked_1 = self.radio_button_4.isChecked()
        checked_2 = self.radio_button_5.isChecked()
        checked_3 = self.radio_button_6.isChecked()
        self.config.set(ConfigSections.special_mode.none, str(checked_1).lower())
        self.config.set(ConfigSections.special_mode.custom_ng,     str(checked_2).lower())
        self.config.set(ConfigSections.special_mode.progressive_z, str(checked_3).lower())
        self.custom_level_field.setVisible(checked_2)
    
    def preset_drop_down_changed(self, index):
        current = self.preset_drop_down.itemText(index)
        if current == "Custom":
            return
        main_num = preset_to_bytes[current]
        sub_num = self.get_param_bytes()[1]
        self.set_param_bytes(main_num, sub_num)

    def matches_preset(self):
        main_num = self.get_param_bytes()[0]
        if main_num in bytes_to_preset:
            self.preset_drop_down.setCurrentText(bytes_to_preset[main_num])
            return
        self.preset_drop_down.setCurrentText("Custom")

    def param_string_field_changed(self, _):
        #Check that input is valid hex
        try:
            main_num, sub_num = self.get_param_bytes()
        except ValueError:
            main_num, sub_num = (0, 0)
        self.set_param_bytes(main_num, sub_num)
        #Apply bytes to params
        for widget in main_widget_to_param:
            if (main_num & main_widget_to_param[widget] != 0) != widget.isChecked():
                widget.setChecked(not widget.isChecked())
        for widget in sub_widget_to_param:
            check = False
            index = getattr(self, f"{widget.accessibleName()}_get_index")()
            if not index:
                continue
            for num in range(2):
                if sub_num & sub_widget_to_param[widget]*0x1000**num != 0:
                    check = True
                    if index != shift_to_spin_index[num]:
                        check = getattr(self, f"{widget.accessibleName()}_set_index")(shift_to_spin_index[num])
            if not check and index != 2:
                getattr(self, f"{widget.accessibleName()}_set_index")(2)
    
    def add_main_param(self, widget):
        main_num, sub_num = self.get_param_bytes()
        extra_num = main_widget_to_param[widget]
        if main_num & extra_num == 0:
            main_num += extra_num
        self.set_param_bytes(main_num, sub_num)
    
    def remove_main_param(self, widget):
        main_num, sub_num = self.get_param_bytes()
        extra_num = main_widget_to_param[widget]
        if main_num & extra_num != 0:
            main_num -= extra_num
        self.set_param_bytes(main_num, sub_num)
    
    def change_sub_param(self, widget, index):
        main_num, sub_num = self.get_param_bytes()
        extra_num = sub_widget_to_param[widget]
        for num in range(2):
            abs_num = extra_num*0x1000**num
            if num == spin_index_to_shift[index]:
                if sub_num & abs_num == 0:
                    sub_num += abs_num
            else:
                if sub_num & abs_num != 0:
                    sub_num -= abs_num
        self.set_param_bytes(main_num, sub_num)
    
    def get_param_bytes(self):
        total_num = int(self.param_string_field.text(), 16)
        factor = 0x10**main_param_length
        return (total_num % factor, total_num // factor)
    
    def set_param_bytes(self, main_num, sub_num):
        factor = 0x10**main_param_length
        total_num = main_num + sub_num*factor
        self.param_string_field.setText(self.param_string_format.format(total_num).upper())
    
    def custom_level_field_changed(self):
        self.config.set(ConfigSections.special_mode.custom_ng_level, str(self.custom_level_field.value()))
    
    def starting_items_field_changed(self, text : str):
        self.config.set(ConfigSections.start_with.items, text)
    
    def game_path_field_changed(self, text : str):
        self.config.set(ConfigSections.misc.game_path, text)
    
    def add_to_modified_files(self, filetype : str, file : str) -> None:
        self.modified_files.add_file(filetype, file)
    
    def remove_from_modified_files(self, filetype : str, file : str) -> None:
        self.modified_files.remove_file(filetype, file)

    def browse_map_button_clicked(self):
        if self.config.get(ConfigSections.map.selected_map):
            self.config.set(ConfigSections.map.selected_map, "")
        else:
            path = QFileDialog.getOpenFileName(parent=self, caption="Open", dir="MapEdit\\Custom", filter="*.json")[0]
            if path:
                self.config.set(ConfigSections.map.selected_map, path.replace("/", "\\"))
        self.reset_selected_map_state()
    
    def reset_selected_map_state(self):
        selected_map = self.config.get(ConfigSections.map.selected_map)
        if self.config.getboolean(ConfigSections.map.room_layout) and selected_map:
            self.browse_map_button.setIcon(QPixmap("Data\\cancel.png"))
            self.browse_map_button.setToolTip("Revert map selection back to random.")
            self.setWindowTitle(f"{SCRIPT_NAME} ({selected_map})")
        else:
            self.browse_map_button.setIcon(QPixmap("Data\\browse.png"))
            self.browse_map_button.setToolTip("Manually browse a custom map to play on.")
            self.setWindowTitle(SCRIPT_NAME)
    
    def outfit_config_button_clicked(self):
        miriam_selected_outfit_list   = self.config.get(ConfigSections.outfit.miriam_outfits).split(",")
        zangetsu_selected_outfit_list = self.config.get(ConfigSections.outfit.zangetsu_outfits).split(",")
        for index in range(self.miriam_outfit_list.count()):
            item = self.miriam_outfit_list.item(index)
            item.setSelected(item.text() in miriam_selected_outfit_list)
        for index in range(self.zangetsu_outfit_list.count()):
            item = self.zangetsu_outfit_list.item(index)
            item.setSelected(item.text() in zangetsu_selected_outfit_list)
        max_size = max(self.miriam_outfit_list.count(), self.zangetsu_outfit_list.count())
        self.outfit_window = QDialog(self)
        self.outfit_window.setLayout(self.outfit_window_layout)
        self.outfit_window.setWindowTitle("Outfit")
        self.outfit_window.setFixedSize(0, int(self.size_multiplier*min(140 + max_size*24, 500)))
        self.outfit_window.exec()
    
    def outfit_confirm_button_clicked(self):
        miriam_selected_outfit_list   = []
        zangetsu_selected_outfit_list = []
        for item in self.miriam_outfit_list.selectedItems():
            miriam_selected_outfit_list.append(item.text())
        for item in self.zangetsu_outfit_list.selectedItems():
            zangetsu_selected_outfit_list.append(item.text())
        miriam_selected_outfit_list.sort()
        zangetsu_selected_outfit_list.sort()
        self.config.set(ConfigSections.outfit.miriam_outfits, ",".join(miriam_selected_outfit_list))
        self.config.set(ConfigSections.outfit.zangetsu_outfits, ",".join(zangetsu_selected_outfit_list))
        self.update_modified_files_for_outfit()
        self.outfit_window.close()
    
    def update_modified_files_for_outfit(self):
        if self.config.getboolean(ConfigSections.graphics.outfit_color) and self.config.get(ConfigSections.outfit.miriam_outfits):
            self.add_to_modified_files("UI"     , "Face_Miriam")
            self.add_to_modified_files("Texture", "T_Body01_01_Color")
            self.add_to_modified_files("Texture", "T_Pl01_Cloth_Bace")
        else:
            self.remove_from_modified_files("UI"     , "Face_Miriam"      )
            self.remove_from_modified_files("Texture", "T_Body01_01_Color")
            self.remove_from_modified_files("Texture", "T_Pl01_Cloth_Bace")
        if self.config.getboolean(ConfigSections.graphics.outfit_color) and self.config.get(ConfigSections.outfit.zangetsu_outfits):
            self.add_to_modified_files("UI"     , "Face_Zangetsu"      )
            self.add_to_modified_files("Texture", "T_N1011_body_color" )
            self.add_to_modified_files("Texture", "T_N1011_face_color" )
            self.add_to_modified_files("Texture", "T_N1011_equip_color")
            self.add_to_modified_files("Texture", "T_Tknife05_Base"    )
        else:
            self.remove_from_modified_files("UI"     , "Face_Zangetsu"      )
            self.remove_from_modified_files("Texture", "T_N1011_body_color" )
            self.remove_from_modified_files("Texture", "T_N1011_face_color" )
            self.remove_from_modified_files("Texture", "T_N1011_equip_color")
            self.remove_from_modified_files("Texture", "T_Tknife05_Base"    )

    def browse_game_path_button_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "Folder")
        if path:
            self.game_path_field.setText(path.replace("/", "\\"))
    