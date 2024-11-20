import sqlite3
from config import get_database_path

def generate_non_filipino_id():
    """Generate a new Non_Filipino_Id by incrementing the max existing ID."""
    conn = sqlite3.connect(get_database_path())
    cursor = conn.cursor()

    # Get the max Non_Filipino_Id from the Non_Filipino table
    cursor.execute("SELECT MAX(Non_Filipino_Id) FROM Non_Filipino")
    max_id = cursor.fetchone()[0]
    new_id = (max_id + 1) if max_id is not None else 1  # Increment the ID or start at 1 if no records exist

    conn.close()
    return new_id

def insert_non_filipino_data(passport_no, acr_no, date_of_issue):
    """
    Insert a new Non-Filipino record into the database and return the generated Non_Filipino_Id.
    
    Args:
        passport_no (str): Passport number of the non-Filipino individual.
        acr_no (str): ACR (Alien Certificate of Registration) number.
        date_of_issue (str): Date of issue of the passport or ACR.

    Returns:
        int: The generated Non_Filipino_Id for the inserted record.
    """
    conn = sqlite3.connect(get_database_path())
    cursor = conn.cursor()

    # Generate a new Non_Filipino_Id
    non_filipino_id = generate_non_filipino_id()

    # Insert the data into the Non_Filipino table
    cursor.execute(
        """
        INSERT INTO Non_Filipino (Non_Filipino_Id, Passport_No, Acr_No, Date_Of_Issue)
        VALUES (?, ?, ?, ?)
        """,
        (non_filipino_id, passport_no, acr_no, date_of_issue)
    )

    conn.commit()
    conn.close()

    return non_filipino_id
