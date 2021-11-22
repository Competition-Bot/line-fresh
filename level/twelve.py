from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def leveltwelve_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
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
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://spot.line.me/detail/720382419873591332'
                            )
                        ]
                    )),
                TextSendMessage(
                    text="「日記8」\n\n以前阿嬤常常帶我去虎尾糖廠買冰棒吃~然後坐在月台看火車~小時候我曾經在作文上寫我要當火車司機呢！\n\n我最喜歡這班車！"),
                ImageSendMessage("https://i.imgur.com/pELde59.jpg",
                                 "https://i.imgur.com/pELde59.jpg"),
                ImageSendMessage("https://i.imgur.com/bcf4Npy.png",
                                 "https://i.imgur.com/bcf4Npy.png"),
                TextSendMessage(
                    text="(請輸入『我搭00:00的000出發!』00:00為時間;000為車種)"),
            ]
        ))
