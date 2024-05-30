import os
import shutil
import textwrap
import traceback
from pathlib import Path

from PySide6.QtCore import QThread

from randomizer.Constants import ASSETS_DIR
from randomizer import Data
from configuration import Config
from configuration import ConfigSections
from ..widgets.Signaller import Signaller

_IMPORT_LOG_PATH = Path("Tools\\UModel\\import.log").absolute()

class Import(QThread):
    def __init__(self, config : Config, asset_list):
        QThread.__init__(self)
        self.signaller = Signaller()
        self.config = config
        self.asset_list = asset_list
    
    def run(self):
        try:
            self.process()
        except Exception:
            self.signaller.error.emit(traceback.format_exc())

    def process(self):
        self.signaller.step_changed.emit("Importing assets...")
        current = 0
        self.signaller.progress.emit(current)
        
        #Extract specific assets from the game's pak using UModel
        
        if os.path.isdir(ASSETS_DIR) and self.asset_list == list(Data.file_to_path):
            shutil.rmtree(ASSETS_DIR)

        output_path = os.path.abspath("")
        #There a limit of around 8000 characters per command, split the list of packages into multiple batches of maximum 7500 characters
        allPackages = " ".join([f"-pkg=\"{ASSETS_DIR}\\{Data.file_to_path[asset]}\\{asset.split("(")[0]}\"" for asset in self.asset_list])
        batches = textwrap.wrap(allPackages, 7500)
        root = os.getcwd()
        os.chdir("Tools\\UModel")
        _IMPORT_LOG_PATH.unlink(missing_ok=True)
        hadError = False
        for batch in batches:
            result = os.system(f"cmd /c umodel_64.exe -path=\"{self.config.get(ConfigSections.misc.game_path)}\\BloodstainedRotN\\Content\\Paks\" -out=\"{output_path}\" -save {batch} >> {_IMPORT_LOG_PATH}")
            if result != 0:
                hadError = True
            current += batch.count(" ") + 1
            self.signaller.progress.emit(current)
        os.chdir(root)
        if hadError:
            self.signaller.error.emit(f"An error occured during import. Please check {_IMPORT_LOG_PATH} for more details")
        self.signaller.finished.emit()
