from linebot.models import (
    TextSendMessage, ImageSendMessage, FlexSendMessage,BubbleContainer
)

from api.lineBotApi import line_bot_api


def levelseven_message(event):
    line_bot_api.reply_message(
        event.reply_token,
            [
                FlexSendMessage(
                alt_text='小春留言',
                contents=BubbleContainer(
                    size="kilo",
                    direction="ltr",
                    body={
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                                {
                                    "type": "text",
                                    "text": "「還記得我們以前常常玩的猜數字1A2B嗎？玩了第4遍還是很好玩呢!」",
                                    "wrap": True,
                                },
                            {
                                    "type": "text",
                                    "text": "小春留",
                                    "align": "end"
                                    }
                        ]
                    }
                )),
                ImageSendMessage("https://i.imgur.com/wV1Oinq.jpg",
                                 "https://i.imgur.com/wV1Oinq.jpg"),
                ImageSendMessage("https://i.imgur.com/Vbk0FCa.jpg",
                                 "https://i.imgur.com/Vbk0FCa.jpg"),
                TextSendMessage(
                    text="( 參考1A2B過程以及文字密碼表，輸入『ＯＯ』ＯＯ為兩個中文字 )")
            ]
        )
