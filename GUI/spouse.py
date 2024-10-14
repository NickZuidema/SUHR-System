import sqlite3

def generate_spouse_id(saved_id):
    # Connect to the database
    conn = sqlite3.connect(r'C:\Users\Admin\Documents\GitHub\SUHR-System\Database\SUHRSystem.db')
    cursor = conn.cursor()

    # Query to count existing spouses for the given saved_id
    cursor.execute("SELECT COUNT(*) FROM Spouse WHERE Spouse_Id LIKE ?", (saved_id + '%',))
    count = cursor.fetchone()[0]

    # Generate Spouse_Id using saved_id and the count of existing spouses
    spouse_id = f"{saved_id}-{count + 1:03}"  # e.g., 20241009-001

    # Since Spouse_Info_Id should be the same as Spouse_Id
    spouse_info_id = spouse_id

    # Ensure that you insert only if spouse_name is provided
    full_name = ""  # Placeholder, should be assigned later

    conn.close()
    return spouse_id, full_name

def insert_spouse_data(spouse_id, full_name):
    conn = sqlite3.connect(r'C:\Users\Admin\Documents\GitHub\SUHR-System\Database\SUHRSystem.db')
    cursor = conn.cursor()

    # Since Spouse_Info_Id is the same as Spouse_Id
    spouse_info_id = spouse_id

    sql = '''INSERT INTO Spouse (Spouse_Id, Full_Name, Spouse_Info_Id)
             VALUES (?, ?, ?)'''
    cursor.execute(sql, (spouse_id, full_name, spouse_info_id))

    conn.commit()
    conn.close()
