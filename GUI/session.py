import os
import pickle

class SessionManager:
    def __init__(self):
        self.session_file = 'session.pkl'

    def save_session(self, username):
        """Save the user session."""
        try:
            # Ensure the session file is writable
            with open(self.session_file, 'wb') as file:
                pickle.dump(username, file)
            print("Session saved successfully.")
        except Exception as e:
            print(f"Error saving session: {e}")
        
    def check_session(self):
        """Check if there is an active session."""
        try:
            # Check if session file exists before opening it
            if os.path.exists(self.session_file):
                with open(self.session_file, 'rb') as file:
                    username = pickle.load(file)
                print("Session found.")
                return username
            print("No active session.")
            return None
        except Exception as e:
            print(f"Error checking session: {e}")
            return None

    def clear_session(self):
        """Clear the current session."""
        try:
            # Check if session file exists before attempting to delete it
            if os.path.exists(self.session_file):
                os.remove(self.session_file)
                print("Session cleared.")
            else:
                print("No session file found to clear.")
        except Exception as e:
            print(f"Error clearing session: {e}")
