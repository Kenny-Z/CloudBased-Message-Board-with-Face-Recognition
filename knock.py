import cv2
import face_recognition
from get_url import SMMS
import os


class Knockknock():
    def __init__(self):
        self.smms = SMMS('Huey', 'ahgyzhy168')

    def knockmsg(self):
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, frame = capture.read()
        locations = face_recognition.face_locations(frame)  # get face location
        for face_location in locations:  # get 4 coordinates of face
            top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]  # crop the image

        cv2.imwrite('capture.jpg', face_image)  # save face
        self.smms.upload_image(r'capture.jpg')
        os.remove('capture.jpg')
        capture.release()
        cv2.destroyAllWindows()
        # return True

#
# if __name__ == '__main__':
#     Knock = Knockknock()
#     Knock.knockmsg()
