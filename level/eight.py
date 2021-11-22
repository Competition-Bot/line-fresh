from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def leveleight_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text="日記本提到的答案的確是屋敷呢，但現在好像改建成雲林故事館了，去那邊看看吧！"),
                TemplateSendMessage(
                    alt_text='雲林故事館',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i2.wp.com/img.journey.tw/20180408220323_54.jpg?resize=1100%2C730&ssl=1',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        title='雲林故事館',
                        text='過去為郡守官邸，現作為雲林故事館，集合在地生活、藝術、教育、文化，並典藏本土文學作家的文學作品',
                        actions=[
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://liff.line.me/1582347558-VdW5GZDw/detail/629478315530393395?utm_campaign=629478315530393395&utm_medium=CopyURL&utm_source=Share'
                            )
                        ]
                    )
                ),
                TextSendMessage(
                    text="「日記5」\n\n我們每次下課後常常在官邸畫畫呢，一邊吃我們最愛的烤地瓜，一邊想我們的『虎尾大儒俠』，啊!我還記得我把結局放在官邸的門牌後面喔！"),
                ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                                 "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
                TextSendMessage(
                    text="(輸入『OOOO』OOOO是大寫英文字母)"),
            ]
        ))
