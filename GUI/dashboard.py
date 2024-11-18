import sqlite3
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication

#dashboard design file
from ui_main_dashboard_copy import Ui_MainWindow

from addnewemp import AddEmployeeWindow
from recordwindow import RecordWindow
from config import get_database_path
from session import SessionManager
from main import MainWindow  # Import the MainWindow (login page)
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QApplication
from view_record import MainWindow

class Dashboard(QMainWindow):
    def __init__(self, db_path, username=None):
        # Properly initialize the QMainWindow base class
        super(Dashboard, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_path = db_path
        self.username = username  # Save the username for user-specific context
        self.connection = None
        self.cursor = None

        # Create a session manager instance
        self.session_manager = SessionManager()

        # Check if there is an active session
        if not self.username:
            QMessageBox.warning(self, "Session Expired", "You must log in first.")
            self.redirect_to_login()  # Redirect to login if no session exists
        else:
            print(f"Session active for user: {self.username}")

        self.connect_db()
        self.populate_employee_table()

        # Connect button clicks to functions
        self.ui.pushButton_5.clicked.connect(self.search_employees)
        self.ui.pushButton_4.clicked.connect(self.add_new_employee)
        self.ui.pushButton_3.clicked.connect(self.open_archive)
        self.ui.refresh_button.clicked.connect(self.populate_employee_table)

        # Connect logout button to logout function
        self.ui.pushButton_2.clicked.connect(self.logout)

        # Connect cell click signal to the custom slot method
        self.ui.tableWidget.cellClicked.connect(self.cell_clicked)


    def connect_db(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Could not connect to the database: {e}")
            self.close()

    def populate_employee_table(self):
        """Populate the employee table on the dashboard only if there is an active session."""
        try:
            if not self.username:  # Check again, in case session expires while in dashboard
                QMessageBox.warning(self, "No Session", "No active session found. Please log in.")
                self.redirect_to_login()
                return  # Do not proceed to fetch data if no session

            query = "SELECT * FROM Employee"
            self.cursor.execute(query)
            employees = self.cursor.fetchall()

            # Get the column names from the cursor description
            column_names = [description[0] for description in self.cursor.description]
            self.ui.tableWidget.setColumnCount(len(column_names))  # Set the column count
            self.ui.tableWidget.setHorizontalHeaderLabels(column_names)  # Set column headers
            
            if employees:  # Check if there is any data
                self.ui.tableWidget.setRowCount(len(employees))
                for row_index, row_data in enumerate(employees):
                    for column_index, item in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))
            else:
                QMessageBox.information(self, "No Records", "No employee data available.")
                # Optionally, display a "No records" message in the table area
                self.ui.tableWidget.setRowCount(1)
                self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("No records available"))
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error fetching employee data: {e}")

    def search_employees(self):
        """Search for employees based on the input in the search field."""
        search_text = self.ui.lineEdit.text().strip().lower()
        dropDown_data = self.ui.comboBox.currentText()
        print(f"Selected Filter {dropDown_data}")

        if not search_text:
            self.populate_employee_table()
            return
        
        try:
            if not self.username:
                QMessageBox.warning(self, "No Session", "You must log in to search.")
                return

            if dropDown_data == "Name":
                query = """SELECT * FROM Employee  
                        WHERE LOWER(Last_Name) LIKE ? OR 
                                LOWER(First_Name) LIKE ? OR 
                                LOWER(Middle_Name) LIKE ?"""
                search_pattern = f"%{search_text}%"
                self.cursor.execute(query, (search_pattern, search_pattern, search_pattern))

            elif dropDown_data == "ID":
                query = """SELECT * FROM Employee Where 
                        Employee_Id LIKE ? """
                search_pattern = f"{search_text}%"
                self.cursor.execute(query, (search_pattern,))
                

            elif dropDown_data == "Employment Date":
                query = """SELECT * FROM Employee Where Date_Employed Like ?"""
                search_pattern = f"{search_text}%"
                self.cursor.execute(query, (search_pattern,))
            
            results = self.cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)  # Clear previous results

            for row_index, row_data in enumerate(results):
                self.ui.tableWidget.insertRow(row_index)
                for column_index, item in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

            if not results:
                QMessageBox.information(self, "Search Result", "No matching records found.")
            else:
                QMessageBox.information(self, "Search Result", f"{len(results)} matching records found.")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error searching employee data: {e}")

    def add_new_employee(self):
        """Open the Add Employee window."""
        self.add_employee_window = AddEmployeeWindow()
        self.add_employee_window.show()

    def open_archive(self):
        """Open the Archive window."""
        self.archive_window = RecordWindow()
        self.archive_window.show()

    def cell_clicked(self, row, column):
        """Handle cell click event in the employee table."""
        # Collect employee data from the clicked row (if needed)
        employee_id = self.ui.tableWidget.item(row, 0).text()  # Assuming the Employee_Id is in the first column

        # Initialize and show the view record window with the selected employee ID
        self.view_record_window = MainWindow(employee_id)
        self.view_record_window.show()


        
        # Display the data in a message box or use it for other purposes
        # QMessageBox.information(self, "Employee Data", 
        #                         f"You clicked on:\n{employee_data}")

    def logout(self):
        """Handle the logout functionality."""
        # Clear the session
        self.session_manager.clear_session()
        QMessageBox.information(self, "Logged Out", "You have successfully logged out.")

        # Redirect to the login window
        self.redirect_to_login()

    def redirect_to_login(self):
        """Redirect to the login page (main.py)"""
        from main import MainWindow  # Import here to avoid circular import
        self.main_window = MainWindow()  # Create a new login window
        self.main_window.show()  # Show the login window
        self.close()  # Close the dashboard window

    def closeEvent(self, event):
        """Close the database connection when the application exits."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        event.accept()

if __name__ == "__main__":
    db_path = get_database_path()
    app = QApplication([])
    window = Dashboard(db_path)  # Do not pass username if there's no session
    app.exec()
    window.show()  # This will not be reached if no session