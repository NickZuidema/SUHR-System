import sqlite3
import sys
import uuid
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QFileDialog
from PySide6.QtGui import QPalette, QColor

#ui link
from ui_edit import Ui_MainWindow

from config import get_database_path,get_profile_path
from session import SessionManager
import os

# def force_light_mode(app):
#     palette = QPalette()
#     palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))
#     palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
#     palette.setColor(QPalette.ColorRole.AlternateBase, QColor(240, 240, 240))
#     palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))
#     palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
#     palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))
#     palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
#     palette.setColor(QPalette.ColorRole.Highlight, QColor(30, 144, 255))
#     palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
#     app.setPalette(palette)

class Edit_MainWindow(QMainWindow):
    def __init__(self,id=id):
        super(Edit_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id_val = id
        print(f"Id val is {self.id_val}")

        #finalize changes
        self.ui.editRecord_btn.clicked.connect(self.edit_confirm)

        self.ui.update_picture_btn.clicked.connect(self.edit_emp_image)

        database_path = get_database_path()
        
        try:
        # Use 'with' to ensure the connection is properly managed
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()



                # Use the passed employee_id for the query
                cursor.execute("""
                    SELECT Last_Name, First_Name, Middle_Name, Dgte_Address, Home_Address, Date_Of_Birth, Home_Address, 
                            Citizenship, Civil_Status, Sss_No, Pagibig_No, Philhealth_No, Tax_Id, Contact_No, Church, Criminal_Record, employee_image, 
                            Department
                    FROM Employee
                    WHERE Employee_Id = ?
                """, (self.id_val,))
                employee_data = cursor.fetchone()

                if employee_data is None:
                    raise ValueError(f"No employee found with ID {self.id_val}")
                
                cursor.execute("""
                    SELECT Name from Position 
                    where Position_Id = (select Position_Id from Employee where Employee_Id = ?)
                """, (self.id_val,))
                employee_position_data = cursor.fetchone()

                if employee_position_data is None:
                    raise ValueError(f"Employee Position Error: No Employee found with ID {self.id_val}")
                

                cursor.execute("""
                    select Last_Name, First_Name, Middle_Name from Spouse where Spouse_Id = (select spouse_id from Employee where Employee_Id = ?);
                """, (self.id_val,))
                employee_spouse_data = cursor.fetchone()

                if employee_spouse_data is None:
                    raise ValueError(f"Spouse Data Error:No Employee found with ID {self.id_val}")

                # Concatenate Last_Name, First_Name, and Middle_Name to form the full name
                last_name, first_name, middle_name = employee_data[0], employee_data[1], employee_data[2]
                full_name = f"{last_name}, {first_name} {middle_name or ''}".strip()

                #spouse name
                spouse_lname, spouse_fname, spouse_mname = employee_spouse_data[0], employee_spouse_data[1], employee_spouse_data[2]
                spouse_full_name = f"{spouse_lname}, {spouse_fname} {spouse_mname or ''}".strip()


                # Populate UI fields with data from the database
                # Initialize the Names
                self.ui.edit_firstName.setPlainText(first_name)  
                self.ui.edit_middleName.setPlainText(middle_name)  
                self.ui.edit_lastName.setPlainText(last_name)  
                self.ui.edit_Position.setPlainText(employee_position_data[0])
                self.ui.edit_department.setPlainText(employee_data[17])

                self.ui.edit_dgte_address.setPlainText(employee_data[3])
                self.ui.edit_home_address.setPlainText(employee_data[4])

                self.ui.edit_DoB.setPlainText(employee_data[5])
                self.ui.edit_PoB.setPlainText(employee_data[6])

                self.ui.edit_citizen.setPlainText(employee_data[7])

                self.ui.edit_contactNo.setPlainText(employee_data[13])

                parse_email_nospace = full_name.replace(" ","")
                parse_email_notabs = parse_email_nospace.replace("\t","")
                parse_email_final = parse_email_notabs.replace(",","")
                self.ui.edit_email_add.setPlainText(parse_email_final+"@su.edu.ph")

                self.ui.edit_TIN.setPlainText(employee_data[12])
                self.ui.edit_SSS.setPlainText(employee_data[9])
                self.ui.edit_pagibig.setPlainText(employee_data[10])
                self.ui.edit_philhealth.setPlainText(employee_data[11])

                self.ui.edit_church.setPlainText(employee_data[14])

                self.ui.edit_civil.setPlainText(employee_data[8])

                self.ui.edit_case.setPlainText(employee_data[15])

                self.ui.employee_image_name.setText(employee_data[16])
                
                self.ui.edit_spouse.setPlainText(spouse_fname)

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while accessing the database: {e}")
        except ValueError as e:
            QMessageBox.warning(self, "Record Not Found", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred: {e}")

    def edit_emp_image(self):
         # Open a file dialog restricted to a specific folder and image files
        folder_path = get_profile_path()
        file_filter = "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Select an Image", folder_path, file_filter)
        
        
        if file_path:  # If a file is selected
            file_name = os.path.basename(file_path)
            print(f"Grabbed {file_name}")
            self.ui.employee_image_name.setText(file_name)

    def edit_confirm(self):

        # Define a list of tuples mapping variable names to UI fields, make things easier instead of typing like a monkey (ithink)
        # will comment out things that are necessary to update (can be seen in the dashboard)
        fields = [

            ("lastname", self.ui.edit_lastName), 
            ("firstname", self.ui.edit_firstName),
            ("midname", self.ui.edit_middleName),
           
            ("position", self.ui.edit_Position), 
            ("duma_address", self.ui.edit_dgte_address), 
            ("home_address",self.ui.edit_home_address), 
            ("date_of_birth",self.ui.edit_DoB), 
            ("place_of_birth",self.ui.edit_PoB), 
            ("citizenship",self.ui.edit_citizen), 
            ("church",self.ui.edit_church), 
            ("passport_num",self.ui.edit_passportNo), 
            ("acr_num",self.ui.edit_acrNo), 
            ("date_issued",self.ui.edit_date_issued), 

            ("contact_num",self.ui.edit_contactNo),

            #no email in the employee table 
            ("email_address",self.ui.edit_email_add),

            ("tin", self.ui.edit_TIN),
            ("sss_num",self.ui.edit_SSS),
            ("pag_ibig",self.ui.edit_pagibig),
            ("ph_health_num",self.ui.edit_philhealth),


            #father and mother are in a separate table
            ("father",self.ui.edit_father_name),
            ("father_occ",self.ui.edit_father_occ),
            ("father_home_address", self.ui.edit_father_home),
            
            ("mother",self.ui.edit_mother_name),
            ("mother_occ",self.ui.edit_mother_occ),
            ("mother_home_address", self.ui.edit_father_address),
        ]

        # Extract the values into a dictionary or variables
        data = {name: field.toPlainText() for name, field in fields}
        
        
        database_path = get_database_path()
        try:
        # Use 'with' to ensure the connection is properly managed
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()

                position_num = 0
                if data['position'] != '':
                    position_num = int(data['position'])


                # Use the passed employee_id for the query
                cursor.execute("""
                    UPDATE Employee
                    SET Last_Name = ?, Middle_Name = ?, First_Name = ?,
                        Position_Id = ?, Dgte_Address = ?, Home_Address = ?,
                        Date_Of_Birth = ?, Place_Of_Birth = ?, Citizenship = ?,
                        Church = ?, Non_Filipino_Id = ?, Contact_No = ?,
                        Tax_Id = ?, Sss_No = ?, Pagibig_No = ?, Philhealth_No = ?
                    WHERE Employee_Id = ?
                """, (data['lastname'],data['midname'],data['firstname'],position_num,data['duma_address'],
                      data['home_address'], data['date_of_birth'],data['place_of_birth'], data['citizenship'], data['church'],
                      data['passport_num'], data['contact_num'], data['tin'], data['sss_num'],data['pag_ibig'],data['ph_health_num'],
                      self.id_val))
                conn.commit()
                
        
                QMessageBox.information(self, "Edit Result", f"Updated Record for {self.id_val}.")

                
                
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while editing: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # force_light_mode(app)
    window = Edit_MainWindow()
    window.show()
    sys.exit(app.exec())