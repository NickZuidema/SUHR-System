import sqlite3
from config import get_database_path

db_path = get_database_path()

def generate_child_id(employee_id):
    """Generate a new Child_Id for a child, ensuring it's unique."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Start by trying to generate a new child ID
        while True:
            # Get the last inserted Child_Id
            #cursor.execute("SELECT Child_Id FROM Child ORDER BY Child_Id DESC LIMIT 1")
            cursor.execute("SELECT count(*) from child;")
            max_id_row = cursor.fetchone()

            if max_id_row:
                last_child_id = max_id_row[0]
                print(f"{last_child_id}")
                
                new_child_id1 = int(last_child_id) + 1
                
                new_child_id = employee_id +"+"+ str(new_child_id1)
            else:
                # If no previous IDs exist, start from 1
                new_child_id = employee_id +"+"+ str(1)

            # Check if the generated ID already exists in the Child table
            cursor.execute("SELECT 1 FROM Child WHERE Child_Id = ?", (str(new_child_id),))
            if cursor.fetchone() is None:
                # If the ID does not exist, break out of the loop
                break

        conn.close()
        return str(new_child_id)  # Return as a simple number, no prefix or padding
    except sqlite3.Error as e:
        print(f"An error occurred while generating Child_Id: {e}")
        return None


def add_employee_to_child_table(employee_employee_id, child_id):
    """Insert a new employee-child relationship into the Employee_Child table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert the relationship
        cursor.execute('''INSERT INTO Employee_Child (Employee_Employee_Id, Child_Child_Id)
                          VALUES (?, ?)''', (employee_employee_id, child_id))

        conn.commit()  # Save changes
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while adding employee to Employee_Child table: {e}")


def store_child(employee_id,last_name, first_name, middle_name, date_of_birth):
    """Store a new child's information in the Child table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Generate a unique Child_Id
        child_id = generate_child_id(employee_id)
        if not child_id:
            print("Failed to generate Child_Id.")
            return None

        # Insert the child's data
        cursor.execute('''INSERT INTO Child (Child_Id, Last_Name, First_Name, Middle_Name, Date_Of_Birth)
                          VALUES (?, ?, ?, ?, ?)''', (child_id, last_name, first_name, middle_name, date_of_birth))

        conn.commit()  # Save changes
        conn.close()

        return child_id  # Return the generated Child_Id

    except sqlite3.Error as e:
        print(f"An error occurred while storing child in Child table: {e}")
        return None


def add_child_to_employee(employee_employee_id, last_name, first_name, middle_name, date_of_birth):
    """Add a child to the database and associate them with an employee."""
    print("Running Child Adding")
    try:
        # Store the child's details in the Child table
        child_id = store_child(employee_employee_id,last_name, first_name, middle_name, date_of_birth)
        if not child_id:
            print("Failed to store child.")
            return

        # Add the relationship to Employee_Child table
        add_employee_to_child_table(employee_employee_id, child_id)

        print(f"Child {child_id} successfully associated with employee {employee_employee_id}.")

    except sqlite3.Error as e:
        print(f"An error occurred while adding child to employee: {e}")
