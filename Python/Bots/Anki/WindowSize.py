import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Size Detector")

    def resizeEvent(self, event):
        width = self.width()
        height = self.height()
        print(f"Window width: {width}, height: {height}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
