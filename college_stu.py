# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'college_stu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from add_college_stu import *
from PyQt5.QtWidgets import QMessageBox

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(377, 364)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 54, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 54, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 91, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 100, 91, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 170, 91, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 111, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 250, 91, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(274, 312, 81, 31))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_stu)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "学院数："))
        self.label_2.setText(_translate("Dialog", "专业数："))
        self.label_3.setText(_translate("Dialog", "班级数："))
        self.label_4.setText(_translate("Dialog", "每个班级的学生数："))
        self.pushButton.setText(_translate("Dialog", "ok"))

    def add_stu(self):
        academy_num=self.lineEdit.text()
        major_num=self.lineEdit_2.text()
        class_num=self.lineEdit_3.text()
        num=self.lineEdit_4.text()
        if academy_num.isdigit()==True and major_num.isdigit()==True and class_num.isdigit()==True and num.isdigit()==True:
            add_college_stu(academy_num,major_num,class_num,num)
            self.success_message()
        else:
            self.show_message()
    def show_message(self):
        QMessageBox.about(self,'Fail!','请在输入框输入数字！')
    def success_message(self):
        QMessageBox.about(self,'success','已成功生成数据！')