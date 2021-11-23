from linebot.models import (
    TextSendMessage,  FlexSendMessage, CarouselContainer, TemplateSendMessage, BubbleContainer, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def leveleleven_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            [
                TextSendMessage(
                    text="原來虎珍的前身是正義百貨行，真是一棟有歷史的建築！"),
                TextSendMessage(
                    text="「日記7」\n\n這裡好多漂亮的裙子喔！幸好我們跟老闆娘阿姨很熟，可以來這裡玩！我們最喜歡在這裡想像我們結婚的樣子了！說好了我們要當彼此的伴娘喔！")
            ]
        ))
