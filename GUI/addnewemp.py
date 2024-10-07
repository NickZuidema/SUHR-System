import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_add_employee_record import Ui_MainWindow  # Import the UI class

class AddEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Initialize the UI
        
        # Additional setup can go here, like connecting buttons or setting defaults

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()  # Create an instance of the AddEmployeeWindow
    window.show()  # Show the window
    sys.exit(app.exec())  # Execute the application
