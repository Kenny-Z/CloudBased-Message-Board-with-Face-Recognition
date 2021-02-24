from twilio.rest import Client


class SendMsg():
    def __init__(self):
        self.account_sid = 'AC3b4db0275454291ce7b825aeeeca2719'
        self.auth_token = '31b8137c4951bd6c232f08eefb0afcd6'
        self.defaultnum = ['+13127927481']
        self.fromnumber = ['+12064527358']  # , '+14158141829', '+15017122661']

    def knocksend(self, body, media):
        self.client = Client(self.account_sid, self.auth_token)
        for number in self.defaultnum:
            message = self.client.messages.create(body=body,
                                             from_=self.fromnumber,
                                             media_url=media,
                                             to=number)

    def send(self, numbers2, body):
        self.client = Client(self.account_sid, self.auth_token)
        message = self.client.messages.create(body=body,
                                                  from_=self.fromnumber,
                                                  to=numbers2)
        print(message.sid)
        print(message.status)
        # print(message.media._uri)


if __name__ == '__main__':
     testmsg = SendMsg()
     testmsg.send('3127927481', 'image test')