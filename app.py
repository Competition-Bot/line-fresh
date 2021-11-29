import os
from flask import Flask, request, abort

from linebot import (
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    JoinEvent, MessageEvent, TextMessage,  TextSendMessage, BoxComponent, ImageSendMessage, MessageAction, URIAction, ButtonsTemplate, PostbackAction, TemplateSendMessage
)

from api.lineBotApi import line_bot_api
from level.error import Help_3, error_Nohelp, error_Nohelp, Help_1, Help_2
from level.start import start_message
from level.zero import levelzero_message
from level.one import levelone_message
from level.two import leveltwo_message
from level.three import levelthree_message
from level.four import levelfour_message
from level.five import levelfive_message
from level.six import levelsix_message
from level.seven import levelseven_message
from level.eight import leveleight_message
from level.nine import levelnine_message
from level.ten import levelten_message
from level.eleven import leveleleven_message
from level.twelve import leveltwelve_message
from level.thirteen import (levelthirteen_one_message,
                            levelthirteen_two_message, levelthirteen_three_message)
from level.end import levelend_message

app = Flask(__name__)


handler = WebhookHandler('dcc7f9bee687f90fe33cc309962f1210')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

level = 'init'
user_id = ''
help = "1"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global user_id
    global level
    global help
    user_id = event.source.user_id
    if((event.message.text == 'start' and level == 'init') or event.message.text == 'start'):
        start_message(event)
        level = 'start'
    elif((event.message.text == '開始遊戲' and level == 'start') or event.message.text == 'test0'):
        levelzero_message(event)
        level = '0'
    elif((event.message.text == '打開日記' and level == '0') or event.message.text == 'test1'):
        level = '1'
        help = '1'
        levelone_message(event)
    


    
    elif((event.message.text == '虎尾厝沙龍' and level == '1') or event.message.text == 'test2'):
        level = '2'
        help = '1'
        leveltwo_message(event)

    elif(((event.message.text == '有6隻石頭鳥' or event.message.text == '有六隻石頭鳥') and level == '2') or event.message.text == 'test3'):
        help = '1'
        level = '3'
        levelthree_message(event)
    elif((event.message.text == '前往合同廳舍' and level == '3') or event.message.text == 'test4'):
        level = '4'
        help = '1'
        levelfour_message(event)   
    elif(((event.message.text == '少了7隻' or event.message.text == '少了七隻') and level == '4') or event.message.text == 'test5'):
        level = '5'
        help = '1'
        levelfive_message(event)
    elif((event.message.text == '前往雲林布袋戲館' and level == '5') or event.message.text == 'test6'):
        level = '6'
        help = '1'
        levelsix_message(event)
    elif((event.message.text == '生、丑' and level == '6') or event.message.text == 'test7'):
        level = '7'
        help = '1'
        levelseven_message(event)
    elif((event.message.text == '屋敷' and level == '7') or event.message.text == 'test8'):
        level = '8'
        help = '1'
        leveleight_message(event)
    elif(((event.message.text == 'COOL' or event.message.text == 'cool') and level == '8') or event.message.text == 'test9'):
        level = '9'
        help = '1'
        levelnine_message(event)
    elif((event.message.text == '1921' and level == '9') or event.message.text == 'test10'):
        level = '10'
        help = '1'
        levelten_message(event)
    elif((event.message.text == '前往虎珍堂' and level == '10') or event.message.text == 'test11'):
        level = '11'
        help = '1'
        leveleleven_message(user_id)
    elif(((event.message.text == 'EADCB' or event.message.text == 'eadcb') and level == '11') or event.message.text == 'test12'):
        level = '12'
        help = '1'
        leveltwelve_message(event)
    elif(((event.message.text == '我搭14:00的區間車出發' or event.message.text == '我搭14：00的區間車出發') and level == '12') or event.message.text == 'test13'):
        level = '13-1'
        help = '1'
        levelthirteen_one_message(event)
    elif(((event.message.text == '8' or event.message.text == '八') and level == '13-1')):
        level = '13-2'
        help = '1'
        levelthirteen_two_message(event)
    elif(((event.message.text == '3' or event.message.text != '三') and level == '13-2')):
        level = '13-3'
        help = '1'
        levelthirteen_three_message(event)
    elif((event.message.text == '五分車' and level == '13-3') or event.message.text == 'end'):
        level = 'end'
        levelend_message(event)



    elif((event.message.text == '我需要幫忙' and level == '1')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        else:
            Help_2(event,level)
    elif((event.message.text != '虎尾厝沙龍' and level == '1')): #嘿嘿答錯
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '2')):
        if(help == '1'):
            Help_1(event)
            help = '2'
        else:
            Help_2(event)
    elif((event.message.text != '有6隻石頭鳥' and event.message.text != '有六隻石頭鳥' and level == '2')): #嘿嘿答錯
        error_Nohelp(event,help)
    
    


    elif((event.message.text == '我需要幫忙' and level == '3')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        else:
            Help_2(event,level)
    elif((event.message.text != '前往合同廳舍' and level == '3')): #嘿嘿答錯
        error_Nohelp(event,help)
    
    

    elif((event.message.text == '我需要幫忙' and level == '4')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        elif(help == '2'):
            Help_2(event,level)
            help = '3'
        elif(help == '3'):
            Help_3(event,level)
    elif(((event.message.text != '少了7隻' and event.message.text != '少了七隻') and level == '4')):
        error_Nohelp(event,help)


    

    elif((event.message.text == '我需要幫忙' and level == '5')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        elif(help == '2'):
            Help_2(event,level)
            help = '3'
        elif(help == '3'):
            Help_3(event,level)
    elif((event.message.text != '前往雲林布袋戲館' and level == '5')):
        error_Nohelp(event,help)
    

    
    elif((event.message.text == '我需要幫忙' and level == '6')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        else:
            Help_2(event,level)
    elif((event.message.text != '生、丑' and level == '6')):
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '7')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        elif(help == '2'):
            Help_2(event,level)
            help = '3'
        elif(help == '3'):
            Help_3(event,level)
    elif((event.message.text != '屋敷' and level == '7')):
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '8')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        elif(help == '2'):
            Help_2(event,level)
            help = '3'
        elif(help == '3'):
            Help_3(event,level)
    elif(((event.message.text != 'cool' and event.message.text != 'cool') and level == '8')):
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '9')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        else:
            Help_2(event,level)
    elif((event.message.text != '1921' and level == '9')):
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '10')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        elif(help == '2'):
            Help_2(event,level)
            help = '3'
        elif(help == '3'):
            Help_3(event,level)
    elif((event.message.text != '前往虎珍堂' and level == '10')):
        error_Nohelp(event,help)
    
    

    elif((event.message.text == '我需要幫忙' and level == '11')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        else:
            Help_2(event,level)
    elif(((event.message.text != 'EADCB' and event.message.text != 'eadcb') and level == '11')):
        error_Nohelp(event,help)
    

    
    elif((event.message.text == '我需要幫忙' and level == '12')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        elif(help == '2'):
            Help_2(event,level)
            help = '3'
        elif(help == '3'):
            Help_3(event,level)
    elif(((event.message.text != '我搭14:00的區間車出發' and event.message.text != '我搭14：00的區間車出發') and level == '12')):
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '13-1')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        else:
            Help_2(event,level)
    elif(((event.message.text != '8' and event.message.text != '八') and level == '13-1')):
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '13-2')):
        Help_1(event,level)
    elif(((event.message.text != '3' and event.message.text != '三') and level == '13-2')):
        error_Nohelp(event,help)
    


    elif((event.message.text == '我需要幫忙' and level == '13-3')):
        if(help == '1'):
            Help_1(event,level)
            help = '2'
        else:
            Help_2(event,level)
    elif((event.message.text != '五分車' and level == '13-3')):
        error_Nohelp(event,help)
    
    


@handler.add(JoinEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.push_message('<to>', TextSendMessage(text='Hello World!'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
