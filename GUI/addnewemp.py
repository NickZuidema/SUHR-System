from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from employee_data import collect_employee_data
from ui_add_employee_record import Ui_MainWindow
from generatepdf import save_pdf
import sys
import datetime
import sqlite3
import spouse
import academic 
from benefit import insert_benefit_data  # Ensure this function returns the Benefit_Id
from config import get_database_path, get_pdf_path
class AddEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_employee_data)

    def get_employee_data(self):
        employee_id = self.generate_employee_id()
        archived = 0
        employee_data = collect_employee_data(self.ui, employee_id, archived)

        # Handle spouse information if provided
        first_name = self.ui.Spouse_FirstName.toPlainText()
        middle_name = self.ui.Spouse_MiddleName.toPlainText()
        last_name = self.ui.Spouse_LastName.toPlainText()
        date_of_marriage = self.ui.DateOfMarriage.toPlainText()
        place_of_marriage = self.ui.PlaceOfMarriage.toPlainText()

        # Insert benefit data with default values for education and medical
        benefit_id = insert_benefit_data()  # Get the new Benefit_Id from the inserted record

         # Generate Salary_Id and insert salary data
        salary_id = self.insert_salary_data() # Now it works because insert_salary_data is part of this class
        
        if first_name or middle_name or last_name:  # Check if at least one spouse name part is provided
            Saved_ID = employee_id.replace('-', '')  # Removing hyphens from employee_id for Saved_ID
            spouse_id = spouse.generate_spouse_id(Saved_ID)

            # Insert the spouse data into the respective tables
            spouse.insert_spouse_data(spouse_id, first_name, middle_name, last_name, date_of_marriage, place_of_marriage)

            # Update the employee record to include the Spouse_Id
            self.update_employee_spouse_id(employee_data['employee_id'], spouse_id)

        # Insert academic record data if provided
        elementary_id = self.ui.elementary_school.toPlainText()
        elementary_fin = self.ui.yeargraduate_elementary.toPlainText()
        seniorhigh_id = self.ui.highschool.toPlainText()
        seniorhigh_diploma = self.ui.diploma_highschool.toPlainText()
        seniorhigh_fin = self.ui.yeargraduate_highschool.toPlainText()
        college_id = self.ui.College.toPlainText()
        college_diploma = self.ui.diploma_college.toPlainText()
        gradschool_id = self.ui.Graduateschool.toPlainText()
        gradschool_diploma = self.ui.diploma_college.toPlainText()
        gradschool_fin = self.ui.yeargraduate_graduateschool.toPlainText()

        # Only proceed if at least one field is filled
        if elementary_id or seniorhigh_fin or seniorhigh_id or college_id or gradschool_id:
            # Insert the academic data
            academic_record_id = academic.insert_academic_record_data(
                elementary_id, elementary_fin, seniorhigh_fin, 
                seniorhigh_id, seniorhigh_diploma, seniorhigh_fin, 
                college_id, college_diploma, gradschool_id, 
                gradschool_diploma, gradschool_fin
            )

            # Update employee data with the new Academic_Record_Id
            self.save_employee_data(employee_data, benefit_id, archived, spouse_id,salary_id, academic_record_id)
        else:
            # If no academic record, save employee data with None for academic_record_id
            self.save_employee_data(employee_data, benefit_id, archived, spouse_id,salary_id, None)

        # Save employee data to the database with the Benefit_Id and initially without Spouse_Id
        pdf_file_path = f"{get_pdf_path()}\\{employee_id}.pdf"
        # Call the save_pdf function from generatepdf.py
        save_pdf(employee_data, pdf_file_path)  # Pass the employee data and the PDF file path

    def generate_employee_id(self):
        today_date = datetime.datetime.now().strftime('%Y%m%d')
        count = self.get_employee_count_for_today(today_date)
        employee_id = f"{today_date}-{count + 1:03}"

        print(f"Generated Employee ID: {employee_id}")  # Debugging line
        
        # Ensure uniqueness of Employee_Id
        while self.check_employee_id_exists(employee_id):
            print(f"Duplicate Employee ID found: {employee_id}. Regenerating.")
            count += 1
            employee_id = f"{today_date}-{count + 1:03}"  # Increment the count and regenerate the ID
        
        return employee_id

    def get_employee_count_for_today(self, today_date):
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()
        query = """
        SELECT COUNT(*) FROM Employee
        WHERE strftime('%Y%m%d', Date_Employed) = ?
        """
        cursor.execute(query, (today_date,))
        count = cursor.fetchone()[0]
        print(f"Employee count for {today_date}: {count}")  # Debugging line
        conn.close()
        return count

    def check_employee_id_exists(self, employee_id):
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM Employee WHERE Employee_Id = ?"
        cursor.execute(query, (employee_id,))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0

    def save_employee_data(self, data, benefit_id, archived, spouse_id, salary_id, academic_record_id):

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
                self.generate_position_id(),  # Use Position_Id here
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
                academic_record_id,  # Updated to Academic_Record_Id
                None,  # Placeholder for Criminal_Record
                0,     # Initially not Regular
                benefit_id,  # Use the Benefit_Id here
                None,  # Placeholder for Salary_Id
                data["contact_num"],
                archived
            )
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Employee record added successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def update_employee_spouse_id(self, employee_id, spouse_id):
        try:
            conn = sqlite3.connect(get_database_path())
            cursor = conn.cursor()
            sql = '''UPDATE Employee
                     SET Spouse_Id = ?
                     WHERE Employee_Id = ?'''
            cursor.execute(sql, (spouse_id, employee_id))
            conn.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred while updating spouse ID: {e}")
        finally:
            conn.close()
            
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
        count = self.get_position_count_for_today()
        today_date = datetime.datetime.now().strftime('%Y%m%d')
        position_id = f"{today_date}-{count + 1:03}"
        return position_id

    def get_position_count_for_today(self):
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()
        query = """
        SELECT COUNT(*) FROM Position
        """
        cursor.execute(query)
        count = cursor.fetchone()[0]
        conn.close()
        return count

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()
    window.show()
    sys.exit(app.exec())