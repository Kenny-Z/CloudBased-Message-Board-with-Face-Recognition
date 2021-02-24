# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        Form.setMinimumSize(QtCore.QSize(1024, 600))
        Form.setMaximumSize(QtCore.QSize(1024, 600))
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/login/main.jpg);\n"
"}")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(80, 150, 851, 231))
        self.textEdit.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 420, 200, 80))
        self.pushButton_4.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 16pt \"MV Boli\";\n"
"    border-radius: 25px; \n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(0,0,0);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(0,0,0);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.diaplay_login = QtWidgets.QPushButton(Form)
        self.diaplay_login.setGeometry(QtCore.QRect(520, 420, 200, 80))
        self.diaplay_login.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 16pt \"MV Boli\";\n"
"    border-radius: 25px; \n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(0,0,0);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(255,255,255);\n"
"  \n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(0,0,0);\n"
"}\n"
"")
        self.diaplay_login.setCheckable(False)
        self.diaplay_login.setObjectName("diaplay_login")

        self.retranslateUi(Form)
        self.diaplay_login.clicked.connect(Form.show_login_GUI)
        self.pushButton_4.clicked.connect(Form.image)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "Knock Knock!!"))
        self.diaplay_login.setText(_translate("Form", "Login"))
import image_rc
