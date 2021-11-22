from linebot.models import (
    TextSendMessage, ImageSendMessage,TemplateSendMessage,ButtonsTemplate,URIAction
)

from api.lineBotApi import line_bot_api


def levelfour_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TemplateSendMessage(
                    alt_text='合同廳舍',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/igkuCI8.jpg',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        title='合同廳舍',
                        text='虎尾合同廳舍位於雲林縣虎尾鎮，係為台灣日治時期消防單位觀測轄區失火位置與完成通報之緊急救災建築物。',
                        actions=[
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://liff.line.me/1582347558-VdW5GZDw/detail/532301960250921592?utm_campaign=532301960250921592&utm_medium=CopyURL&utm_source=Share'
                            )
                        ]
                    )
                ),
                TextSendMessage(
                    text="「日記3」 %0D%0A 你找對地方了，史艷文，還記得我們以前常常大鬧警局嗎，還會偷偷溜消防廳的天梯呢，嘻嘻 %0D%0A 我偷偷留了下一個地方的線索，合同廳舍裡面有一個會飛的動物呦！"),
                TemplateSendMessage(
                    alt_text='合同廳舍',
                    template=ButtonsTemplate(
                        text='你還記得我們少了幾支羽毛嗎? %0D%0A (請輸入『少了O支』)',
                        actions=[
                            URIAction(
                                label='打開相機辨識尋找物件',
                                uri='https://miro.com/app/board/o9J_lwl7Qi0=/'
                            )
                        ]
                    )
                ),
            ]))
