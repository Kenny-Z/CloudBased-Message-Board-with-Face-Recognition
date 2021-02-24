# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_message.ui'
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
"    border-image: url(:/login/after_login.JPG);\n"
"}")
        self.Exit_returnButton = QtWidgets.QPushButton(Form)
        self.Exit_returnButton.setGeometry(QtCore.QRect(680, 430, 250, 50))
        self.Exit_returnButton.setStyleSheet("QPushButton {    \n"
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
        self.Exit_returnButton.setCheckable(False)
        self.Exit_returnButton.setObjectName("Exit_returnButton")
        self.send_message_btn = QtWidgets.QPushButton(Form)
        self.send_message_btn.setEnabled(False)
        self.send_message_btn.setGeometry(QtCore.QRect(80, 430, 250, 50))
        self.send_message_btn.setStyleSheet("QPushButton {    \n"
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
        self.send_message_btn.setObjectName("send_message_btn")
        self.Message_send = QtWidgets.QTextEdit(Form)
        self.Message_send.setGeometry(QtCore.QRect(80, 170, 851, 231))
        self.Message_send.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.Message_send.setObjectName("Message_send")
        self.Name_send_to = QtWidgets.QLineEdit(Form)
        self.Name_send_to.setGeometry(QtCore.QRect(190, 100, 200, 50))
        self.Name_send_to.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Name_send_to.setObjectName("Name_send_to")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 91, 32))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Mongolian Baiti\";\n"
"text-decoration: underline;")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.Exit_returnButton.clicked.connect(Form.return_personal)
        self.send_message_btn.clicked.connect(Form.check_send)
        self.Message_send.textChanged.connect(Form.enable_send)
        self.Name_send_to.textChanged['QString'].connect(Form.enable_send)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Exit_returnButton.setText(_translate("Form", "RETURN"))
        self.send_message_btn.setText(_translate("Form", "Send"))
        self.label_3.setText(_translate("Form", "Send To:"))
import image_rc
