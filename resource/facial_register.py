# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facial_register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        self.registerButton = QtWidgets.QPushButton(Form)
        self.registerButton.setEnabled(False)
        self.registerButton.setGeometry(QtCore.QRect(100, 370, 300, 50))
        self.registerButton.setMinimumSize(QtCore.QSize(0, 45))
        self.registerButton.setStyleSheet("QPushButton {    \n"
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
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(180, 180, 180);\n"
"}")
        self.registerButton.setObjectName("registerButton")
        self.facialreturn = QtWidgets.QPushButton(Form)
        self.facialreturn.setGeometry(QtCore.QRect(100, 430, 300, 50))
        self.facialreturn.setMinimumSize(QtCore.QSize(0, 50))
        self.facialreturn.setStyleSheet("QPushButton {    \n"
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
        self.facialreturn.setObjectName("facialreturn")

        self.retranslateUi(Form)
        self.facialreturn.clicked.connect(Form.return_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.registerButton.setText(_translate("Form", "Facial Register"))
        self.facialreturn.setText(_translate("Form", "Return"))
