# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personal.ui'
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
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(80, 180, 871, 221))
        self.listView.setObjectName("listView")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 120, 231, 41))
        self.comboBox.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.send_btn = QtWidgets.QPushButton(Form)
        self.send_btn.setGeometry(QtCore.QRect(80, 440, 250, 50))
        self.send_btn.setStyleSheet("QPushButton {    \n"
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
        self.send_btn.setObjectName("send_btn")
        self.logout_btn = QtWidgets.QPushButton(Form)
        self.logout_btn.setGeometry(QtCore.QRect(700, 440, 250, 50))
        self.logout_btn.setStyleSheet("QPushButton {    \n"
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
        self.logout_btn.setObjectName("logout_btn")

        self.retranslateUi(Form)
        self.logout_btn.clicked.connect(Form.logout_pane)
        self.send_btn.clicked.connect(Form.send_button)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "ALL"))
        self.comboBox.setItemText(1, _translate("Form", "Group"))
        self.comboBox.setItemText(2, _translate("Form", "Personal"))
        self.send_btn.setText(_translate("Form", "Send"))
        self.logout_btn.setText(_translate("Form", "log out"))
import image_rc
