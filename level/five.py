from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, FlexSendMessage
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
                FlexSendMessage(
                    {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://i.imgur.com/gi0z0bv.png",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "fit",
                            "action": {
                                "type": "uri",
                                "uri": "http://linecorp.com/"
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "一台復古的收音機",
                                    "weight": "bold",
                                    "size": "lg"
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "打開收音機",
                                        "uri": "https://liff.line.me/1656608345-0Yx6zYOX"
                                    }
                                },
                                {
                                    "type": "spacer",
                                    "size": "sm"
                                }
                            ],
                            "flex": 0
                        }
                    }
                ),
                TextSendMessage(
                    text="(輸入『前往0000』，0000是地點名稱，00數量僅供參考)\n\n(線索在合同廳舍的門牌號碼中，輸入正確的收音機頻道)")
            ]
        ))
