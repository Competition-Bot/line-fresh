from linebot.models import (
    TextSendMessage,  FlexSendMessage, CarouselContainer, TemplateSendMessage, BubbleContainer, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def leveleleven_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            FlexSendMessage(
                alt_text='日記7',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                        "type": "image",
                        "url": "https://joes.tw/wp-content/uploads/20190719193350_27.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "20:14"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "虎珍堂",
                                "wrap": True,
                                "size": "md",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "虎珍堂菓寮店～70年日治時代老屋風華再現，用地瓜與乳酪蛋糕做成散步美食「虎月燒」！",
                                "wrap": True,
                                "size": "sm",
                                "margin": "sm"
                            }
                        ],
                        "offsetTop": "none",
                        "paddingAll": "lg"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "查看熱點資訊",
                                    "uri": "https://liff.line.me/1582347558-VdW5GZDw/detail/486254094835523175?utm_campaign=486254094835523175&utm_medium=CopyURL&utm_source=Share"
                                },
                                "height": "sm"
                            }
                        ]
                    },
                    "styles": {
                        "body": {
                            "separator": True
                        }
                    }
                }),
            TextSendMessage(
                text="原來虎珍的前身是正義百貨行，真是一棟有歷史的建築！"),
            FlexSendMessage(
                alt_text='日記7',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "direction": "ltr",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "「日記7」",
                                "wrap": True,
                                "weight": "bold",
                                 "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "這裡好多漂亮的裙子喔！幸好我們跟老闆娘阿姨很熟，可以來這裡玩！我們最喜歡在這裡想像我們結婚的樣子了！說好了我們要當彼此的伴娘喔！",
                                "wrap": True,
                                "margin": "md",
                                "size": "sm"
                            }
                        ]
                    }
                }),
            
        ]
    )
