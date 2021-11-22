from linebot.models import (
    TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction
)

from api.lineBotApi import line_bot_api


def levelzero_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text="我是一個到處旅行的旅人，這天，我來到了虎尾旅行，走著走著我在地上撿到了一本日記本"),
                TemplateSendMessage(
                    alt_text='陳舊的日記本',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        text='陳舊的日記本',
                        actions=[
                            MessageAction(
                                label='開啟日記',
                                text='開啟日記'
                            ),
                        ]
                    )
                )
            ]
        ))
