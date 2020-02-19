# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zouban_lesson.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from add_lesson import *
from PyQt5.QtWidgets import QMessageBox

class Ui_Dialog6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(379, 217)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_lesson)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "走班课程数量："))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def add_lesson(self):
        num=self.lineEdit_2.text()
        if num.isdigit()==True:
            add_lesson(num)
            self.success_message()
        else:
            self.show_message()
    def show_message(self):
        QMessageBox.about(self,'Fail!','请在输入框输入数字！')
    def success_message(self):
        QMessageBox.about(self,'success','已成功生成数据！')