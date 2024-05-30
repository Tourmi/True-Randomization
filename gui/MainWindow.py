import os
import sys
import requests
import traceback
import psutil

from looseversion import LooseVersion
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QGraphicsView
from PySide6.QtWidgets import QMessageBox

from randomizer.Constants import *

from configuration import Config
from configuration import ConfigSections
from .widgets import MessageBox
from .widgets import ProgressBar
from .threads.Update import Update
from .sections import ParametersSection
from .sections import ButtonsSection
from .sections import ModifiedFilesSection

class MainWindow(QGraphicsView):
    def __init__(self, config : Config):
        super().__init__()
        sys.excepthook = self.exception_hook
        self.config = config
        self.modified_files_widget : ModifiedFilesSection
        self.setEnabled(False)
        self.init()
        self.check_for_updates()

    def init(self):
        self.first_time = False
        if not self.config.getint(ConfigSections.misc.window_size) in window_sizes:
            self.config.set(ConfigSections.misc.window_size, window_sizes[-1])
            self.first_time = True
        self.size_multiplier = self.config.getint(ConfigSections.misc.window_size)/1080
        
        self.setStyleSheet("QWidget{background:transparent; color: #ffffff; font-family: Cambria; font-size: " + str(int(self.size_multiplier*18)) + "px}"
        + "QGraphicsView{border-image: url(MapEdit/Data/background.png)}"
        + "QComboBox{background-color: #21222e; selection-background-color: #320288ff}"
        + "QComboBox QAbstractItemView{border: 1px solid #21222e}"
        + "QScrollBar::add-page{background-color: #1b1c26}"
        + "QScrollBar::sub-page{background-color: #1b1c26}"
        + "QMenu{background-color: #21222e; margin: 4px}"
        + "QMenu::item{padding: 2px 4px 2px 4px}"
        + "QMenu::item:selected{background: #320288ff}"
        + "QMenu::item:pressed{border: 1px solid #640288ff}" 
        + "QDialog{background-color: #21222e}"
        + "QMessageBox{background-color: #21222e}"
        + "QPushButton{background-color: #21222e}"
        + "QProgressDialog{background-color: #21222e}"
        + "QProgressBar{border: 2px solid white; text-align: center; font: bold}"
        + "QSpinBox{background-color: #21222e; selection-background-color: #320288ff}"
        + "QLineEdit{background-color: #21222e; selection-background-color: #320288ff}"
        + "QListWidget{background-color: #21222e; border: 1px solid #21222e}"
        + "QListWidget::item:selected:!active{background-color: #320288ff; color: #ffffff}"
        + "QToolTip{border: 1px solid white; background-color: #21222e; color: #ffffff; font-family: Cambria; font-size: " + str(int(self.size_multiplier*18)) + "px}")
        
        #Main layout
        
        main_window_layout = QHBoxLayout()
        main_window_layout.setSpacing(int(self.size_multiplier*10))
        self.setLayout(main_window_layout)

        self.modified_files_widget = ModifiedFilesSection.from_default()

        #Left Label

        artwork_label = QLabel()
        artwork_label.setStyleSheet("border: 1px solid white")
        artwork_label.setPixmap(QPixmap("Data\\artwork.png"))
        artwork_label.setScaledContents(True)
        artwork_label.setFixedSize(int(self.size_multiplier*550), int(self.size_multiplier*978))
        main_window_layout.addWidget(artwork_label)
        
        #Center widget
        
        center_widget_layout = QVBoxLayout()
        center_widget_layout.setSpacing(int(self.size_multiplier*10))
        main_window_layout.addLayout(center_widget_layout)

        center_widget_layout.addWidget(ParametersSection(self, self.config, self.size_multiplier, self.modified_files_widget))
        center_widget_layout.addWidget(ButtonsSection(self, self.size_multiplier, self.config))
        
        
        #Right panel
        right_groupbox = QGroupBox()
        right_groupbox.setFixedSize(int(self.size_multiplier*550), int(self.size_multiplier*978))
        main_window_layout.addWidget(right_groupbox)
        right_groupbox_layout = QVBoxLayout()
        right_groupbox.setLayout(right_groupbox_layout)

        right_groupbox_layout.addWidget(self.modified_files_widget)

        right_groupbox_layout_bottom = QHBoxLayout()
        right_groupbox_layout.addStretch(1)
        right_groupbox_layout.addLayout(right_groupbox_layout_bottom)
        
        discord_label = QLabel()
        discord_label.setText("<a href=\"https://discord.gg/nUbFA7MEeU\"><font face=Cambria color=#0080ff>Discord</font></a>")
        discord_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        discord_label.setOpenExternalLinks(True)
        right_groupbox_layout_bottom.addStretch(1)
        right_groupbox_layout_bottom.addWidget(discord_label)

        #Window
        
        self.setFixedSize(int(self.size_multiplier*1800), int(self.size_multiplier*1000))
        self.setWindowIcon(QIcon(self.resource_path("Bloodstained.ico")))
        self.show()
        
        #Position
        
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())
        
        QApplication.processEvents()

    def update_finished(self):
        sys.exit()

    def check_for_updates(self):
        if os.path.isfile("delete.me"):
            os.remove("delete.me")
        for index in range(3):
            if os.path.isfile(f"Tools\\UAssetAPI\\delete{index + 1}.me"):
                os.remove(f"Tools\\UAssetAPI\\delete{index + 1}.me")
        try:
            release_json = requests.get(UPDATE_URL).json()
        except requests.ConnectionError:
            self.check_for_resolution()
            return
        try:
            tag = LooseVersion(release_json["tag_name"])
        except KeyError:
            self.check_for_resolution()
            return
        if tag > LooseVersion(self.config.get(ConfigSections.misc.version)):
            choice = QMessageBox.question(self, 
                                          "Auto Updater", 
                                          "New version found:\n\n" + release_json["body"] + "\n\nUpdate ?", 
                                          QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if choice == QMessageBox.StandardButton.Yes:
                if "Map Editor.exe" in (program.name() for program in psutil.process_iter()):
                    MessageBox.error(self, "MapEditor.exe is running, cannot overwrite.")
                    self.check_for_resolution()
                    return
                
                self.progress_bar = ProgressBar(0, release_json["assets"][0]["size"], self, "Status")
                self.worker = Update(self.config, release_json)
                self.progress_bar.connect_to(self.worker.signaller)
                self.progress_bar.setAutoClose(False)
                self.progress_bar.setAutoReset(False)
                self.worker.signaller.finished.connect(self.update_finished)
                self.worker.start()
            else:
                self.check_for_resolution()
        else:
            self.check_for_resolution()
    
    def check_for_resolution(self):
        if self.first_time:
            pass
            #self.setting_button_clicked()
        self.setEnabled(True)
    
    def exception_hook(self, exc_type, exc_value, exc_traceback):
        traceback_format = traceback.format_exception(exc_type, exc_value, exc_traceback)
        traceback_string = "".join(traceback_format)
        print(traceback_string)
        MessageBox.error(self, "An error has occured.\nCheck the command window for more detail.")

    @staticmethod
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            base_path = getattr(sys, '_MEIPASS')
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)