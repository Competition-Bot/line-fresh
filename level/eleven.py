from linebot.models import (
    TextSendMessage,  FlexSendMessage, CarouselContainer, TemplateSendMessage, BubbleContainer, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def leveleleven_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            [
                TemplateSendMessage(
                    alt_text='虎珍堂',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://joes.tw/wp-content/uploads/20190719193350_27.jpg',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        title='虎珍堂',
                        text='虎珍堂菓寮店～70年日治時代老屋風華再現，用地瓜與乳酪蛋糕做成散步美食「虎月燒」！',
                        actions=[
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://liff.line.me/1582347558-VdW5GZDw/detail/486254094835523175?utm_campaign=486254094835523175&utm_medium=CopyURL&utm_source=Share'
                            )
                        ]
                    )
                ),
            ]
        ))
