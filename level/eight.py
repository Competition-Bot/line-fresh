from linebot.models import (
    TextSendMessage, FlexSendMessage,ImageSendMessage
)

from api.lineBotApi import line_bot_api


def leveleight_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(
                text="日記本提到的答案的確是屋敷呢，但現在好像改建成雲林故事館了，去那邊看看吧！"),
            FlexSendMessage(
                alt_text='雲林故事館',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                            "type": "image",
                            "url": "https://i2.wp.com/img.journey.tw/20180408220323_54.jpg?resize=1100%2C730&ssl=1",
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
                                    "text": "雲林故事館",
                                    "wrap": True,
                                    "size": "md",
                                    "weight": "bold"
                                },
                            {
                                    "type": "text",
                                    "text": "雲林故事館為日據時期所留下的虎尾郡守官邸，經歷過修復後重新開放，成為一座專門講述兒童故事、舉辦活動的場域，用心的模式再次融入了虎尾居民的生活中。",
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
                                        "uri": "https://liff.line.me/1582347558-VdW5GZDw/detail/629478315530393395?utm_campaign=629478315530393395&utm_medium=CopyURL&utm_source=Share"
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
                alt_text='日記5',
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
                                "text": "「日記5」",
                                "wrap": True,
                                "weight": "bold",
                                 "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "我們每次下課後常常在官邸畫畫呢，一邊吃我們最愛的烤地瓜，一邊想我們的『虎尾大儒俠』，啊!我還記得我把結局放在官邸的門牌後面喔！",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            }
                        ]
                    }
                }),
            ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                             "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
            TextSendMessage(
                text="( 輸入『OOOO』OOOO是大寫英文字母 )"),
        ]
    )
