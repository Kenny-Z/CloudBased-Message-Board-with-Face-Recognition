from PyQt5.Qt import *
from GUI.resource.login import Ui_Form


class LoginPane(QWidget, Ui_Form):

    show_register_GUI_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)
    show_facial_login_GUI_signal = pyqtSignal()
    return_display_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
       super().__init__(parent, *args, **kwargs)
       self.setAttribute(Qt.WA_StyledBackground, True)
       self.setupUi(self)
       #movie = QMovie(":/login/login_gif.gif")
       #movie.setScaledSize(QSize(300, 200))
       #self.login_gif.setMovie(movie)
       #movie.start()

    def show_register_GUI(self):
        #print("register")
        self.show_register_GUI_signal.emit()

    def enable_login(self):
        account =  self.name_comboBox.currentText()
        pwd = self.password_edit.text()
        #print(account, pwd)
        if len(account)>0 and len(pwd)>0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_login(self):
        account = self.name_comboBox.currentText()
        pwd = self.password_edit.text()
        self.check_login_signal.emit(account, pwd)

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom_part)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.login_bottom_part.pos())
        animation.setKeyValueAt(0.2, self.login_bottom_part.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.login_bottom_part.pos())
        animation.setKeyValueAt(0.7, self.login_bottom_part.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.login_bottom_part.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_facial_login_GUI(self):
        self.show_facial_login_GUI_signal.emit()

    def return_display(self):
        self.return_display_signal.emit()

if __name__ == '__main__':
    import sys
    myapp = QApplication(sys.argv)
    window = LoginPane()
    window.return_display_signal.connect(lambda: print("return_display"))
    window.show()
    sys.exit(myapp.exec_())