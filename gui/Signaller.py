from PySide6.QtCore import QObject, Signal

class Signaller(QObject):
    progress = Signal(int)
    finished = Signal()
    error    = Signal(str)