import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_preview_template import Ui_MainWindow
from config import get_database_path  # Import get_database_path from config

class MainWindow(QMainWindow):
    def __init__(self, employee_id):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Get the database path from the config module
        database_path = get_database_path()

        try:
            # Use 'with' to ensure the connection is properly managed
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()

                # Use the passed employee_id for the query
                cursor.execute("""
                    SELECT Last_Name, First_Name, Middle_Name, Dgte_Address, Home_Address, Date_Of_Birth,
                           Citizenship, Civil_Status, Sss_No, Pagibig_No, Philhealth_No, Contact_No
                    FROM Employee
                    WHERE Employee_Id = ?
                """, (employee_id,))
                employee_data = cursor.fetchone()

                if employee_data is None:
                    raise ValueError(f"No employee found with ID {employee_id}")

                # Concatenate Last_Name, First_Name, and Middle_Name to form the full name
                last_name, first_name, middle_name = employee_data[0], employee_data[1], employee_data[2]
                full_name = f"{last_name}, {first_name} {middle_name or ''}".strip()

                # Populate UI fields with data from the database
                self.ui.employee_name.setText(full_name)  # Set full name in QLabel
                self.ui.employee_dumaguete_address.setPlainText(employee_data[3])  # Set Dumaguete address in QTextEdit
                self.ui.employee_home_address.setPlainText(employee_data[4])  # Set Home address in QTextEdit
                self.ui.employee_birthday.setText(employee_data[5])  # Set Date of Birth
                self.ui.employee_citizenship.setText(employee_data[6])  # Set Citizenship
                self.ui.employee_civil_status.setText(employee_data[7])  # Set Civil Status
                self.ui.employee_sss.setText(employee_data[8])  # Set SSS number
                self.ui.employee_pagibig.setText(employee_data[9])  # Set Pag-IBIG number
                self.ui.employee_philHealth.setText(employee_data[10])  # Set PhilHealth number
                self.ui.employee_phonenumber.setText(employee_data[11])  # Set Contact number

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while accessing the database: {e}")
        except ValueError as e:
            QMessageBox.warning(self, "Record Not Found", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage, replace '20241114-006' with the actual employee_id passed from the dashboard
    app = QApplication(sys.argv)
    window = MainWindow('20241114-006')  # Pass employee_id dynamically
    window.show()
    sys.exit(app.exec())
