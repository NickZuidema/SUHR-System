import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect('C:/HR/SUHR-System/Database/SUHRSystem.db')  # Use absolute path
    cursor = conn.cursor()
    print("Connected to the database.")
    
    # Disable foreign keys
    cursor.execute("PRAGMA foreign_keys = OFF;")
    print("Foreign keys disabled.")
    
    # Retrieve all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = cursor.fetchall()
    
    # Check if any tables are found
    if not tables:
        print("No tables found in the database.")
    else:
        # Delete all rows from each table and confirm deletion
        for table in tables:
            table_name = table[0]
            # Count rows before deletion
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            print(f"Table {table_name} has {row_count} rows before deletion.")
            
            # Delete all rows
            cursor.execute(f"DELETE FROM {table_name}")
            conn.commit()  # Commit immediately to ensure deletion

            # Count rows after deletion to confirm
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count_after = cursor.fetchone()[0]
            print(f"Deleted all rows from table: {table_name}. Row count after deletion: {row_count_after}")
    
    # Re-enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")
    print("Foreign keys re-enabled.")
    
except sqlite3.Error as e:
    print("Error with the database operation:", e)

finally:
    if conn:
        conn.close()
        print("Connection closed.")
