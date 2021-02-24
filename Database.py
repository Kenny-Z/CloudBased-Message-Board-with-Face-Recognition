import mysql.connector
import datetime
import numpy as np


class DB:
    # def __init__(self):
    #     self.mydb = mysql.connector.connect(
    #         host="127.0.0.1",
    #         user="root",
    #         passwd="zwj971020Q",
    #     )
    #     mycursor = self.mydb.cursor()
    #     mycursor.execute("CREATE DATABASE knockknock")

    def create_table(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()
        mycursor.execute(
            "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,"
            " name VARCHAR(255),"
            " user_groups VARCHAR(255),"
            " feature BLOB,"
            " password VARCHAR(255))"
        )
        mycursor.execute(
            "CREATE TABLE messages (id INT AUTO_INCREMENT PRIMARY KEY, "
            "revtime TIMESTAMP(6), "
            "content VARCHAR(255), "
            "recipient VARCHAR(16))"
        )

    def insert_message(self, content, recipient):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()

        theTime = datetime.datetime.now()

        sql = "INSERT INTO messages (revtime, content, recipient) VALUES (%s, %s, %s)"
        val = (theTime, content, recipient)
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    def feature_looking(self, index):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()
        sql = "SELECT feature FROM users WHERE id = %s"
        val = (index, )
        mycursor.execute(sql, val)
        values = mycursor.fetchall()
        print("values=", values)
        feature = np.frombuffer(values[0][0], dtype=np.float64)
        print(feature.size)
        return feature

    def message_looking(self, recipient):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()
        sql = "SELECT revtime, content FROM messages WHERE recipient = %s"
        val = (recipient,)
        mycursor.execute(sql, val)
        message = mycursor.fetchone()
        display = ''
        while message is not None:
            display = display + message[0].strftime("%m/%d/%Y, %H:%M:%S")+'\n'+message[1]+'\n'
            message = mycursor.fetchone()
        return display

    def group_message_looking(self, user):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()
        sql = "SELECT user_groups FROM users WHERE name = %s"
        val = (user,)
        mycursor.execute(sql, val)
        group = mycursor.fetchone()
        sql = "SELECT revtime, content FROM messages WHERE recipient = %s"
        val = (group[0],)
        mycursor.execute(sql, val)
        message = mycursor.fetchone()
        display = ''
        while message is not None:
            display = display + message[0].strftime("%m/%d/%Y, %H:%M:%S")+'\n'+message[1]+'\n'
            message = mycursor.fetchone()
        return display

    def password_looking(self, username):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()
        sql = "SELECT password FROM users WHERE name = %s"
        val = (username,)
        mycursor.execute(sql, val)
        password = mycursor.fetchone()
        return password

    def registration(self, name, user_groups, feature, password):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure = True
        )
        mycursor = self.mydb.cursor()
        bytes_feature = feature.tostring()
        # print(bytes_feature.size)
        sql = "INSERT INTO users (name, user_groups, feature, password) VALUES (%s, %s, %s, %s)"
        val = (name, user_groups, bytes_feature, password)
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "registration success.")

    def user_count(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()
        sql = "SELECT COUNT(*) from users"
        mycursor.execute(sql)
        # self.mydb.commit()
        number = int(mycursor.fetchone()[0])
        print(number)

        return number

    def name_looking(self, index):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zwj971020Q",
            database="knockknock",
            use_pure=True
        )
        mycursor = self.mydb.cursor()
        print("index:", index)
        mycursor.execute("SELECT name from users where id = %s", (index, ))

        name = mycursor.fetchall()[0]
        return name


if __name__ == "__main__":
    print('start')
    # DATABASE = DB()
    # DATABASE.registration('haiyu', 'student', '123', )
    # DATABASE.message_looking('all')
