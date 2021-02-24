from PyQt5.Qt import *
from GUI.resource.register import Ui_Form
from signup import Signup
from Database import DB


class RegisterPane(QWidget, Ui_Form):

    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str, str)
    show_facial_register_GUI_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
       super().__init__(parent, *args, **kwargs)
       self.setAttribute(Qt.WA_StyledBackground, True)
       self.setupUi(self)

       self.animation_targets = [self.ResetButton,self.Exit_returnButton]
       self.animation_targets_pos = [target.pos()for target in self.animation_targets]

    def showhidemenu(self, checked):
        #print("show & hide", checked)
        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            #if not checked:
            animation.setStartValue(self.MenuButton.pos())
            animation.setEndValue(self.animation_targets_pos[idx])
            #else:
             #   animation.setEndValue(self.MenuButton.pos())
             #   animation.setStartValue(self.animation_targets_pos[idx])
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation_group.addAnimation(animation)
        animation_group.setDirection(checked)

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def reset(self):
        #print("reset")
        self.name_line.clear()
        self.password_line.clear()
        self.confirm_line.clear()

    def exit_return(self):
        self.exit_signal.emit()

    def enable_register(self):
        name_text = self.name_line.text()
        password_text = self.password_line.text()
        confirm_text = self.confirm_line.text()
        if len(name_text) > 0 and len(password_text) > 0 and len(confirm_text) > 0 and password_text == confirm_text:
            self.facialregisterButton.setEnabled(True)
        else:
            self.facialregisterButton.setEnabled(False)

    def capture_register(self):
        self.show_facial_register_GUI_signal.emit()
        name_text = self.name_line.text()
        password_text = self.password_line.text()
        self.register_account_pwd_signal.emit(name_text, password_text)
        DATABASE = DB()
        signup = Signup()
        face, facecode = signup.get_face()
        DATABASE.registration(name_text, 'student', facecode, password_text)

        em = QErrorMessage(self)
        em.setWindowTitle("success")
        em.showMessage("Success!")


if __name__ == '__main__':
    import sys
    myapp = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda: print("return"))
    window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show_facial_register_GUI_signal.connect(lambda: print("show0"))
    window.show()
    sys.exit(myapp.exec_())