def save_employee_data(self, data):
        try:
            conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR\SUHR-System\Database\SUHRSystem.db')
            conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
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