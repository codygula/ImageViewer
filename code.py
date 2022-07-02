from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel 
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QPixmap
import sys, os
from PIL import Image


image1 = Image.open("img049.jpg")

width, height = image1.size
newSize = (300, 300)
image2 = image1.resize(newSize)
image2.save("thumbnailimg.jpg")


class Ui(QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi("interface.ui", self) # Load the .ui file
        self.show() # Show the GUI


        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo1.setLayout(vbox)
        self.show()
        # self.Photo1.picture()
        #self.Photo2.setText("testing")


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application