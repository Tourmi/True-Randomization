from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Signaller(QObject):
    progress = Signal(int)
    finished = Signal()
    error    = Signal(str)