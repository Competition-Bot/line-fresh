from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, FlexSendMessage, BubbleContainer
)
from linebot.models.flex_message import BoxComponent


from api.lineBotApi import line_bot_api


def levelfive_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                FlexSendMessage(
                    alt_text='start',
                    contents=BubbleContainer(
                        size="kilo",
                        direction="ltr",
                        body={
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "「這是電台節目表，你應該還記得我們最愛聽什麼節目吧」",
                                    "wrap": True,
                                },
                                {
                                    "type": "text",
                                    "text": " 小春留",
                                    "align": "end"
                                }
                            ]
                        }
                    )),
                ImageSendMessage("https://i.imgur.com/iUKYj9Z.jpg",
                                 "https://i.imgur.com/iUKYj9Z.jpg"),
                FlexSendMessage(
                    alt_text='start',
                    contents=BubbleContainer(
                        hero={
                            "type": "image",
                            "url": "https://i.imgur.com/4F59BsC.png",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "fit",
                        },
                        body=BoxComponent(
                            layout="vertical",
                            contents=[
                                {
                                    "type": "text",
                                    "text": "一台復古的收音機",
                                    "weight": "bold",
                                    "size": "lg"
                                }
                            ]
                        ),
                        footer=BoxComponent(
                            layout="vertical",
                            spacing="sm",
                            contents=[
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "打開收音機",
                                        "uri": "https://liff.line.me/1656608345-0Yx6zYOX"
                                    }
                                }
                            ]
                        )
                    )
                ),
                TextSendMessage(
                    text="(輸入『前往0000』，0000是地點名稱，00數量僅供參考)\n\n(線索在合同廳舍的門牌號碼中，輸入正確的收音機頻道)")
            ]
        ))
