import sqlite3
import os
from config import get_database_path
from openpyxl import Workbook
from datetime import datetime, timedelta
import re

GUI_path = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(GUI_path)
logs_directory = os.path.join(main_dir, 'logs')

class SessionManager:
    def __init__(self):
        self.db_path = get_database_path()  # Get the database path from config
        self.connection = None
        self.cursor = None
        self.create_sessions_table()  # Ensure the sessions table exists
        self.log_folder = logs_directory  # Log folder path
        self.log_file = os.path.join(self.log_folder, "login_logout_log.xlsx")  # Log file path
        self.ensure_log_exists()  # Ensure log file exists and is ready
        self.session_timeout = timedelta(minutes=30)  # Set session timeout (e.g., 30 minutes)
        self.activity_log_file = os.path.join(self.log_folder, "activity_log.xlsx")  # Activity log file path
        self.ensure_activity_log_exists()  # Ensure activity log file exists and is ready

    def connect_db(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def create_sessions_table(self):
        """Create the Sessions table if it doesn't already exist."""
        self.connect_db()
        try:
            query = """
            CREATE TABLE IF NOT EXISTS Session (
                session_id TEXT PRIMARY KEY, 
                user_id TEXT NOT NULL, 
                login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expiration_time TIMESTAMP
            )
            """
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating session table: {e}")

    def save_session(self, session_id, user_id, expiration_time=None):
        """Save the user session to the database."""
        self.connect_db()
        try:
            if expiration_time is None:
                expiration_time = datetime.now() + self.session_timeout  # Set default expiration time
            
            query = """
            INSERT OR REPLACE INTO Session (session_id, user_id, login_time, expiration_time)
            VALUES (?, ?, CURRENT_TIMESTAMP, ?)
            """
            self.cursor.execute(query, (session_id, user_id, expiration_time))
            self.connection.commit()
            print("Session saved successfully.")
            self.log_to_excel(user_id, "Login")  # Log login action
        except sqlite3.Error as e:
            print(f"Error saving session: {e}")

    def check_session(self):
        """Check if there is an active session for the user."""
        self.connect_db()
        try:
            query = "SELECT * FROM Session ORDER BY login_time DESC LIMIT 1"
            self.cursor.execute(query)
            session = self.cursor.fetchone()
            
            if session:
                session_id, user_id, login_time, expiration_time = session
                print(f"Session found for user {user_id} (Session ID: {session_id})")
                
                # Use the format to parse datetime with microseconds
                expiration_time = datetime.strptime(expiration_time, "%Y-%m-%d %H:%M:%S.%f") if expiration_time else None
                
                if expiration_time and datetime.now() > expiration_time:
                    print("Session has expired.")
                    return None  # Session expired
                else:
                    return user_id  # Return user_id if session is still valid
            else:
                print("No active session found.")
                return None
        except sqlite3.Error as e:
            print(f"Error checking session: {e}")
            return None

    def clear_session(self):
        """Clear the current session from the database."""
        self.connect_db()
        try:
            query = "DELETE FROM Session"
            self.cursor.execute(query)
            self.connection.commit()
            print("Session cleared.")
            self.log_to_excel(None, "Logout")  # Log logout action
        except sqlite3.Error as e:
            print(f"Error clearing session: {e}")

    def close_db(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def ensure_log_exists(self):
        """Ensure the Excel log file exists and is ready."""
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)  # Create the log folder if it doesn't exist
        if not os.path.exists(self.log_file):
            wb = Workbook()
            sheet = wb.active
            # Ensure the title is valid by replacing invalid characters (e.g., "/")
            valid_title = "Login_Logout_Log"  # Replace invalid characters if necessary
            sheet.title = valid_title
            sheet.append(["Timestamp", "Username", "Action"])
            wb.save(self.log_file)

    def log_to_excel(self, username, action):
        """Log login/logout action to Excel file."""
        from openpyxl import load_workbook
        from datetime import datetime

        # Ensure valid sheet title by removing invalid characters
        valid_title = "Login_Logout_Log"
        # Alternatively, you could replace any invalid characters dynamically:
        valid_title = re.sub(r'[\\/*?:"<>|]', "_", valid_title)

        # Load or create the workbook
        wb = load_workbook(self.log_file)
        sheet = wb.active
        
        # If the sheet title is invalid, reset it
        if sheet.title != valid_title:
            sheet.title = valid_title
        
        # Log the action (login/logout/failed login) with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append([timestamp, username, action])
        
        # Save the workbook
        wb.save(self.log_file)

    def ensure_activity_log_exists(self):
        """Ensure the Excel activity log file exists and is ready."""
        if not os.path.exists(self.activity_log_file):
            wb = Workbook()
            sheet = wb.active
            valid_title = "Activity_Log"
            sheet.title = valid_title
            sheet.append(["Timestamp", "Username", "Activity"])
            wb.save(self.activity_log_file)

    def log_activity(self, username, activity):
        """Log user activity to Excel file."""
        from openpyxl import load_workbook
        from datetime import datetime

        valid_title = "Activity_Log"
        valid_title = re.sub(r'[\\/*?:"<>|]', "_", valid_title)

        wb = load_workbook(self.activity_log_file)
        sheet = wb.active
        
        if sheet.title != valid_title:
            sheet.title = valid_title
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append([timestamp, username, activity])
        
        wb.save(self.activity_log_file)

    def is_user_logged_in(self):
        """Check if any user is currently logged in."""
        user_id = self.check_session()
        return user_id is not None

    def log_failed_attempt(self, username):
        """Log failed login attempt to Excel file."""
        self.log_to_excel(username, "Failed Login")

if __name__ == "__main__":
    session_manager = SessionManager()
    if session_manager.is_user_logged_in():
        print("A user is logged in. Proceed with opening windows.")
        # ...existing code for opening windows...
    else:
        print("No user is logged in. Preventing windows from opening.")
        # Prevent any windows from opening
        exit()
