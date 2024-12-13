from PySide6.QtWidgets import QApplication, QMainWindow
from ui_record import Ui_MainWindow     
import sys

class Archive(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = Archive()  
    window.show()
    sys.exit(app.exec())


