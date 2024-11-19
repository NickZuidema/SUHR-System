import sqlite3
import sys
import uuid
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6.QtGui import QPalette, QColor

#ui link
from ui_edit import Ui_MainWindow

from config import get_database_path
from session import SessionManager
import os

# def force_light_mode(app):
#     palette = QPalette()
#     palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))
#     palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
#     palette.setColor(QPalette.ColorRole.AlternateBase, QColor(240, 240, 240))
#     palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))
#     palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
#     palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
#     palette.setColor(QPalette.ColorRole.Highlight, QColor(30, 144, 255))
#     palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
#     app.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # force_light_mode(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())