from linebot.models import (
    TextSendMessage, ImageSendMessage, FlexSendMessage
)

from api.lineBotApi import line_bot_api


def levelone_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [FlexSendMessage(
            alt_text='一封信件掉落',
            contents={
                "type": "bubble",
                "size": "kilo",
                "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "（一封信件掉落）",
                                "wrap": True,
                                "margin": "sm",
                                "color": "#959595"
                            },
                            {
                                "type": "text",
                                "text": "給小花：",
                                "margin": "md"
                            },
                            {
                                "type": "text",
                                "text": "我要搬家了，我很想念我們以前的冒險種種，我希望你可以跟著我的腳步，再次回憶我們的秘密！",
                                "wrap": True,
                                "margin": "xs"
                            },
                            {
                                "type": "text",
                                "text": "小春上",
                                "align": "end",
                                "margin": "md"
                            }
                        ]
                }
            }),

         FlexSendMessage(
            alt_text='日記1',
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
                                "text": "「日記1」",
                                "wrap": True,
                                "weight": "bold",
                                "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "今天早上的時候我又遇見那隻黑斑貓，我今天餵他我的早餐地瓜，他全部吃光光了！",
                                "wrap": True,
                                "margin": "sm"
                            },
                            {
                                "type": "text",
                                "text": "他還對我說：",
                                "margin": "md"
                            }, {
                                "type": "text",
                                "text": "「喵，喵，喵，喵，喵～」",
                                "margin": "xs"
                            },
                            {
                                "type": "text",
                                "text": "「喵～喵，喵，喵」",
                                "margin": "none"
                            }
                        ]
                }
            }),
         ImageSendMessage("https://i.imgur.com/RoQgakz.png",
                          "https://i.imgur.com/RoQgakz.png"),
         ImageSendMessage("https://i.imgur.com/lxu1dMG.png",
                          "https://i.imgur.com/lxu1dMG.png"),
         TextSendMessage(
            text="( 請輸入『OOOO』, 答案為景點名，OO數量僅供參考 )"),
         ])
