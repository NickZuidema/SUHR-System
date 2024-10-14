import sqlite3

# Function to generate and insert spouse data
def insert_spouse_data(spouse_id, full_name, date_of_marriage, place_of_marriage):
    try:
        # Connect to the database
        conn = sqlite3.connect(r'C:\Users\Admin\Documents\GitHub\SUHR-System\Database\SUHRSystem.db')
        cursor = conn.cursor()

        # Insert spouse info first
        sql_spouse_info = '''
            INSERT INTO Spouse_Info (Date_Of_Marriage, Place_Of_Marriage)
            VALUES (?, ?)
        '''
        cursor.execute(sql_spouse_info, (date_of_marriage, place_of_marriage))
        
        # Get the auto-incremented Spouse_Info_Id
        spouse_info_id = cursor.lastrowid

        # Combine spouse_id and spouse_info_id for the Spouse_Info_Id
        combined_spouse_info_id = f"{spouse_id}-{spouse_info_id}"

        # Insert spouse data using the original spouse_id and the combined Spouse_Info_Id
        sql_spouse = '''
            INSERT INTO Spouse (Spouse_Id, Full_Name, Spouse_Info_Id)
            VALUES (?, ?, ?)
        '''
        cursor.execute(sql_spouse, (spouse_id, full_name, combined_spouse_info_id))

        # Commit changes
        conn.commit()
        print(f"Spouse data inserted successfully: {spouse_id}, {full_name}, Spouse_Info_Id: {combined_spouse_info_id}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to generate spouse_id using Saved_ID and count from the database
def generate_spouse_id(saved_id):
    try:
        # Connect to the database
        conn = sqlite3.connect(r'C:\Users\Admin\Documents\GitHub\SUHR-System\Database\SUHRSystem.db')
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