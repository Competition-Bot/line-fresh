from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api


def levelend_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(
                    text="「日記10」\n\n小花！恭喜你到達了這趟旅途的最後一站，雖然我們沒辦法像以前一樣到處冒險了，但是！跟你的回憶，我是一輩子都不會忘記的~經過這次的重溫之旅，我彷彿又跟你探險了一次呢！就算我搬家到了北部，我們還是要常常聯絡喔！"),
                TextSendMessage(
                    text="小花當時的冒險就到這邊結束了，回顧著他們倆的互動，我好像也回到了當時的虎尾！不知不覺，就進入了歷史文化的脈絡中。不知道她們倆現在過得怎樣，但我想她們也正在編織她們的人生冒險之旅吧！"),
                TextSendMessage(
                    text="系統回應：您完成了『虎尾手札 - 穿梭巷弄的少女』所有內容，恭喜您將進入專屬社群『虎尾大儒俠』,您的密碼為oeifejffe")
            ]
        ))
