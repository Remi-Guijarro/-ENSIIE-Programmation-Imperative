# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advance.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import tpimage
import effets_geom
import effets_photom
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1300, 850)
        mainWindow.setStyleSheet("background-color: rgb(99, 102, 112);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImgBtn.setGeometry(QtCore.QRect(40, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectImgBtn.setFont(font)
        self.selectImgBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectImgBtn.setText("Select Image")
        self.selectImgBtn.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    border:2px solid white;\n"
"    border-radius:15px;\n"
"    transition : all ease 1s;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"   color:rgb(99, 102, 112);\n"
"}")
        self.selectImgBtn.setObjectName("selectImgBtn")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(270, 40, 1011, 781))
        self.imageLbl.setAutoFillBackground(False)
        self.imageLbl.setStyleSheet("background-color:white;")
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.rotatImage = QtWidgets.QPushButton(self.centralwidget)
        self.rotatImage.setText("Rotate")
        self.rotatImage.setGeometry(QtCore.QRect(500, 0, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rotatImage.setFont(font)
        self.rotatImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rotatImage.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    border:2px solid white;\n"
"    border-radius:15px;\n"
"    transition : all ease 1s;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"   color:rgb(99, 102, 112);\n"
"}")
        self.rotatImage.setObjectName("rotatImage")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.selectImgBtn.clicked.connect(self.setImage)
        self.rotatImage.clicked.connect(self.rotateImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImgBtn.setText(_translate("MainWindow", "Select Image"))

    def setImage(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Image","","Image Files (*.png *.jpg *.jpeg *.bmp *.pgm)")
        if self.filename:
            self.pixmap = QtGui.QPixmap(self.filename)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)

    def rotateImage(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size 
            qim = ImageQt(effets_geom.RotationNB(img1,xsize,ysize))
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

