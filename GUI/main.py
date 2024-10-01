import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_login import Ui_Login  # Import the Ui_Login class

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)
        self.connect_db()  # Establish the connection once at startup

    def connect_db(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(r'C:\Users\leeu6\OneDrive\Desktop\SUHR\SUHR-System\Database\SUHRSystem.db')
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Could not connect to the database: {e}")
            sys.exit(1)

    def authenticate(self, username, password):
        """Authenticate the user by checking the provided username and password."""
        try:
           
            query = "SELECT * FROM users WHERE User_Id=? AND password=?"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()

           
            self.cursor.close()

            
            return result is not None
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error querying the database: {e}")
            return False

    def handle_login(self):
        """Handle the login button click event."""
        username = self.ui.textEdit.toPlainText()
        password = self.ui.textEdit_2.toPlainText()

        if self.authenticate(username, password):
            QMessageBox.information(self, "Success", "Login successful!")
            # Proceed to the next part of your application
        else:
            QMessageBox.warning(self, "Error", "Login failed! Please check your credentials.")

    def closeEvent(self, event):
        """Close the database connection when the application exits."""
        if hasattr(self, 'connection'):
            self.connection.close()
        event.accept()  # Accept the close event

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
