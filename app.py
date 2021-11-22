import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, MessageAction, URIAction, ButtonsTemplate, PostbackAction, TemplateSendMessage
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
    line_bot_api.push_message('<to>', TextSendMessage(text='Hello World!'))
    if(event.message.text == '開始1'):
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text='虎尾驛',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i2.wp.com/ivychi.com/wp-content/uploads/20201104123257_57.jpg',
                    imageAspectRatio='rectangle',
                    imageSize='cover',
                    imageBackgroundColor='#FFFFFF',
                    title='虎尾驛',
                    text='虎尾驛為中華民國雲林縣虎尾鎮一已廢棄木造火車站，原是虎尾糖廠小火車車站。',
                    actions=[
                        MessageAction(
                            label='查看日記',
                            text='查看日記'
                        ),
                        URIAction(
                            label='查看熱點資訊',
                            uri='https://spot.line.me/detail/720382419873591332'
                        )
                    ]
                )
            ))
    elif(event.message.text == '查看日記'):
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(
                text="以前阿嬤常常帶我去虎尾糖廠買冰棒吃～然後坐在月台看火車～小時候我曾經在作文上寫我要當火車司機呢！"),
             TextSendMessage(text="我最喜歡這班車！"),
             ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                              "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
             TextSendMessage(text="請輸入『我搭00：00的000出發！』(00：00為時間、000為車種)")])
    elif(event.message.text == '我搭14:00的2077出發！' or event.message.text == '我搭14：00的2077出發！' or event.message.text == '我搭14：00的2077出發!' or event.message.text == '我搭14:00的2077出發!'):
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text='虎尾鐵橋',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Huwei_Dual_gauge_track_bridge_01.jpg/288px-Huwei_Dual_gauge_track_bridge_01.jpg',
                    imageAspectRatio='rectangle',
                    imageSize='cover',
                    imageBackgroundColor='#FFFFFF',
                    title='虎尾鐵橋',
                    text='虎尾糖廠鐵橋，舊名番薯莊板仔橋，於台灣日治時期興建並於國民政府時代延建，為雲林縣縣定古蹟。',
                    actions=[
                        MessageAction(
                            label='查看日記',
                            text='查看日記'
                        ),
                        URIAction(
                            label='查看熱點資訊',
                            uri='https://spot.line.me/detail/720382419873591332'
                        )
                    ]
                )
            ))

    elif(event.message.text == '開始2'):
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(
                text="這是電台節目表，你應該還記得我們最愛聽什麼節目吧!"),
             ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                              "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
             TemplateSendMessage(
                alt_text='一台復古收音機',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://raw.githubusercontent.com/tsaiyuyes7/LIFF_test/main/img/radio.png',
                    imageAspectRatio='rectangle',
                    imageSize='cover',
                    imageBackgroundColor='#FFFFFF',
                    text='一台復古收音機',
                    actions=[
                        URIAction(
                            label='開啟收音機',
                            uri='https://liff.line.me/1656608345-0Yx6zYOX'
                        )
                    ]
                )
            ),
                TextSendMessage(text="請輸入『前往xxx』(xxx是地點名)")]
        )

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TemplateSendMessage(
    #         alt_text='This is a buttons template',
    #         template=ButtonsTemplate(
    #             thumbnail_image_url='https://ithelp.ithome.com.tw/storage/image/fight.svg',
    #             imageAspectRatio='rectangle',
    #             imageSize='cover',
    #             imageBackgroundColor='#FFFFFF',
    #             title='iThome鐵人2021',
    #             text='Buttons template',
    #             actions=[
    #                 PostbackAction(
    #                     label='postback',
    #                     display_text='postback text',
    #                     data='action=buy&itemid=1'
    #                 ),
    #                 MessageAction(
    #                     label='message',
    #                     text='message text'
    #                 ),
    #                 URIAction(
    #                     label='uri',
    #                     uri='http://example.com/'
    #                 )
    #             ]
    #         )
    #     ))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
