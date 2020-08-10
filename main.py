# -*- coding: utf-8 -*-
"""
 Amharic OCR UI made on the top of Tesseract engine, Python-opencv and PYQT5 library
 Author - Tesfamichael Molla ( TME Education ambassador in Ethiopia )
 email -  hope.miky1074@gmail.com 

 I have used tesseract engine located in the project root directory ./Tesseract-OCR which can be 
 downloaded here -> https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe 
 Opencv is used to load the image and to do some preprocessing on the image. Opencv can be installed using -> pip install python-opencv
 Pytesseract is used to connect the python script to the tesseract engine and can be installed using -> pip install pytesseract
 The GUI is made using PYQT5 library which can be installed using -> pip install PyQt5
 Amharic fonts are unique in their brhaviours so i have used a custom font which can be found https://software.sil.org/abyssinica/
 
"""

#  Importing libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit, QFileDialog
import cv2
import numpy as np
import pytesseract
import io 
from PIL import ImageFont, ImageDraw, Image

# Setting tesseract cmd installation file path, this will be flexible based on your installation location.
pytesseract.pytesseract.tesseract_cmd=r"Tesseract-OCR\\tesseract.exe"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Init declaration for the UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_realimage = QtWidgets.QLabel(self.centralwidget)
        self.label_realimage.setGeometry(QtCore.QRect(10, 20, 561, 611))
        self.label_realimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_realimage.setObjectName("label_realimage")
        self.label_resultimage = QtWidgets.QLabel(self.centralwidget)
        self.label_resultimage.setGeometry(QtCore.QRect(610, 20, 561, 611))
        self.label_resultimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultimage.setObjectName("label_resultimage")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 650, 581, 211))
        self.groupBox.setObjectName("groupBox")
        self.btn_chooseimage = QtWidgets.QPushButton(self.groupBox)
        self.btn_chooseimage.setGeometry(QtCore.QRect(120, 90, 121, 23))
        self.btn_chooseimage.setObjectName("btn_chooseimage")
         
        self.btn_boundingboxes = QtWidgets.QPushButton(self.groupBox)
        self.btn_boundingboxes.setGeometry(QtCore.QRect(120, 150, 121, 23))
        self.btn_boundingboxes.setObjectName("btn_boundingboxes")
        self.btn_generatetext = QtWidgets.QPushButton(self.groupBox)
        self.btn_generatetext.setGeometry(QtCore.QRect(350, 90, 121, 23))
        self.btn_generatetext.setObjectName("btn_generatetext")
        self.btn_translate = QtWidgets.QPushButton(self.groupBox)
        self.btn_translate.setGeometry(QtCore.QRect(350, 150, 121, 23))
        self.btn_translate.setObjectName("btn_translate")
        self.btn_proceed = QtWidgets.QPushButton(self.groupBox)
        self.btn_proceed.setGeometry(QtCore.QRect(150, 40, 251, 23))
        self.btn_proceed.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_proceed.setCheckable(False)
        self.btn_proceed.setDefault(False)
        self.btn_proceed.setFlat(False)
        self.btn_proceed.setObjectName("btn_proceed")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(130, 120, 111, 16))
        self.label_3.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(360, 120, 141, 16))
        self.label_4.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(360, 180, 121, 16))
        self.label_5.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(130, 180, 111, 16))
        self.label_6.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_6.setObjectName("label_6")
        self.spinBox_fontsize = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_fontsize.setGeometry(QtCore.QRect(470, 40, 42, 22))
        self.spinBox_fontsize.setProperty("value", 15)
        self.spinBox_fontsize.setObjectName("spinBox_fontsize")
        self.spinBox_fontsize.valueChanged.connect(self.fontchanged)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(420, 40, 41, 21))
        self.label_7.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_7.setObjectName("label_7")
        self.textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit.setGeometry(QtCore.QRect(650, 660, 531, 201))
        self.textedit.setObjectName("textedit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Setting some variables we are going to use
        self.filepath = ""     # Holds the file path for image
        self.fontsize = 15     # Intial font size to be displayed on the result image 
        self.text = ""         # Text to be assigned to the TextEdit Widget from the result of tesseract
        self.image = None      # Holds the opencv Iamage read from the filepath
        self.resultimage = None     # Holds the result image form tesseract
        self.btn_chooseimage.clicked.connect(self.showDialog)               # Assigning a method for a click action on the button Widget
        self.btn_proceed.clicked.connect(self.generateText)
        self.btn_generatetext.clicked.connect(self.assignText)
        self.btn_boundingboxes.clicked.connect(self.generatBoundingBox)
        self.btn_translate.clicked.connect(self.translateText)

        self.btn_boundingboxes.setDisabled(True)                             # Disabling buttons until the user choose an image
        self.btn_generatetext.setDisabled(True)
        self.btn_translate.setDisabled(True)

    
    # Open File dialog box with some filtering options and siplay an error if the its canceled
    def showDialog(self):
        options = QFileDialog.Options()
        fname, ok = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Image Files (*.jpg *.png *.jpeg *.PNG)", options=options)
        if ok:
            self.filepath = fname
            self.show_image()
            self.btn_boundingboxes.setDisabled(False)
            self.btn_generatetext.setDisabled(False)
            self.btn_translate.setDisabled(False)
        else:
            self.disperrmessage("FileName Error", "Please choos an image again.")
    
    def fontchanged(self):
        self.fontsize = int(self.spinBox_fontsize.value())

    # Generate an output image and a text from the source image and display it on another label Widget
    def generateText(self):
        if len(self.filepath) > 0:
            try:
                self.text = ""
                img = cv2.imread(self.filepath)
                grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                imgh, imgw = grey.shape
                self.resultimage = np.zeros((imgh, imgw, 3), np.uint8)
                text = pytesseract.image_to_data(img, lang="amh")
                imgpil = Image.fromarray(self.resultimage)
                draw = ImageDraw.Draw(imgpil)
                font = ImageFont.truetype(".\\fonts\\AbyssinicaSIL-Regular.ttf", self.fontsize)

                for x, i in enumerate(text.splitlines()):
                    if x != 0 and len(i.split()) == 12:
                        i = i.split()
                        self.text += i[11] + " "
                        x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
                        draw.text((x,y), i[11], fill=(255,255,255,0), font=font)


                self.resultimage = np.array(imgpil)
                self.show_resultimage()
            except:
                self.disperrmessage("Runtime Error" , "please try again")
        else:
            self.disperrmessage("Idle image Error" , "Please choose an image first")
    
    # To be done for future / Just displaying a messageBox Widget
    def translateText(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This feature not available for this version")
        msg.setWindowTitle("Feature")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    # Display error messages on a messageBox Widget
    def disperrmessage(self, tittle, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(tittle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    # Draw a bounding box arround the detected texts and display it 
    def generatBoundingBox(self):
        try:
            img = cv2.imread(self.filepath)
            text = pytesseract.image_to_data(img, lang="amh")
            for x, i in enumerate(text.splitlines()):
                
                if x != 0 and len(i.split()) == 12:
                    i = i.split()
                    x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
            
            cv2.imshow("Bounding boxes", img)
        except:
            self.disperrmessage("Error" , "Please try again or restart the app")

    def assignText(self):
        try:
            fontdb = QFontDatabase()
            fontdb.addApplicationFont(".\\AbyssinicaSIL-Regular.ttf")
            font  = QFont("Abyssinica SIL", 10, 1)
            self.textedit.setFont(font)
            self.textedit.setText(self.text)
        except:
            self.disperrmessage("Error" , "Please try again or restart the app")

    @QtCore.pyqtSlot()
    def show_image(self):
        self.image = cv2.imread(self.filepath)
        self.image = cv2.resize(self.image, (500,800))
        self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_realimage.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.label_realimage.setScaledContents(True)
        

    @QtCore.pyqtSlot()
    def show_resultimage(self):
        self.resultimage = cv2.resize(self.resultimage, (500,800))
        self.resultimage = QtGui.QImage(self.resultimage.data, self.resultimage.shape[1], self.resultimage.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_resultimage.setPixmap(QtGui.QPixmap.fromImage(self.resultimage))
        self.label_resultimage.setScaledContents(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Amharic OCR"))
        self.label_realimage.setText(_translate("MainWindow", "Real Image"))
        self.label_resultimage.setText(_translate("MainWindow", "Result image"))
        self.groupBox.setTitle(_translate("MainWindow", "ToolBox"))
        self.btn_chooseimage.setText(_translate("MainWindow", "Choose image"))
        self.btn_boundingboxes.setText(_translate("MainWindow", "Bounding boxes"))
        self.btn_generatetext.setText(_translate("MainWindow", "Generat text"))
        self.btn_translate.setText(_translate("MainWindow", "Translate to English"))
        self.btn_proceed.setText(_translate("MainWindow", "Proceed"))
        self.label_3.setText(_translate("MainWindow", "choose image from file"))
        self.label_4.setText(_translate("MainWindow", "Generate text from image"))
        self.label_5.setText(_translate("MainWindow", "Translate text to English"))
        self.label_6.setText(_translate("MainWindow", "Show areas with texts"))
        self.label_7.setText(_translate("MainWindow", "Font size"))




app = QApplication(sys.argv)
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())