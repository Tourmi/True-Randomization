import os
import shutil
import traceback

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from configuration.Config import Config
from configuration.ConfigSections import ConfigSections
from .Signaller import Signaller
import Manager

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
        current = 0
        self.signaller.progress.emit(current)
        
        #Extract specific assets from the game's pak using UModel
        
        if os.path.isdir(Manager.asset_dir) and self.asset_list == list(Manager.file_to_path):
            shutil.rmtree(Manager.asset_dir)
        
        for asset in self.asset_list:
            output_path = os.path.abspath("")
            
            root = os.getcwd()
            os.chdir("Tools\\UModel")
            os.system("cmd /c umodel_64.exe -path=\"" + self.config.get(ConfigSections.misc.game_path) + "\\BloodstainedRotN\\Content\\Paks\" -out=\"" + output_path + "\" -save \"" + Manager.asset_dir + "\\" + Manager.file_to_path[asset] + "\\" + asset.split("(")[0] + "\"")
            os.chdir(root)
            
            current += 1
            self.signaller.progress.emit(current)
        
        self.signaller.finished.emit()
