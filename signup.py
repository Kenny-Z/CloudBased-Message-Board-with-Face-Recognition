import cv2
import face_recognition
import numpy
from Database import DB
login_user = ''


class Signup:
    def __init__(self):
        pass

    def get_face(self):
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # open default camera and
        ret, frame = capture.read()  # get one frame
        for face_location in face_recognition.face_locations(frame):
            top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]
        print(face_recognition.face_encodings(face_image))
        face_encoding = face_recognition.face_encodings(face_image)[0]  # get face encode
        print(face_encoding.size)
        return face_image, face_encoding

    def get_name(self):
        known_face_names = input("Please input your name:")
        return known_face_names

    def get_group(self):
        known_face_group= input("Please input your group:")
        return known_face_group


class Login:
    def __init__(self):
        self.Database = DB()

    def get_face(self):
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # open default camera and
        ret, frame = capture.read()  # get one frame
        for face_location in face_recognition.face_locations(frame):
            top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]
        # print(face_recognition.face_encodings(face_image))

        # print(self.face_encoding.size)
        return face_image

    def compare(self, face_img):
        self.face_encoding = face_recognition.face_encodings(face_img)[0]  # get face encode
        status = 0
        possible_name = ''
        count = self.Database.user_count()
        self.known_face = numpy.empty([128, 1], dtype=numpy.float64)
        for index in range(count):
            self.known_face = numpy.column_stack((self.known_face, self.Database.feature_looking(index+1)))
            print(self.face_encoding.size)
        self.face_encoding = numpy.reshape(self.face_encoding, [128, 1])
        matches = face_recognition.compare_faces(self.known_face, self.face_encoding, tolerance=0.6)
        for match in range(count):  # compare one by one
            if matches[match] == 1:
                id = match + 1
                possible_name = self.Database.name_looking(id)
                status = 1
                break
        global login_user
        login_user = possible_name[0]
        # print(id)
        print(login_user)
        # print('is this you?')
        return login_user, id, status



    # DATABASE.create_table()
    # signup = Signup()
    # face, facecode = signup.get_face()
    # print(face.shape)
    # user_name = signup.get_name()
    # user_group = signup.get_group()
    # DATABASE.registration(user_name, user_group, facecode, '123')
    #
    # login = Login()
    # face = login.get_face()
    # cv2.imshow('', face)
    # cv2.waitKey(0)
    # login.compare()

