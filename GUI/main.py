import sys
import sqlite3
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStyleFactory
from ui_login import Ui_Login  # Import the Ui_Login class

import os

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)


def force_light_mode(app):
    # Create a palette with light mode colors
    palette = QPalette()

    # Set light mode background colors
    palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))        # White background
    palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))         # Black text
    palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))         # White input background
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(240, 240, 240))# Slightly gray background for widgets
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))  # Tooltip background
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))        # Tooltip text
    palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))               # Text color
    palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))       # Button background
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))         # Button text
    palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))       # Bright text (for warnings, etc.)
    palette.setColor(QPalette.ColorRole.Highlight, QColor(30, 144, 255))     # Highlight color
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255)) # Highlighted text (white)

    # Apply the palette to the application
    app.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)
        self.connect_db()  # Establish the connection once at startup

         # Set a default font for the application
        default_font = QFont("Helvetica", 12)  # Change to your desired font and size
        QApplication.setFont(default_font)

    def connect_db(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(r'SUHRSystem.db')
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
        username = self.ui.lineEdit
        password = self.ui.lineEdit_2

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

    # Force the application to use the Fusion style for a more uniform cross-platform look
    #app.setStyle(QStyleFactory.create('Fusion'))

    force_light_mode(app)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
