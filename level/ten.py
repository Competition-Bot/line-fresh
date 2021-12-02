from linebot.models import (
    TextSendMessage, ImageSendMessage, FlexSendMessage, BubbleContainer
)

from api.lineBotApi import line_bot_api


def levelten_message(event):
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
                                    "text": "「下一個地點是我們最常去的地方！不過不知道你解不解的開這個謎呢？嘻嘻」",
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
            ImageSendMessage("https://i.imgur.com/ij73rKs.png",
                             "https://i.imgur.com/ij73rKs.png"),
            ImageSendMessage("https://i.imgur.com/nBudfmg.png",
                             "https://i.imgur.com/nBudfmg.png"),
            TextSendMessage(
                text="( 請參考數獨以及文字表格，輸入『前往OOOO』，OO是中文字，數量僅供參考 )"),
        ]
    )
