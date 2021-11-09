import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,PostbackAction,MessageAction,URIAction
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'qDvsOUDQMWXwONG+aH+fwhbeD5qU7Cs9okmn5FngnuXAZlykbPx77W6O5cuvPAjVloywUpG3ZD1hSMTT28SvctIcybUYHJlAmJY2e4KzbeHeUDVVmfAbeZwqZiDPAafYoyUSdpd59O0ARk937Vv7VwdB04t89/1O/w1cDnyilFU=')
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


level = 1


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global level
    if(event.message.text == '第一關'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="第一關pass"))
        level += 1
    elif(event.message.text == '第二關' and level == 2):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="第二關pass"))
        level += 1
    elif(event.message.text == '第三關' and level == 3):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="第三關pass"))
        level += 1
    elif(event.message.text == '第四關' and level == 4):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="第四關pass"))
        level += 1
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="你輸入錯了!，第"+str(level)+"關還沒通過"))


def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='This is a buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://ithelp.ithome.com.tw/storage/image/fight.svg',
                imageAspectRatio='rectangle',
                imageSize='cover',
                imageBackgroundColor='#FFFFFF',
                title='iThome鐵人2021',
                text='Buttons template',
                actions=[
                    PostbackAction(
                        label='postback',
                        display_text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message',
                        text='message text'
                    ),
                    URIAction(
                        label='uri',
                        uri='http://example.com/'
                    )
                ]
            )
        ))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
