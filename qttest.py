# -*- coding: utf-8 -*-
# ui与代码分离


import sys

from CAPTCHA import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore


class recognizer(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(recognizer, self).__init__()
        self.setupUi(self)
  #      self.pushButton.clicked.connect(self.showpic)  # 槽函数不用加括号

    def showpic(self):  # 定义槽
        self.originalpic.setPixmap(QtGui.QPixmap('C:/Users/Limbo/Desktop/CK101CAPTCHA/0000_222E.png'))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = recognizer()
    ui.show()
    sys.exit(app.exec_())
