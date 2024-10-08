import sqlite3
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui_main_dashboard import Ui_MainWindow 
from addnewemp import AddEmployeeWindow  # Import your AddEmployeeWindow class

class Dashboard(QMainWindow):
    def __init__(self, db_path):
        super(Dashboard, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_path = db_path  
        self.connection = None
        self.cursor = None

        self.connect_db()
        self.populate_employee_table()

        self.ui.pushButton_5.clicked.connect(self.search_employees)
        self.ui.pushButton_4.clicked.connect(self.add_new_employee)  # Connect the button

    def connect_db(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Could not connect to the database: {e}")
            self.close()  

    def populate_employee_table(self):
        """Populate the employee table on the dashboard."""
        try:
            query = "SELECT * FROM currently_employed"
            self.cursor.execute(query)
            employees = self.cursor.fetchall()

            self.ui.tableWidget.setRowCount(len(employees))
            for row_index, row_data in enumerate(employees):
                for column_index, item in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error fetching employee data: {e}")

    def search_employees(self):
        """Search for employees based on the input in the search field."""
        search_text = self.ui.lineEdit.text().strip().lower()  
        if not search_text:  
            self.populate_employee_table()
            return
        
        try:
            query = """SELECT * FROM currently_employed  
                       WHERE LOWER(Last_Name) LIKE ? OR 
                             LOWER(First_Name) LIKE ? OR 
                             LOWER(Middle_Name) LIKE ? OR 
                             LOWER(Position_Id) LIKE ?"""  
            
            search_pattern = f"%{search_text}%"
            self.cursor.execute(query, (search_pattern, search_pattern, search_pattern, search_pattern))
            results = self.cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)

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
        self.add_employee_window = AddEmployeeWindow()  # Create an instance of AddEmployeeWindow
        self.   add_employee_window.show()  # Show the window

    def closeEvent(self, event):
        """Close the database connection when the application exits."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        event.accept()  
