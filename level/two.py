from linebot.models import (
    TextSendMessage, ImageSendMessage, FlexSendMessage
)

from api.lineBotApi import line_bot_api


def leveltwo_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            FlexSendMessage(
                alt_text='虎尾厝沙龍',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                            "type": "image",
                            "url": "https://pic.pimg.tw/as660707/1371195583-2324753213.jpg",
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
                                    "text": "虎尾厝沙龍",
                                    "wrap": True,
                                    "size": "md",
                                    "weight": "bold"
                                },
                            {
                                    "type": "text",
                                    "text": "虎尾厝沙龍, 隱身虎尾鎮鬧區的幽靜巷弄中，原為1940年吳中醫師興建的「和洋式住宅」．2011年，搖身一變，成為「獨立冊店」,以「生態、性別、另類全球化」為營運理念,虎尾厝積極關注台灣社會及世界脈動。",
                                    "wrap": True,
                                    "size": "sm",
                                    "margin": "sm"
                                },
                            {
                                    "type": "text",
                                    "text": "在這裏，你可以找一個舒適的角落看書、享用咖啡茶點、觀賞主題展覽，不定期舉辦精彩的活動與鄉親分享！",
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
                                        "uri": "https://liff.line.me/1582347558-VdW5GZDw/detail/486258846029846639?utm_campaign=486258846029846639&utm_medium=CopyURL&utm_source=Share"
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
                text="原來這裡就是虎尾厝沙龍呀，啊！這個是藝術家王忠龍的石頭鳥鐵雕圍牆"),
            ImageSendMessage("https://i.imgur.com/IU3w7Kf.png",
                             "https://i.imgur.com/IU3w7Kf.png"),
            TextSendMessage(
                text="( 請輸入『有Ｏ隻石頭鳥』，可以參考上方示意圖，至實際場景中詳細觀看 )"),
        ])
