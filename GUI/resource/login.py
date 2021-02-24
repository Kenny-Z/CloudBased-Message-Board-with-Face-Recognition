# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(500, 200))
        self.widget.setMaximumSize(QtCore.QSize(500, 200))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_gif = QtWidgets.QLabel(self.widget)
        self.login_gif.setMinimumSize(QtCore.QSize(500, 200))
        self.login_gif.setMaximumSize(QtCore.QSize(500, 200))
        self.login_gif.setStyleSheet("border-image: url(:/login/login_1.jpg);")
        self.login_gif.setText("")
        self.login_gif.setObjectName("login_gif")
        self.horizontalLayout_2.addWidget(self.login_gif, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.widget)
        self.login_bottom_part = QtWidgets.QWidget(Form)
        self.login_bottom_part.setMinimumSize(QtCore.QSize(500, 300))
        self.login_bottom_part.setMaximumSize(QtCore.QSize(500, 300))
        self.login_bottom_part.setStyleSheet("Qweidget#login_bottom_part{\n"
"\n"
"border-image: url(:/register-background/register-background.jpg);\n"
"}")
        self.login_bottom_part.setObjectName("login_bottom_part")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_bottom_part)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.login_bottom_part)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom_part)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(38)
        self.gridLayout.setObjectName("gridLayout")
        self.password_edit = QtWidgets.QLineEdit(self.widget_3)
        self.password_edit.setMinimumSize(QtCore.QSize(0, 45))
        self.password_edit.setStyleSheet("QLineEdit {\n"
"    \n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"     border:none;\n"
"     border-bottom:1px solid lightgray;\n"
"     background-color:transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom-color: rgb(220, 220, 220);\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_edit.setClearButtonEnabled(True)
        self.password_edit.setObjectName("password_edit")
        self.gridLayout.addWidget(self.password_edit, 1, 0, 1, 2)
        self.login_btn = QtWidgets.QPushButton(self.widget_3)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn.setStyleSheet("QPushButton {    \n"
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
"QPushButton:disabled{\n"
"    background-color: rgb(180, 180, 180);\n"
"}")
        self.login_btn.setCheckable(False)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.name_comboBox = QtWidgets.QComboBox(self.widget_3)
        self.name_comboBox.setMinimumSize(QtCore.QSize(0, 45))
        self.name_comboBox.setStyleSheet("QComboBox {\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"     border:none;\n"
"     border-bottom:1px solid lightgray;\n"
"     background-color:transparent;\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom-color: rgb(220, 220, 220);\n"
"}\n"
"QComboBox:focus{\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox::drop-down{\n"
"     border-bottom:transparent;\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: url(:/login/img1.jpg);\n"
"    width:15px;\n"
"    height:20px;\n"
"}")
        self.name_comboBox.setEditable(True)
        self.name_comboBox.setObjectName("name_comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/user1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/user2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_comboBox.addItem(icon1, "")
        self.gridLayout.addWidget(self.name_comboBox, 0, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setStyleSheet("QPushButton {    \n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.login_bottom_part)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/login/img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(1, 6)
        self.verticalLayout.addWidget(self.login_bottom_part)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.show_register_GUI)
        self.name_comboBox.editTextChanged['QString'].connect(Form.enable_login)
        self.password_edit.textChanged['QString'].connect(Form.enable_login)
        self.login_btn.clicked.connect(Form.check_login)
        self.pushButton_3.clicked.connect(Form.show_facial_login_GUI)
        self.pushButton_4.clicked.connect(Form.return_display)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Register"))
        self.login_btn.setText(_translate("Form", "LOGIN"))
        self.pushButton_4.setText(_translate("Form", "Return"))
        self.name_comboBox.setItemText(0, _translate("Form", "haiyu"))
        self.name_comboBox.setItemText(1, _translate("Form", "yige"))
        self.pushButton_3.setText(_translate("Form", "Face Login"))
import image_rc
