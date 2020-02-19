# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'k12_stu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from add_k12_stu import *


class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 288)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 81, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 91, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 121, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 91, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 180, 91, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_stu)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请选择学段："))
        self.comboBox.setItemText(0, _translate("Dialog", "小学"))
        self.comboBox.setItemText(1, _translate("Dialog", "初中"))
        self.comboBox.setItemText(2, _translate("Dialog", "高中"))
        self.label_3.setText(_translate("Dialog", "班级数量："))
        self.label_4.setText(_translate("Dialog", "每个班级的学生数："))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def add_stu(self):
        xueduan=self.comboBox.currentText()#获取下拉选择列表选中的学段
        class_num=self.lineEdit_2.text()#获取输入的班级数量
        ave_stu=self.lineEdit_3.text()#获取输入的每个班级的学生数
        if class_num.isdigit()==True and ave_stu.isdigit()==True:#判断输入框输入是否为数字
            add_k12_stu(xueduan,class_num,ave_stu)#将窗口输入的信息传入相应的处理函数，生成excel数据
            self.success_message()#成功生成数据的提示信息
        else:
            self.show_message()#输入框未输入数字的提示信息
    def show_message(self):
        QMessageBox.about(self,'Fail!','请在输入框输入数字！')
    def success_message(self):
        QMessageBox.about(self,'success','已成功生成数据！')



