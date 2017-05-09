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
        self.centralwidget.setObjectName("centralwidget")
        self.originalpic = QtWidgets.QLabel(self.centralwidget)
        self.originalpic.setGeometry(QtCore.QRect(320, 200, 120, 40))
        self.originalpic.setText("")
        self.originalpic.setObjectName("originalpic")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(630, 490, 112, 34))
        self.Quit.setObjectName("Quit")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(330, 300, 81, 18))
        self.result.setText("")
        self.result.setObjectName("result")
        self.rec = QtWidgets.QPushButton(self.centralwidget)
        self.rec.setGeometry(QtCore.QRect(470, 300, 112, 34))
        self.rec.setObjectName("rec")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.rec.setText(_translate("MainWindow", "Recognize"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.fileopen.setText(_translate("MainWindow", "打开"))
        self.fileopen.setToolTip(_translate("MainWindow", "打开"))

