from linebot.models import (
    MessageAction, URIAction, ButtonsTemplate, TemplateSendMessage
)


def join_message(line_bot_api, event):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='虎尾驛',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i2.wp.com/ivychi.com/wp-content/uploads/20201104123257_57.jpg',
                imageAspectRatio='rectangle',
                imageSize='cover',
                imageBackgroundColor='#FFFFFF',
                title='虎尾驛',
                text='虎尾驛為中華民國雲林縣虎尾鎮一已廢棄木造火車站，原是虎尾糖廠小火車車站。',
                actions=[
                    MessageAction(
                        label='查看日記',
                        text='查看日記'
                    ),
                    URIAction(
                        label='查看熱點資訊',
                        uri='https://spot.line.me/detail/720382419873591332'
                    )
                ]
            )
        ))
