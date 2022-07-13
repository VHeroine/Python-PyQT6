from PyQt6.QtWidgets import *
from PyQt6 import uic, QtGui


class MainGUI(QMainWindow):
    """The main user interface class."""

    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi("ImageViewer.ui", self)
        self.show()

def main():
    """The main function of application."""
    app = QApplication([])
    window = MainGUI()
    app.exec()

if __name__ == "__main__":
    main()