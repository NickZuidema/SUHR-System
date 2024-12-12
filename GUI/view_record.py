import sys
import sqlite3
from PySide6.QtWidgets import QApplication,QGraphicsView,QGraphicsPixmapItem,QGraphicsScene, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt 
from ui_preview_template_withscroll import Ui_MainWindow
from config import get_database_path,get_profile_path  # Import get_database_path from config

from edit_employee import Edit_MainWindow

from salary import SalaryDialog

import os

class MainWindow(QMainWindow):
    def __init__(self, employee_id):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the archive button to the archive_employee method
        self.ui.archive_button.clicked.connect(self.archive_employee)


        self.empID = employee_id
        self.ui.edit_info_button.clicked.connect(self.edit_employee_record)

        self.ui.archive_button_2.clicked.connect(self.salary_employee)

        # Get the database path from the config module
        database_path = get_database_path()


        try:
            # Use 'with' to ensure the connection is properly managed
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()

                # Use the passed employee_id for the query
                cursor.execute("""
                    SELECT Last_Name, First_Name, Middle_Name, Dgte_Address, Home_Address, Date_Of_Birth,
                           Citizenship, Civil_Status, Sss_No, Pagibig_No, Philhealth_No, Contact_No, employee_image, Department
                    FROM Employee
                    WHERE Employee_Id = ?
                """, (employee_id,))
                employee_data = cursor.fetchone()

                if employee_data is None:
                    raise ValueError(f"No employee found with ID {employee_id}")

                # Concatenate Last_Name, First_Name, and Middle_Name to form the full name
                last_name, first_name, middle_name = employee_data[0], employee_data[1], employee_data[2]
                full_name = f"{last_name}, {first_name} {middle_name or ''}".strip()

                # Populate UI fields with data from the database
                self.ui.employee_name.setText(full_name)  # Set full name in QLabel
                self.ui.employee_dumaguete_address.setPlainText(employee_data[3])  # Set Dumaguete address in QTextEdit
                self.ui.employee_home_address.setPlainText(employee_data[4])  # Set Home address in QTextEdit
                self.ui.employee_birthday.setText(employee_data[5])  # Set Date of Birth
                self.ui.employee_citizenship.setText(employee_data[6])  # Set Citizenship
                self.ui.employee_civil_status.setText(employee_data[7])  # Set Civil Status
                self.ui.employee_sss.setText(employee_data[8])  # Set SSS number
                self.ui.employee_pagibig.setText(employee_data[9])  # Set Pag-IBIG number
                self.ui.employee_philHealth.setText(employee_data[10])  # Set PhilHealth number
                self.ui.employee_phonenumber.setText(employee_data[11])  # Set Contact number
                self.ui.employee_children.setText("No children information available")  # Default message
                self.ui.employee_religion.setText("No religion information available")  # Default message
                self.ui.employee_father.setText("No father information available")  # Default message
                self.ui.employee_mother.setText("No mother information available")  # Default message
                self.ui.employee_department.setText(employee_data[13])



                #-----load image in process ----------
                scene = QGraphicsScene()

                image_path = get_profile_path()
                
                if(employee_data[12] == None):
                    image_file = os.path.join(image_path, 'default.jpg')
                else:
                    image_file = os.path.join(image_path, employee_data[12])
                
                # Create a scene and load the image
                scene = QGraphicsScene()
                pixmap = QPixmap(image_file)

                if pixmap.isNull():
                    QMessageBox.warning(self, "Invalid Image", f"Failed to load image: {image_file}")
                    return

                # Resize the image to fit the QGraphicsView
                scaled_pixmap = pixmap.scaled(
                    self.ui.Profile_pic_2.width(),
                    self.ui.Profile_pic_2.height(),
                    aspectMode=Qt.AspectRatioMode.KeepAspectRatio
                )

                # Add the image to the scene
                image_item = QGraphicsPixmapItem(scaled_pixmap)
                scene.addItem(image_item)

                # Set the scene in the QGraphicsView
                self.ui.Profile_pic_2.setScene(scene)

                #----------end of image process------

                #display position
                cursor.execute("""
                    select Name from position where position_id = (select position_id from Employee where Employee_Id = ?);
                """, (employee_id,))
                position_data = cursor.fetchone()

                if position_data and position_data[0]:
                    self.ui.employee_position.setText(position_data[0])  # Set church affiliation in QLabel
                else:
                    self.ui.employee_position.setText("No position data")

                # Fetch and display church affiliation
                cursor.execute("""
                    SELECT Church
                    FROM Employee
                    WHERE Employee_Id = ?
                """, (employee_id,))
                church_data = cursor.fetchone()

                if church_data and church_data[0]:
                    self.ui.employee_religion.setText(church_data[0])  # Set church affiliation in QLabel
                else:
                    self.ui.employee_religion.setText("No religion information available")

                # Fetch and display spouse information
                cursor.execute("""
                    SELECT First_Name, Middle_Name, Last_Name
                    FROM Spouse
                    WHERE Spouse_Info_Id = (
                        SELECT Spouse_Info_Id
                        FROM Employee
                        WHERE Employee_Id = ?
                    )
                """, (employee_id,))
                spouse_data = cursor.fetchone()

                if spouse_data:
                    spouse_first_name, spouse_middle_name, spouse_last_name = spouse_data
                    spouse_full_name = f"{spouse_last_name}, {spouse_first_name} {spouse_middle_name or ''}".strip()
                    self.ui.employee_spouse.setText(spouse_full_name)  # Set spouse full name in QLabel
                else:
                    self.ui.employee_spouse.setText("No spouse information available")

                # Fetch and display children information
                cursor.execute("""
                               
                    select Last_Name, First_Name, Middle_Name, Date_Of_Birth from Child 
                    where Child_Id = (select Child_Child_Id from Employee_Child where Employee_Employee_Id = ?)
                            
                """, (employee_id,))
                children_data = cursor.fetchone()

                if children_data:
                    
                    child_last_name, child_first_name, child_middle_name, child_dob = children_data[0], children_data[1], children_data[2], children_data[3]
                    child_full_name = f"{child_last_name}, {child_first_name} {child_middle_name or ''}"
                    children_info = f"{child_full_name} DOB:{child_dob}"
                    self.ui.employee_children.setText(children_info)  # Set children info in QLabel
                else:
                    self.ui.employee_children.setText("No children information available")

                # Fetch and display parent information
                cursor.execute("""
                    SELECT Father_Last_Name, Father_First_Name, Father_Middle_Name, 
                           Mother_Last_Name, Mother_First_Name, Mother_Middle_Name
                    FROM Parent
                    WHERE Parent_Id = (
                        SELECT Parent_Parent_Id
                        FROM Employee_Parent
                        WHERE Employee_Employee_Id = ?
                    )
                """, (employee_id,))
                parent_data = cursor.fetchone()

                if parent_data:
                    father_last_name, father_first_name, father_middle_name, mother_last_name, mother_first_name, mother_middle_name = parent_data
                    father_full_name = f"{father_last_name}, {father_first_name} {father_middle_name or ''}".strip()
                    mother_full_name = f"{mother_last_name}, {mother_first_name} {mother_middle_name or ''}".strip()
                    self.ui.employee_father.setText(father_full_name)  # Set father full name in QLabel
                    self.ui.employee_mother.setText(mother_full_name)  # Set mother full name in QLabel
                else:
                    self.ui.employee_father.setText("No father information available")
                    self.ui.employee_mother.setText("No mother information available")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while accessing the database: {e}")
        except ValueError as e:
            QMessageBox.warning(self, "Record Not Found", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred: {e}")

    def edit_employee_record(self):
        print("editing employee")
        self.edit_emp_window = Edit_MainWindow(self.empID)
        self.edit_emp_window.show()

    def salary_employee(self):
        print("getting salary record")
        self.salary_emp_window = SalaryDialog()
        self.salary_emp_window.show()

    def archive_employee(self):
        try:
            # Retrieve the employee ID (adjust this to fetch dynamically if needed)
            # employee_id = '20241115-001'  # Replace with the employee ID currently being displayed or selected
            employee_id = self.empID
            # Get the database path
            database_path = get_database_path()

            # Connect to the database
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()

                # Update the Archived column to 1 (true) for the specified Employee_Id
                cursor.execute("UPDATE Employee SET Archived = 1 WHERE Employee_Id = ?", (employee_id,))
                conn.commit()

            # Notify the user of success
            QMessageBox.information(self, "Success", f"Employee {employee_id} has been archived.")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while archiving: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage, replace '20241114-006' with the actual employee_id passed from the dashboard
    app = QApplication(sys.argv)
    window = MainWindow('20241114-006')  # Pass employee_id dynamically
    window.show()
    sys.exit(app.exec())
