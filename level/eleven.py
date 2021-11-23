from linebot.models import (
    TextSendMessage,  FlexSendMessage, CarouselContainer, TemplateSendMessage, BubbleContainer, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def leveleleven_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(
                text="原來虎珍的前身是正義百貨行，真是一棟有歷史的建築！"),
            TemplateSendMessage(
                alt_text='看板模糊圖',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/0Y7WXxz.jpg',
                    imageAspectRatio='rectangle',
                    imageSize='cover',
                    imageBackgroundColor='#FFFFFF',
                    text='請依照虎珍糖右手邊的看板獲得線索，輸入『OOOOO』，OOOOO是五個英文字母',
                )
            ),
        ]
    )
