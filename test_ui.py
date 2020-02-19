import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QFileDialog, QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# 对应父窗口文件
from mainplatform import Ui_MainWindow
# 对应子窗口文件
from k12_stu import Ui_Dialog1
from college_stu import Ui_Dialog2
from teacher import Ui_Dialog3
from room import Ui_Dialog4
from lesson_stu import Ui_Dialog5
from zouban_lesson import Ui_Dialog6
from xingzhengban_lesson import Ui_Dialog7
import os
# 父窗口
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
class Child1(QDialog,Ui_Dialog1):
    def __init__(self):
        super(Child1, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
class Child2(QDialog,Ui_Dialog2):
    def __init__(self):
        super(Child2, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
class Child3(QDialog,Ui_Dialog3):
    def __init__(self):
        super(Child3, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
class Child4(QDialog,Ui_Dialog4):
    def __init__(self):
        super(Child4, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
class Child5(QDialog,Ui_Dialog5):
    def __init__(self):
        super(Child5, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
class Child6(QDialog,Ui_Dialog6):
    def __init__(self):
        super(Child6, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
class Child7(QDialog,Ui_Dialog7):
    def __init__(self):
        super(Child7, self).__init__()
        self.setupUi(self)
    def OPEN(self):
        self.show()
if __name__ =="__main__":
    app = QApplication(sys.argv)
    main = Main()
    ch1 = Child1()
    ch2 = Child2()
    ch3 = Child3()
    ch4 = Child4()
    ch5 = Child5()
    ch6 = Child6()
    ch7 = Child7()
    main.show()
    main.pushButton.clicked.connect(ch1.OPEN)
    main.pushButton_2.clicked.connect(ch2.OPEN)
    main.pushButton_3.clicked.connect(ch3.OPEN)
    main.pushButton_4.clicked.connect(ch4.OPEN)
    main.pushButton_5.clicked.connect(ch5.OPEN)
    main.pushButton_6.clicked.connect(ch6.OPEN)
    main.pushButton_7.clicked.connect(ch7.OPEN)
    sys.exit(app.exec_())
