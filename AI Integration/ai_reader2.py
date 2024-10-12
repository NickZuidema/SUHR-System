import sys
import cv2

from transformers import TrOCRProcessor, VisionEncoderDecoderModel

import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget, QScrollArea, QLineEdit
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QPoint, QRect


# TrOCR processor and model initialization
processor = TrOCRProcessor.from_pretrained('C:/Users/Acer/Desktop/code samples/softeng implementation project/handwriting model/processor')
model = VisionEncoderDecoderModel.from_pretrained('C:/Users/Acer/Desktop/code samples/softeng implementation project/handwriting model/model')

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.rectangles = []  
        self.label_list = []
        self.start_point = None
        self.end_point = None
        self.drawing = False
        self.image = None
        self.allowDraw = False

    def allow_drawing_action(self, message, label):
        self.allowDraw = message
        self.rectLabel = label

    def set_image(self, img):
        self.image = img
        height, width, channel = img.shape
        bytes_per_line = 3 * width
        q_img = QImage(img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
        self.setPixmap(QPixmap.fromImage(q_img))

    def mousePressEvent(self, event):
        if self.allowDraw and event.button() == Qt.MouseButton.LeftButton:
            self.start_point = event.position().toPoint()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing and event.button() == Qt.MouseButton.LeftButton:
            self.end_point = event.position().toPoint()
            self.drawing = False
            self.allowDraw = False
            self.rectangles.append((self.start_point, self.end_point))
            self.label_list.append(self.rectLabel)
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.pixmap() and self.start_point and self.end_point:
            painter = QPainter(self)
            painter.setPen(QPen(QColor(255, 0, 0), 2, Qt.PenStyle.SolidLine))

            # Draw existing rectangles
            for rect in self.rectangles:
                start, end = rect
                rect_to_draw = QRect(start, end)
                painter.drawRect(rect_to_draw)

            # Draw the current rectangle while dragging
            if self.drawing and self.start_point and self.end_point:
                current_rect = QRect(self.start_point, self.end_point)
                painter.drawRect(current_rect)

            #for future update, add feature that adds a button that deletes all rectangles

    def erase_event(self):
        self.rectangles = []
        self.label_list = []
        self.update()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw and Crop")
        self.setGeometry(0, 0, 1500, 800)

        # Create a scroll area
        self.scroll_area = QScrollArea()
        self.image_label = ImageLabel()

        # Set the QLabel inside the scroll area
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setWidgetResizable(True)

        # Buttons
        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_image)

        self.crop_button = QPushButton("Crop Area")
        self.crop_button.clicked.connect(self.crop_rectangles)

        self.draw_button = QPushButton("Draw Rect")
        self.draw_button.clicked.connect(self.draw_rectangles)
        
        self.label_input = QLineEdit(self)
        self.label_input.setPlaceholderText("Enter label for rectangle")
        
        self.erase_button = QPushButton("Erase all")
        self.erase_button.clicked.connect(self.erase_all)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.open_button)
        layout.addWidget(self.crop_button)
        layout.addWidget(self.draw_button)
        layout.addWidget(self.label_input)
        layout.addWidget(self.erase_button)
        self.setLayout(layout)

        self.image = None

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.bmp)")
        if file_name:
            self.image = cv2.imread(file_name)
            if self.image is None:
                print("Error loading image!")
                return

            self.image_label.set_image(self.image)

    def draw_rectangles(self):
        drawState = True
        rectangleLabel = self.label_input.text()
        self.image_label.allow_drawing_action(drawState,rectangleLabel)
        print("Drawing")

    def erase_all(self):
        self.image_label.erase_event()
        print("erasing all")

    def crop_rectangles(self):
        if self.image is None or not self.image_label.rectangles:
            print("Invalid Input")
            return

        for i, (start, end) in enumerate(self.image_label.rectangles):
            x1, y1 = start.x(), start.y()
            x2, y2 = end.x(), end.y()

            # Ensure the coordinates are in the right order
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)

            # Crop the image
            cropped_img = self.image[y1:y2, x1:x2]

            # Ensure the cropped region is valid
            if cropped_img.size == 0:
                print(f"Skipping invalid crop region: {(x1, y1, x2, y2)}")
                continue

            
            

            # Convert from BGR to RGB
            final_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)

            # Apply the processor
            pixel_values = processor(images=final_img, return_tensors="pt").pixel_values

            # Generate text from the model
            generated_ids = model.generate(pixel_values)
            generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

            labeled_name = self.image_label.label_list[i]
            print(f"Showing {labeled_name}")
            print(generated_text)

            cv2.imshow("Cropped Image", final_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Save the cropped image
            '''
            cropped_filename = f"cropped_{i}.png"
            cv2.imwrite(cropped_filename, cropped_img)
            print(f"Saved: {cropped_filename}")
            '''
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())