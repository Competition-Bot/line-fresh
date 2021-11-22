from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelnine_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text="原來雲林記憶cool以前是虎尾登記所啊，現在這裡在賣刨冰跟飲料，在夏日來一碗清涼的日式刨冰，真是一大享受！"),
                TemplateSendMessage(
                    alt_text='雲林記憶cool',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://scontent.ftpe11-2.fna.fbcdn.net/v/t1.6435-9/s960x960/106779778_974176556357765_4994270149081776820_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=e3f864&_nc_ohc=ID1JwE5mvyEAX9bEeWE&_nc_ht=scontent.ftpe11-2.fna&oh=20e42055c8cb597e7f51ad6279c1de18&oe=61C135C5',
                        imageAspectRatio='rectangle',
                        imageSize='cover',
                        imageBackgroundColor='#FFFFFF',
                        title='雲林記憶cool',
                        text='雲林記憶cool，原名虎尾出張所或虎尾登記所，目前已經成為儲存雲林文史記憶以及虎尾重要景點之一',
                        actions=[
                            URIAction(
                                label='查看熱點資訊',
                                uri='https://miro.com/app/board/o9J_lwl7Qi0=/'
                            )
                        ]
                    )
                ),
                TextSendMessage(
                    text="「日記6」\n\n哈哈你終於來到這啦史艷文，以前你心情不好時總是會躲到這裡偷偷的哭，我那時候為了逗你笑害我快累死啦！我們還一起想像我們在這裡登記了好多房子！對了！我們在這裡偷偷埋了時光膠囊，不知道你還記不記得？說好了等十年後再一起打開！\n\n怕你這個小迷糊忘記了時光膠囊的密碼，在這裡提示你跟虎尾登記所的設立年份有關喔~"),
                TextSendMessage(
                    text="(請輸入時光膠囊密碼『OOOO』)"),
            ]
        ))
