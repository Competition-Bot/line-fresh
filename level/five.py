from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelfive_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text="「這是電台節目表，你應該還記得我們最愛聽什麼節目吧!」\n小春留"),
                ImageSendMessage("https://i.imgur.com/iUKYj9Z.jpg",
                                 "https://i.imgur.com/iUKYj9Z.jpg"),
                TemplateSendMessage(
                    alt_text='一台復古的收音機',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/gi0z0bv.png',
                        imageAspectRatio='rectangle',
                        imageSize='fit',
                        imageBackgroundColor='#FFFFFF',
                        text='一台復古的收音機',
                        actions=[
                            URIAction(
                                label='打開收音機',
                                uri='https://liff.line.me/1656608345-0Yx6zYOX'
                            )
                        ]
                    )
                ),
                TextSendMessage(
                    text="(輸入『前往0000』，0000是地點名稱，00數量僅供參考)\n\n(線索在合同廳舍的門牌號碼中，輸入正確的收音機頻道)")
            ]
        ))
