from linebot.models import (
    TextSendMessage,  FlexSendMessage, CarouselContainer, TemplateSendMessage, BubbleContainer, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def leveleleven_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
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
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "這裡好多漂亮的裙子喔！幸好我們跟老闆娘阿姨很熟，可以來這裡玩！我們最喜歡在這裡想像我們結婚的樣子了！說好了我們要當彼此的伴娘喔！",
                                "wrap": True,
                                "margin": "md"
                            }
                        ]
                    }
                }),
        ]
    )
