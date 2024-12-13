import sqlite3
from config import get_database_path
from ui_salary import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPlainTextEdit, QLabel, QPushButton, QMessageBox
import sys

DATABASE_PATH = get_database_path()

def generate_salary_id():
    """Generate a new Salary_Id for the Employee table."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Get the maximum Salary_Id from the Employee table, or start from 1 if it's the first employee
    cursor.execute("SELECT MAX(Salary_Id) FROM Salary")
    max_salary_id = cursor.fetchone()[0]
    salary_id = (max_salary_id + 1) if max_salary_id is not None else 1

    conn.close()

    return salary_id

def insert_salary_data(monthly_salary, overtime_salary, total_salary):
    """Insert a new salary record with provided monthly, overtime, and total salary."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        # Generate a new Salary_Id
        salary_id = generate_salary_id()
        if salary_id is None:
            raise ValueError("Could not generate a valid Salary ID.")

        # Print the values being inserted for debugging
        print(f"Inserting salary data: Salary_Id={salary_id}, Monthly_Salary={monthly_salary}, Overtime_Salary={overtime_salary}, Total_Salary={total_salary}")

        # Insert the new salary record
        cursor.execute("INSERT INTO Salary (Salary_Id, Monthly_Salary, Overtime_Salary, Total_Salary) VALUES (?, ?, ?, ?)",
                       (salary_id, monthly_salary, overtime_salary, total_salary))

        conn.commit()
        print(f"New salary record added with ID: {salary_id}")

    except sqlite3.Error as e:
        print(f"Error inserting salary data: {e}")
        salary_id = None  # Return None if there is an error

    finally:
        if conn:
            conn.close()

    return salary_id


def update_employee_with_salary(employee_id, monthly_salary, overtime_salary, total_salary):
    """Add a salary record and link the generated Salary_Id to an employee."""
    conn = None
    try:
        # Insert salary data and retrieve the new Salary_Id
        salary_id = insert_salary_data(monthly_salary, overtime_salary, total_salary)
        if salary_id is None:
            raise ValueError("Could not create and retrieve Salary ID.")

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute("UPDATE Employee SET Salary_Id = ? WHERE Employee_Id = ?",
                       (salary_id, employee_id))

        conn.commit()
        print(f"Employee {employee_id} updated with Salary ID: {salary_id}")

    except sqlite3.Error as e:
        print(f"Error updating employee with Salary ID: {e}")

    finally:
        if conn:
            conn.close()


class SalaryDialog(QDialog):
    def __init__(self,emp_id):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.employee_id = emp_id
        print(f"At Salary Dialog EMP id is {emp_id}")
        # Connect the buttons to their respective functions

       
        self.ui.apply.clicked.connect(self.on_apply)

        self.ui.close.clicked.connect(self.on_close)
        
        conn = None
        try:
        
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()

            cursor.execute("""select Monthly_Salary, Overtime_Salary, Total_Salary
                           from Salary where 
                           Salary_Id = (select Salary_Id from Employee where Employee_Id = ?)
                           """,
                        (self.employee_id,))
            salary_data = cursor.fetchone()
           
            if salary_data is None:
                QMessageBox.information(self, "Salary Data", "Employee has no Salary Data")
            else:
                self.ui.salary_Monthly.setPlainText(str(salary_data[0]))
                self.ui.salary_Overtime.setPlainText(str(salary_data[1]))
                self.ui.salary_Total.setPlainText(str(salary_data[2]))

        except sqlite3.Error as e:
            print(f"Error: {e}")

    def on_apply(self):
        
       

        if self.ui.apply_confirm_changes.isChecked() == True:

            """Handle the Apply button to insert and update salary information."""
            monthly_salary = float(self.ui.salary_Monthly.toPlainText())
            overtime_salary = float(self.ui.salary_Overtime.toPlainText())
            total_salary = float(self.ui.salary_Total.toPlainText())

            # Update the employee record with salary data
            employee_id = self.employee_id # Example Employee ID; this could be passed dynamically
            update_employee_with_salary(employee_id, monthly_salary, overtime_salary, total_salary)

            QMessageBox.information(self, "Updated Salary Data", f"Updated Salary Data for {self.employee_id}")
        
        else:
            QMessageBox.warning(self, "Error", f"Confirm Update On Record: {self.employee_id}")
        

    def on_close(self):
        """Close the dialog."""
        self.close()

# Example usage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SalaryDialog()
    window.show()
    sys.exit(app.exec())