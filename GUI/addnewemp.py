from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_add_employee_record import Ui_MainWindow  # Import the UI class
import sys
import datetime
import sqlite3

class AddEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.get_employee_data)

    def get_employee_data(self):
        # Generate employee ID
        employee_id = self.generate_employee_id()
        archived = 0  # Default to active (0)

        # Collect employee data
        employee_data = {
            "employee_id": employee_id,  # Include the generated ID
            "Archived": archived,
            "first_name": self.ui.FirstName.toPlainText(),
            "middle_name": self.ui.MiddleName.toPlainText(),
            "last_name": self.ui.SurName.toPlainText(),
            "position": self.ui.Position.toPlainText(),  # Make sure this field exists
            "dmg_address": self.ui.DumaAddress.toPlainText(),
            "home_address": self.ui.HomeAddress.toPlainText(),
            "date_of_birth": self.ui.DateOfBirth.toPlainText(),
            "place_of_birth": self.ui.PlaceOfBirth.toPlainText(),
            "citizenship": self.ui.Citizenship.toPlainText(),
            "passport_num": self.ui.NONFILIPINO_passport.toPlainText(),
            "acr_num": self.ui.NONFILIPINO_acrnum.toPlainText(),
            "passport_date_issued": self.ui.NONFILIPINO_dateissued.toPlainText(),
            "contact_num": self.ui.ContactNumber.toPlainText(),
            "email": self.ui.Email.toPlainText(),
            "tin": self.ui.TINnumber.toPlainText(),
            "sss": self.ui.SSSnumber.toPlainText(),
            "pagibig": self.ui.PagIbigNumber.toPlainText(),
            "philhealth": self.ui.PhilHNumber.toPlainText(),
            "church_affiliation": self.ui.ChurchAffiliation.toPlainText(),
            "father_name": self.ui.FatherName.toPlainText(),
            "father_job": self.ui.FatherJob.toPlainText(),
            "father_address": self.ui.FatherAddress.toPlainText(),
            "mother_name": self.ui.MotherName.toPlainText(),
            "mother_job": self.ui.MotherJob.toPlainText(),
            "mother_address": self.ui.MotherAddress.toPlainText(),
            "sibling1_name": self.ui.sibling1_name.toPlainText(),
            "sibling1_occupation": self.ui.sibling1_occupation.toPlainText(),
            "sibling1_address": self.ui.sibling1_address.toPlainText(),
            "sibling2_name": self.ui.sibling2_name.toPlainText(),
            "sibling2_occupation": self.ui.sibling2_occupation.toPlainText(),
            "sibling2_address": self.ui.sibling2_address.toPlainText(),
            "civil_status": self.ui.CivilStatus.toPlainText(),
            "spouse_name": self.ui.SpouseName.toPlainText(),
            "place_of_marriage": self.ui.PlaceOfMarriage.toPlainText(),
            "date_of_marriage": self.ui.DateOfMarriage.toPlainText(),
            "child1_name": self.ui.child1_name.toPlainText(),
            "child1_birthdate": self.ui.child1_dateofbirth.toPlainText(),
            "child2_name": self.ui.child2_name.toPlainText(),
            "child2_birthdate": self.ui.child2_dateofbirth.toPlainText(),
            "elementary_school": self.ui.elementary_school.toPlainText(),
            "elementary_address": self.ui.elementary_school_address.toPlainText(),
            "elem_diploma": self.ui.diploma_elementary.toPlainText(),
            "elem_yeargraduated": self.ui.yeargraduate_elementary.toPlainText(),
            "highschool_name": self.ui.highschool.toPlainText(),
            "highschool_address": self.ui.address_highschool.toPlainText(),
            "highschool_diploma": self.ui.diploma_highschool.toPlainText(),
            "highschool_yeargraduated": self.ui.yeargraduate_highschool.toPlainText(),
            "college_school": self.ui.College.toPlainText(),
            "college_address": self.ui.address_college.toPlainText(),
            "college_diploma": self.ui.diploma_college.toPlainText(),
            "college_yeargraduated": self.ui.yeargraduate_college.toPlainText(),
            "graduate_school": self.ui.Graduateschool.toPlainText(),
            "graduate_address": self.ui.address_graduateschool.toPlainText(),
            "graduate_diploma": self.ui.diploma_graduateschool.toPlainText(),
            "graduate_yeargraduated": self.ui.yeargraduate_graduateschool.toPlainText(),
            "related_staff1": self.ui.staff_name1.toPlainText(),
            "related_staff1_relationship": self.ui.staff_relationship2.toPlainText(),
            "related_staff1_position": self.ui.staff_position3.toPlainText(),
            "related_staff2": self.ui.staff_name2.toPlainText(),
            "related_staff2_relationship": self.ui.staff_relationship2_2.toPlainText(),
            "related_staff2_position": self.ui.staff_position2.toPlainText(),
            "scholarship_awards": self.ui.scholarships_awards.toPlainText(),
            "publications": self.ui.publications.toPlainText(),
            "name_of_employer": self.ui.name_employer.toPlainText(),
            "position_workplace": self.ui.position_workplace.toPlainText(),
            "period_of_employment": self.ui.period_employment.toPlainText(),
            "reason_for_leaving": self.ui.reason.toPlainText(),
            "employer_address": self.ui.address_employment.toPlainText(),
            "government_examinations": self.ui.government_examination.toPlainText(),
            "government_rating": self.ui.government_rating.toPlainText(),
            "government_date": self.ui.government_date.toPlainText(),
            "government_place": self.ui.Government_place.toPlainText(),
            "criminal_case_name": self.ui.case_name.toPlainText(),
        }
        
        # For testing purposes, print the data
        print(f"Generated Employee ID: {employee_id}")
        print(employee_data)

        # Save the employee data to the database
        self.save_employee_data(employee_data)

    def generate_employee_id(self):
        today_date = datetime.datetime.now().strftime('%Y%m%d')
        count = self.get_employee_count_for_today(today_date)
        employee_id = f"{today_date}-{count+1:03}"  # e.g., 20241009-001
        return employee_id
    
    def get_employee_count_for_today(self, today_date):
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR\SUHR-System\Database\SUHRSystem.db')  
        cursor = conn.cursor()

        # Query to count the number of employees employed today
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
            conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR\SUHR-System\Database\SUHRSystem.db')

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
                data["employee_id"],               # Employee_Id
                data["last_name"],                 # Last_Name
                data["first_name"],                # First_Name
                data["middle_name"],               # Middle_Name
                datetime.datetime.now().strftime('%Y-%m-%d'),  # Date_Employed
                data.get("position"),              # Position_Id
                data["dmg_address"],               # Dgte_Address
                data["home_address"],              # Home_Address
                data["date_of_birth"],             # Date_Of_Birth
                data["place_of_birth"],            # Place_Of_Birth
                data["citizenship"],               # Citizenship
                data.get("passport_num"),          # Non_Filipino_Id
                data["church_affiliation"],        # Church
                data["tin"],                       # Tax_Id
                data["sss"],                       # Sss_No
                data["philhealth"],                # Philhealth_No
                data["pagibig"],                   # Pagibig_No
                data["civil_status"],              # Civil_Status
                data.get("spouse_name"),           # Spouse_Id
                None,                              # Academic_Id (to be handled)
                None,                              # Criminal_Record (if applicable)
                0,                                 # Regular (default to 0)
                None,                              # Benefit_Id (to be handled)
                None,                              # Salary_Id (to be handled)
                data["contact_num"],               # Contact_No
                data["Archived"]                   # Archived
            )

            cursor.execute(sql, values)
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Employee record added successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def get_archive_count_for_today(self, today_date):
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR\SUHR-System\Database\SUHRSystem.db')  
        cursor = conn.cursor()

        # Use Archived field instead of Archive_Id
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
