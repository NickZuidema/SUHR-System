import sqlite3
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from ui_main_dashboard_copy import Ui_MainWindow
from addnewemp import AddEmployeeWindow
from recordwindow import RecordWindow
from config import get_database_path
from session import SessionManager
from main import MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QApplication
from view_record import MainWindow

class Dashboard(QMainWindow):
    def __init__(self, db_path, username=None):
        super(Dashboard, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_path = db_path
        self.username = username
        self.connection = None
        self.cursor = None

        self.session_manager = SessionManager()

        if not self.username:
            QMessageBox.warning(self, "Session Expired", "You must log in first.")
            self.redirect_to_login()
        else:
            print(f"Session active for user: {self.username}")

        self.connect_db()
        self.populate_employee_table()

        self.ui.pushButton_5.clicked.connect(self.search_employees)
        self.ui.pushButton_4.clicked.connect(self.add_new_employee)
        self.ui.pushButton_3.clicked.connect(self.open_archive)
        self.ui.refresh_button.clicked.connect(self.populate_employee_table)
        self.ui.pushButton_2.clicked.connect(self.logout)
        self.ui.tableWidget.cellClicked.connect(self.cell_clicked)

    def connect_db(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Could not connect to the database: {e}")
            self.close()

    def populate_employee_table(self):
        try:
            if not self.username:
                QMessageBox.warning(self, "No Session", "No active session found. Please log in.")
                self.redirect_to_login()
                return

            query = "SELECT * FROM Employee where Archived = 0"
            self.cursor.execute(query)
            employees = self.cursor.fetchall()

            column_names = [description[0] for description in self.cursor.description]
            self.ui.tableWidget.setColumnCount(len(column_names))
            self.ui.tableWidget.setHorizontalHeaderLabels(column_names)
            
            if employees:
                self.ui.tableWidget.setRowCount(len(employees))
                for row_index, row_data in enumerate(employees):
                    for column_index, item in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))
            else:
                QMessageBox.information(self, "No Records", "No employee data available.")
                self.ui.tableWidget.setRowCount(1)
                self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("No records available"))
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error fetching employee data: {e}")

    def search_employees(self):
        search_text = self.ui.lineEdit.text().strip().lower()
        dropDown_data = self.ui.comboBox.currentText()
        print(f"Selected Filter: {dropDown_data}")
        print(f"Search Text: '{search_text}'")

        if not search_text:
            self.populate_employee_table()
            return
        
        try:
            if not self.username:
                QMessageBox.warning(self, "No Session", "You must log in to search.")
                return

            if dropDown_data == "Name":
                query = """SELECT * FROM Employee
                        WHERE (LOWER(Last_Name) LIKE ? OR
                                LOWER(First_Name) LIKE ? OR
                                LOWER(Middle_Name) LIKE ?) AND Archived = 0"""
                search_pattern = f"%{search_text}%"
                print(f"Search Query: {query} with pattern '{search_pattern}'")
                self.cursor.execute(query, (search_pattern, search_pattern, search_pattern))

            elif dropDown_data == "ID":
                query = """SELECT * FROM Employee
                        WHERE Employee_Id LIKE ? AND Archived = 0"""
                search_pattern = f"{search_text}%"
                self.cursor.execute(query, (search_pattern,))

            elif dropDown_data == "Employment Date":
                query = """SELECT * FROM Employee
                        WHERE Date_Employed LIKE ? AND Archived = 0"""
                search_pattern = f"{search_text}%"
                self.cursor.execute(query, (search_pattern,))

            results = self.cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)
            if results:
                for row_index, row_data in enumerate(results):
                    self.ui.tableWidget.insertRow(row_index)
                    for column_index, item in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))
                QMessageBox.information(self, "Search Result", f"{len(results)} matching records found.")
            else:
                QMessageBox.information(self, "Search Result", "No matching records found.")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error searching employee data: {e}")

    def add_new_employee(self):
        self.add_employee_window = AddEmployeeWindow()
        self.add_employee_window.show()

    def open_archive(self):
        self.archive_window = RecordWindow()
        self.archive_window.show()

    def cell_clicked(self, row, column):
        employee_id = self.ui.tableWidget.item(row, 0).text()
        self.view_record_window = MainWindow(employee_id)
        self.view_record_window.show()

    def logout(self):
        self.session_manager.clear_session()
        QMessageBox.information(self, "Logged Out", "You have successfully logged out.")
        self.redirect_to_login()

    def redirect_to_login(self):
        from main import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def closeEvent(self, event):
        if self.session_manager.is_user_logged_in():
            self.session_manager.clear_session()
            print("User logged out automatically due to program closure.")
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        event.accept()

if __name__ == "__main__":
    db_path = get_database_path()
    app = QApplication([])
    window = Dashboard(db_path)
    app.exec()
    window.show()