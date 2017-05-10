# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAPTCHA.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(630, 490, 112, 34))
        self.Quit.setObjectName("Quit")
        self.ImgShow = QtWidgets.QGroupBox(self.centralwidget)
        self.ImgShow.setGeometry(QtCore.QRect(240, 10, 281, 151))
        self.ImgShow.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.ImgShow.setObjectName("ImgShow")
        self.originalpic = QtWidgets.QLabel(self.ImgShow)
        self.originalpic.setGeometry(QtCore.QRect(10, 30, 261, 101))
        self.originalpic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.originalpic.setText("")
        self.originalpic.setObjectName("originalpic")
        self.REC = QtWidgets.QGroupBox(self.centralwidget)
        self.REC.setGeometry(QtCore.QRect(240, 200, 281, 301))
        self.REC.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.REC.setObjectName("REC")
        self.result = QtWidgets.QLabel(self.REC)
        self.result.setGeometry(QtCore.QRect(20, 50, 241, 61))
        self.result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.result.setText("")
        self.result.setObjectName("result")
        self.rec = QtWidgets.QPushButton(self.REC)
        self.rec.setGeometry(QtCore.QRect(80, 120, 112, 34))
        self.rec.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 9pt \"Microsoft YaHei UI\";")
        self.rec.setObjectName("rec")
        self.revise = QtWidgets.QLabel(self.REC)
        self.revise.setGeometry(QtCore.QRect(20, 190, 241, 61))
        self.revise.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.revise.setText("")
        self.revise.setObjectName("revise")
        self.label = QtWidgets.QLabel(self.REC)
        self.label.setGeometry(QtCore.QRect(110, 30, 81, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.REC)
        self.label_2.setGeometry(QtCore.QRect(100, 170, 81, 18))
        self.label_2.setObjectName("label_2")
        self.update = QtWidgets.QPushButton(self.REC)
        self.update.setGeometry(QtCore.QRect(80, 260, 112, 34))
        self.update.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 9pt \"Microsoft YaHei UI\";")
        self.update.setObjectName("update")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileopen = QtWidgets.QAction(MainWindow)
        self.fileopen.setObjectName("fileopen")
        self.menu.addAction(self.fileopen)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.Quit.clicked.connect(MainWindow.close)
        self.rec.clicked.connect(MainWindow.recognize)
        self.update.clicked.connect(MainWindow.updaterevise)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CAPTCHArecognizer"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.ImgShow.setTitle(_translate("MainWindow", "ImgShow"))
        self.REC.setTitle(_translate("MainWindow", "Recognize"))
        self.rec.setText(_translate("MainWindow", "Recognize"))
        self.label.setText(_translate("MainWindow", "Result"))
        self.label_2.setText(_translate("MainWindow", "MarkInfo"))
        self.update.setText(_translate("MainWindow", "Update"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.fileopen.setText(_translate("MainWindow", "Open"))
        self.fileopen.setToolTip(_translate("MainWindow", "Open"))

