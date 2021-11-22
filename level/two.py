from linebot.models import (
    TextSendMessage, ImageSendMessage,TemplateSendMessage,ButtonsTemplate,URIAction
)

from api.lineBotApi import line_bot_api


def leveltwo_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TemplateSendMessage(
                    alt_text='虎尾厝沙龍',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i2.wp.com/ivychi.com/wp-content/uploads/20201104123257_57.jpg',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        title='虎尾厝沙龍',
                        text='虎尾厝沙龍，原為1940年吳中醫師興建的「和洋式住宅」，現為「獨立冊店」，積極關注台灣社會及世界脈動。',
                        actions=[
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://liff.line.me/1582347558-VdW5GZDw/detail/486258846029846639?utm_campaign=486258846029846639&utm_medium=CopyURL&utm_source=Share'
                            )
                        ]
                    )
                ),
                TextSendMessage(
                    text="原來這裡就是虎尾厝沙龍呀，啊!這個是藝術家王忠龍的石頭鳥鐵雕圍牆"),
                ImageSendMessage("https://i.imgur.com/IU3w7Kf.png",
                                 "https://i.imgur.com/IU3w7Kf.png"),
                TextSendMessage(
                    text="（請輸入『有Ｏ隻石頭鳥』，可以參考上方示意圖，至實際場景中詳細觀看）"),
            ]))
