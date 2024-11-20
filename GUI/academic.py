import sqlite3
from config import get_database_path

# Function to insert academic record data
def insert_academic_record_data(
    elementary_id, elementary_fin, elementary_diploma, highschool_id, 
    highschool_diploma, highschool_fin, college_id, 
    college_diploma, college_fin, gradschool_id, gradschool_diploma, 
    gradschool_fin
):
    conn = None  # Initialize conn here to avoid the UnboundLocalError
    try:
        # Connect to the database
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Insert academic record data
        sql_academic_record = '''
            INSERT INTO Academic_Record (
                Elementary_ID, Elementary_Fin, Elementary_Diploma, HighSchool_ID, 
                HighSchool_Diploma, HighSchool_Fin, 
                College_ID, College_Diploma, College_Fin, GradSchool_ID, 
                GradSchool_Diploma, GradSchool_Fin
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(sql_academic_record, (
            elementary_id, elementary_fin, elementary_diploma, highschool_id,
            highschool_diploma, highschool_fin,
            college_id, college_diploma, college_fin, gradschool_id,
            gradschool_diploma, gradschool_fin
        ))

        # Commit changes
        conn.commit()
        academic_record_id = cursor.lastrowid
        print(f"Academic record data inserted successfully. Academic_Record_Id: {academic_record_id}")
        
        return academic_record_id

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()  # Ensure connection is closed only if it was successfully created
