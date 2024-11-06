import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QFileDialog, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QClipboard

class CSVReaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Reader App")
        self.setGeometry(100, 100, 600, 400)

        # Main layout
        layout = QVBoxLayout(self)

        # Load CSV button
        self.load_button = QPushButton("Load CSV")
        self.load_button.clicked.connect(self.load_csv)
        layout.addWidget(self.load_button)

        # Scrollable area for dynamic content
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        # Container for rows of labels, values, and copy buttons
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.scroll_area.setWidget(self.content_widget)

    def load_csv(self):
        # Open file dialog to select CSV
        csv_file, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv);;All Files (*)")
        if csv_file:
            # Clear previous entries
            for i in reversed(range(self.content_layout.count())):
                widget = self.content_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Read CSV file
            with open(csv_file, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row if it exists
                for row in reader:
                    if len(row) >= 2:  # Ensure each row has at least two elements
                        label, value = row[0], row[1]
                        self.add_row(label, value)

    def add_row(self, label_text, value_text):
        # Row layout with label QLineEdit, value QLineEdit, and copy button
        row_layout = QHBoxLayout()

        # Label input
        label_input = QLineEdit(self)
        label_input.setText(label_text)
        label_input.setReadOnly(True)
        row_layout.addWidget(label_input)

        # Value input
        value_input = QLineEdit(self)
        value_input.setText(value_text)
        row_layout.addWidget(value_input)

        # Copy button
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(value_input.text()))
        row_layout.addWidget(copy_button)

        # Add row to content layout
        self.content_layout.addLayout(row_layout)

    def copy_to_clipboard(self, value):
        clipboard = QApplication.instance().clipboard()
        clipboard.setText(value)
        print(f"Copied: {value}") 

# Run the application
app = QApplication(sys.argv)
window = CSVReaderApp()
window.show()
sys.exit(app.exec())
