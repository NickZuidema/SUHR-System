import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_login import Ui_Login
from dashboard import Dashboard  

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)
        self.db_path = r'C:\Users\leeu6\Desktop\SUHR\SUHR-System\Database\SUHRSystem.db'  

    def authenticate(self, username, password):
        """Authenticate the user by checking the provided username and password."""
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM user WHERE User_Id=? AND password=?"
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
            QMessageBox.information(self, "Success", "Login successful!")
            self.show_dashboard()  
        else:
            QMessageBox.warning(self, "Error", "Login failed! Please check your credentials.")

    def show_dashboard(self):
        """Show the main dashboard after login."""
        self.dashboard = Dashboard(self.db_path)  
        self.dashboard.show()
        self.hide() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
