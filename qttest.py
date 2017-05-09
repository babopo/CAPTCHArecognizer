# -*- coding: utf-8 -*-
# ui与代码分离


import sys

import main
from CAPTCHA import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore


Openfile = ''  # 全局变量储存打开的文件路径

class recognizer(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(recognizer, self).__init__()
        self.setupUi(self)
        self.fileopen.triggered.connect(self.showpic)
  #      self.pushButton.clicked.connect(self.showpic)  # 槽函数不用加括号

    def showpic(self):  # 定义槽
        global Openfile
        file, ok = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)
        self.originalpic.setPixmap(QtGui.QPixmap(file))
        Openfile = file

    def recognize(self):
        text = main.recognize(Openfile)
        self.result.setText(text)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = recognizer()
    ui.show()
    sys.exit(app.exec_())
