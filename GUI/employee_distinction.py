import sqlite3
from config import get_database_path

def generate_distinction_id():
    """Generate a new Distinction_Id for a distinction, ensuring it's unique."""
    try:
        with sqlite3.connect(get_database_path()) as conn:
            cursor = conn.cursor()

            while True:
                cursor.execute("SELECT Distinction_Id FROM Distinction ORDER BY Distinction_Id DESC LIMIT 1")
                max_id_row = cursor.fetchone()

                if max_id_row:
                    last_distinction_id = str(max_id_row[0])  # Convert to string
                    if last_distinction_id.isdigit():
                        new_distinction_id = int(last_distinction_id) + 1
                    else:
                        new_distinction_id = int(last_distinction_id[1:]) + 1
                else:
                    new_distinction_id = 1

                cursor.execute("SELECT 1 FROM Distinction WHERE Distinction_Id = ?", (str(new_distinction_id),))
                if cursor.fetchone() is None:
                    break
        return str(new_distinction_id)  # Return as a simple number
    except sqlite3.Error as e:
        print(f"An error occurred while generating Distinction_Id: {e}")
        return None


def add_distinction_to_academic_record(academic_id, year, semester):
    """Add a new distinction to an academic record."""
    try:
        # Generate a unique Distinction_Id
        distinction_id = generate_distinction_id()
        if not distinction_id:
            print("Failed to generate Distinction_Id.")
            return

        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Insert the distinction for the academic record
        cursor.execute('''INSERT INTO Distinction (Distinction_Id, Academic_Id, Year, Semester)
                          VALUES (?, ?, ?, ?)''', (distinction_id, academic_id, year, semester))

        conn.commit()  # Save changes
        conn.close()

        print(f"Distinction {distinction_id} successfully added to academic record {academic_id}.")
    
    except sqlite3.Error as e:
        print(f"An error occurred while adding distinction: {e}")

def get_distinctions_for_academic_record(academic_id):
    """Retrieve all distinctions for a given academic record."""
    try:
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Retrieve distinctions related to the given academic record
        cursor.execute('''SELECT Distinction_Id, Year, Semester
                          FROM Distinction
                          WHERE Academic_Id = ?''', (academic_id,))
        distinctions = cursor.fetchall()

        conn.close()

        if distinctions:
            print(f"Distinctions for Academic Record {academic_id}:")
            for distinction in distinctions:
                print(f"Distinction ID: {distinction[0]}, Year: {distinction[1]}, Semester: {distinction[2]}")
        else:
            print(f"No distinctions found for Academic Record {academic_id}.")
    
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving distinctions: {e}")
