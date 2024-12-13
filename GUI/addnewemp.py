from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt 
from employee_data import collect_employee_data
from ui_add_employee_record import Ui_MainWindow
from generatepdf import save_pdf
import sys
import datetime
import sqlite3

import os

import spouse
import academic 
from benefit import insert_benefit_data
from config import get_database_path,get_pdf_path,get_profile_path
from position import generate_position_id
import employee_child
import employee_sibling
import employee_publication
import employee_distinction
import government_exam
import employee_parent
from nonfilipino import insert_non_filipino_data
from session import SessionManager  # Import SessionManager

class AddEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.session_manager = SessionManager()  # Initialize SessionManager

        image_path = get_profile_path()
        image_file = os.path.join(image_path,'employee_1.png')
        self.employee_picture = image_file

        self.ui.pushButton.clicked.connect(self.get_employee_data)

        self.ui.Image_Upload.clicked.connect(self.get_employee_image)
        
    def get_employee_image(self):
        # Open a file dialog restricted to a specific folder and image files
        folder_path = get_profile_path()
        file_filter = "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Select an Image", folder_path, file_filter)
        
        
        if file_path:  # If a file is selected
            # Load and scale the image to fit the QLabel
            pixmap = QPixmap(file_path)
            file_name = os.path.basename(file_path)
            print(f"Grabbed {file_name}")
            scaled_pixmap = pixmap.scaled(self.ui.employee_picture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.employee_picture.setPixmap(scaled_pixmap)
            self.ui.EmployeeImageLabel.setText(file_name)
            self.employee_picture = file_name

    def get_employee_data(self):
        employee_id = self.generate_employee_id()
        archived = 0
        employee_data = collect_employee_data(self.ui, employee_id, archived)

        passport_no = self.ui.NONFILIPINO_passport.toPlainText()
        acr_no = self.ui.NONFILIPINO_acrnum.toPlainText()
        date_of_issue = self.ui.NONFILIPINO_dateissued.toPlainText()

        if passport_no:
            insert_non_filipino_data(passport_no, acr_no, date_of_issue)

        employee_data["passport_num"] = passport_no

        first_name = "n/a"
        middle_name = "n/a"
        last_name = "n/a"

        spouse_id = 0

        first_name = self.ui.Spouse_FirstName.toPlainText()
        middle_name = self.ui.Spouse_MiddleName.toPlainText()
        last_name = self.ui.Spouse_LastName.toPlainText()
        date_of_marriage = self.ui.DateOfMarriage.toPlainText()
        place_of_marriage = self.ui.PlaceOfMarriage.toPlainText()

        benefit_id = insert_benefit_data()

        salary_id = self.insert_salary_data()
        
        #this has : if first_name or middle_name or last_name: until self.update_employee, 
        #this will remain with no condition due to a bug that leaves an error when no spouse name is applied to the field
        
        Saved_ID = employee_id.replace('-', '')
        spouse_id = spouse.generate_spouse_id(Saved_ID)

        spouse.insert_spouse_data(spouse_id, first_name, middle_name, last_name, date_of_marriage, place_of_marriage)

        self.update_employee_spouse_id(employee_data['employee_id'], spouse_id)
        


        #children data
        print("running child")
        child_first_name = " " +self.ui.child1_FirstName.toPlainText()
        child_middle_name = " " + self.ui.child1_MiddleName.toPlainText()
        child_last_name = " "+ self.ui.child1_LastName.toPlainText()
        child_date_of_birth =  " "+self.ui.child1_dateofbirth.toPlainText()

        print(f"{child_first_name},{child_middle_name},{child_last_name},{child_date_of_birth}")
        if child_first_name or child_middle_name or child_last_name:
            employee_child.add_child_to_employee(
                employee_id, child_last_name, child_first_name, child_middle_name, child_date_of_birth
            )
        

        print("running sibling")
        sibling1_first_name = " "+self.ui.sibling1_FirstName.toPlainText()
        sibling1_middle_name = " "+self.ui.sibling1_MiddleName.toPlainText()
        sibling1_last_name = " "+self.ui.sibling1_LastName.toPlainText()
        sibling1_occupation = " "+self.ui.sibling1_occupation.toPlainText()
        sibling1_address = " "+self.ui.sibling1_address.toPlainText()

        if sibling1_first_name or sibling1_middle_name or sibling1_last_name:
            employee_sibling.add_sibling_to_employee(
                employee_id, sibling1_last_name, sibling1_first_name, sibling1_middle_name, sibling1_occupation, sibling1_address
            )

        print("running school")
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

        academic_record_id = None
        if elementary_id or seniorhigh_fin or seniorhigh_id or college_id or gradschool_id:
            academic_record_id = self.insert_academic_record_data(
                elementary_id, elementary_fin, seniorhigh_fin, 
                seniorhigh_id, seniorhigh_diploma, seniorhigh_fin, 
                college_id, college_diploma, gradschool_id, 
                gradschool_diploma, gradschool_fin
            )

            default_year = "2023"
            default_semester = 1
            employee_distinction.add_distinction_to_academic_record(academic_record_id, default_year, default_semester)

        self.save_employee_data(employee_data, benefit_id, archived, spouse_id, salary_id, academic_record_id)

        publications = self.ui.publications.toPlainText()
        if publications:
            publication_list = publications.split(';')
            if academic_record_id:
                for publication in publication_list:
                    name, link = publication.split(',')
                    # Debug print
                    print(f"Adding publication: name={name.strip()}, link={link.strip()}")
                    employee_publication.add_publication_to_academic_record(academic_record_id, name.strip(), link.strip())
            else:
                print(f"No academic record found for employee {employee_id}. Publications not added.")

        government_title = self.ui.government_examination.toPlainText()
        government_score = self.ui.government_rating.toPlainText()
        government_date = self.ui.government_date.toPlainText()
        government_score_max = 100

        if government_title or government_score or government_date:
            if academic_record_id:
                government_exam.add_government_exam_to_academic_record(
                    academic_record_id, government_title, government_date, government_score, government_score_max
                )
            else:
                print(f"No academic record found for employee {employee_id}. Government exam not added.")

        father_first_name = " "+self.ui.Father_FirstName.toPlainText()
        father_middle_name = " "+self.ui.Father_MiddleName.toPlainText()
        father_last_name = " "+self.ui.Father_LastName.toPlainText()
        father_occupation = " "+self.ui.FatherJob.toPlainText()
        father_address = " "+self.ui.FatherAddress.toPlainText()
        mother_first_name = " "+self.ui.Mother_FirstName.toPlainText()
        mother_middle_name = " "+self.ui.Mother_MiddleName.toPlainText()
        mother_last_name =" "+ self.ui.Mother_LastName.toPlainText()
        mother_occupation = " "+self.ui.MotherJob.toPlainText()
        mother_address = " "+self.ui.MotherAddress.toPlainText()

        if father_first_name or father_middle_name or father_last_name or mother_first_name or mother_middle_name or mother_last_name:
            parent_family_id = employee_parent.add_parent_to_parent_family_table(
                father_last_name, father_first_name, father_middle_name, father_occupation, father_address,
                mother_last_name, mother_first_name, mother_middle_name, mother_occupation, mother_address
            )
            if parent_family_id:
                employee_parent.add_employee_to_parent_table(employee_id, parent_family_id)

        pdf_directory = get_pdf_path()
        pdf_file_path = os.path.join(pdf_directory, f"{employee_data['employee_id']}.pdf")
        save_pdf(employee_data, pdf_file_path)
        print(f"Saving pdf to {pdf_file_path}")
        self.session_manager.log_activity(employee_data['employee_id'], "Added new employee record")

    def generate_employee_id(self):
        today_date = datetime.datetime.now().strftime('%Y%m%d')
        count = self.get_employee_count_for_today(today_date)
        employee_id = f"{today_date}-{count + 1:03}"
        
        while self.check_employee_id_exists(employee_id):
            count += 1
            employee_id = f"{today_date}-{count + 1:03}"
        
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
                Archived,
                employee_image
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            position_name = data["position"]
            position_id = generate_position_id(position_name)
            values = (
                data["employee_id"],
                data["last_name"],
                data["first_name"],
                data["middle_name"],
                datetime.datetime.now().strftime('%Y-%m-%d'),
                position_id,
                data["dmg_address"],
                data["home_address"],
                data["date_of_birth"],
                data["place_of_birth"],
                data["citizenship"],
                data["passport_num"],
                data["church_affiliation"],
                data["tin"],
                data["sss"],
                data["philhealth"],
                data["pagibig"],
                data["civil_status"],
                spouse_id,
                academic_record_id,
                data["criminal_case_name"],
                0,
                benefit_id,
                salary_id,
                data["contact_num"],
                archived,
                self.employee_picture
            )
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Employee record added successfully.")
            self.session_manager.log_activity(data["employee_id"], "Employee record saved successfully")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            self.session_manager.log_activity(data["employee_id"], f"Error saving employee record: {e}")

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
            self.session_manager.log_activity(employee_id, f"Error updating spouse ID: {e}")
        finally:
            conn.close()
            
    def insert_salary_data(self):
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        cursor.execute("SELECT MAX(Salary_Id) FROM Salary")
        max_id = cursor.fetchone()[0]
        new_salary_id = (max_id + 1) if max_id is not None else 1

        new_salary_id = int(new_salary_id)

        monthly_salary = 0.0  
        overtime_salary = 0.0  
        total_salary = monthly_salary + overtime_salary

        cursor.execute(
            "INSERT INTO Salary (Salary_Id, Monthly_Salary, Overtime_Salary, Total_Salary) VALUES (?, ?, ?, ?)",
            (new_salary_id, monthly_salary, overtime_salary, total_salary)
        )
        conn.commit()
        conn.close()

        return new_salary_id
    
    def generate_salary_id(self):
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

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

    def insert_academic_record_data(
        self, elementary_id, elementary_fin, elementary_diploma, highschool_id, 
        highschool_diploma, highschool_fin, college_id, 
        college_diploma, college_fin, gradschool_id, gradschool_diploma, 
        gradschool_fin
    ):
        conn = None  # Initialize conn here to avoid the UnboundLocalError
        try:
            # Connect to the database
            conn = sqlite3.connect(get_database_path())
            cursor = conn.cursor()
    
            # Insert academic record data
            sql_academic_record = '''
                INSERT INTO Academic_Record (
                    Elementary_ID, Elementary_Fin, Elementary_Diploma, HighSchool_ID, 
                    HighSchool_Diploma, HighSchool_Fin, 
                    College_ID, College_Diploma, College_Fin, GradSchool_ID, 
                    GradSchool_Diploma, GradSchool_Fin
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(sql_academic_record, (
                elementary_id, elementary_fin, elementary_diploma, highschool_id,
                highschool_diploma, highschool_fin,
                college_id, college_diploma, college_fin, gradschool_id,
                gradschool_diploma, gradschool_fin
            ))
    
            # Commit changes
            conn.commit()
            academic_record_id = cursor.lastrowid
            print(f"Academic record data inserted successfully. Academic_Record_Id: {academic_record_id}")
    
            return academic_record_id
    
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()  # Ensure connection is closed only if it was successfully created

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddEmployeeWindow()
    window.show()
    sys.exit(app.exec())