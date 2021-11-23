from linebot.models import (
    TextSendMessage, ImageSendMessage
)

from api.lineBotApi import line_bot_api


def levelone_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(
                text="（一封信件掉落）\n給小花：\n我要搬家了，我很想念我們以前的冒險種種，我希望你可以跟著我的腳步，再次回憶我們的秘密! 小春上"),
             TextSendMessage(
                text="「日記1」\n\n今天早上的時候我又遇見那隻黑斑貓，我今天餵他我的早餐地瓜，他全部吃光光了！\n他還對我說：\n「喵，喵，喵～喵～喵～」\n「喵～喵，喵，喵」"),
             ImageSendMessage("https://i.imgur.com/RoQgakz.png",
                              "https://i.imgur.com/RoQgakz.png"),
             ImageSendMessage("https://i.imgur.com/lxu1dMG.png",
                              "https://i.imgur.com/lxu1dMG.png"),
             TextSendMessage(
                text="（請輸入『OO』，前面為數字，後面是英文大寫字母）"),
             ]))
