import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, ImageMessage, messages
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
            TextSendMessage(text="以前阿嬤常常帶我去虎尾糖廠買冰棒吃～然後坐在月台看火車～小時候我曾經在作文上寫我要當火車司機呢！"))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="我最喜歡這班車！"))
        line_bot_api.reply_message(
            event.reply_token,
            ImageMessage(type="image", originalContentUrl="data:image/png;base64,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",
                         previewImageUrl="data:image/png;base64,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")
        )
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入『我搭00：00的000出發！』(00：00為時間、000為車種)"))
    elif(event.message.text):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="我搭14：00的2077出發！』(00：00為時間、000為車種)"))


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
