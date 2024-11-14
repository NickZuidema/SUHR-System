import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QHeaderView, QStatusBar
)
from PySide6.QtCore import Qt
import sqlite3
from Path import db_path  # Import db_path
from config import get_database_path


class RecordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Record Manager")
        self.setGeometry(100, 100, 800, 600)
        
        # Connect to the SUHRSystem.db database using the path from Path.py
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
        # Optionally, add predefined positions, or load dynamically
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.filter_combo)
        
        # Table setup
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Position", "Department", "Employment Date"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Archive Button
        self.archive_button = QPushButton("Archive Selected Row", self)
        self.archive_button.setEnabled(False)
        self.archive_button.clicked.connect(self.archive_selected_row)
        
        # Add widgets to main layout
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.archive_button)
        
        # Status bar
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        
        # Connect table selection signal
        self.table.itemSelectionChanged.connect(self.on_row_selected)

    def load_data(self):
        # Query to retrieve data from the Employee table
        self.cursor.execute("""
            SELECT First_Name || ' ' || Last_Name AS Name, 
                   Position_Id, 
                   'Department Placeholder' AS Department, 
                   Date_Employed 
            FROM Employee
            WHERE Archived = 0
        """)
        rows = self.cursor.fetchall()
        
        # Populate the table
        self.table.setRowCount(len(rows))
        for row_num, row_data in enumerate(rows):
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
    
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
            WHERE Archived = 0
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
        # Enable the archive button only if a row is selected
        selected_items = self.table.selectedItems()
        self.archive_button.setEnabled(bool(selected_items))
        
    def archive_selected_row(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            # Get the row number of the first selected item
            row = selected_items[0].row()
            name = self.table.item(row, 0).text().split()
            first_name, last_name = name[0], name[-1]
            
            # Archive the selected row in the database
            self.cursor.execute("""
                UPDATE Employee 
                SET Archived = 1 
                WHERE First_Name = ? AND Last_Name = ?
            """, (first_name, last_name))
            self.conn.commit()
            
            # Refresh the data in the table
            self.load_data()
            self.statusbar.showMessage(f"Archived: {first_name} {last_name}", 5000)

    def closeEvent(self, event):
        # Close the database connection when the window is closed
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecordWindow()
    window.show()
    sys.exit(app.exec())
