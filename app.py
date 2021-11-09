from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('qDvsOUDQMWXwONG+aH+fwhbeD5qU7Cs9okmn5FngnuXAZlykbPx77W6O5cuvPAjVloywUpG3ZD1hSMTT28SvctIcybUYHJlAmJY2e4KzbeHeUDVVmfAbeZwqZiDPAafYoyUSdpd59O0ARk937Vv7VwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dcc7f9bee687f90fe33cc309962f1210')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


target = False

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if(event.message.text == '你好'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="hello"))
        target = True
    elif(event.message.text == 'hello' and target == True):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="hi"))
    elif(event.message.text == 'hello'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="hello"))



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)