from linebot.models import (
    TextSendMessage, FlexSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelnine_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(
                text="原來雲林記憶cool以前是虎尾登記所啊，現在這裡在賣刨冰跟飲料，在夏日來一碗清涼的日式刨冰，真是一大享受！"),
            FlexSendMessage(
                alt_text='雲林記憶cool',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "hero": {
                            "type": "image",
                            "url": "https://scontent.ftpe11-2.fna.fbcdn.net/v/t1.6435-9/s960x960/106779778_974176556357765_4994270149081776820_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=e3f864&_nc_ohc=ID1JwE5mvyEAX9bEeWE&_nc_ht=scontent.ftpe11-2.fna&oh=20e42055c8cb597e7f51ad6279c1de18&oe=61C135C5",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "20:14"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                                {
                                    "type": "text",
                                    "text": "雲林記憶cool",
                                    "wrap": True,
                                    "size": "md",
                                    "weight": "bold"
                                },
                            {
                                    "type": "text",
                                    "text": "虎尾登記所，原稱「台南地方法院虎尾出張所」，設立於1921年，主要為辦理地方不動產登記業務，管轄範圍涵蓋日治時期虎尾郡轄下各街庄。",
                                    "wrap": True,
                                    "size": "sm",
                                    "margin": "sm"
                                },
                            {
                                    "type": "text",
                                    "text": "隨著虎尾地區工商經濟蓬蓬發展，嘉南大圳完工通水，出現大量可耕地，原本的虎尾登記所辦公廳舍即因狹小不敷使用，遂於1930年搬遷擴建於今址。登記所內部儲存櫃完整，見證早期登記所的功能與意義，亦為日治時期土地產權制度的見證。",
                                    "wrap": True,
                                    "size": "sm",
                                    "margin": "sm"
                                },
                            {
                                    "type": "text",
                                    "text": "戰後登記所曾做為法院倉庫，現由社團法人台灣公益CEO協會經營使用，取名為雲林記憶Cool。",
                                    "wrap": True,
                                    "size": "sm",
                                    "margin": "sm"
                                }
                        ],
                        "offsetTop": "none",
                        "paddingAll": "lg"
                    },
                    "styles": {
                        "body": {
                            "separator": True
                        }
                    }
                }),
            FlexSendMessage(
                alt_text='日記6',
                contents={
                    "type": "bubble",
                    "size": "kilo",
                    "direction": "ltr",
                    "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "「日記6」",
                                    "wrap": True,
                                    "weight": "bold",
                                    "size": "md"
                                },
                                {
                                    "type": "text",
                                    "text": "哈哈你終於來到這啦史艷文，以前你心情不好時總是會躲到這裡偷偷的哭，我那時候為了逗你笑害我快累死啦！我們還一起想像我們在這裡登記了好多房子！對了！我們在這裡偷偷埋了時光膠囊，不知道你還記不記得？說好了等十年後再一起打開！",
                                    "wrap": True,
                                    "margin": "md",
                                    "size": "md"
                                },
                                {
                                    "type": "text",
                                    "text": "怕你這個小迷糊忘記了時光膠囊的密碼，在這裡提示你跟虎尾登記所的設立年份有關喔~",
                                    "wrap": True,
                                    "margin": "md",
                                    "size": "md"
                                }
                            ]
                    }
                }),
            TextSendMessage(
                text="( 請輸入時光膠囊密碼『OOOO』 )"),
        ]
    )
