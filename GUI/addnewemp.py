from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_add_employee_record import Ui_MainWindow  # Import the UI class
import sys

class AddEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.get_employee_data)

    def get_employee_data(self):
        # Collect employee data
        employee_data = {
            "first_name": self.ui.FirstName.toPlainText(),
            "middle_name": self.ui.MiddleName.toPlainText(),
            "last_name": self.ui.SurName.toPlainText(),
            "position": self.ui.Position.toPlainText(),
            "department": self.ui.Department.toPlainText(),
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
            # Academic records
            "elementary_school": self.ui.elementary_school.toPlainText(),
            "elementary_address": self.ui.elementary_school_address.toPlainText(),
            "elem_diploma": self.ui.diploma_elementary.toPlainText(),
            "elem_yeargraduated": self.ui.yeargraduate_elementary.toPlainText(),
            "highschool_name": self.ui.highschool_name.toPlainText(),
            "highschool_address": self.ui.highschool_address.toPlainText(),
            "highschool_diploma": self.ui.diploma_highschool.toPlainText(),
            "highschool_yeargraduated": self.ui.yeargraduate_highschool.toPlainText(),
            "college_school": self.ui.college_school.toPlainText(),
            "college_address": self.ui.college_school_address.toPlainText(),
            "college_diploma": self.ui.diploma_college.toPlainText(),
            "college_yeargraduated": self.ui.yeargraduate_college.toPlainText(),
            "graduate_school": self.ui.Graduateschool.toPlainText(),
            "graduate_address": self.ui.address_graduateschool.toPlainText(),
            "graduate_diploma": self.ui.diploma_graduateschool.toPlainText(),
            "graduate_yeargraduated": self.ui.yeargraduate_graduateschool.toPlainText(),
            
            #related staff
            "related_staff1": self.ui.staff_name1.toPlainText(),
            "related_staff1_relationship": self.ui.staff_relationship2.toPlainText(),
            "related_staff1_position": self.ui.staff_position3.toPlainText(),
            
            
            "related_staff2": self.ui.staff_name2.toPlainText(),
            "related_staff2_relationship": self.ui.staff_relationship2_2.toPlainText(),
            "related_staff2_position": self.ui.staff_position2.toPlainText(),
            #dont forget to add staff_addfield button later on self.staff_addfield = QPushButton(self.scrollAreaWidgetContents_2)
            
            "schorlarship_awards": self.ui.scholarships_awards.toPlainText(),
            "publications": self.ui.publications.toPlainText(),
            
            #recirds of previous employmer  
            "name_of_employer": self.ui.name_employer.toPlainText(),
            "position_workplace": self.ui.position_workplace.toPlainText(),
            "period_of_employment": self.ui.period_employment.toPlainText(),
            "reason_for_leaving": self.ui.reason.toPlainText(),
            "employer_address": self.ui.address_employment.toPlainText(),
            
            #government examinations
            "government_examinations": self.ui.government_examination.toPlainText(),
            "government_rating": self.ui.government_rating.toPlainText(),
            "government_date": self.ui.government_date.toPlainText(),
            "government_place": self.ui.Government_place.toPlainText(),
            
            #involvement in criminal cases
            "criminal_case_name": self.ui.case_name.toPlainText(),
        }

    #     # Here you can validate and process the employee_data
    #     if self.validate_data(employee_data):
    #         self.save_to_database(employee_data)  # Method to save data
    #         QMessageBox.information(self, "Success", "Employee record added successfully.")
    #     else:
    #         QMessageBox.warning(self, "Input Error", "Please fill in all required fields.")

    # def validate_data(self, data):
    #     # Basic validation to check if any required field is empty
    #     for key, value in data.items():
    #         if not value:
    #             return False
    #     return True

    # def save_to_database(self, data):
    #     # Implement your SQLite database insert logic here
    #     pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()
    window.show()
    sys.exit(app.exec())
