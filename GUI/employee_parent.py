import sqlite3
from config import get_database_path

def generate_parent_parent_id():
    try:
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Check if there's existing data in the Employee_Parent table
        cursor.execute("SELECT MAX(Parent_Parent_Id) FROM Employee_Parent")
        max_id = cursor.fetchone()[0]
        
        # Generate a new Parent_Parent_Id by incrementing the max value from Employee_Parent table
        new_parent_parent_id = (int(max_id) + 1) if max_id is not None else 1

        conn.close()
        return new_parent_parent_id
    except sqlite3.Error as e:
        print(f"An error occurred while generating Parent_Parent_Id: {e}")
        return None

def add_employee_to_parent_table(employee_employee_id):
    """Insert a new employee's reference into the Employee_Parent table."""
    try:
        parent_parent_id = generate_parent_parent_id()  # Generate a new Parent_Parent_Id
        if parent_parent_id is None:
            print("Failed to generate Parent_Parent_Id.")
            return

        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Insert the new employee reference into Employee_Parent table
        cursor.execute('''INSERT INTO Employee_Parent (Employee_Employee_Id, Parent_Parent_Id)
                          VALUES (?, ?)''', (employee_employee_id, parent_parent_id))

        conn.commit()  # Ensure that the transaction is committed before closing
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while adding employee to Employee_Parent table: {e}")
