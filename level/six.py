from linebot.models import (
    TextSendMessage, ImageSendMessage, FlexSendMessage
)

from api.lineBotApi import line_bot_api


def levelsix_message(event):
    line_bot_api.reply_message(
        event.reply_token,
            [
                FlexSendMessage(
                alt_text='雲林布袋戲館',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                        "type": "image",
                        "url": "https://i.imgur.com/maIwW8X.jpg",
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
                                "text": "雲林布袋戲館",
                                "wrap": True,
                                "size": "md",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "原為虎尾郡役所，日治時期臺南州虎尾郡的治安及行政機關，2001年10月31日由雲林縣政府公告為歷史建築，現為雲林布袋戲館。2013雲林農業博覽會期間獲選為農博百大亮點。",
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
                                    "uri": "https://liff.line.me/1582347558-VdW5GZDw/detail/486255906888094199?utm_campaign=486255906888094199&utm_medium=CopyURL&utm_source=Share"
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
                alt_text='日記4',
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
                                "text": "「日記4」",
                                "wrap": True,
                                "weight": "bold",
                                 "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "史艷文，看來你也還記得我們一起創造的的「虎尾大儒俠」呢！",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            }
                        ]
                    }
                }),
                ImageSendMessage("https://i.imgur.com/72yAVXk.png",
                                 "https://i.imgur.com/72yAVXk.png"),
                TextSendMessage(
                    text="( 參考生旦淨末丑的角色說明，推敲小春與小花自創的故事裡是「生、淨」的角色是什麼。 )\n( 請輸入『生、淨』，按照順序回答人物名 )")
            ]
        )
