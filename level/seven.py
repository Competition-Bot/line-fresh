from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelseven_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text="「還記得我們以前常常玩的猜數字1A2B嗎？玩了第4遍還是很好玩呢!」小春留"),
                ImageSendMessage("https://i.imgur.com/wV1Oinq.jpg",
                                 "https://i.imgur.com/wV1Oinq.jpg"),
                ImageSendMessage("https://i.imgur.com/xMHkT0i.jpg",
                                 "https://i.imgur.com/xMHkT0i.jpg"),
                TextSendMessage(
                    text="(參考1A2B過程以及文字密碼表，輸入『ＯＯ』ＯＯ為兩個中文字)")
            ]
        ))
