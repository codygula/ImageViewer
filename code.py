# TODO fix class. This should be fairly easy. get the class to work, call it for each open qlabel in the interface.ui
#


from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel 
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QPixmap
import sys, os
from PIL import Image

import boto3
import uuid

# Class to display a thumbnail image
class Photothumbnail:
    def __init__(self, prefix, suffix):
        #self.bucketName = bucketName
        #self.objectName = objectName
        #self.fileName = fileName
        self.prefix = prefix
        self.suffix = suffix

    def getObjectName(self):
        return self.prefix + self.suffix + ".jpg"

    def getFileName(self):
        return "/tmp/" + "s3image" + str(uuid.uuid1())

    def downLoad(self):
        s3.meta.client.download_file("newtestbucket25324dhfghgfhd8gds0", self.getObjectName, self.getFileName)



s3 = boto3.resource("s3")


# image34 = "/tmp/" + "s3image" + str(uuid.uuid1())
# s3.meta.client.download_file("newtestbucket25324dhfghgfhd8gds0", "Picture1.jpg", image34)

image1 = Image.open(Photothumbnail.downLoad("Picture", "1"))

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