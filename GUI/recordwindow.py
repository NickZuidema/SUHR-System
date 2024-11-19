import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QHeaderView, QStatusBar
)
from PySide6.QtCore import Qt
import sqlite3
from config import get_database_path  # Import get_database_path from config

#Archived Employee Manager

class RecordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Archived Employee Manager")
        self.setGeometry(100, 100, 800, 600)
        
        # Connect to the SUHRSystem.db database using the path from config.py
        self.conn = sqlite3.connect(get_database_path())
        self.cursor = self.conn.cursor()
        
        # Set up the UI
        self.setup_ui()
        # Load data into the table
        self.load_data()

    def setup_ui(self):
        # Central widget and layout
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        main_layout = QVBoxLayout(self.centralwidget)
        
        # Search and Filter section
        search_layout = QHBoxLayout()
        
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.filter_data)
        
        self.filter_combo = QComboBox(self)
        self.filter_combo.addItem("All Positions")
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.filter_combo)
        
        # Table setup
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Position", "Department", "Employment Date"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Unarchive Button
        self.unarchive_button = QPushButton("Unarchive Selected Row", self)
        self.unarchive_button.setEnabled(False)
        self.unarchive_button.clicked.connect(self.unarchive_selected_row)
        
        # Add widgets to main layout
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.unarchive_button)
        
        # Status bar
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        
        # Connect table selection signal
        self.table.itemSelectionChanged.connect(self.on_row_selected)

    def load_data(self):
        # Query to retrieve data for archived employees only
        self.cursor.execute("""
            SELECT Employee_Id, First_Name || ' ' || Last_Name AS Name, 
                Position_Id, 
                'Department Placeholder' AS Department, 
                Date_Employed 
            FROM Employee
            WHERE Archived = 1
        """)
        rows = self.cursor.fetchall()
        
        # Populate the table
        self.table.setRowCount(len(rows))
        for row_num, row_data in enumerate(rows):
            employee_id = row_data[0]
            for col_num, col_data in enumerate(row_data[1:]):
                item = QTableWidgetItem(str(col_data))
                if col_num == 0:
                    item.setData(Qt.UserRole, employee_id)  # Store Employee_Id in UserRole
                self.table.setItem(row_num, col_num, item)

    
    def filter_data(self):
        # Retrieve the search and filter values
        search_text = self.search_bar.text().lower()
        position_filter = self.filter_combo.currentText()
        
        # Clear the table before re-populating
        self.table.setRowCount(0)
        
        # Base query
        query = """
            SELECT First_Name || ' ' || Last_Name AS Name, 
                   Position_Id, 
                   'Department Placeholder' AS Department, 
                   Date_Employed 
            FROM Employee
            WHERE Archived = 1
        """
        params = []
        
        # Apply position filter if selected
        if position_filter != "All Positions":
            query += " AND Position_Id = ?"
            params.append(position_filter)
        
        # Apply search filter to the Name column
        query += " AND LOWER(First_Name || ' ' || Last_Name) LIKE ?"
        params.append(f"%{search_text}%")
        
        # Execute the query
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        
        # Populate the table with filtered results
        self.table.setRowCount(len(rows))
        for row_num, row_data in enumerate(rows):
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def on_row_selected(self):
        # Enable the unarchive button only if a row is selected
        selected_items = self.table.selectedItems()
        self.unarchive_button.setEnabled(bool(selected_items))
        
    def unarchive_selected_row(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            # Get the row number of the first selected item
            row = selected_items[0].row()
            employee_id = self.table.item(row, 0).data(Qt.UserRole)  # Retrieve Employee_Id using UserRole
            
            # Unarchive the selected row in the database
            self.cursor.execute("""
                UPDATE Employee 
                SET Archived = 0 
                WHERE Employee_Id = ?
            """, (employee_id,))
            self.conn.commit()
            
            # Refresh the data in the table
            self.load_data()
            self.statusbar.showMessage(f"Unarchived employee with ID: {employee_id}", 5000)

    def closeEvent(self, event):
        # Close the database connection when the window is closed
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecordWindow()
    window.show()
    sys.exit(app.exec())
