# -*- coding: utf-8 -*-
# ui与代码分离


import sys
import os

import main
import QtTools
from CAPTCHA import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore


Openfile = ''  # 全局变量记录打开的文件路径
text1 = ''  # 记录识别结果


class recognizer(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(recognizer, self).__init__()
        self.setupUi(self)
        self.fileopen.triggered.connect(self.showpic)
        # self.pushButton.clicked.connect(self.showpic)  # 槽函数不用加括号

        # Label字体设置
        self.result.setFont(QtGui.QFont("Roman times", 15, QtGui.QFont.Bold))
        self.revise.setFont(QtGui.QFont("Roman times", 15, QtGui.QFont.Bold))
        self.result.setAlignment(QtCore.Qt.AlignCenter)  # 文字居中
        self.revise.setAlignment(QtCore.Qt.AlignCenter)

    def showpic(self):  # 定义槽 打开图片
        global Openfile
        file, ok = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)
        self.originalpic.setPixmap(QtGui.QPixmap(file).scaled(self.originalpic.size()))  # 显示图片自适应窗口大小
        Openfile = file

    def recognize(self):  # 连接识别程序
        global text1
        text1 = main.recognize(Openfile)  # 识别结果
        self.result.setText(text1)
        text2num, text2 = QtTools.get_name(Openfile)  # 标注结果
        self.revise.setText(text2)

    def updaterevise(self):  # 更新标注信息
        global Openfile
        temp = Openfile.split('_')[0]
        newname = temp + '_' + text1 + '.png'
        Openfile = newname  # 更新打开路径
        os.rename(Openfile, newname)
        QtWidgets.QMessageBox.information(self, "Info", "Update success")  # 运行成功弹窗


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = recognizer()
    ui.show()
    sys.exit(app.exec_())
