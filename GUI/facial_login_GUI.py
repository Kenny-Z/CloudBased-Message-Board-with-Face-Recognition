from PyQt5.Qt import *
from GUI.resource.facial_login import Ui_Form
from PyQt5 import QtGui
from signup import Login
import cv2


class FacialLoginPane(QWidget, Ui_Form):

    return_login_signal = pyqtSignal()
    show_personal_GUI_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
       super().__init__(parent, *args, **kwargs)
       self.setAttribute(Qt.WA_StyledBackground, True)
       self.setupUi(self)

    def return_login(self):
        self.return_login_signal.emit()

    def show_image(self):
        login = Login()
        face = login.get_face()
        cv2.imwrite('face_img.png', face)
        self.label.setPixmap(QtGui.QPixmap('face_img.png'))
        self.label.setScaledContents(True)

    def show_logged(self):

        # imgName, imgType = QFileDialog.getOpenFileName(self, "OpenImage", "", "*.jpg;;*.png;;All Files(*)")
        # jpg = QtGui.QPixmap(imgName)
        # self.label.setPixmap(jpg)
        login = Login()
        face = cv2.imread('face_img.png')
        # cv2.imshow('', face)
        # cv2.waitKey(0)
        status = 0
        [possible_name, id, status] = login.compare(face)
        print(status)
        if status == 0:
            print("fail")
            em = QErrorMessage(self)
            em.setWindowTitle("Failure")
            em.showMessage("Failure!")
        else:
            print("success")
            em = QErrorMessage(self)
            em.setWindowTitle("Success!")
            em.showMessage("Welcome")

            self.show_personal_GUI_signal.emit()


if __name__ == '__main__':
    import sys
    myapp = QApplication(sys.argv)
    window = FacialLoginPane()
    window.return_login_signal.connect(lambda: print("return1"))
    window.show()
    sys.exit(myapp.exec_())