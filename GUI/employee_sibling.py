import sqlite3
from config import get_database_path

db_path = get_database_path()

def generate_sibling_id():
    """Generate a new Sibling_Id for a sibling based on existing Sibling_Sibling_Id."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get the last inserted Sibling_Id
        cursor.execute("SELECT Sibling_Sibling_Id FROM Employee_Sibling ORDER BY Sibling_Sibling_Id DESC LIMIT 1")
        max_id_row = cursor.fetchone()

        
        if max_id_row:
            # Extract the numeric part of the ID and increment
            last_sibling_id = max_id_row[0]
            if last_sibling_id.isdigit():  # Ensure it's a valid number
                new_sibling_id = int(last_sibling_id) + 1
            else:
                # If it's not a valid number (e.g., contains 'S'), strip the prefix 'S'
                new_sibling_id = int(last_sibling_id[1:]) + 1
        else:
            # If no previous IDs exist, start from 1
            new_sibling_id = 1

        conn.close()
        return str(new_sibling_id)  # Return as a simple number, no prefix or padding
    except sqlite3.Error as e:
        print(f"An error occurred while generating Sibling_Id: {e}")
        return None


def add_employee_to_sibling_table(employee_employee_id, sibling_id):
    """Insert a new employee-sibling relationship into the Employee_Sibling table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert the relationship
        cursor.execute('''INSERT INTO Employee_Sibling (Employee_Employee_Id, Sibling_Sibling_Id)
                          VALUES (?, ?)''', (employee_employee_id, sibling_id))

        conn.commit()  # Save changes
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while adding employee to Employee_Sibling table: {e}")


def store_sibling(last_name, first_name, middle_name, occupation, address):
    """Store a new sibling's information in the Sibling table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Generate a unique Sibling_Id
        sibling_id = generate_sibling_id()
        if not sibling_id:
            print("Failed to generate Sibling_Id.")
            return None

        # Insert the sibling's data
        cursor.execute('''INSERT INTO Sibling (Sibling_Id, Last_Name, First_Name, Middle_Name, Occupation, Address)
                          VALUES (?, ?, ?, ?, ?, ?)''', 
                       (sibling_id, last_name, first_name, middle_name, occupation, address))

        conn.commit()  # Save changes
        conn.close()

        return sibling_id  # Return the generated Sibling_Id

    except sqlite3.Error as e:
        print(f"An error occurred while storing sibling in Sibling table: {e}")
        return None


def add_sibling_to_employee(employee_employee_id, last_name, first_name, middle_name, occupation, address):
    """Add a sibling to the database and associate them with an employee."""
    try:
        # Store the sibling's details in the Sibling table
        sibling_id = store_sibling(last_name, first_name, middle_name, occupation, address)
        if not sibling_id:
            print("Failed to store sibling.")
            return

        # Add the relationship to Employee_Sibling table
        add_employee_to_sibling_table(employee_employee_id, sibling_id)

        print(f"Sibling {sibling_id} successfully associated with employee {employee_employee_id}.")

    except sqlite3.Error as e:
        print(f"An error occurred while adding sibling to employee: {e}")
