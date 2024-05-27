from __future__ import annotations

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QWidget

type FileCategories = dict[str, set[str]]

left_side_categories = ["DataTable", "StringTable"]

class ModifiedFilesWidget(QWidget):
    def __init__(self, file_categories : FileCategories) -> None:
        super(ModifiedFilesWidget, self).__init__()
        self.modified_files = file_categories

        layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        layout.addLayout(left_layout)
        right_layout = QVBoxLayout()
        layout.addLayout(right_layout)
        self.setLayout(layout)

        self.labels : dict[str, QLabel] = {}
        for category in file_categories.keys():
            label = QLabel(self)
            self.labels[category] = label
            if category in left_side_categories: left_layout.addWidget(label)
            else: right_layout.addWidget(label)
            self._label_change(category)

    @staticmethod
    def from_default() -> ModifiedFilesWidget:
        return ModifiedFilesWidget({
            "DataTable": {
                "PB_DT_AmmunitionMaster",
                "PB_DT_ArchiveEnemyMaster",
                "PB_DT_ArmorMaster",
                "PB_DT_ArtsCommandMaster",
                "PB_DT_BallisticMaster",
                "PB_DT_BloodlessAbilityData",
                "PB_DT_BookMaster",
                "PB_DT_BRVAttackDamage",
                "PB_DT_BRVCharacterParameters",
                "PB_DT_BulletMaster",
                "PB_DT_CharacterMaster",
                "PB_DT_CharacterParameterMaster",
                "PB_DT_CharaUniqueParameterMaster",
                "PB_DT_CollisionMaster",
                "PB_DT_ConsumableMaster",
                "PB_DT_CoordinateParameter",
                "PB_DT_CraftMaster",
                "PB_DT_DamageMaster",
                "PB_DT_DialogueTableItems",
                "PB_DT_DialogueTextMaster",
                "PB_DT_DropRateMaster",
                "PB_DT_EnchantParameterType",
                "PB_DT_EventFlagMaster",
                "PB_DT_GimmickFlagMaster",
                "PB_DT_HairSalonOldDefaults",
                "PB_DT_ItemMaster",
                "PB_DT_QuestMaster",
                "PB_DT_RoomMaster",
                "PB_DT_SetBonus",
                "PB_DT_ShardMaster",
                "PB_DT_SoundMaster",
                "PB_DT_SpecialEffectDefinitionMaster",
                "PB_DT_SpecialEffectGroupMaster",
                "PB_DT_SpecialEffectMaster",
                "PB_DT_WeaponMaster"
            },
            "StringTable": {
                "PBMasterStringTable",
                "PBScenarioStringTable",
                "PBSystemStringTable"
            },
            "Texture": {
                "T_N3127_Body_Color",
                "T_N3127_Uni_Color",
                "m51_EBT_BG",
                "m51_EBT_BG_01",
                "m51_EBT_Block",
                "m51_EBT_Block_00",
                "m51_EBT_Block_01",
                "m51_EBT_Door",
                "time_shard_diffuse"
            },
            "UI": {
                "WindowMinimap02",
                "icon",
                "ui_icon_pickup_dagger",
                "ui_icon_pickup_timeShard",
                "ui_icon_results_dagger",
                "ui_icon_results_timeShard"
            },
            "Blueprint": {
                "PBExtraModeInfo_BP"
            }})

    def add_file(self, category : str, file : str) -> None:
        self.modified_files[category].add(file)
        self._label_change(category)

    def remove_file(self, category : str, file : str) -> None:
        self.modified_files[category].discard(file)
        self._label_change(category)

    def _label_change(self, category) -> None:
        files  = self.modified_files[category]
        label  = self.labels[category]
        string = f"Modified {category}:\n\n"
        for file in sorted(files):
            string += f"{file}\n"
        label.setText(string)