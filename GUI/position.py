import sqlite3
from config import get_database_path

def generate_position_id(name):
    """
    Generates a new Position_Id for the Position table and inserts a new record.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(get_database_path())
        cursor = conn.cursor()

        # Query to get the maximum Position_Id
        cursor.execute("SELECT MAX(Position_Id) FROM Position")
        max_id = cursor.fetchone()[0]

        # Generate a new Position_Id
        new_position_id = (max_id + 1) if max_id is not None else 1

        # Insert the new position record
        cursor.execute(
            "INSERT INTO Position (Position_Id, Name) VALUES (?, ?)",
            (new_position_id, name)
        )
        conn.commit()

        # Close the connection
        conn.close()

        return new_position_id

    except sqlite3.Error as e:
        print(f"Error while generating Position_Id: {e}")
        return None

# Test the function
if __name__ == "__main__":
    position_id = generate_position_id("Software Engineer")
    if position_id:
        print(f"Generated Position_Id: {position_id}")
    else:
        print("Failed to generate Position_Id.")