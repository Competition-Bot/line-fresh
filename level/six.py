from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelsix_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TemplateSendMessage(
                    alt_text='雲林布袋戲館',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/maIwW8X.jpg',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        title='雲林布袋戲館',
                        text='原為日本時代之台南州虎尾郡郡役所建築，九十六年起做為布袋戲介紹之展示館。',
                        actions=[
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://liff.line.me/1582347558-VdW5GZDw/detail/486255906888094199?utm_campaign=486255906888094199&utm_medium=CopyURL&utm_source=Share'
                            )
                        ]
                    )
                ),
                TextSendMessage(
                    text="「日記4」\n史艷文，看來你也還記得我們一起創造的的「虎尾大儒俠」呢！"),
                ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                                 "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
                TextSendMessage(
                    text="（參考生旦淨末丑的角色說明，推敲小春與小花自創的故事裡是「生、淨」的角色是什麼。）\n（請輸入『生、淨』, 按照順序回答人物名）")
            ]
        ))
