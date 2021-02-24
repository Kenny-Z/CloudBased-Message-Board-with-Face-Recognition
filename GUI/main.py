from login_GUI import LoginPane
from register_GUI import RegisterPane
from display_GUI import DisplayPane
from facial_login_GUI import FacialLoginPane
from personal_GUI import PersonalPane
from send_message_GUI import SendMessagePane
from Database import DB
import signup


from PyQt5.Qt import *

if __name__ == '__main__':
    global login_user
    import sys
    app = QApplication(sys.argv)

    display_pane = DisplayPane()

    login_pane = LoginPane(display_pane)
    login_pane.move(265, display_pane.height())
    login_pane.show()

    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()

    facial_login_pane = FacialLoginPane(login_pane)
    facial_login_pane.move(0, login_pane.height())
    facial_login_pane.show()

    personal_pane = PersonalPane()

    send_message_pane = SendMessagePane()

    def exit_signal_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(), 0))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)


    def return_display_pane():
        animation = QPropertyAnimation(login_pane)
        animation.setTargetObject(login_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(265, 50))
        animation.setEndValue(QPoint(display_pane.width(), 50))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def return_login_signal_pane():
        animation = QPropertyAnimation(facial_login_pane)
        animation.setTargetObject(facial_login_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(), 0))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def return_personal_pane():
        send_message_pane.hide()
        personal_pane.show()

    def logout_pane():
        personal_pane.hide()
        login_pane.show()

    def show_login_GUI_signal():
        #print("show1")
        animation = QPropertyAnimation(login_pane)
        animation.setTargetObject(login_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(265, display_pane.height()))
        animation.setEndValue(QPoint(265, 50))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_register_GUI_signal():
        #print("show2")
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, login_pane.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_facial_login_GUI_signal():
        #print("show4")
        animation = QPropertyAnimation(facial_login_pane)
        animation.setTargetObject(facial_login_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, login_pane.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_send_message_GUI_signal():
        send_message_pane.show()
        personal_pane.hide()

    def check_login(account, pwd):
        DATABASE = DB()
        password = DATABASE.password_looking(account)[0]
        print(account)
        print(password)
        if pwd == password:
            #print("login")
            signup.login_user = account
            print(signup.login_user)
            personal_pane.show()
            login_pane.hide()


        else:
            login_pane.show_error_animation()



    def show_personal_GUI_signal():
        personal_pane.show()
        login_pane.hide()

    display_pane.show_login_GUI_signal.connect(show_login_GUI_signal)

    register_pane.exit_signal.connect(exit_signal_pane)
    register_pane.register_account_pwd_signal.connect(lambda name_text, password_text: print(name_text, password_text))

    login_pane.show_register_GUI_signal.connect(show_register_GUI_signal)
    login_pane.check_login_signal.connect(check_login)
    login_pane.show_facial_login_GUI_signal.connect(show_facial_login_GUI_signal)
    login_pane.return_display_signal.connect(return_display_pane)


    facial_login_pane.return_login_signal.connect(return_login_signal_pane)
    facial_login_pane.show_personal_GUI_signal.connect(show_personal_GUI_signal)

    personal_pane.logout_pane_signal.connect(logout_pane)
    personal_pane.show_send_message_GUI_signal.connect(show_send_message_GUI_signal)

    send_message_pane.return_personal_signal.connect(return_personal_pane)
    send_message_pane.send_name_tel_message_signal.connect(lambda message_send, send_to: print(message_send, send_to))

    display_pane.show()
    sys.exit(app.exec_())