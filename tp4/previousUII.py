# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advance.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import tpimage
import effets_geom
import effets_photom
import filtrages
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
        self.selectImgBtn.setGeometry(QtCore.QRect(60, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectImgBtn.setFont(font)
        self.selectImgBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.imageLbl.setGeometry(QtCore.QRect(280, 70, 1011, 731))
        self.imageLbl.setAutoFillBackground(False)
        self.imageLbl.setStyleSheet("background-color:white;")
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.rotatImage = QtWidgets.QPushButton(self.centralwidget)
        self.rotatImage.setGeometry(QtCore.QRect(710, 20, 111, 31))
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
        self.relief = QtWidgets.QPushButton(self.centralwidget)
        self.relief.setGeometry(QtCore.QRect(60, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.relief.setFont(font)
        self.relief.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.relief.setStyleSheet("QPushButton{\n"
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
        self.relief.setObjectName("relief")
        self.fonte = QtWidgets.QPushButton(self.centralwidget)
        self.fonte.setGeometry(QtCore.QRect(60, 220, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fonte.setFont(font)
        self.fonte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fonte.setStyleSheet("QPushButton{\n"
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
        self.fonte.setObjectName("fonte")
        self.lightIncrease = QtWidgets.QPushButton(self.centralwidget)
        self.lightIncrease.setGeometry(QtCore.QRect(60, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lightIncrease.setFont(font)
        self.lightIncrease.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lightIncrease.setStyleSheet("QPushButton{\n"
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
        self.lightIncrease.setObjectName("lightIncrease")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.selectImgBtn.clicked.connect(self.setImage)
        self.rotatImage.clicked.connect(self.rotateImage)
        self.relief.clicked.connect(self.setReliefFX)
        self.fonte.clicked.connect(self.setFontFx)
        self.lightIncrease.clicked.connect(self.increasePictureLight)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.selectImgBtn.setText(_translate("mainWindow", "Select Image"))
        self.rotatImage.setText(_translate("mainWindow", "Rotate "))
        self.relief.setText(_translate("mainWindow", "Fx: Relief"))
        self.fonte.setText(_translate("mainWindow", "Fx : Fonte"))
        self.lightIncrease.setText(_translate("mainWindow", "increase Light"))

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
            img1 = filtrages.filtrerImageNB(img1,xsize,ysize,5) 
            qim = ImageQt(img1)
            img1.save('img.png')
            self.filename = 'img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")

    def setReliefFX(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size 
            img1 = effets_photom.deriv1xNB(img1,xsize,ysize)
            qim = ImageQt(img1)
            img1.save('img.png')
            self.filename = 'img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")

    def setFontFx(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size 
            img1 = effets_geom.effetFonteNB(img1,xsize,ysize)
            qim = ImageQt(img1)
            img1.save('img.png')
            self.filename = 'img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")
    
    def increasePictureLight(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size 
            img1 = effets_photom.plusClairNB(img1,xsize,ysize)
            qim = ImageQt(img1)
            img1.save('img.png')
            self.filename = 'img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
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

