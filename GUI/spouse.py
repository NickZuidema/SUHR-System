import sqlite3

# Function to generate and insert spouse data
def insert_spouse_data(spouse_id, first_name, middle_name, last_name, date_of_marriage, place_of_marriage):
    try:
        # Connect to the database
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()

        # Insert spouse info first
        sql_spouse_info = '''
            INSERT INTO Spouse_Info (Date_Of_Marriage, Place_Of_Marriage)
            VALUES (?, ?)
        '''
        cursor.execute(sql_spouse_info, (date_of_marriage, place_of_marriage))
        
        # Get the auto-incremented Spouse_Info_Id
        spouse_info_id = cursor.lastrowid

        # Insert spouse data using the original spouse_id and the Spouse_Info_Id
        sql_spouse = '''
            INSERT INTO Spouse (Spouse_Id, First_Name, Middle_Name, Last_Name, Spouse_Info_Id)
            VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(sql_spouse, (spouse_id, first_name, middle_name, last_name, spouse_info_id))

        # Commit changes
        conn.commit()
        print(f"Spouse data inserted successfully: {spouse_id}, {first_name} {middle_name} {last_name}, Spouse_Info_Id: {spouse_info_id}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to generate spouse_id using Saved_ID and count from the database
def generate_spouse_id(saved_id):
    try:
        # Connect to the database (provide the correct path)
        conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()

        # Get the count of spouses related to this saved_id
        query = "SELECT COUNT(*) FROM Spouse WHERE Spouse_Id LIKE ?"
        cursor.execute(query, (saved_id + '%',))
        count = cursor.fetchone()[0]

        # Generate a new Spouse_Id by appending the count
        spouse_id = f"{saved_id}-S{count + 1:03}"  # e.g., 20241009001-S001
        return spouse_id

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
