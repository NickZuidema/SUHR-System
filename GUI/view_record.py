import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from ui_preview_template import Ui_MainWindow
from config import get_database_path  # Import get_database_path from config

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Get the database path from the config module
        database_path = get_database_path()

        try:
            # Use 'with' to ensure the connection is properly managed
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()

                # Example of employee_id in the format YYYYMMDD-XXX
                employee_id = '20241108-001'  # Replace with the actual employee ID you want to display

                # Retrieve data for the specific employee ID from the Employee table
                cursor.execute("SELECT Dgte_Address, Home_Address, Date_Of_Birth, Citizenship, Civil_Status, Sss_No, Pagibig_No, Contact_No FROM Employee WHERE Employee_Id = ?", (employee_id,))
                employee_data = cursor.fetchone()

                if employee_data is None:
                    raise ValueError(f"No employee found with ID {employee_id}")

           
                self.ui.employee_dumaguete_address.setPlainText(employee_data[0])  # Set Dumaguete address in QTextEdit
                self.ui.employee_home_address.setPlainText(employee_data[1])  # Set Home address in QTextEdit
              
            
                self.ui.employee_birthday.setText(employee_data[2]) 
                self.ui.employee_citizenship.setText(employee_data[3])
                self.ui.employee_civil_status.setText(employee_data[4])
                self.ui.employee_sss.setText(employee_id[5])  
                self.ui.employee_pagibig.setText(employee_id[6])
                self.ui.employee_philHealth.setText(employee_id[7])
                self.ui.employee_phonenumber.setText(employee_id[8])
                self.ui.employee_email.setText(employee_id[9])
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while accessing the database: {e}")
        except ValueError as e:
            QMessageBox.warning(self, "Record Not Found", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
