from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, QScrollBar, QLabel
from PyQt6.QtCore import Qt
import sys

class ScrollBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scroll Bar Demo")
        self.setGeometry(100, 100, 600, 400)

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Vertical layout
        self.vertical_layout = QVBoxLayout(self.central_widget)

        # Scroll Area
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)

        # Content widget inside the scroll area
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)

        # Adding multiple labels as content
        for i in range(20):
            label = QLabel(f"Item {i+1}")
            self.content_layout.addWidget(label)

        # Set the layout for content widget
        self.content_widget.setLayout(self.content_layout)
        self.scroll_area.setWidget(self.content_widget)

        # Add scroll area to the main layout
        self.vertical_layout.addWidget(self.scroll_area)

        # Custom Vertical ScrollBar
        self.vertical_scrollbar = QScrollBar(Qt.Orientation.Vertical, self)
        self.scroll_area.setVerticalScrollBar(self.vertical_scrollbar)

        # Connect scrollbar to a method to print its position
        self.vertical_scrollbar.valueChanged.connect(self.print_scroll_position)

    def print_scroll_position(self, value):
        print(f"Vertical Scroll Position: {value}")

# Main block to execute the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollBarDemo()
    window.show()
    sys.exit(app.exec())
