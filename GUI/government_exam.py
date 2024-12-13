import sqlite3
from config import get_database_path

db_path = get_database_path()

def generate_government_exam_id():
    """Generate a new Government_Exam_Id for a government exam, ensuring it's unique."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

      
        # Get the last inserted Government_Exam_Id
        cursor.execute("SELECT count(*) from Government_Exam;")
        max_id_row = cursor.fetchone()

        if max_id_row:

            last_exam_id = int(max_id_row[0])
            new_exam_id = last_exam_id + 1
            print(f'new id:{new_exam_id}')
            
        else:
            # If no previous IDs exist, start from 1
            new_exam_id = 1

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

        conn = sqlite3.connect(db_path)
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
        conn = sqlite3.connect(db_path)
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
