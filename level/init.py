from linebot.models import (
    MessageAction, ButtonsTemplate, TemplateSendMessage
)


def init_message(line_bot_api, event):
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
                text='小春與小欣是從小一起在虎尾長大的好朋友，她們喜歡在巷弄間到處探險，藏著她倆的秘密，升上高中後小春將搬離虎尾去外地',
                actions=[
                    MessageAction(
                        label='開始遊戲',
                        text='開始遊戲'
                    ),
                ]
            )
        ))
