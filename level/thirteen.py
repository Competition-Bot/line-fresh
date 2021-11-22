from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelthirteen_one_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TemplateSendMessage(
                    alt_text='虎尾鐵橋',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Huwei_Dual_gauge_track_bridge_01.jpg/288px-Huwei_Dual_gauge_track_bridge_01.jpg',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        title='虎尾鐵橋',
                        text='虎尾糖廠鐵橋，舊名番薯莊板仔橋，於台灣日治時期興建並於國民政府時代延建，為雲林縣縣定古蹟。',
                        actions=[
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://spot.line.me/detail/720382419873591332'
                            )
                        ]
                    )
                ),
                TextSendMessage(
                    text="「日記9」\n\n這是最後一個謎題啦~我們以前最喜歡模仿電視上的主持人玩遊戲了！接下來進入快問快答時間~！"),
                TextSendMessage(
                    text="「虎尾鐵橋總共有幾個叉叉?」\n(請輸入數字)"),
                ImageSendMessage("https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg",
                                 "https://ithelp.ithome.com.tw/upload/images/20200111/201068658m7crqYkfm.jpg"),
            ]
        ))


def levelthirteen_two_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="「虎珍堂的虎月燒總共有幾種口味？」\n(請輸入數字)"),
        ))

def levelthirteen_three_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="「虎尾糖廠唯一載運甘蔗的車種是哪種呢？」\n(請輸入『OOO』,OOO是車種名)"),
        ))
