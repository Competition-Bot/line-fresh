from linebot.models import (
    TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction
)

from api.lineBotApi import line_bot_api


def levelzero_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(
                text="我是一個到處旅行的旅人，這天，我來到了虎尾旅行，走著走著我在地上撿到了一本日記本"),
            ]))
