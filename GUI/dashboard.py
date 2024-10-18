import sqlite3
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QApplication
from ui_main_dashboard import Ui_MainWindow
from addnewemp import AddEmployeeWindow
from recordwindow import ArchiveWindow

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

        # Connect button clicks to functions
        self.ui.pushButton_5.clicked.connect(self.search_employees)
        self.ui.pushButton_4.clicked.connect(self.add_new_employee)
        self.ui.pushButton_3.clicked.connect(self.open_archive)

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
            query = "SELECT * FROM Employee"
            self.cursor.execute(query)
            employees = self.cursor.fetchall()

            # Get the column names from the cursor description
            column_names = [description[0] for description in self.cursor.description]
            self.ui.tableWidget.setColumnCount(len(column_names))  # Set the column count
            self.ui.tableWidget.setHorizontalHeaderLabels(column_names)  # Set column headers
            
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
            query = """SELECT * FROM Employee  
                       WHERE LOWER(Last_Name) LIKE ? OR 
                             LOWER(First_Name) LIKE ? OR 
                             LOWER(Middle_Name) LIKE ?"""
            
            search_pattern = f"%{search_text}%"
            self.cursor.execute(query, (search_pattern, search_pattern, search_pattern))
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
        self.archive_window = ArchiveWindow()
        self.archive_window.show()

    def closeEvent(self, event):
        """Close the database connection when the application exits."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        event.accept()

if __name__ == "__main__":
    db_path = r"C:\Users\leeu6\Desktop\SUHR-System\SUHR-System\Database\SUHRSystem.db"
    app = QApplication([])
    window = Dashboard(db_path)
    window.show()
    app.exec()
