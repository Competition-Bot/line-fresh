from typing import Text
from linebot.models import (
    TextSendMessage, FlexSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api

def error_Nohelp(event,help):
    if( help == "1"):
        text = "哎呀! 再仔細看看提示吧! 如果還需要幫助的話請輸入「我需要幫忙」"
    else:
        text = "嘿嘿~答錯嘍! 再好好想想吧! 需要幫助的話請輸入「我需要幫忙」"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text)
    )

def levelone_Help1(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("好哇! 到「虎尾厝沙龍」的門口右側，數數看共有幾個石頭鳥吧！")
    )

def levelone_Help2(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("好哇! 1,2,3....總共有6隻!輸入「有6隻石頭鳥」來進行下一關吧！")
    )