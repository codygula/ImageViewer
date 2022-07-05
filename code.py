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
    newSize = (200, 200)
    image2 = image1.resize(newSize)
    image2.save(thumbNailName)


# Get names of objects in bucket
s3Bucket = s3.Bucket("newtestbucket25324dhfghgfhd8gds0")

listOfPhotos = []

for thing in s3Bucket.objects.all():
    print(thing.key)
    print(type(thing))
    # if str(thing).endswith(".jpg" or ".png" or ".raw"):
    # print("Success!")
    listOfPhotos.append(thing.key)

print(listOfPhotos)


# Iterate over names 
i=0
while i <= (len(listOfPhotos) - 1):
    destFile1 = "/tmp/testingtestingtesting" + str(i) + ".jpg"
    s3Object1 = listOfPhotos[i]
    try:
        download(s3Object1, destFile1)
        imageResize(destFile1, "thumbnailimg" + str(i) + ".jpg")
    except:
        print("error")
        destFile1 = "img049.jpg"
        imageResize(destFile1, "thumbnailimg" + str(i) + ".jpg")
    i = i + 1


class Ui(QDialog):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi("interface.ui", self) # Load the .ui file
        self.show() # Show the GUI

# TODO This whole thing obviously needs to be redone.

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

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg7.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo7.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg8.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo8.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg9.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo9.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg10.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo10.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg11.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo11.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg12.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo12.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg13.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo13.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg14.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo14.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg15.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo15.setLayout(vbox)
        self.show()

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("thumbnailimg5.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.Photo5.setLayout(vbox)
        self.show()


app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application


