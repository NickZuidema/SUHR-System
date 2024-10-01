from PySide6.QtWidgets import QApplication, QMainWindow
from generated_ui import Ui_Login  # Import the generated UI class

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create an instance of the Ui_MainWindow class
        self.ui = Ui_Login()

        # Set up the UI
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    import sys

    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of the main window
    window = MainWindow()

    # Show the window
    window.show()

    # Start the event loop
    sys.exit(app.exec())