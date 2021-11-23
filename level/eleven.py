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
            ]
        ))
