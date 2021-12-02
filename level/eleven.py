from linebot.models import (
    TextSendMessage,  FlexSendMessage
)
import time

from api.lineBotApi import line_bot_api


def leveleleven_message(user_id):
    line_bot_api.push_message(
        user_id,[
            FlexSendMessage(
                alt_text='虎珍堂',
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
        ]
    )
    time.sleep(0.8)
    line_bot_api.push_message(
        user_id,
        [
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
                                 "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "這裡好多漂亮的裙子喔！幸好我們跟老闆娘阿姨很熟，可以來這裡玩！我們最喜歡在這裡想像我們結婚的樣子了！說好了我們要當彼此的伴娘喔！",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            }
                        ]
                    }
                }),
        ]
    )
    time.sleep(0.8)
    line_bot_api.push_message(
        user_id,
        [
            FlexSendMessage(
                alt_text='看板模糊圖',
                contents={
                    "type": "carousel",
                    "contents": [
                        {
                            "type": "bubble",
                            "size": "micro",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.imgur.com/xnRHvyW.png",
                                        "size": "full",
                                        "aspectMode": "cover",
                                        "gravity": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "position": "absolute",
                                        "background": {
                                            "type": "linearGradient",
                                            "angle": "0deg",
                                            "endColor": "#00000000",
                                            "startColor": "#00000099"
                                        },
                                        "width": "100%",
                                        "height": "40%",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "A 新茜娜面霜",
                                                                "size": "md",
                                                                "color": "#ffffff",
                                                                "align": "center",
                                                                "weight": "bold"
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "spacing": "xs"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px",
                                        "paddingAll": "20px"
                                    }
                                ],
                                "paddingAll": "0px"
                            }
                        },
                        {
                            "type": "bubble",
                            "size": "micro",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.imgur.com/a1oTHKo.png",
                                        "size": "full",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "gravity": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "position": "absolute",
                                        "background": {
                                            "type": "linearGradient",
                                            "angle": "0deg",
                                            "endColor": "#00000000",
                                            "startColor": "#00000099"
                                        },
                                        "width": "100%",
                                        "height": "40%",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "B 皇家痱子粉",
                                                                "size": "md",
                                                                "color": "#ffffff",
                                                                "align": "center",
                                                                "weight": "bold"
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "spacing": "xs"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px",
                                        "paddingAll": "20px"
                                    }
                                ],
                                "paddingAll": "0px"
                            }
                        },
                        {
                            "type": "bubble",
                            "size": "micro",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.imgur.com/3eMqaXF.png",
                                        "size": "full",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "gravity": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "position": "absolute",
                                        "background": {
                                            "type": "linearGradient",
                                            "angle": "0deg",
                                            "endColor": "#00000000",
                                            "startColor": "#00000099"
                                        },
                                        "width": "100%",
                                        "height": "40%",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "C 麗娜珍珠膏",
                                                                "size": "md",
                                                                "color": "#ffffff",
                                                                "align": "center",
                                                                "weight": "bold"
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "spacing": "xs"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px",
                                        "paddingAll": "20px"
                                    }
                                ],
                                "paddingAll": "0px"
                            }
                        },
                        {
                            "type": "bubble",
                            "size": "micro",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.imgur.com/FSN4sNj.png",
                                        "size": "full",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "gravity": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "position": "absolute",
                                        "background": {
                                            "type": "linearGradient",
                                            "angle": "0deg",
                                            "endColor": "#00000000",
                                            "startColor": "#00000099"
                                        },
                                        "width": "100%",
                                        "height": "40%",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "D 耐斯洗髮粉",
                                                                "size": "md",
                                                                "color": "#ffffff",
                                                                "align": "center",
                                                                "weight": "bold"
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "spacing": "xs"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px",
                                        "paddingAll": "20px"
                                    }
                                ],
                                "paddingAll": "0px"
                            }
                        },
                        {
                            "type": "bubble",
                            "size": "micro",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.imgur.com/ZyFc4xW.png",
                                        "size": "full",
                                        "aspectMode": "cover",
                                        "aspectRatio": "1:1",
                                        "gravity": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "position": "absolute",
                                        "background": {
                                            "type": "linearGradient",
                                            "angle": "0deg",
                                            "endColor": "#00000000",
                                            "startColor": "#00000099"
                                        },
                                        "width": "100%",
                                        "height": "40%",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "E 百雀羚",
                                                                "size": "md",
                                                                "color": "#ffffff",
                                                                "align": "center",
                                                                "weight": "bold"
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "spacing": "xs"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetBottom": "0px",
                                        "offsetStart": "0px",
                                        "offsetEnd": "0px",
                                        "paddingAll": "20px"
                                    }
                                ],
                                "paddingAll": "0px"
                            }
                        }
                    ]
                }),
        ]
    )
    time.sleep(0.8)
    line_bot_api.push_message(
        user_id,
        [
            FlexSendMessage(
                alt_text='看板模糊圖',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/0Y7WXxz.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "看板模糊圖",
                                "wrap": True,
                                "size": "md",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "請依照虎珍糖右手邊的看板獲得線索，輸入『OOOOO』，OOOOO是五個英文字母",
                                "wrap": True,
                                "size": "sm",
                                "margin": "sm"
                            }
                        ],
                        "offsetTop": "none",
                        "paddingAll": "lg"
                    }
                }),
        ]
    )

