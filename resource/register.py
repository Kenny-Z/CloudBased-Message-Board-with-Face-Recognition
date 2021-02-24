# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
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
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/login/bg.png);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 180, 65, 32))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Mongolian Baiti\";\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 106, 32))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Mongolian Baiti\";\n"
"text-decoration: underline;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 300, 92, 32))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Mongolian Baiti\";\n"
"text-decoration: underline;")
        self.label_3.setObjectName("label_3")
        self.name_line = QtWidgets.QLineEdit(Form)
        self.name_line.setGeometry(QtCore.QRect(150, 170, 221, 45))
        self.name_line.setMinimumSize(QtCore.QSize(0, 45))
        self.name_line.setClearButtonEnabled(True)
        self.name_line.setObjectName("name_line")
        self.password_line = QtWidgets.QLineEdit(Form)
        self.password_line.setGeometry(QtCore.QRect(150, 230, 221, 45))
        self.password_line.setMinimumSize(QtCore.QSize(0, 45))
        self.password_line.setClearButtonEnabled(True)
        self.password_line.setObjectName("password_line")
        self.confirm_line = QtWidgets.QLineEdit(Form)
        self.confirm_line.setGeometry(QtCore.QRect(150, 290, 221, 45))
        self.confirm_line.setMinimumSize(QtCore.QSize(0, 45))
        self.confirm_line.setClearButtonEnabled(True)
        self.confirm_line.setObjectName("confirm_line")
        self.registerButton = QtWidgets.QPushButton(Form)
        self.registerButton.setEnabled(False)
        self.registerButton.setGeometry(QtCore.QRect(90, 360, 331, 50))
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
        self.MenuButton = QtWidgets.QPushButton(Form)
        self.MenuButton.setGeometry(QtCore.QRect(10, 70, 150, 50))
        self.MenuButton.setStyleSheet("QPushButton {    \n"
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
        self.MenuButton.setCheckable(True)
        self.MenuButton.setObjectName("MenuButton")
        self.ResetButton = QtWidgets.QPushButton(Form)
        self.ResetButton.setGeometry(QtCore.QRect(170, 70, 150, 50))
        self.ResetButton.setStyleSheet("QPushButton {    \n"
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
        self.ResetButton.setCheckable(False)
        self.ResetButton.setObjectName("ResetButton")
        self.Exit_returnButton = QtWidgets.QPushButton(Form)
        self.Exit_returnButton.setGeometry(QtCore.QRect(340, 70, 150, 50))
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
        self.facialregisterButton = QtWidgets.QPushButton(Form)
        self.facialregisterButton.setEnabled(True)
        self.facialregisterButton.setGeometry(QtCore.QRect(90, 420, 331, 50))
        self.facialregisterButton.setMinimumSize(QtCore.QSize(0, 45))
        self.facialregisterButton.setStyleSheet("QPushButton {    \n"
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
        self.facialregisterButton.setObjectName("facialregisterButton")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.name_line.raise_()
        self.password_line.raise_()
        self.confirm_line.raise_()
        self.registerButton.raise_()
        self.ResetButton.raise_()
        self.Exit_returnButton.raise_()
        self.MenuButton.raise_()
        self.facialregisterButton.raise_()

        self.retranslateUi(Form)
        self.Exit_returnButton.clicked.connect(Form.exit_return)
        self.registerButton.clicked.connect(Form.register)
        self.ResetButton.clicked.connect(Form.reset)
        self.MenuButton.clicked['bool'].connect(self.MenuButton.showMenu)
        self.MenuButton.clicked.connect(Form.showhidemenu)
        self.password_line.textChanged['QString'].connect(Form.enable_register)
        self.name_line.textChanged['QString'].connect(Form.enable_register)
        self.confirm_line.textChanged['QString'].connect(Form.enable_register)
        self.facialregisterButton.clicked.connect(Form.show_facial_register_GUI)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.label_3.setText(_translate("Form", "Confirm:"))
        self.registerButton.setText(_translate("Form", "register"))
        self.MenuButton.setText(_translate("Form", "MENU"))
        self.ResetButton.setText(_translate("Form", "RESET"))
        self.Exit_returnButton.setText(_translate("Form", "RETURN"))
        self.facialregisterButton.setText(_translate("Form", "Facial Register"))
import image_rc
