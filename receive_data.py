from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Database import DB
import re

DATABASE = DB()
# DATABASE.create_table()
server = Flask(__name__)
@server.route("/sms", methods=['GET', 'POST'])
def sms_reply():  # bind this function to /sms route
    """
    1.request.form.get("key", type=str, default=None) 获取表单数据，
    2.request.args.get("key") 获取get请求参数，
    3.request.values.get("key") 获取所有参数。
    """
    # Start our TwiML response
    resp = MessagingResponse()
    resp.message("Message received")

    # Body insert to mysql
    text = request.values.get('Body', None)
    text = "".join(text)
    text = re.split('\@', text)
    to_usr = text[0]
    body = text[1]
    DATABASE.insert_message(body, to_usr)

    return str(resp)


if __name__ == "__main__":
    server.debug = True
    server.run(port=5000)  # debug=True, when code changes, the server will autoly load the new code
