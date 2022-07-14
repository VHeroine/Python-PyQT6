from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6 import uic, QtGui
import os


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
        self.file_list = None
        self.file_counter = None
        self.actionOpen_Image.triggered.connect(self.open_image)
        self.actionOpen_Folder.triggered.connect(self.open_directory)
        self.actionQuit.triggered.connect(self.exit)
        self.pushButton.clicked.connect(self.previous_image)
        self.pushButton_2.clicked.connect(self.next_image)

    def resizeEvent(self, event):
        try:
            imagemap = QtGui.QPixmap(self.current_file)
        except:
            imagemap = QtGui.QPixmap("Default.jpg")
        imagemap = imagemap.scaled(self.width(), self.height())
        self.label.setPixmap(imagemap)
        self.label.resize(self.width(), self.height())

    def exit(self):
        QApplication.exit()

    def scale_image(self):
            imagemap = QtGui.QPixmap(self.current_file)
            imagemap = imagemap.scaled(self.width(), self.height())
            self.label.setPixmap(imagemap)

    def open_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Image Files (*.bmp *.png *.jpg *.jpeg)")
        if filename != "":
            self.current_file = filename
            self.scale_image()

    def next_image(self):
        if self.file_counter is not None:
            self.file_counter += 1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            self.scale_image()

    def previous_image(self):
        if self.file_counter is not None:
            self.file_counter -= 1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            self.scale_image()

    def open_directory(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.file_list = [directory + '/' + f for f in os.listdir(directory) if f.endswith(".jpg") or
        f.endswith(".jpeg") or f.endswith(".png") or f.endswith(".bmp")]
        self.file_counter = 0
        self.scale_image()


def main():
    """The main function of application."""
    app = QApplication([])
    window = MainGUI()
    app.exec()


if __name__ == "__main__":
    main()