import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
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
    if(event.message.text == '開始'):
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text="以前阿嬤常常帶我去虎尾糖廠買冰棒吃～然後坐在月台看火車～小時候我曾經在作文上寫我要當火車司機呢！"),
             TextSendMessage(text="我最喜歡這班車！"),
             ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                              "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
             TextSendMessage(text="請輸入『我搭00：00的000出發！』(00：00為時間、000為車種)"),
             TextSendMessage(text="我搭14：00的2077出發！』(00：00為時間、000為車種)")])


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TemplateSendMessage(
#             alt_text='This is a buttons template',
#             template=ButtonsTemplate(
#                 thumbnail_image_url='https://ithelp.ithome.com.tw/storage/image/fight.svg',
#                 imageAspectRatio='rectangle',
#                 imageSize='cover',
#                 imageBackgroundColor='#FFFFFF',
#                 title='iThome鐵人2021',
#                 text='Buttons template',
#                 actions=[
#                     PostbackAction(
#                         label='postback',
#                         display_text='postback text',
#                         data='action=buy&itemid=1'
#                     ),
#                     MessageAction(
#                         label='message',
#                         text='message text'
#                     ),
#                     URIAction(
#                         label='uri',
#                         uri='http://example.com/'
#                     )
#                 ]
#             )
#         ))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
