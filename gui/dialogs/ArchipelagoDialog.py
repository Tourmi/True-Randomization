from __future__ import annotations

from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QDialog

from configuration import Config
from configuration import ConfigSections

class ArchipelagoDialog(QDialog):
    def __init__(self, parent : QWidget, config : Config, size_multiplier : float):
        super().__init__(parent)
        self.config = config
        self.size_multiplier = size_multiplier

        #Archipelago
        archi_window_layout = QGridLayout()
        archi_window_layout.setSpacing(int(10 * self.size_multiplier))

        self.archi_check_box = QCheckBox("Enable Archipelago")
        archi_window_layout.addWidget(self.archi_check_box, 0, 0, 1, 2)

        archi_name_label = QLabel("Archipelago Name")
        archi_window_layout.addWidget(archi_name_label, 1, 0)

        self.archi_name_field = QLineEdit()
        archi_window_layout.addWidget(self.archi_name_field, 1, 1)

        progression_label = QLabel("Progression Balancing")
        archi_window_layout.addWidget(progression_label, 2, 0)

        self.progression_field = QSpinBox()
        self.progression_field.setRange(0, 99)
        archi_window_layout.addWidget(self.progression_field, 2, 1)


        accessibility_label = QLabel("Accessibility")
        archi_window_layout.addWidget(accessibility_label, 3, 0)

        self.accessibility_drop_down = QComboBox()
        self.accessibility_drop_down.addItem("Locations")
        self.accessibility_drop_down.addItem("Items")
        self.accessibility_drop_down.addItem("Minimal")
        archi_window_layout.addWidget(self.accessibility_drop_down, 3, 1)

        self.death_link_check_box = QCheckBox("Death Link")
        archi_window_layout.addWidget(self.death_link_check_box, 4, 0, 1, 2)

        archi_apply_layout = QHBoxLayout()

        archi_apply_button = QPushButton("Apply")
        archi_apply_button.clicked.connect(self.archi_apply_button_clicked)
        archi_apply_layout.addStretch(1)
        archi_apply_layout.addWidget(archi_apply_button)
        archi_window_layout.addLayout(archi_apply_layout, 5, 0, 1, 2)

        self.archi_check_box.setChecked(self.config.getboolean(ConfigSections.archipelago.enabled))
        self.archi_name_field.setText(self.config.get(ConfigSections.archipelago.name))
        self.progression_field.setValue(self.config.getint(ConfigSections.archipelago.progression))
        dropdown_index = self.accessibility_drop_down.findText(self.config.get(ConfigSections.archipelago.accessibility).capitalize())
        self.accessibility_drop_down.setCurrentIndex(dropdown_index)
        self.death_link_check_box.setChecked(self.config.getboolean(ConfigSections.archipelago.death_link))

        self.setLayout(archi_window_layout)
        self.setWindowTitle("Archipelago")

    def archi_apply_button_clicked(self):
        self.config.set(ConfigSections.archipelago.enabled, self.archi_check_box.isChecked())
        self.config.set(ConfigSections.archipelago.name, self.archi_name_field.text())
        self.config.set(ConfigSections.archipelago.progression, self.progression_field.value())
        self.config.set(ConfigSections.archipelago.accessibility, self.accessibility_drop_down.currentText().lower())
        self.config.set(ConfigSections.archipelago.death_link, self.death_link_check_box.isChecked())
        self.close()