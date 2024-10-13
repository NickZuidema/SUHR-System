from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from employee_data import collect_employee_data
from ui_add_employee_record import Ui_MainWindow
from generatepdf import save_pdf
import sys
import datetime
import sqlite3
import spouse
from fpdf import FPDF

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

        # Save employee data to the database
        self.save_employee_data(employee_data)

        # Define the path for saving the PDF
        pdf_file_path = f"C:\\Users\\leeu6\\Desktop\\pdf\\{employee_data['employee_id']}.pdf"
        
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
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()
        query = """
        SELECT COUNT(*) FROM Employee
        WHERE strftime('%Y%m%d', Date_Employed) = ?
        """
        cursor.execute(query, (today_date,))
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def save_employee_data(self, data):
        try:
            conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\Database\SUHRSystem.db')
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
                None,
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

    # def save_pdf(self, employee_data):
    #     pdf = FPDF()
    #     pdf.add_page()
    #     pdf.set_font("Arial", 'B', 16)
    #     pdf.cell(0, 10, "Employee Registration", ln=True, align='C')
    #     pdf.ln(10)
    #     pdf.set_font("Arial", size=12)
    #     fields = {
    #         "Employee ID": employee_data.get('employee_id', 'N/A'),
    #         "First Name": employee_data.get('first_name', 'N/A'),
    #         "Middle Name": employee_data.get('middle_name', 'N/A'),
    #         "Last Name": employee_data.get('last_name', 'N/A'),
    #         "Position": employee_data.get('position', 'N/A'),
    #         "Date Employed": datetime.datetime.now().strftime('%Y-%m-%d'),
    #         "Date of Birth": employee_data.get('date_of_birth', 'N/A'),
    #         "Place of Birth": employee_data.get('place_of_birth', 'N/A'),
    #         "Citizenship": employee_data.get('citizenship', 'N/A'),
    #         "Passport Number": employee_data.get('passport_num', 'N/A'),
    #         "Contact Number": employee_data.get('contact_num', 'N/A'),
    #         "Email": employee_data.get('email', 'N/A'),
    #         "Damage Address": employee_data.get('dmg_address', 'N/A'),
    #         "Home Address": employee_data.get('home_address', 'N/A'),
    #         "Civil Status": employee_data.get('civil_status', 'N/A'),
    #         "Spouse Name": employee_data.get('spouse_name', 'N/A'),
    #         "Place of Marriage": employee_data.get('place_of_marriage', 'N/A'),
    #         "Date of Marriage": employee_data.get('date_of_marriage', 'N/A'),
    #         "Child 1 Name": employee_data.get('child1_name', 'N/A'),
    #         "Child 1 Birthdate": employee_data.get('child1_birthdate', 'N/A'),
    #         "Child 2 Name": employee_data.get('child2_name', 'N/A'),
    #         "Child 2 Birthdate": employee_data.get('child2_birthdate', 'N/A'),
    #         "Elementary School": employee_data.get('elementary_school', 'N/A'),
    #         "Elementary Address": employee_data.get('elementary_address', 'N/A'),
    #         "Elementary Diploma": employee_data.get('elem_diploma', 'N/A'),
    #         "Elementary Year Graduated": employee_data.get('elem_yeargraduated', 'N/A'),
    #         "High School Name": employee_data.get('highschool_name', 'N/A'),
    #         "High School Address": employee_data.get('highschool_address', 'N/A'),
    #         "High School Diploma": employee_data.get('highschool_diploma', 'N/A'),
    #         "High School Year Graduated": employee_data.get('highschool_yeargraduated', 'N/A'),
    #         "College Name": employee_data.get('college_school', 'N/A'),
    #         "College Address": employee_data.get('college_address', 'N/A'),
    #         "College Diploma": employee_data.get('college_diploma', 'N/A'),
    #         "College Year Graduated": employee_data.get('college_yeargraduated', 'N/A'),
    #         "Graduate School": employee_data.get('graduate_school', 'N/A'),
    #         "Graduate Address": employee_data.get('graduate_address', 'N/A'),
    #         "Graduate Diploma": employee_data.get('graduate_diploma', 'N/A'),
    #         "Graduate Year Graduated": employee_data.get('graduate_yeargraduated', 'N/A'),
    #         "Related Staff 1": employee_data.get('related_staff1', 'N/A'),
    #         "Related Staff 1 Relationship": employee_data.get('related_staff1_relationship', 'N/A'),
    #         "Related Staff 1 Position": employee_data.get('related_staff1_position', 'N/A'),
    #         "Related Staff 2": employee_data.get('related_staff2', 'N/A'),
    #         "Related Staff 2 Relationship": employee_data.get('related_staff2_relationship', 'N/A'),
    #         "Related Staff 2 Position": employee_data.get('related_staff2_position', 'N/A'),
    #         "Scholarship Awards": employee_data.get('scholarship_awards', 'N/A'),
    #         "Publications": employee_data.get('publications', 'N/A'),
    #         "Name of Employer": employee_data.get('name_of_employer', 'N/A'),
    #         "Position at Workplace": employee_data.get('position_workplace', 'N/A'),
    #         "Period of Employment": employee_data.get('period_of_employment', 'N/A'),
    #         "Reason for Leaving": employee_data.get('reason_for_leaving', 'N/A'),
    #         "Employer Address": employee_data.get('employer_address', 'N/A'),
    #         "Government Examinations": employee_data.get('government_examinations', 'N/A'),
    #         "Government Rating": employee_data.get('government_rating', 'N/A'),
    #         "Government Date": employee_data.get('government_date', 'N/A'),
    #         "Government Place": employee_data.get('government_place', 'N/A'),
    #         "Criminal Case Name": employee_data.get('criminal_case_name', 'N/A'),
    #     }
    #     for label, value in fields.items():
    #         pdf.cell(50, 10, label + ":", ln=False)
    #         pdf.cell(0, 10, str(value), ln=True)
    #     pdf_file_path = f"C:\\Users\\leeu6\\Desktop\\pdf\\{employee_data['employee_id']}.pdf"
    #     pdf.output(pdf_file_path)
    #     QMessageBox.information(self, "Success", f"PDF saved successfully at:\n{pdf_file_path}")
    

    def get_archive_count_for_today(self, today_date):
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\Database\SUHRSystem.db')
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
