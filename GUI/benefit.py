import sqlite3

def generate_benefit_id():
    """Generate the next available Benefit ID."""
    conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
    cursor = conn.cursor()

    # Get the maximum Benefit_Id from the table to increment for the new record
    cursor.execute("SELECT MAX(Benefit_Id) FROM Benefit")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        benefit_id = 1  # Start with 1 if the table is empty
    else:
        benefit_id = max_id + 1  # Increment for the new record
    
    conn.close()
    return benefit_id

def insert_benefit_data():
    conn = sqlite3.connect(r'C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db')
    cursor = conn.cursor()

    # Define your benefit values
    education_value = 50
    medical_value = 50
    
    # Generate a new Benefit_Id
    cursor.execute("SELECT MAX(Benefit_Id) FROM Benefit")
    max_id = cursor.fetchone()[0]
    new_benefit_id = (max_id + 1) if max_id is not None else 1  # Start from 1 if no records exist

    # Insert the new benefit record
    cursor.execute("INSERT INTO Benefit (Benefit_Id, Education, Medical) VALUES (?, ?, ?)",
                   (new_benefit_id, education_value, medical_value))
    
    conn.commit()
    conn.close()

    return new_benefit_id  # Return the new Benefit_Id

# Example usage
if __name__ == "__main__":
    insert_benefit_data()  # This will add a new benefit record with Education and Medical set to 50
