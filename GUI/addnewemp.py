from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from employee_data import collect_employee_data
from ui_add_employee_record import Ui_MainWindow
from generatepdf import save_pdf
import sys
import sqlite3
import datetime
import spouse
from benefit import insert_benefit_data  # Ensure this function returns the Benefit_Id
from config import get_database_path
class AddEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_employee_data)

    def get_employee_data(self):
        employee_id = self.generate_employee_id()  # Generate employee ID
        archived = 0
        employee_data = collect_employee_data(self.ui, employee_id, archived)

        # Insert benefit data with default values for education and medical
        benefit_id = insert_benefit_data()  # Get the Benefit_Id from inserted record

        # Generate Salary_Id and insert salary data
        salary_id = self.insert_salary_data()  # Now it works because insert_salary_data is part of this class

        # Generate Position_Id (if necessary) and insert the employee data
        position_id = self.generate_position_id()  # Use this for the Position_Id

        # Save employee data to the database with the Benefit_Id and Salary_Id
        spouse_id = None  # Initialize spouse_id
        self.save_employee_data(employee_data, benefit_id, archived, spouse_id, salary_id, position_id)

        # Handle spouse information if provided
        first_name = self.ui.Spouse_FirstName.toPlainText()
        middle_name = self.ui.Spouse_MiddleName.toPlainText()
        last_name = self.ui.Spouse_LastName.toPlainText()
        date_of_marriage = self.ui.DateOfMarriage.toPlainText()
        place_of_marriage = self.ui.PlaceOfMarriage.toPlainText()

        if first_name or middle_name or last_name:  # Check if spouse name parts are provided
            Saved_ID = employee_id.replace('-', '')  # Removing hyphens for Saved_ID
            spouse_id = spouse.generate_spouse_id(Saved_ID)

            # Insert spouse data
            spouse.insert_spouse_data(spouse_id, first_name, middle_name, last_name, date_of_marriage, place_of_marriage)

            # **Now update the employee record with the Spouse_Id**
            self.update_employee_spouse_id(employee_data['employee_id'], spouse_id)

        # Define the path for saving the PDF
        pdf_file_path = f"C:\\Users\\leeu6\\Desktop\\SUHR-System\\pdf\\{employee_data['employee_id']}.pdf"

        # Call the save_pdf function
        save_pdf(employee_data, pdf_file_path)  # Pass employee data and PDF file path

    def update_employee_spouse_id(self, employee_id, spouse_id):
        """Update the Spouse_Id for the employee record in the database."""
        try:
            conn = sqlite3.connect(get_database_path())
            cursor = conn.cursor()

            # Update the Employee record to include the Spouse_Id
            cursor.execute(
                "UPDATE Employee SET Spouse_Id = ? WHERE Employee_Id = ?",
                (spouse_id, employee_id)
            )
            conn.commit()
            conn.close()

            print(f"Employee {employee_id} Spouse_Id updated to {spouse_id}.")
        except sqlite3.Error as e:
            print(f"Error updating Spouse_Id: {e}")

    # Other methods (insert_salary_data, generate_employee_id, save_employee_data, etc.) go here...

    def insert_salary_data(self):
        """Generate a new Salary_Id and insert a record in the Salary table."""
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Generate the new Salary_Id by getting the max value from the Salary table and incrementing it
        cursor.execute("SELECT MAX(Salary_Id) FROM Salary")
        max_id = cursor.fetchone()[0]
        new_salary_id = (max_id + 1) if max_id is not None else 1

        # You can insert default salary values. Adjust these as needed.
        monthly_salary = 0.0  # Set default or fetched monthly salary
        overtime_salary = 0.0  # Set default or fetched overtime salary
        total_salary = monthly_salary + overtime_salary  # Calculate total salary

        # Insert the new salary data into the Salary table
        cursor.execute(
            "INSERT INTO Salary (Salary_Id, Monthly_Salary, Overtime_Salary, Total_Salary) VALUES (?, ?, ?, ?)",
            (new_salary_id, monthly_salary, overtime_salary, total_salary)
        )
        conn.commit()
        conn.close()

        return new_salary_id

    # Other methods (generate_employee_id, save_employee_data, etc.) go here...

    def generate_employee_id(self):
        """Generate a unique Employee_Id based on the current date and count."""
        today_date = datetime.datetime.now().strftime('%Y%m%d')  # Format as YYYYMMDD
        count = self.get_employee_count_for_today(today_date)  # Get the count of employees for today
        employee_id = f"{today_date}-{count + 1:03}"  # Format as YYYYMMDD-### (e.g., 20231107-001)
        return employee_id

    def get_employee_count_for_today(self, today_date):
        print(f"Connecting to database: {get_database_path()}")
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM Employee WHERE strftime('%Y%m%d', Date_Employed) = ?"
        cursor.execute(query, (today_date,))
        count = cursor.fetchone()[0]
        conn.close()
        return count


    def generate_salary_id(self):
        """Generate a new Salary_Id for the Employee table."""
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Get the maximum Salary_Id from the Employee table, or start from 1 if it's the first employee
        cursor.execute("SELECT MAX(Salary_Id) FROM Employee")
        max_salary_id = cursor.fetchone()[0]
        salary_id = (max_salary_id + 1) if max_salary_id is not None else 1

        conn.close()

        return salary_id

    def generate_position_id(self):
        """Generate a new Position_Id."""
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Get the maximum Position_Id from the Position table, or start from 1 if it's the first entry
        cursor.execute("SELECT MAX(Position_Id) FROM Position")
        max_position_id = cursor.fetchone()[0]
        position_id = (max_position_id + 1) if max_position_id is not None else 1

        conn.close()

        return position_id

    def save_employee_data(self, data, benefit_id, archived, spouse_id, salary_id, position_id):
        try:
            conn = sqlite3.connect(get_database_path())
            cursor = conn.cursor()
            sql = '''INSERT INTO Employee (
                Employee_Id,
                Last_Name,
                First_Name,
                Middle_Name,
                Date_Employed,
                Position_Id,
                Dgte_Address,
                Home_Address,
                Date_Of_Birth,
                Place_Of_Birth,
                Citizenship,
                Non_Filipino_Id,
                Church,
                Tax_Id,
                Sss_No,
                Philhealth_No,
                Pagibig_No,
                Civil_Status,
                Spouse_Id,
                Academic_Id,
                Criminal_Record,
                Regular,
                Benefit_Id,
                Salary_Id,
                Contact_No,
                Archived
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            values = (
                data["employee_id"],
                data["last_name"],
                data["first_name"],
                data["middle_name"],
                datetime.datetime.now().strftime('%Y-%m-%d'),
                position_id,  # Use Position_Id here
                data["dmg_address"],
                data["home_address"],
                data["date_of_birth"],
                data["place_of_birth"],
                data["citizenship"],
                data.get("passport_num"),
                data["church_affiliation"],
                data["tin"],
                data["sss"],
                data["philhealth"],
                data["pagibig"],
                data["civil_status"],
                spouse_id,  # Initially None
                None,  # Placeholder for Academic_Id
                None,  # Placeholder for Criminal_Record
                0,     # Initially not Regular
                benefit_id,  # Use the Benefit_Id here
                salary_id,   # Use the generated Salary_Id here
                data["contact_num"],
                archived
            )
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Employee record added successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def get_archive_count_for_today(self, today_date):
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM Employee WHERE strftime('%Y%m%d', Date_Employed) = ? AND Archived = 1"
        cursor.execute(query, (today_date,))
        count = cursor.fetchone()[0]
        conn.close()
        return count

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()
    window.show()
    sys.exit(app.exec())
