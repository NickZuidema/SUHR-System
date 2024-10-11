import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
from PyQt6.QtCore import Qt, QRect, QPoint

class RectangleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rectangle Drawer")

        # Set up the main layout
        self.layout = QVBoxLayout()

        # Input field for rectangle label
        self.label_input = QLineEdit(self)
        self.label_input.setPlaceholderText("Enter label for rectangle")
        self.layout.addWidget(self.label_input)

        # Button to start drawing
        self.draw_button = QPushButton("Draw Rectangle", self)
        self.draw_button.clicked.connect(self.start_drawing)
        self.layout.addWidget(self.draw_button)

        # Set up the custom widget for drawing
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

        self.start_point = None
        self.end_point = None
        self.drawing = False
        self.rectangles = []

    def start_drawing(self):
        self.start_point = None  # Reset starting point
        self.end_point = None    # Reset ending point
        self.drawing = True       # Enable drawing
        self.update()            # Request a repaint

    def mousePressEvent(self, event):
        if self.drawing and event.button() == Qt.MouseButton.LeftButton:
            self.start_point = event.position().toPoint()
            self.end_point = self.start_point  # Initialize end point to start point

    def mouseMoveEvent(self, event):
        if self.drawing and self.start_point:
            self.end_point = event.position().toPoint()
            self.update()  # Request a repaint

    def mouseReleaseEvent(self, event):
        if self.drawing and event.button() == Qt.MouseButton.LeftButton:
            self.end_point = event.position().toPoint()
            self.rectangles.append((self.start_point, self.end_point))
            self.drawing = False  # Disable drawing after finishing the rectangle
            self.update()  # Request a repaint
            self.show_message("Rectangle drawn!")  # Notify user

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw existing rectangles
        for start, end in self.rectangles:
            rect_to_draw = QRect(start, end)
            painter.setPen(QPen(QColor(255, 0, 0), 2, Qt.PenStyle.SolidLine))
            painter.drawRect(rect_to_draw)

        # Draw the current rectangle while dragging
        if self.drawing and self.start_point and self.end_point:
            current_rect = QRect(self.start_point, self.end_point)
            painter.setPen(QPen(QColor(0, 255, 0), 2, Qt.PenStyle.DashLine))  # Drawing rectangle in green
            painter.drawRect(current_rect)

    def show_message(self, message):
        QMessageBox.information(self, "Info", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RectangleDrawer()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
