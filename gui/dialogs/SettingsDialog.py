from __future__ import annotations

import subprocess
import sys

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QDialog

from configuration import ConfigSections
from randomizer.Constants import *

class SettingsDialog(QDialog):
    def __init__(self, parent, config, size_multiplier):
        super().__init__(parent)
        self.config = config
        self.size_multiplier = size_multiplier

        self.setWindowTitle("Settings")
        self.setFixedSize(0, 0)
        #Settings
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        window_size_layout = QHBoxLayout()
        layout.addLayout(window_size_layout)

        window_size_label = QLabel("Window Size")
        window_size_layout.addWidget(window_size_label)
        
        self.window_size_drop_down = QComboBox()
        self.window_size_drop_down.addItem("720p")
        self.window_size_drop_down.addItem("900p")
        self.window_size_drop_down.addItem("1080p and above")
        self.window_size_drop_down.setCurrentIndex(window_sizes.index(self.config.getint(ConfigSections.misc.window_size)))
        window_size_layout.addWidget(self.window_size_drop_down)

        setting_apply_layout = QHBoxLayout()
        layout.addLayout(setting_apply_layout)
        
        setting_apply_button = QPushButton("Apply")
        setting_apply_button.clicked.connect(self.setting_apply_button_clicked)
        setting_apply_layout.addStretch(1)
        setting_apply_layout.addWidget(setting_apply_button)

    def setting_apply_button_clicked(self):
        if self.config.getint(ConfigSections.misc.window_size) == window_sizes[self.window_size_drop_down.currentIndex()]:
            self.close()
            return
        self.config.set(ConfigSections.misc.window_size, str(window_sizes[self.window_size_drop_down.currentIndex()]))
        self.config.write()
        subprocess.Popen([sys.executable, *sys.argv])
        sys.exit()