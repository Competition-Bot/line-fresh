from linebot.models import (
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
)

from api.lineBotApi import line_bot_api


def start_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text='start',
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
                                        "size": "lg"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "margin": "md",
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
                                                        "wrap": True,
                                                        "color": "#666666",
                                                        "size": "sm",
                                                        "flex": 5
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "玩家將扮演撿到日記本的角色，將依循日記的指示探索虎尾的巷弄，進而發現小春與小花之間的點點滴滴。",
                                                        "wrap": True,
                                                        "color": "#666666",
                                                        "size": "sm",
                                                        "flex": 5
                                                    }
                                                ],
                                                "margin": "md"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "message",
                                                    "label": "開始遊戲",
                                                    "text": "開始遊戲"
                                                }
                                            }
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
