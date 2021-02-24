from PyQt5.Qt import *
from GUI.resource.personal import Ui_Form
from Database import DB
import signup

class PersonalPane(QWidget, Ui_Form):

    logout_pane_signal = pyqtSignal()
    show_send_message_GUI_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
       super().__init__(parent, *args, **kwargs)
       self.setAttribute(Qt.WA_StyledBackground, True)
       self.setupUi(self)

    def logout_pane(self):
        self.logout_pane_signal.emit()

    def send_button(self):
        self.show_send_message_GUI_signal.emit()

    def refresh_show(self):
        message_type = self.comboBox.currentText()
        self.pushButton.setText(message_type)
        database = DB()
        print(signup.login_user)
        if message_type == 'Personal':
            display = database.message_looking(signup.login_user)
            self.textEdit.setPlainText(display)
        if message_type == 'Group':
            display = database.group_message_looking(signup.login_user)
            self.textEdit.setPlainText(display)
        if message_type == 'ALL':
            display = database.message_looking('all')
            self.textEdit.setPlainText(display)



if __name__ == '__main__':
    import sys
    myapp = QApplication(sys.argv)
    window = PersonalPane()
    window.logout_pane_signal.connect(lambda: print("logout"))
    window.show()
    sys.exit(myapp.exec_())