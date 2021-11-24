from linebot.models import (
    TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction, FlexSendMessage
)

import time

from api.lineBotApi import line_bot_api


def levelzero_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(
                text="我是一個到處旅行的旅人，這天，我來到了虎尾旅行，走著走著我在地上撿到了一本日記本"),
            FlexSendMessage(
                alt_text='陳舊的日記本',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                            "type": "image",
                            "url": "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
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
                                    "text": "陳舊的日記本",
                                    "wrap": True,
                                    "size": "md",
                                    "weight": "bold"
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
                                        "type": "message",
                                        "label": "打開日記",
                                        "text": '打開日記'
                                    },
                                    "height": "sm"
                                }
                        ]
                    },
                    "styles": {
                        "body": {
                            "separator": True,
                            "backgroundColor": "#333333"
                        }
                    }
                })
        ]
    )

    
