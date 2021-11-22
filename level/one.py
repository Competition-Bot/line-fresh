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
                text="（一封信件掉落） %0D%0A 給小欣： %0D%0A 我要搬家了，我很想念我們以前的冒險種種，我希望你可以跟著我的腳步，再次回憶我們的秘密! 小春上"),
             TextSendMessage(
                text="「日記1」 %0D%0A 今天早上的時候我又遇見那隻黑斑貓，我今天餵他我的早餐地瓜，他全部吃光光了！ %0D%0A 他還對我說： %0D%0A 「喵，喵，喵～喵～喵～」 %0D%0A 「喵～喵，喵，喵」"),
             ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                              "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
             ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                              "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
             TextSendMessage(
                text="（請輸入『OO』，前面為數字，後面是英文大寫字母）"),
             ]))
