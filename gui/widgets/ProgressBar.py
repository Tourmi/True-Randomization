from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QProgressDialog
from . import Signaller
from . import MessageBox

class ProgressBar(QProgressDialog):
    def __init__(self, min : int, max : int, parent : QWidget, title : str):
        super().__init__("", None, min, max, parent) # type: ignore
        self.setWindowTitle(title)
        self.setWindowModality(Qt.WindowModality.WindowModal)
    
    def connect_to(self, signaller : Signaller):
        signaller.progress.connect(self._set_progress)
        signaller.error.connect(self._thread_failure)
        signaller.step_changed.connect(self.setLabelText)
    
    def _set_progress(self, progress):
        self.setValue(progress)
    
    def _thread_failure(self, detail):
        self.close()
        self.parentWidget().setEnabled(True)
        print(detail)
        MessageBox.error(self, "An error has occured.\nCheck the command window for more detail.")