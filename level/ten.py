from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelten_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text="「下一個地點是我們最常去的地方！不過不知道你解不解的開這個謎呢？嘻嘻」\n小春留"),
                ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                                 "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
                ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                                 "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
                TextSendMessage(
                    text="(請參考數獨以及文字表格，輸入『前往OOOO』，OO是中文字，數量僅供參考)"),
            ]
        ))
