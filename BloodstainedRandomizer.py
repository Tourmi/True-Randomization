import sys
from PySide6.QtWidgets import QApplication

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