from linebot.models import (
    TextSendMessage, FlexSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)
import time
from api.lineBotApi import line_bot_api

def levelone_message(user_id):
    line_bot_api.push_message(
        user_id,[
            FlexSendMessage(
                alt_text='合同廳舍',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/igkuCI8.jpg",
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
                                "text": "合同廳舍",
                                "wrap": True,
                                "size": "md",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "虎尾合同廳舍位於雲林縣虎尾鎮，係為台灣日治時期消防單位觀測轄區失火位置與完成通報之緊急救災建築物。",
                                "wrap": True,
                                "size": "sm",
                                "margin": "sm"
                            },
                            {
                                "type": "text",
                                "text": "合同廳舍為日治時期官方辦公廳舍的特殊建築類型之一，所謂「合同」乃合署辦公之意，反映在空間組織上則是不同單位的空間群組以及各自獨立的出入動線。",
                                "wrap": True,
                                "size": "sm",
                                "margin": "sm"
                            },
                            {
                                "type": "text",
                                "text": "現在為結合誠品書店及星巴克咖啡重新翻修的三級古蹟，同時也是誠品書店及星巴克咖啡在雲林縣第一間門市。",
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
                                    "uri": "https://liff.line.me/1582347558-VdW5GZDw/detail/532301960250921592?utm_campaign=532301960250921592&utm_medium=CopyURL&utm_source=Share"
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
        ]
    )

    time.sleep(0.8)

    line_bot_api.push_message(
        user_id,[
            FlexSendMessage(
                alt_text='日記3',
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
                                "text": "「日記3」",
                                "wrap": True,
                                "weight": "bold",
                                 "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "你找對地方了，史艷文，還記得我們以前常常大鬧警局嗎，還會偷偷溜消防廳的天梯呢，嘻嘻",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "我偷偷留了下一個地方的線索，合同廳舍裡面有一個會飛的動物呦！",
                                "wrap": True,
                                "margin": "sm",
                                "size": "md"
                            }
                        ]
                    }
                }),
        ]
    )

    time.sleep(0.8)

    line_bot_api.push_message(
        user_id,[
            FlexSendMessage(
                alt_text='你還記得我們少了幾支羽毛嗎?',
                contents={
                    "type": "bubble",
                    'size': "kilo",
                    'direction': "ltr",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "你還記得我們少了幾支羽毛嗎?\n( 請輸入『少了O支』)",
                                "wrap": True,
                                "margin": "sm"
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "打開相機辨識尋找物件",
                                    "uri": "https://liff.line.me/1656608345-9Xz3PVkQ"
                                }
                            }
                        ]
                    }
                })
        ]
    )

# def levelfour_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         [
#             FlexSendMessage(
#                 alt_text='合同廳舍',
#                 contents={
#                     "type": "bubble",
#                     "size": "kilo",
#                     "hero": {
#                         "type": "image",
#                         "url": "https://i.imgur.com/igkuCI8.jpg",
#                         "size": "full",
#                         "aspectMode": "cover",
#                         "aspectRatio": "20:14"
#                     },
#                     "body": {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "合同廳舍",
#                                 "wrap": True,
#                                 "size": "md",
#                                 "weight": "bold"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "虎尾合同廳舍位於雲林縣虎尾鎮，係為台灣日治時期消防單位觀測轄區失火位置與完成通報之緊急救災建築物。",
#                                 "wrap": True,
#                                 "size": "sm",
#                                 "margin": "sm"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "合同廳舍為日治時期官方辦公廳舍的特殊建築類型之一，所謂「合同」乃合署辦公之意，反映在空間組織上則是不同單位的空間群組以及各自獨立的出入動線。",
#                                 "wrap": True,
#                                 "size": "sm",
#                                 "margin": "sm"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "現在為結合誠品書店及星巴克咖啡重新翻修的三級古蹟，同時也是誠品書店及星巴克咖啡在雲林縣第一間門市。",
#                                 "wrap": True,
#                                 "size": "sm",
#                                 "margin": "sm"
#                             }
#                         ],
#                         "offsetTop": "none",
#                         "paddingAll": "lg"
#                     },
#                     "footer": {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "button",
#                                 "action": {
#                                     "type": "uri",
#                                     "label": "查看熱點資訊",
#                                     "uri": "https://liff.line.me/1582347558-VdW5GZDw/detail/532301960250921592?utm_campaign=532301960250921592&utm_medium=CopyURL&utm_source=Share"
#                                 },
#                                 "height": "sm"
#                             }
#                         ]
#                     },
#                     "styles": {
#                         "body": {
#                             "separator": True
#                         }
#                     }
#                 }),
#             FlexSendMessage(
#                 alt_text='日記3',
#                 contents={
#                     "type": "bubble",
#                     "size": "kilo",
#                     "direction": "ltr",
#                     "body": {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "「日記3」",
#                                 "wrap": True,
#                                 "weight": "bold",
#                                  "size": "md"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "你找對地方了，史艷文，還記得我們以前常常大鬧警局嗎，還會偷偷溜消防廳的天梯呢，嘻嘻",
#                                 "wrap": True,
#                                 "margin": "md",
#                                 "size": "md"
#                             },
#                             {
#                                 "type": "text",
#                                 "text": "我偷偷留了下一個地方的線索，合同廳舍裡面有一個會飛的動物呦！",
#                                 "wrap": True,
#                                 "margin": "sm",
#                                 "size": "md"
#                             }
#                         ]
#                     }
#                 }),
#             FlexSendMessage(
#                 alt_text='你還記得我們少了幾支羽毛嗎?',
#                 contents={
#                     "type": "bubble",
#                     'size': "kilo",
#                     'direction': "ltr",
#                     "body": {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "text",
#                                 "text": "你還記得我們少了幾支羽毛嗎?\n( 請輸入『少了O支』)",
#                                 "wrap": True,
#                                 "margin": "sm"
#                             }
#                         ]
#                     },
#                     "footer": {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                             {
#                                 "type": "button",
#                                 "action": {
#                                     "type": "uri",
#                                     "label": "打開相機辨識尋找物件",
#                                     "uri": "https://liff.line.me/1656608345-9Xz3PVkQ"
#                                 }
#                             }
#                         ]
#                     }
#                 })
#         ])
