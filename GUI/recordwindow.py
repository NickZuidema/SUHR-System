import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_record import Ui_MainWindow  # Make sure this points to your UI module

class ArchiveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    archive_window = ArchiveWindow()  # Create an instance of ArchiveWindow
    archive_window.show()  # Show the window
    sys.exit(app.exec())
