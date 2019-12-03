# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:37:42 2019

@author: Helen
"""
import sys
import os
import cv2 as cv
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtGui
import matplotlib.pyplot as plt

myfile = "loadImage.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(myfile)
#current_filename=''


class HelenApp(QMainWindow):
  def __init__(self):
    super(HelenApp, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.openImage.clicked.connect(self.openImagefile)
    self.ui.saveImage.clicked.connect(self.saveImage)
    self.ui.ok.clicked.connect(self.okfunc)
    self.ui.cancel.clicked.connect(self.cancel)
    self.ui.deepLabV3.clicked.connect(self.DeepLabV3plus)
    
  def okfunc(self):
    self.close()
  def cancel(self):
    self.close()
  
  
  # function show Image to LbImage(QLabel)
  def showImage2LbImage(self, LabelImage, filename): # hàm showImage2LbImage có 2 biến LableImage and filename
    # LabelImage: Name of created label 
    # filename: link to file name

    pixmap = QPixmap(filename)      
    LabelImage.setAlignment(QtCore.Qt.AlignCenter)   
    LabelImage.setPixmap(pixmap.scaled(LabelImage.size(),QtCore.Qt.KeepAspectRatio))    
    LabelImage.show() 
    
    
  def openImagefile(self):
    global filename
    filename, _ = QFileDialog.getOpenFileName(self, 'open file') 
    # dấu phẩy và gạch ngang (,_) nghĩa là chỉ lấy 1 biến đầu và ko lấy biến sau
    self.showImage2LbImage(self.ui.imagebox, filename)
    
    #get image name to for saveImage func
    filePath = str(filename)
    fileObject = filePath.split('/')
    global imageName
    imageName = fileObject[ len(fileObject) - 1 ]
    print(imageName)
      
  def DeepLabV3plus(self):
    self.showImage2LbImage(self.ui.segmentation_box, filename)
    
  def saveImage(self):
    savefile, _ = QFileDialog.getSaveFileName(self, "Save Image", imageName)
    pixmap = QPixmap(filename)
    pixmap.save(savefile, "JPG")
    
    
if __name__== "__main__":
  app = QApplication(sys.argv)
  window = HelenApp()
  window.show()
  sys.exit(app.exec_())