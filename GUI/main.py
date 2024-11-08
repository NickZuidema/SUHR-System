# main.py
import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_login import Ui_Login
from config import get_database_path
from session import SessionManager  # Import the session manager

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)
        self.db_path = get_database_path()

        # Create a session manager instance
        self.session_manager = SessionManager()

        # Check for an active session on start
        self.check_session()

    def authenticate(self, username, password):
        """Authenticate the user by checking the provided username and password."""
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
        """Handle the login button click event."""
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if self.authenticate(username, password):
            self.session_manager.save_session(username)  # Save session
            QMessageBox.information(self, "Success", "Login successful!")
            self.show_dashboard(username)  # Pass username to Dashboard  
        else:
            QMessageBox.warning(self, "Error", "Login failed! Please check your credentials.")

    def show_dashboard(self, username=None):
        """Show the main dashboard after login."""
        from dashboard import Dashboard  # Import locally to avoid circular import
        self.dashboard = Dashboard(self.db_path, username)  # Pass both db_path and username to Dashboard
        self.dashboard.show()
        self.hide()  # Hide login window

    def check_session(self):
        """Check if there's an active session."""
        user = self.session_manager.check_session()
        if user:
            self.show_dashboard(user)  # Automatically show dashboard if session exists
        else:
            self.ui.pushButton.setEnabled(True)  # Enable login button for the user to log in

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
