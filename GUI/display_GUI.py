from PyQt5.Qt import *
from GUI.resource.display import Ui_Form
from Database import DB
from knock import Knockknock


class DisplayPane(QWidget, Ui_Form):

    show_login_GUI_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def show_login_GUI(self):
        self.show_login_GUI_signal.emit()

    def image(self):
        knock = Knockknock()
        knock.knockmsg()
        em = QErrorMessage(self)
        em.setWindowTitle("success")
        em.showMessage("Success!")

    def refresh_msgs(self):
        database = DB()
        display = database.message_looking('all')
        self.textEdit.setPlainText(display)


if __name__ == '__main__':
    import sys
    myapp = QApplication(sys.argv)
    window = DisplayPane()
    window.show()
    sys.exit(myapp.exec_())