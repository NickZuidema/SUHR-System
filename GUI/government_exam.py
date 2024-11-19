import sqlite3
from config import get_database_path

def generate_government_exam_id():
    """Generate a new Government_Exam_Id for a government exam, ensuring it's unique."""
    try:
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Start by trying to generate a new government exam ID
        while True:
            # Get the last inserted Government_Exam_Id
            cursor.execute("SELECT Government_Exam_Id FROM Government_Exam ORDER BY Government_Exam_Id DESC LIMIT 1")
            max_id_row = cursor.fetchone()

            if max_id_row:
                # Extract the numeric part and increment
                last_exam_id = str(max_id_row[0])  # Convert to string
                if last_exam_id.isdigit():
                    new_exam_id = int(last_exam_id) + 1
                else:
                    # If there is any non-numeric part, just increment the numeric part
                    new_exam_id = int(last_exam_id[1:]) + 1  # Assuming any prefix is a letter
            else:
                # If no previous IDs exist, start from 1
                new_exam_id = 1

            # Check if the generated ID already exists in the Government_Exam table
            cursor.execute("SELECT 1 FROM Government_Exam WHERE Government_Exam_Id = ?", (str(new_exam_id),))
            if cursor.fetchone() is None:
                # If the ID does not exist, break out of the loop
                break

        conn.close()
        return str(new_exam_id)  # Return as a simple number, no prefix or padding
    except sqlite3.Error as e:
        print(f"An error occurred while generating Government_Exam_Id: {e}")
        return None

def add_government_exam_to_academic_record(academic_id, title, date, score_achieved, score_max):
    """Add a new government exam record to an academic record."""
    try:
        # Generate a unique Government_Exam_Id
        exam_id = generate_government_exam_id()
        if not exam_id:
            print("Failed to generate Government_Exam_Id.")
            return

        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Insert the government exam record for the academic record
        cursor.execute('''INSERT INTO Government_Exam (Government_Exam_Id, Academic_Id, Title, Date, Score_Achieved, Score_Max)
                          VALUES (?, ?, ?, ?, ?, ?)''', (exam_id, academic_id, title, date, score_achieved, score_max))

        conn.commit()  # Save changes
        conn.close()

        print(f"Government Exam {exam_id} successfully added to academic record {academic_id}.")
    
    except sqlite3.Error as e:
        print(f"An error occurred while adding government exam: {e}")

def get_government_exams_for_academic_record(academic_id):
    """Retrieve all government exams for a given academic record."""
    try:
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Retrieve government exams related to the given academic record
        cursor.execute('''SELECT Government_Exam_Id, Title, Date, Score_Achieved, Score_Max
                          FROM Government_Exam
                          WHERE Academic_Id = ?''', (academic_id,))
        exams = cursor.fetchall()

        conn.close()

        if exams:
            print(f"Government Exams for Academic Record {academic_id}:")
            for exam in exams:
                print(f"Exam ID: {exam[0]}, Title: {exam[1]}, Date: {exam[2]}, Score: {exam[3]}/{exam[4]}")
        else:
            print(f"No government exams found for Academic Record {academic_id}.")
    
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving government exams: {e}")
