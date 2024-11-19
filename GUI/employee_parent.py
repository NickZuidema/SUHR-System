import sqlite3
from config import get_database_path

def generate_parent_family_id():
    """Generate a new Parent_Id for the new family based on existing Parent_Parent_Id."""
    try:
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

   
        cursor.execute("SELECT Parent_Parent_Id FROM Employee_Parent ORDER BY Parent_Parent_Id DESC LIMIT 1")
        max_id_row = cursor.fetchone()

        
        new_parent_family_id = (int(max_id_row[0]) + 1) if max_id_row else 1

        conn.close()
        return new_parent_family_id
    except sqlite3.Error as e:
        print(f"An error occurred while generating Parent_Id: {e}")
        return None


def add_employee_to_parent_table(employee_employee_id, parent_family_id):
    """Insert a new employee's reference into the Employee_Parent table."""
    try:
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

      
        cursor.execute('''INSERT INTO Employee_Parent (Employee_Employee_Id, Parent_Parent_Id)
                          VALUES (?, ?)''', (employee_employee_id, parent_family_id))

        conn.commit() 
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while adding employee to Employee_Parent table: {e}")


def store_parent_family(last_name_father, first_name_father, middle_name_father,
                        last_name_mother, first_name_mother, middle_name_mother,
                        occupation, address):
    """Store both the father and mother as a parent family in the Parent table."""
    try:
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

       
        cursor.execute('''INSERT INTO Parent (Father_Last_Name, Father_First_Name, Father_Middle_Name,
                                              Mother_Last_Name, Mother_First_Name, Mother_Middle_Name,
                                              Occupation, Address)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (last_name_father, first_name_father, middle_name_father,
                        last_name_mother, first_name_mother, middle_name_mother,
                        occupation, address))

        conn.commit()  
        parent_family_id = cursor.lastrowid  
        conn.close()

        return parent_family_id 

    except sqlite3.Error as e:
        print(f"An error occurred while storing parent family in Parent table: {e}")
        return None

def add_parent_to_parent_family_table(last_name_father, first_name_father, middle_name_father,
                                      last_name_mother, first_name_mother, middle_name_mother,
                                      occupation, address):
    """Insert the father and mother as a family into the Parent table."""
    try:
      
        parent_family_id = generate_parent_family_id()
        if parent_family_id is None:
            print("Failed to generate Parent_Id.")
            return

       
        parent_family_id = store_parent_family(last_name_father, first_name_father, middle_name_father,
                                               last_name_mother, first_name_mother, middle_name_mother,
                                               occupation, address)

        if parent_family_id is None:
            print("Failed to store parent family.")
            return

        return parent_family_id 

    except sqlite3.Error as e:
        print(f"An error occurred while adding parent family to Parent table: {e}")
