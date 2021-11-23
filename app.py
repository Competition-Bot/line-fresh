import os
from flask import Flask, request, abort

from linebot import (
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    JoinEvent, MessageEvent, TextMessage, FlexSendMessage, BubbleContainer, ImageComponent, TextComponent, BoxComponent, TextSendMessage, BoxComponent, ImageSendMessage, MessageAction, URIAction, ButtonsTemplate, PostbackAction, TemplateSendMessage
)

from api.lineBotApi import line_bot_api

from level.start import start_message
from level.zero import levelzero_message
from level.one import levelone_message
from level.two import leveltwo_message
from level.three import levelthree_message
from level.four import levelfour_message
from level.five import levelfive_message
from level.six import levelsix_message
from level.seven import levelseven_message
from level.eight import leveleight_message
from level.nine import levelnine_message
from level.ten import levelten_message
from level.eleven import leveleleven_message
from level.twelve import leveltwelve_message
from level.thirteen import (levelthirteen_one_message,
                            levelthirteen_two_message, levelthirteen_three_message)
from level.end import levelend_message

app = Flask(__name__)


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


level = 'init'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global level
    if((event.message.text == 'start' and level == 'init') or event.message.text == 'start'):
        start_message(event)
        level = 'start'
    elif((event.message.text == '開始遊戲' and level == 'start') or event.message.text == 'test0'):
        levelzero_message(event)
        level = '0'
    elif((event.message.text == '打開日記' and level == '0') or event.message.text == 'test1'):
        level = '1'
        levelone_message(event)
    elif((event.message.text == '2B' and level == '1') or event.message.text == 'test2'):
        level = '2'
        leveltwo_message(event)
    elif(((event.message.text == '有6隻石頭鳥' or event.message.text == '有六隻石頭鳥') and level == '2') or event.message.text == 'test3'):
        level = '3'
        levelthree_message(event)
    elif((event.message.text == '前往合同廳舍' and level == '3') or event.message.text == 'test4'):
        level = '4'
        levelfour_message(event)
    elif(((event.message.text == '少了6隻' or event.message.text == '少了六隻') and level == '4') or event.message.text == 'test5'):
        level = '5'
        levelfive_message(event)
    elif((event.message.text == '前往雲林布袋戲館' and level == '5') or event.message.text == 'test6'):
        level = '6'
        levelsix_message(event)
    elif((event.message.text == '生、淨' and level == '6') or event.message.text == 'test7'):
        level = '7'
        levelseven_message(event)
    elif((event.message.text == '屋敷' and level == '7') or event.message.text == 'test8'):
        level = '8'
        leveleight_message(event)
    elif(((event.message.text == 'COOL' or event.message.text == 'cool') and level == '8') or event.message.text == 'test9'):
        level = '9'
        levelnine_message(event)
    elif((event.message.text == '1921' and level == '9') or event.message.text == 'test10'):
        level = '10'
        levelten_message(event)
    elif((event.message.text == '前往虎珍堂' and level == '10') or event.message.text == 'test11'):
        level = '11'
        leveleleven_message(event)
    elif((event.message.text == 'EADCB' and level == '11') or event.message.text == 'test12'):
        level = '12'
        leveltwelve_message(event)
    elif(((event.message.text == '我搭14:00的區間車出發' or event.message.text == '我搭14：00的區間車出發') and level == '12') or event.message.text == 'test13'):
        level = '13-1'
        levelthirteen_one_message(event)
    elif((event.message.text == '8' and level == '13-1')):
        level = '13-2'
        levelthirteen_two_message(event)
    elif((event.message.text == '3' and level == '13-2')):
        level = '13-3'
        levelthirteen_three_message(event)
    elif((event.message.text == '五分車' and level == '13-3') or event.message.text == 'test10'):
        level = 'end'
        levelend_message(event)
    elif(event.message.text == 'test'):
        line_bot_api.reply_message(
            event.reply_token,
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text='test',
                    contents=BubbleContainer(
                        hero=ImageComponent(
                            url="https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                            size="full",
                            aspectRatio="20:13",
                            aspectMode="cover",
                        ),
                        body=BoxComponent(
                            layout="vertical",
                            contents=[
                                BoxComponent(
                                    layout="vertical",
                                    margin="lg",
                                    spacing="sm",
                                    contents=[
                                        {
                                            "type": "text",
                                            "text": "虎尾手札 - 穿梭巷弄的少女",
                                            "weight": "bold",
                                            "size": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "lg",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "小春與小花是要好的朋友，她們喜歡在巷弄間到處探險，藏著她倆的秘密，升上高中後小春將搬離虎尾去外地，因此她將策劃一場紀念她們友誼的冒險...",
                                                            "wrap": 'true',
                                                            "color": "#666666",
                                                            "size": "sm",
                                                            "flex": 5
                                                        }
                                                    ]
                                                },
                                            ]
                                        }
                                     ]
                                )
                            ]
                        )
                    )
                )
            )
        )


@handler.add(JoinEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.push_message('<to>', TextSendMessage(text='Hello World!'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
