from PyQt6.QtWidgets import *
from PyQt6 import uic, QtGui


class MainGUI(QMainWindow):
    """The main user interface class."""

    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi("ImageViewer.ui", self)
        self.show()
        self.current_file = "Default.jpg"
        imagemap = QtGui.QPixmap(self.current_file)
        imagemap = imagemap.scaled(self.width(), self.height())
        self.label.setPixmap(imagemap)
        self.label.setMinimumSize(1, 1)

    def resizeEvent(self, event):
        try:
            imagemap = QtGui.QPixmap(self.current_file)
        except:
            imagemap = QtGui.QPixmap("Default.jpg")
        imagemap = imagemap.scaled(self.width(), self.height())
        self.label.setPixmap(imagemap)
        self.label.resize(self.width(), self.height())
        

def main():
    """The main function of application."""
    app = QApplication([])
    window = MainGUI()
    app.exec()

if __name__ == "__main__":
    main()