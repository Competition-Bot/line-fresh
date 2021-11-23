from linebot.models import (
    TextSendMessage, ImageSendMessage, FlexSendMessage
)

from api.lineBotApi import line_bot_api


def levelthirteen_one_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                FlexSendMessage(
                    alt_text='虎尾鐵橋',
                    contents={
                        "type": "bubble",
                        "size": "kilo",
                        "hero": {
                            "type": "image",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Huwei_Dual_gauge_track_bridge_01.jpg/288px-Huwei_Dual_gauge_track_bridge_01.jpg",
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
                                    "text": "虎尾鐵橋",
                                    "wrap": True,
                                    "size": "md",
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "text": "虎尾糖廠鐵橋，又被稱作虎尾鐵橋，舊名番薯莊板仔橋，是一座鋼桁架橋、鈑梁橋及工字梁橋混合型式的橋梁，於台灣日治時期興建並於國民政府時代延建，位於台灣雲林縣虎尾鎮，為雲林縣縣定古蹟。目前屬於台灣糖業公司，作為糖業鐵路。",
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
                    alt_text='日記9',
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
                                    "text": "「日記9」",
                                    "wrap": True,
                                    "weight": "bold",
                                    "size": "md"
                                },
                                {
                                    "type": "text",
                                    "text": "這是最後一個謎題啦~我們以前最喜歡模仿電視上的主持人玩遊戲了！接下來進入快問快答時間~！",
                                    "wrap": True,
                                    "margin": "md",
                                    "size": "md"
                                }
                            ]
                        }
                    }),

                FlexSendMessage(
                    alt_text='虎尾鐵橋總共有幾個叉叉？',
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
                                    "text": "「虎尾鐵橋總共有幾個叉叉？」",
                                    "wrap": True,
                                    "size": "md"
                                },
                                {
                                    "type": "text",
                                    "text": "( 請輸入數字 )",
                                    "wrap": True,
                                    "margin": "md",
                                    "size": "md"
                                }
                            ]
                        }
                    }),
                ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                                 "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
            ]
        ))


def levelthirteen_two_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(
            alt_text='虎珍堂的虎月燒總共有幾種口味？',
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
                                "text": "「虎珍堂的虎月燒總共有幾種口味？」",
                                "wrap": True,
                                "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "( 請輸入數字 )",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            }
                        ]
                }
            })
    )


def levelthirteen_three_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(
            alt_text='虎尾糖廠唯一載運甘蔗的車種是哪種呢？',
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
                                "text": "「虎尾糖廠唯一載運甘蔗的車種是哪種呢？」",
                                "wrap": True,
                                "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "( 請輸入『OOO』，OOO是車種名 )",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            }
                        ]
                }
            }))
