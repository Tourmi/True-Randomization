import os
import shutil
import traceback

from PySide6.QtCore import QThread

from randomizer.Constants import ASSETS_DIR
from randomizer import Data
from configuration import Config
from configuration import ConfigSections
from ..widgets.Signaller import Signaller

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
        
        for asset in self.asset_list:
            output_path = os.path.abspath("")
            
            root = os.getcwd()
            os.chdir("Tools\\UModel")
            os.system("cmd /c umodel_64.exe -path=\"" + self.config.get(ConfigSections.misc.game_path) + "\\BloodstainedRotN\\Content\\Paks\" -out=\"" + output_path + "\" -save \"" + ASSETS_DIR + "\\" + Data.file_to_path[asset] + "\\" + asset.split("(")[0] + "\"")
            os.chdir(root)
            
            current += 1
            self.signaller.progress.emit(current)
        
        self.signaller.finished.emit()
