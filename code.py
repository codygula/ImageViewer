# This is very inelegant, but it mostly works


from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel 
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QPixmap
import sys, os
from PIL import Image

import boto3
import uuid

s3 = boto3.resource("s3")

s3Bucket = "newtestbucket25324dhfghgfhd8gds0"

# Download object from S3 and save it to a file
def download(s3Object, destFile):
    s3.meta.client.download_file("newtestbucket25324dhfghgfhd8gds0", s3Object, destFile)
    print(f"downloaded {s3Object} to {destFile}")


# Image resize
def imageResize(picture, thumbNailName):
    image1 = Image.open(picture)
    width, height = image1.size
    newSize = (300, 300)
    image2 = image1.resize(newSize)
    image2.save(thumbNailName)

i=1
while i <= 4:
    destFile1 = "/tmp/testingtestingtesting" + str(i) + ".jpg"
    s3Object1 = "Picture" + str(i) + ".jpg"
    download(s3Object1, destFile1)
    imageResize(destFile1, "thumbnailimg" + str(i) + ".jpg")
    i = i + 1


class Ui(QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi("interface.ui", self) # Load the .ui file
        self.show() # Show the GUI


        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg1.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo1.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg2.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo2.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg3.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo3.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg4.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo4.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg5.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo5.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg6.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo6.setLayout(vbox)
        self.show()


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application


