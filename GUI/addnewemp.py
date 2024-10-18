from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from employee_data import collect_employee_data
from ui_add_employee_record import Ui_MainWindow
from generatepdf import save_pdf
import sys
import datetime
import sqlite3
import spouse
from benefit import insert_benefit_data  # Ensure this function returns the Benefit_Id

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

        # Insert benefit data with default values for education and medical
        benefit_id = insert_benefit_data()  # Get the new Benefit_Id from the inserted record

        # Save employee data to the database with the Benefit_Id
        spouse_id = None  # Initialize spouse_id
        self.save_employee_data(employee_data, benefit_id, archived, spouse_id)

        # Handle spouse information if provided
        first_name = self.ui.Spouse_FirstName.toPlainText()
        middle_name = self.ui.Spouse_MiddleName.toPlainText()
        last_name = self.ui.Spouse_LastName.toPlainText()
        date_of_marriage = self.ui.DateOfMarriage.toPlainText()
        place_of_marriage = self.ui.PlaceOfMarriage.toPlainText()

        if first_name or middle_name or last_name:  # Check if at least one spouse name part is provided
            Saved_ID = employee_id.replace('-', '')
            spouse_id = spouse.generate_spouse_id(Saved_ID)

            # Insert the spouse data into the respective tables
            spouse.insert_spouse_data(spouse_id, first_name, middle_name, last_name, date_of_marriage, place_of_marriage)

            # Update the employee record to include the Spouse_Id
            self.update_employee_spouse_id(employee_data['employee_id'], spouse_id)

        # Define the path for saving the PDF
        pdf_file_path = f"C:\\Users\\leeu6\\Desktop\\SUHR-System\\pdf\\{employee_data['employee_id']}.pdf"

        # Call the save_pdf function from generatepdf.py
        save_pdf(employee_data, pdf_file_path)  # Pass the employee data and the PDF file path

    def generate_employee_id(self):
        today_date = datetime.datetime.now().strftime('%Y%m%d')
        count = self.get_employee_count_for_today(today_date)
        employee_id = f"{today_date}-{count + 1:03}"
        return employee_id

    def get_employee_count_for_today(self, today_date):
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()
        query = """
        SELECT COUNT(*) FROM Employee
        WHERE strftime('%Y%m%d', Date_Employed) = ?
        """
        cursor.execute(query, (today_date,))
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def generate_position_id(self):
        count = self.get_position_count_for_today()
        today_date = datetime.datetime.now().strftime('%Y%m%d')
        position_id = f"{today_date}-{count + 1:03}"
        return position_id

    def get_position_count_for_today(self):
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()
        query = """
        SELECT COUNT(*) FROM Position
        """
        cursor.execute(query)
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def save_employee_data(self, data, benefit_id, archived, spouse_id):
        try:
            conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
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
                None,
                None,
                0,
                benefit_id,  # Use the Benefit_Id here
                None,
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
            conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
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
        
    def get_archive_count_for_today(self, today_date):
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()
        query = """
        SELECT COUNT(*) FROM Employee
        WHERE strftime('%Y%m%d', Date_Employed) = ? AND Archived = 1
        """
        cursor.execute(query, (today_date,))
        count = cursor.fetchone()[0]
        conn.close()
        return count

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()
    window.show()
    sys.exit(app.exec())
