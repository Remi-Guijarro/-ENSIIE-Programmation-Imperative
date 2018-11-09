# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_source/advance.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from effect_source.effets_geom import *
from effect_source.effets_photom import *
from effect_source.filtrages import *
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(998, 529)
        mainWindow.setStyleSheet("background-color: rgb(99, 102, 112);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setAutoFillBackground(False)
        self.imageLbl.setStyleSheet("background-color:white;")
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.gridLayout_2.addWidget(self.imageLbl, 1, 1, 1, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.selectImgBtn = QtWidgets.QPushButton(self.centralwidget)
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
"*{\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"   color:rgb(99, 102, 112);\n"
"}")
        self.selectImgBtn.setObjectName("selectImgBtn")
        self.gridLayout_4.addWidget(self.selectImgBtn, 0, 0, 1, 1)
        self.fonte = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_4.addWidget(self.fonte, 1, 0, 1, 1)
        self.relief = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_4.addWidget(self.relief, 2, 0, 1, 1)
        self.reduceNoise = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reduceNoise.setFont(font)
        self.reduceNoise.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reduceNoise.setStyleSheet("QPushButton{\n"
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
        self.reduceNoise.setObjectName("reduceNoise")
        self.gridLayout_4.addWidget(self.reduceNoise, 3, 0, 1, 1)
        self.lightIncrease = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_4.addWidget(self.lightIncrease, 4, 0, 1, 1)
        self.Blurp_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Blurp_2.setFont(font)
        self.Blurp_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Blurp_2.setStyleSheet("QPushButton{\n"
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
        self.Blurp_2.setObjectName("Blurp_2")
        self.gridLayout_4.addWidget(self.Blurp_2, 5, 0, 1, 1)
        self.Blurp = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Blurp.setFont(font)
        self.Blurp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Blurp.setStyleSheet("QPushButton{\n"
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
        self.Blurp.setObjectName("Blurp")
        self.gridLayout_4.addWidget(self.Blurp, 6, 0, 1, 1)
        self.blur = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.blur.setFont(font)
        self.blur.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.blur.setStyleSheet("QPushButton{\n"
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
        self.blur.setObjectName("blur")
        self.gridLayout_4.addWidget(self.blur, 7, 0, 1, 1)
        self.reduceNoiseP = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reduceNoiseP.setFont(font)
        self.reduceNoiseP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reduceNoiseP.setStyleSheet("QPushButton{\n"
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
        self.reduceNoiseP.setObjectName("reduceNoiseP")
        self.gridLayout_4.addWidget(self.reduceNoiseP, 8, 0, 1, 1)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save.setStyleSheet("QPushButton{\n"
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
        self.save.setObjectName("save")
        self.gridLayout_4.addWidget(self.save, 9, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 2, 1)
        self.rotatImage = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_2.addWidget(self.rotatImage, 0, 1, 1, 1)
        self.rotatImage_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rotatImage_2.setFont(font)
        self.rotatImage_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rotatImage_2.setStyleSheet("QPushButton{\n"
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
        self.rotatImage_2.setObjectName("rotatImage_2")
        self.gridLayout_2.addWidget(self.rotatImage_2, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 25))
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
        self.blur.clicked.connect(self.blurIMG)
        self.Blurp.clicked.connect(self.blurpIMG)
        self.reduceNoise.clicked.connect(self.reduceNoiseIMG)
        self.reduceNoiseP.clicked.connect(self.reduceNoisepIMG)
        self.Blurp_2.clicked.connect(self.inversionImage)
        self.rotatImage_2.clicked.connect(self.divideImage)
        self.save.clicked.connect(self.saveImage)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.selectImgBtn.setText(_translate("mainWindow", "Select Image"))
        self.fonte.setText(_translate("mainWindow", "Fx : Fonte"))
        self.relief.setText(_translate("mainWindow", "Fx: Relief"))
        self.reduceNoise.setText(_translate("mainWindow", "Reduce Noise"))
        self.lightIncrease.setText(_translate("mainWindow", "increase Light"))
        self.Blurp_2.setText(_translate("mainWindow", "Inversion"))
        self.Blurp.setText(_translate("mainWindow", "Blur +"))
        self.blur.setText(_translate("mainWindow", "Blur"))
        self.reduceNoiseP.setText(_translate("mainWindow", "Reduce Noise +"))
        self.save.setText(_translate("mainWindow", "Save"))
        self.rotatImage.setText(_translate("mainWindow", "Rotate "))
        self.rotatImage_2.setText(_translate("mainWindow", "Divide Size"))


    def setImage(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Image","","Image Files (*.png *.jpg *.jpeg *.bmp *.pgm)")
        if self.filename:
            self.pixmap = QtGui.QPixmap(self.filename)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)

    def saveImage(self):
        if(hasattr(self, 'filename')):
            self.savedPath = QtWidgets.QFileDialog.getSaveFileName(None,"Save File")
            path = ''
            fileExtension = ''
            if(self.savedPath[0] != ""):
                try:
                    path,fileExtension = self.savedPath[0].split('.')
                except Exception:
                    fileExtension = 'png'
                    path = self.savedPath[0]
                print('file will be saved at :> '+str(path+'.'+fileExtension))
                img1=Image.open(self.filename)
                img1.save(path+'.'+fileExtension)
        else:
            print('importer d\'abord une image')
        
    def rotateImage(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = RotationNB(img1,xsize,ysize) 
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
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
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = deriv1xNB(img1,xsize,ysize)
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
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
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = effetFonteNB(img1,xsize,ysize)
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
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
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = plusClairNB(img1,xsize,ysize)
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")

    def reduceNoiseIMG(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = filtrerMedianImageNB(img1,xsize,ysize,3)
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")

    def reduceNoisepIMG(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = filtrerMedianImageNBVAB(img1,xsize,ysize,3)
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")


    def blurIMG(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size 
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = filtrerImageNB(img1,xsize,ysize,3)
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")


    def blurpIMG(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size 
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)          
            img1 = filtrerImageNBVAB(img1,xsize,ysize,3)
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")

    def divideImage(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)
            img1 = quartImageNB(img1,xsize,ysize) 
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
            self.pixmap = QtGui.QPixmap.fromImage(qim)
            self.pixmap = self.pixmap.scaled(self.imageLbl.width(),self.imageLbl.height(),QtCore.Qt.KeepAspectRatio)
            self.imageLbl.setPixmap(self.pixmap)
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)
        else:
            print("ouvrez une image")

    def inversionImage(self):
        if(hasattr(self, 'filename')):
            img1=Image.open(self.filename)
            (xsize,ysize) = img1.size
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)          
            img1 = inversion_videoNB(img1,xsize,ysize) 
            qim = ImageQt(img1)
            img1.save('temporaryFile/img.png')
            self.filename = 'temporaryFile/img.png'
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

