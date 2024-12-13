import sqlite3
import sys
import uuid
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6.QtGui import QPalette, QColor
from ui_login import Ui_Login
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
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.pushButton.clicked.connect(self.handle_login)
        self.db_path = get_database_path()
        self.session_manager = SessionManager()
        self.check_session()

    def authenticate(self, username, password):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM User WHERE User_Id=? AND password=?"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()
                return result is not None
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error querying the database: {e}")
            return False

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if self.authenticate(username, password):
            session_id = str(uuid.uuid4())
            self.session_manager.save_session(session_id, username)
            QMessageBox.information(self, "Success", "Login successful!")
            self.show_dashboard(username)
        else:
            self.session_manager.log_failed_attempt(username)
            QMessageBox.warning(self, "Error", "Login failed! Please check your credentials.")

    def show_dashboard(self, username=None):
        from dashboard import Dashboard
        self.dashboard = Dashboard(self.db_path, username)
        self.dashboard.show()
        self.hide()

    def check_session(self):
        user = self.session_manager.check_session()
        if user:
            self.show_dashboard(user)
        else:
            self.ui.pushButton.setEnabled(True)

    def logout(self):
        self.session_manager.clear_session()
        self.ui.pushButton.setEnabled(True)

    def add_new_employee(self, employee_data):
        # ...existing code to add employee...
        self.session_manager.log_activity(self.current_user, "Add new employee data")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # force_light_mode(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())