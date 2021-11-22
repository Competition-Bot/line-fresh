from linebot.models import (
    MessageAction, ButtonsTemplate, TemplateSendMessage
)

from api.lineBotApi import line_bot_api


def start_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='虎尾手札 - 穿梭巷弄的少女',
            template=ButtonsTemplate(
                thumbnail_image_url='https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg',
                imageAspectRatio='rectangle',
                imageSize='cover',
                imageBackgroundColor='#FFFFFF',
                title='虎尾手札 - 穿梭巷弄的少女',
                text='小春與小欣是從小一起在虎尾長大的好朋友',
                actions=[
                    MessageAction(
                        label='開始遊戲',
                        text='開始遊戲'
                    ),
                ]
            )
        ))
