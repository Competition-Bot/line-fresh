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
            ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                             "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
            ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                             "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
            TextSendMessage(
                text="( 請參考數獨以及文字表格，輸入『前往OOOO』，OO是中文字，數量僅供參考 )"),
        ]
    )
