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
                #this is data which can be accessed from employee table
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
                else:
                    # Concatenate Last_Name, First_Name, and Middle_Name to form the full name
                    last_name, first_name, middle_name = employee_data[0], employee_data[1], employee_data[2]
                    full_name = f"{last_name}, {first_name} {middle_name or ''}".strip()

                    self.ui.edit_firstName.setPlainText(first_name)  
                    self.ui.edit_middleName.setPlainText(middle_name)  
                    self.ui.edit_lastName.setPlainText(last_name)  
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
                

                #employee position table
                cursor.execute("""
                    SELECT Name from Position 
                    where Position_Id = (select Position_Id from Employee where Employee_Id = ?)
                """, (self.id_val,))
                employee_position_data = cursor.fetchone()

                if employee_position_data is None:
                    QMessageBox.information(self, "Employee Position", "No Position Data")

                else:
                    self.ui.edit_Position.setPlainText(employee_position_data[0])
                
                #spouse data
                cursor.execute("""
                    select Last_Name, First_Name, Middle_Name from Spouse where Spouse_Id = (select spouse_id from Employee where Employee_Id = ?);
                """, (self.id_val,))
                employee_spouse_data = cursor.fetchone()

                if employee_spouse_data is None:
                    QMessageBox.information(self, "Spouse Data", "Employee has no Spouse")
                else:
                    #spouse name
                    spouse_lname, spouse_fname, spouse_mname = employee_spouse_data[0], employee_spouse_data[1], employee_spouse_data[2]
                    
                    self.ui.edit_spousefname.setPlainText(spouse_fname)
                    self.ui.edit_spouselname.setPlainText(spouse_lname)
                    self.ui.edit_spousemname.setPlainText(spouse_mname)


                #more spouse data
                cursor.execute("""
                    select Date_of_Marriage, Place_of_Marriage from Spouse_Info 
                               where Spouse_Info_Id = (select Spouse_Info_Id from Spouse 
                               where Spouse_Id = (select Spouse_Id from Employee where Employee_Id = ?));
                """, (self.id_val,))
                employee_spouse_information = cursor.fetchone()

                if employee_spouse_information is None:
                    QMessageBox.information(self, "Spouse Information Data", "Employee has no Spouse Information")
                else:
                    self.ui.edit_marriage_date.setPlainText(employee_spouse_information[0])
                    self.ui.edit_marriage_place.setPlainText(employee_spouse_information[1])

                
                #child data
                cursor.execute("""
                    select Last_Name, First_Name, Middle_Name, Date_Of_Birth from Child 
                    where Child_Id = (select Child_Child_Id from Employee_Child where Employee_Employee_Id = ?);
                """, (self.id_val,))
                employee_child_data = cursor.fetchone()

                if employee_child_data is None:
                    QMessageBox.information(self, "Child Data", "Employee has no children Found")
                else:
                    #child name
                    child_lname, child_fname, child_mname = employee_child_data[0], employee_child_data[1], employee_child_data[2]


                    self.ui.edit_childfname.setPlainText(child_fname)
                    self.ui.edit_childmname.setPlainText(child_mname)
                    self.ui.edit_childlname.setPlainText(child_lname)

                    self.ui.edit_children_DoB.setPlainText(employee_child_data[3])



                #sibling data
                cursor.execute("""
                    select Last_Name, First_Name, Middle_Name, Occupation, Address from Sibling 
                    where Sibling_Id like ?;
                """, (self.id_val+'%',))
                employee_sibling_data = cursor.fetchone()

                if employee_sibling_data is None:
                    QMessageBox.information(self, "Sibling Data", "Employee has no sibling Found")
                else:
                    #sibling name
                    sib_lname, sib_fname, sib_mname = employee_sibling_data[0], employee_sibling_data[1], employee_sibling_data[2]
                    

                    self.ui.edit_siblingfname.setPlainText(sib_fname)
                    self.ui.edit_siblingmname.setPlainText(sib_mname)
                    self.ui.edit_siblinglname.setPlainText(sib_lname)

                    self.ui.edit_siblings_occ.setPlainText(employee_sibling_data[3])
                    self.ui.edit_siblings_address.setPlainText(employee_sibling_data[4])



                #parent data
                cursor.execute("""
                    select Father_Last_Name, Father_First_Name, Father_Middle_Name, Father_Occupation, Father_Address, 
                               Mother_Last_Name, Mother_First_Name, Mother_Middle_Name, Mother_Occupation, Mother_Address
                    from Parent where Parent_Id = (select Parent_Parent_Id from Employee_Parent where Employee_Employee_Id = ?);
                """, (self.id_val,))
                employee_parent_data = cursor.fetchone()

                if employee_parent_data is None:
                    QMessageBox.information(self, "Parent Data", "Employee has no Parents Found")
                else:
                    #parents name
                    self.father_lname, self.father_fname, self.father_mname = employee_parent_data[0], employee_parent_data[1], employee_parent_data[2]
                    father_full_name = f"{self.father_lname}, {self.father_fname} {self.father_mname or ''}".strip()
                    
                    self.mother_lname, self.mother_fname, self.mother_mname = employee_parent_data[5], employee_parent_data[6], employee_parent_data[7]
                    mother_full_name = f"{self.mother_lname}, {self.mother_fname} {self.mother_mname or ''}".strip()
                    
                    self.ui.edit_father_firstname.setPlainText(self.father_fname)
                    self.ui.edit_father_lastname.setPlainText(self.father_lname)
                    self.ui.edit_father_middlename.setPlainText(self.father_mname)

                    self.ui.edit_father_name.setPlainText(father_full_name)
                    self.ui.edit_father_home.setPlainText(employee_parent_data[4])
                    self.ui.edit_father_occ.setPlainText(employee_parent_data[3])

                    self.ui.edit_mother_firstname.setPlainText(self.mother_fname)
                    self.ui.edit_mother_lastname.setPlainText(self.mother_lname)
                    self.ui.edit_mother_middlename.setPlainText(self.mother_mname)

                    self.ui.edit_mother_name.setPlainText(mother_full_name)
                    self.ui.edit_father_address.setPlainText(employee_parent_data[9])
                    self.ui.edit_mother_occ.setPlainText(employee_parent_data[8])
                
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
        print("running edit confirmation")
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
            ("crime",self.ui.edit_case),

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
            ("f_firstname",self.ui.edit_father_firstname),
            ("f_lastname", self.ui.edit_father_lastname),
            ("f_middlename", self.ui.edit_father_middlename),
            ("father_occ",self.ui.edit_father_occ),
            ("father_home_address", self.ui.edit_father_home),
            
            ("m_firstname",self.ui.edit_mother_firstname),
            ("m_lastname", self.ui.edit_mother_lastname),
            ("m_middlename", self.ui.edit_mother_middlename),
            ("mother_occ",self.ui.edit_mother_occ),
            ("mother_home_address", self.ui.edit_father_address),

            ("sib_fname",self.ui.edit_siblingfname),
            ("sib_mname", self.ui.edit_siblingmname),
            ("sib_lname", self.ui.edit_siblinglname),
            ("sib_occ", self.ui.edit_siblings_occ),
            ("sib_addr", self.ui.edit_siblings_address),

            ("civil_status", self.ui.edit_civil),
            ("sp_fname",self.ui.edit_spousefname),
            ("sp_lname",self.ui.edit_spouselname),
            ("sp_mname",self.ui.edit_spousemname),
            ("marriage_date",self.ui.edit_marriage_date),
            ("marriage_place",self.ui.edit_marriage_place),


            ("child_fname",self.ui.edit_childfname),
            ("child_mname",self.ui.edit_childmname),
            ("child_lname", self.ui.edit_childlname),
            ("child_dob", self.ui.edit_children_DoB),
        ]

        # Extract the values into a dictionary or variables
        data = {name: field.toPlainText() for name, field in fields}
        
        
        database_path = get_database_path()

        
        try:
        # Use 'with' to ensure the connection is properly managed
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()

                print("running update")
                
                
                image_name = self.ui.employee_image_name.text()
                print(f"changed to {image_name}")

                # Use the passed employee_id for the query
                cursor.execute("""
                    UPDATE Employee
                    SET Last_Name = ?, Middle_Name = ?, First_Name = ?,
                        Dgte_Address = ?, Home_Address = ?,
                        Date_Of_Birth = ?, Place_Of_Birth = ?, Citizenship = ?,
                        Church = ?, Non_Filipino_Id = ?, Contact_No = ?,
                        Tax_Id = ?, Sss_No = ?, Pagibig_No = ?, Philhealth_No = ?, Civil_Status = ?, Criminal_Record = ?, employee_image = ?
                    WHERE Employee_Id = ?
                """, (data['lastname'],data['midname'],data['firstname'],data['duma_address'],
                      data['home_address'], data['date_of_birth'],data['place_of_birth'], data['citizenship'], data['church'],
                      data['passport_num'], data['contact_num'], data['tin'], data['sss_num'],data['pag_ibig'],data['ph_health_num'], data["civil_status"],
                      data['crime'],image_name,
                      self.id_val))
                conn.commit()


                cursor.execute("""
                    Update Position Set Name = ? where position_id = (select position_id from Employee where Employee_Id = ?);
                """, (data["position"],self.id_val))
                conn.commit()

                cursor.execute("""
                Update Parent Set Father_Last_Name = ?, Father_First_Name = ?, Father_Middle_Name = ?, Father_Occupation = ?, Father_Address = ?,
                Mother_Last_Name = ?, Mother_First_Name = ?, Mother_Middle_Name = ?, Mother_Occupation = ?, Mother_Address = ?
                where Parent_Id = (select Parent_Parent_Id from Employee_Parent where Employee_Employee_Id = (select Employee_Id from Employee where Employee_Id = ?));
                """, (data["f_firstname"], data["f_lastname"], data["f_middlename"], data["father_occ"], data["father_home_address"],
                      data["m_firstname"], data["m_lastname"], data["m_middlename"], data["mother_occ"], data["mother_home_address"],self.id_val))
                conn.commit()


                cursor.execute("""
                Update Spouse 
                    Set Last_Name = ?, First_Name = ?, Middle_Name = ?
                     where Spouse_Id = (select spouse_id from Employee where Employee_id = ?);
                """, (data["sp_lname"],data["sp_fname"],data["sp_mname"],self.id_val))
                conn.commit()

                cursor.execute("""
                Update Spouse_Info Set Date_Of_Marriage = ?, Place_Of_Marriage = ?
                where Spouse_Info_Id = (select Spouse_Info_Id from Spouse where 
                               Spouse_id = (select spouse_id from Employee where Employee_Id = ?) );
                """, (data["marriage_date"],data["marriage_place"],self.id_val))
                conn.commit()

                cursor.execute("""
                Update Child Set Last_Name = ?, First_Name = ?, Middle_Name = ?, Date_of_Birth=?
                where Child_Id = (select Child_Child_Id from Employee_Child 
                               where Employee_Employee_Id = (select Employee_Id from Employee where Employee_Id =?) );
                """, (data["child_lname"],data["child_fname"],data["child_mname"],data["child_dob"],self.id_val))
                conn.commit()

                cursor.execute("""
                Update Sibling Set Last_Name = ?, First_Name = ?, Middle_Name = ?, Occupation = ?, Address = ?
                where Sibling_Id = (select Sibling_Sibling_Id from Employee_Sibling where Employee_Employee_Id = ?);
                """, (data["sib_lname"],data["sib_fname"],data["sib_mname"],data["sib_occ"],data["sib_addr"],self.id_val))
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