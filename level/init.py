from linebot.models import (
    MessageAction, ButtonsTemplate, TemplateSendMessage
)

from api.lineBotApi import line_bot_api


def init_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='虎尾手札 - 穿梭巷弄的少女',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i2.wp.com/ivychi.com/wp-content/uploads/20201104123257_57.jpg',
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
