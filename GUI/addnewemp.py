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
        self.save_employee_data(employee_data, benefit_id)

        # Define the path for saving the PDF
        pdf_file_path = f"C:\\Users\\Admin\\Downloads\\testing shit\\{employee_data['employee_id']}.pdf"

        # Call the save_pdf function from generatepdf.py
        save_pdf(employee_data, pdf_file_path)  # Pass the employee data and the PDF file path

        spouse_name = self.ui.SpouseName.toPlainText()
        if spouse_name:
            Saved_ID = employee_id.replace('-', '')
            spouse_id, full_name = spouse.generate_spouse_id(Saved_ID)
            full_name = spouse_name
            spouse.insert_spouse_data(spouse_id, full_name)

    def generate_employee_id(self):
        today_date = datetime.datetime.now().strftime('%Y%m%d')
        count = self.get_employee_count_for_today(today_date)
        employee_id = f"{today_date}-{count + 1:03}"
        return employee_id

    def get_employee_count_for_today(self, today_date):
        conn = sqlite3.connect(r'C:\Users\Admin\Documents\GitHub\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()
        query = """
        SELECT COUNT(*) FROM Employee
        WHERE strftime('%Y%m%d', Date_Employed) = ?
        """
        cursor.execute(query, (today_date,))
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def save_employee_data(self, data, benefit_id):
        try:
            conn = sqlite3.connect(r'C:\Users\Admin\Documents\GitHub\SUHR-System\Database\SUHRSystem.db')
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
                Benefit_Id,  -- Use Benefit_Id here
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
                data.get("position"),
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
                None,
                None,
                None,
                0,
                benefit_id,  # Use the Benefit_Id here
                None,
                data["contact_num"],
                data["Archived"]
            )
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Employee record added successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def get_archive_count_for_today(self, today_date):
        conn = sqlite3.connect(r'C:\Users\Admin\Documents\GitHub\SUHR-System\Database\SUHRSystem.db')
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