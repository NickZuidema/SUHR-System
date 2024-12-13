import sqlite3
from config import get_database_path

db_path = get_database_path()

# Function to insert academic record data
def insert_academic_record_data(
    elementary_id, elementary_fin, elementary_diploma, elementary_address,
    seniorhigh_fin, seniorhigh_id, seniorhigh_diploma, seniorhigh_address, 
    college_id, college_diploma, college_address, college_fin,
    gradschool_id, gradschool_diploma, gradschool_fin, gradschool_address
):
    conn = None  # Initialize conn here to avoid the UnboundLocalError

    print("at insert academic record data")
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Insert academic record data
        sql_academic_record = '''
            INSERT INTO Academic_Record (
                Elementary_ID, Elementary_Name, Elementary_Address, Elementary_Diploma, Elementary_Fin, 
                HighSchool_ID, HighSchool_Name, HighSchool_Address, HighSchool_Diploma, HighSchool_Fin, 
                SeniorHigh_ID, SeniorHigh_Name, SeniorHigh_Address, SeniorHigh_Diploma, SeniorHigh_Fin, 
                College_ID, College_Name, College_Address, College_Diploma, College_Fin,
                GradSchool_ID, GradSchool_Name, GradSchool_Address, GradSchool_Diploma, GradSchool_Fin
            ) VALUES (?, ?, ?, ?, ?,
                     ?, ?, ?, ?, ?,
                     ?, ?, ?, ?, ?,
                     ?, ?, ?, ?, ?,
                     ?, ?, ?, ?, ?)
        '''
        cursor.execute(sql_academic_record, (
            elementary_id, elementary_id, elementary_address,elementary_diploma,elementary_fin,
            seniorhigh_id, seniorhigh_id, seniorhigh_address, seniorhigh_diploma, seniorhigh_fin, 
            seniorhigh_id, seniorhigh_id, seniorhigh_address, seniorhigh_diploma, seniorhigh_fin, 
            college_id, college_id, college_address, college_diploma, college_fin,
            gradschool_id, gradschool_id, gradschool_address, gradschool_diploma, gradschool_fin
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

# Function to generate academic record ID
def generate_academic_id(saved_id):
    conn = None  # Initialize conn here to avoid the UnboundLocalError
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Count academic records related to the saved ID pattern
        query = "SELECT COUNT(*) FROM Academic_Record WHERE Elementary_ID LIKE ?"
        cursor.execute(query, (saved_id + '%',))
        count = cursor.fetchone()[0]

        # Generate a new Academic_Record ID by appending the count
        academic_id = f"{saved_id}-A{count + 1:03}"  # e.g., 20241009001-A001
        return academic_id

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()  # Ensure connection is closed only if it was successfully created
