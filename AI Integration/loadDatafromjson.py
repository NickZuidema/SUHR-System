import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout,QMessageBox
import os

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)

class DataLoaderApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize GUI elements
        self.initUI()
        
        # Placeholder for loaded data
        self.data = []
        self.current_index = 0

    def initUI(self):
        layout = QVBoxLayout()
        
        # Name field
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Address field
        self.address_label = QLabel("Address:")
        self.address_input = QLineEdit()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)

        # Age field
        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)

        # Job type field
        self.job_label = QLabel("Job Type:")
        self.job_input = QLineEdit()
        layout.addWidget(self.job_label)
        layout.addWidget(self.job_input)

        # Load Data button
        self.load_button = QPushButton("Load Data")
        self.load_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_button)

        # Navigation buttons
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.prev_button.clicked.connect(self.prev_record)
        nav_layout.addWidget(self.prev_button)
        
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_record)
        nav_layout.addWidget(self.next_button)
        
        layout.addLayout(nav_layout)

        # Disable navigation buttons initially
        self.prev_button.setEnabled(False)
        self.next_button.setEnabled(False)

        # Set layout
        self.setLayout(layout)
        self.setWindowTitle('Data Loader')

    def load_data(self):
        # Load the data from the JSON file
        try:
            with open('data.json', 'r') as file:
                self.data = json.load(file)
            
            # Populate the form with the first record
            if self.data:
                self.current_index = 0
                self.populate_form(self.data[0])
                self.update_navigation_buttons()

        except Exception as e:
            print(f"Error loading data: {e}")
            QMessageBox.critical(self, "Database Error", f"Could not connect to the database: {e}")
            sys.exit(1)

    def populate_form(self, record):
        # Set the form fields to the values from the record
        self.name_input.setText(record.get("name", ""))
        self.address_input.setText(record.get("address", ""))
        self.age_input.setText(str(record.get("age", "")))
        self.job_input.setText(record.get("job_type", ""))

    def next_record(self):
        # Go to the next record if available
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.populate_form(self.data[self.current_index])
            self.update_navigation_buttons()

    def prev_record(self):
        # Go to the previous record if available
        if self.current_index > 0:
            self.current_index -= 1
            self.populate_form(self.data[self.current_index])
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        # Update the state of navigation buttons
        self.prev_button.setEnabled(self.current_index > 0)
        self.next_button.setEnabled(self.current_index < len(self.data) - 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataLoaderApp()
    ex.show()
    sys.exit(app.exec())
