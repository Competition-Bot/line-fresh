from linebot.models import (
    TextSendMessage, ImageSendMessage,TemplateSendMessage,ButtonsTemplate,URIAction
)

from api.lineBotApi import line_bot_api


def levelthree_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                FlexSendMessage(
                alt_text='日記2',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "direction": "ltr",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "「日記2」",
                                "wrap": True,
                                "weight": "bold",
                                 "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "這裡是吳哥哥的家，還記得以前他總是告訴我們許多好玩的醫學故事，我們聽的超級開心的!前幾年他考上大學就在北部念書了，不知道他過得好不好，不過我相信他一定是個好醫生的!",
                                "wrap": True,
                                "margin": "md",
                                "size": "md"
                            },
                            {
                                "type": "text",
                                "text": "還記得以前中午一到我們就會守在電視機前面，看史艷文如何化解難關，以下的暗號，我想你一定看得懂吧，我們老地方見~",
                                "wrap": True,
                                "margin": "sm",
                                "size": "md"
                            }
                        ]
                    }
                }),
                ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                                 "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
                TextSendMessage(
                    text="( 請輸入『前往OOOO』 )"),
            ]))
