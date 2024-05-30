from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox

class MessageBox():
    @staticmethod
    def _show_message_box(parent : QWidget, title : str, text : str, icon : QMessageBox.Icon):
        box = QMessageBox(parent)
        box.setWindowTitle(title)
        box.setIcon(icon)
        box.setText(text)
        box.exec()

    @staticmethod
    def error(parent : QWidget, text : str, title = "Error"):
        MessageBox._show_message_box(parent, title, text, QMessageBox.Icon.Critical)
    
    @staticmethod
    def success(parent : QWidget, text : str, title = "Success"):
        MessageBox._show_message_box(parent, title, text, QMessageBox.Icon.Information)

    @staticmethod
    def warn(parent : QWidget, text : str, title = "Warning"):
        MessageBox._show_message_box(parent, title, text, QMessageBox.Icon.Warning)
