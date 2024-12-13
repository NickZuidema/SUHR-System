import sqlite3
from config import get_database_path

db_path = get_database_path()

def generate_publication_id():
    """Generate a new Publication_Id for a publication based on existing Publication_Id."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get the last inserted Publication_Id
        cursor.execute("SELECT Publication_Id FROM Publication ORDER BY Publication_Id DESC LIMIT 1")
        max_id_row = cursor.fetchone()

        # Check if max_id_row contains a valid value
        if max_id_row:
            # Increment the last Publication_Id
            new_publication_id = max_id_row[0] + 1
        else:
            # If no previous IDs exist, start from 1
            new_publication_id = 1

        conn.close()
        return new_publication_id  # Return as a number
    except sqlite3.Error as e:
        print(f"An error occurred while generating Publication_Id: {e}")
        return None

def add_academic_record_publication(academic_record_id, publication_id):
    """Insert a new academic record-publication relationship into the Academic_Record_Publication table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert the relationship
        cursor.execute('''INSERT INTO Academic_Record_Publication (Academic_Record_Academic_Record_Id, Publication_Publication_Id)
                          VALUES (?, ?)''', (academic_record_id, publication_id))

        conn.commit()  # Save changes
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while adding academic record to publication: {e}")

def store_publication(name, link):
    """Store a new publication's information in the Publication table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Generate a unique Publication_Id
        publication_id = generate_publication_id()
        if not publication_id:
            print("Failed to generate Publication_Id.")
            return None

        # Insert the publication's data
        cursor.execute('''INSERT INTO Publication (Publication_Id, Name, Link)
                          VALUES (?, ?, ?)''', 
                       (publication_id, name, link))

        conn.commit()  # Save changes
        conn.close()

        return publication_id  # Return the generated Publication_Id

    except sqlite3.Error as e:
        print(f"An error occurred while storing publication in Publication table: {e}")
        return None

def add_publication_to_academic_record(academic_record_id, name, link):
    """Add a publication to the database and associate it with an academic record."""
    try:
        # Store the publication's details in the Publication table
        publication_id = store_publication(name, link)
        if not publication_id:
            print("Failed to store publication.")
            return

        # Add the relationship to Academic_Record_Publication table
        add_academic_record_publication(academic_record_id, publication_id)

        print(f"Publication {publication_id} successfully associated with academic record {academic_record_id}.")

    except sqlite3.Error as e:
        print(f"An error occurred while adding publication to academic record: {e}")

def get_academic_record_id_from_employee(employee_id):
    """Fetch the Academic_Id for an employee from the Employee table."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Fetch the Academic_Id for the employee
        cursor.execute('''SELECT Academic_Id FROM Employee WHERE Employee_Id = ?''', (employee_id,))
        academic_record_id = cursor.fetchone()

        conn.close()

        if academic_record_id:
            return academic_record_id[0]
        else:
            print(f"No academic record found for employee {employee_id}.")
            return None

    except sqlite3.Error as e:
        print(f"An error occurred while fetching academic record for employee {employee_id}: {e}")
        return None
