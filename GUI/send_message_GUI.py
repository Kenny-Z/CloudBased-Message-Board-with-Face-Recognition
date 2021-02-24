from PyQt5.Qt import *
from GUI.resource.send_message import Ui_Form

class SendMessagePane(QWidget, Ui_Form):

    return_personal_signal = pyqtSignal()
    send_name_tel_message_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
       super().__init__(parent, *args, **kwargs)
       self.setAttribute(Qt.WA_StyledBackground, True)
       self.setupUi(self)

    def return_personal(self):
        self.return_personal_signal.emit()

    def check_send(self):
        #print("send")
        message_send = self.Message_send.toPlainText()
        send_to = self.Name_send_to.text()
        self.send_name_tel_message_signal.emit(message_send, send_to)
        em = QErrorMessage(self)
        em.setWindowTitle("success")
        em.showMessage("Success!")
        self.Message_send.clear()
        self.Name_send_to.clear()

    def enable_send(self):
        #print("panding")
        message_send = self.Message_send.toPlainText()
        send_to = self.Name_send_to.text()
        #print(name_send, tel_send, message_send, send_to)
        if len(message_send) > 0 and len(send_to) > 0:
            self.send_message_btn.setEnabled(True)
        else:
            self.send_message_btn.setEnabled(False)

if __name__ == '__main__':
    import sys
    myapp = QApplication(sys.argv)
    window = SendMessagePane()
    window.return_personal_signal.connect(lambda: print("return_personal"))
    window.send_name_tel_message_signal.connect(lambda m, s_t: print(m, s_t))
    window.show()
    sys.exit(myapp.exec_())