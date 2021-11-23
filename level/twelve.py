from linebot.models import (
    TextSendMessage, ImageSendMessage, FlexSendMessage
)

from api.lineBotApi import line_bot_api


def leveltwelve_message(event):
    line_bot_api.reply_message(
        event.reply_token,
            [
                FlexSendMessage(
                alt_text='虎尾驛',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                        "type": "image",
                        "url": "https://i2.wp.com/ivychi.com/wp-content/uploads/20201104123257_57.jpg",
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
                                "text": "虎尾驛",
                                "wrap": True,
                                "size": "md",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "虎尾驛為中華民國雲林縣虎尾鎮一已廢棄木造火車站，原是虎尾糖廠小火車車站，亦為糖鐵北港線、雲虎線、西螺線、崙背線及莿桐線等的重要車站。",
                                "wrap": True,
                                "size": "sm",
                                "margin": "sm"
                            },
                            {
                                "type": "text",
                                "text": "該建築於2010年1月15日公告為歷史建築，現在用作虎尾遊客中心",
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
                                    "uri": "https://spot.line.me/detail/720382419873591332"
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
                FlexSendMessage(
                alt_text='日記8',
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
                                "text": "「日記8」",
                                "wrap": True,
                                "weight": "bold",
                                 "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "以前阿嬤常常帶我去虎尾糖廠買冰棒吃~然後坐在月台看火車~小時候我曾經在作文上寫我要當火車司機呢！",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "我最喜歡這班車！",
                                "wrap": True,
                                "margin": "sm",
                                "size": "md"
                            }
                        ]
                    }
                }),
                ImageSendMessage("https://i.imgur.com/pELde59.jpg",
                                 "https://i.imgur.com/pELde59.jpg"),
                ImageSendMessage("https://i.imgur.com/bcf4Npy.png",
                                 "https://i.imgur.com/bcf4Npy.png"),
                TextSendMessage(
                    text="請輸入『我搭00:00的000出發!』00:00為時間;000為車種"),
            ]
        )
