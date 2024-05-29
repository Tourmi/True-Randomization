import os
import requests
import shutil
import subprocess
import traceback
import zipfile

from PySide6.QtCore import QThread

from randomizer.Constants import SCRIPT_NAME
from configuration import Config
from .Signaller import Signaller

class Update(QThread):
    def __init__(self, config : Config, progress_bar, api):
        QThread.__init__(self)
        self.config = config
        self.signaller = Signaller()
        self.progress_bar = progress_bar
        self.api = api
    
    def run(self):
        try:
            self.process()
        except Exception:
            self.signaller.error.emit(traceback.format_exc())

    def process(self):
        current = 0
        zip_name = "True Randomization.zip"
        exe_name = f"{SCRIPT_NAME}.exe"
        self.signaller.progress.emit(current)
        
        #Download
        
        with open(zip_name, "wb") as file_writer:
            url = requests.get(self.api["assets"][0]["browser_download_url"], stream=True)
            for data in url.iter_content(chunk_size=4096):
                file_writer.write(data)
                current += len(data)
                self.signaller.progress.emit(current)
        
        self.progress_bar.setLabelText("Extracting...")
        
        #Purge folders
        
        shutil.rmtree("Data")
        shutil.rmtree("MapEdit\\Data")
        shutil.rmtree("Tools\\UE4 DDS Tools")
        shutil.rmtree("Tools\\UE4SS")
        shutil.rmtree("Tools\\UModel")
        shutil.rmtree("Tools\\UnrealPak")
        
        #Extract
        
        os.rename(exe_name, "delete.me")
        os.rename("Tools\\UAssetAPI\\Newtonsoft.Json.dll", "Tools\\UAssetAPI\\delete1.me")
        os.rename("Tools\\UAssetAPI\\UAssetAPI.dll",       "Tools\\UAssetAPI\\delete2.me")
        os.rename("Tools\\UAssetAPI\\UAssetSnippet.dll",   "Tools\\UAssetAPI\\delete3.me")
        with zipfile.ZipFile(zip_name, "r") as zip_ref:
            zip_ref.extractall("")
        os.remove(zip_name)
        
        #Carry previous config params
        new_config = Config()
        self.config.populate_config(new_config)
        new_config.write()
        
        #Open new EXE
        
        subprocess.Popen(exe_name)
        self.signaller.finished.emit()