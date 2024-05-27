import os
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from gui.MainWindow import MainWindow
from configuration.Config import Config

def main():
    config = Config()
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(config.write_and_exit)
    main = MainWindow(config)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()