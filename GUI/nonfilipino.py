import sqlite3
from config import get_database_path

db_path = get_database_path()

def generate_non_filipino_id():
    """Generate a new Non_Filipino_Id by incrementing the max existing ID."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get the max Non_Filipino_Id from the Non_Filipino table
    cursor.execute("SELECT MAX(Non_Filipino_Id) FROM Non_Filipino")
    max_id = cursor.fetchone()[0]
    new_id = (max_id + 1) if max_id is not None else 1  # Increment the ID or start at 1 if no records exist

    conn.close()
    return new_id

def insert_non_filipino_data(passport_no, acr_no, date_of_issue):
    """
    Insert a new Non-Filipino record into the database.

    Args:
        passport_no (str): Passport number of the non-Filipino individual.
        acr_no (str): ACR (Alien Certificate of Registration) number.
        date_of_issue (str): Date of issue of the passport or ACR.

    Returns:
        None
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insert the data into the Non_Filipino table
    cursor.execute(
        """
        INSERT INTO Non_Filipino (Passport_No, Acr_No, Date_Of_Issue)
        VALUES (?, ?, ?)
        """,
        (passport_no, acr_no, date_of_issue)
    )

    conn.commit()
    conn.close()
