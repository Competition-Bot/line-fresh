from typing import Text
from linebot.models import (
    TextSendMessage, FlexSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
)

from api.lineBotApi import line_bot_api

def error_Nohelp(event,help):
    if( help == "1"):
        text = "嘿嘿~答錯嘍! 再好好想想吧! 需要幫助的話請輸入「我需要幫忙」"
    elif( help == "2"):
        text = "哎呀! 再仔細看看提示吧! 如果還需要幫助的話請輸入「我需要幫忙」"
    elif( help == "3"):
        text = "再好好地看看提示喔! 如果真的答不出來請再出輸入「我需要幫忙」"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text)
    )

def Help_1(event,level):
    if(level == '1'):
        text="好哇! 你可以觀察喵喵叫聲的變化，看看跟摩斯密碼表有沒有相似的地方" 
    
    elif(level == '2'):
        text= "好哇! 到「虎尾厝沙龍」的門口右側，數數看共有幾個石頭鳥吧！"
    
    elif(level == '3'):
        text= "好哇! 有沒有看到紙張上方的數字呢?數數看對應到的文字，看看得到什麼線索吧!"
    
    elif(level == '4'):
        text= "好哇! 打開相機了嗎？打開相機後有一個鳥兒的塗鴉，是不是跟合同廳舍的某個標誌很像呢？"
    
    elif(level == '5'):
        text= "好哇! 找到合同廳的門牌號碼了嗎?數字為「491」，那麼跟電台節目表有什麼關係呢?"
    
    elif(level == '6'):
        text= "好哇! 「生」是指一般常見的男性角色喔!「丑」角通常都有很滑稽表現~"
    
    elif(level == '7'):
        text= "好哇! 第4遍的1A1B遊戲得到什麼結果呢?跟文字密碼表有什麼關係?"
    
    elif(level == '8'):
        text= "好哇! 從官邸的門牌可以獲得528這三個數字，跟爬梯子這張圖片有什麼關係呢？"
    
    elif(level == '9'):
        text= "好哇! 密碼為虎尾登記所的設立年分，查查看資料看看是多少吧!"
    
    elif(level == '10'):
        text= "好哇! 將數獨圖解開，看看有顏色的地方對應到什麼數字，再看跟文字表格有什麼關係吧!"
    
    elif(level == '11'):
        text= "好哇! 看板上面寫了好多非常火紅的商品，依照商品出現順序去想想對應的英文字母要怎麼排列吧!"
    
    elif(level == '12'):
        text= "好哇! 把其中一串數字放進九宮格中連起來，似乎得到了一個數字圖形"

    elif(level == '13-1'):
        text= "好哇! 虎尾鐵橋有8個叉叉，你算對了嗎?輸入「8」來進入下一個謎題"
    
    elif(level == '13-2'):
        text= "好哇! 虎珍堂的菜單上有3種口味的虎月燒，輸入「3」進入下一個謎題!"

    elif(level == '13-3'):
        text= "好哇! 把其中一串數字放進九宮格中連起來，似乎得到了一個數字圖形"
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text)
    )

def Help_2(event,level):
    if( level == '1'):
        text = "好哇! 喵喵叫聲的變化，可以分別對應摩斯密碼表中的4和B，那4B對應到地圖的什麼地方呢?"
    
    elif(level== '2'):
        text = "好哇! 1,2,3....總共有7隻!輸入「有7隻石頭鳥」來進行下一關吧！"
    
    elif(level == '3'):
        text= "好哇! 對應到的文字為「合同廳舍」，輸入「前往合同廳舍」，進行下一關吧!"
    
    elif(level == '4'):
        text= "好哇! 還是找不到嗎？鳥兒在合同廳舍的誠品書店門口喔！"
    
    elif(level == '5'):
        text= "好哇! 節目表裡只有「91.4」跟門牌號碼有關係吧!那麼收音機轉到「91.4」頻道，聽聽看撥放出什麼內容吧!"
    
    elif(level == '6'):
        text= "好哇! 小花:嘻嘻，我們把男主角OOO也描述得太帥了吧! 小春:可是XXX超級好笑的 "
    
    elif(level == '7'):
        text= "好哇! 第4遍1A1B遊戲得到「3A0B」，對應到文字密碼表中的什麼文字呢?"
    
    elif(level == '8'):
        text= "好哇! 2連到O，5連到Ｃ，8連到L咦？英文字母下面的圖形跟上面的四個圖形是什麼關係？"
    
    elif(level == '9'):
        text= "好哇! 虎尾登記所在1921年設立，輸入「1921」進入下一關吧!"
    
    elif(level == '10'):
        text= "好哇! 有沒有注意到顏色有深淺之分呢?試試看將同一個色系的深淺色數字對應到表格中，可以得到什麼文字內容 "
    
    elif(level == '11'):
        text= "好哇! 商品出現的順序是「E：...」、「A:...」、「D:...」、「C:...」、「B:...」，輸入「EADCB」進入下一個關卡吧!"
    
    elif(level == '12'):
        text= "好哇! 四串數字放進九宮格，獲得了2077數字，對應到時刻表的車次，是哪一班呢？"
    
    elif(level == '13-1'):
        text= "好哇! 虎尾鐵橋有8個叉叉，你算對了嗎?輸入「8」來進入下一個謎題"

    elif(level == '13-3'):
        text= "好哇! 答案為五分車，你找到了嗎?輸入「五分車」完成謎題吧!"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text)
    )

def Help_3(event,level):
    if(level == "4"):
        text= "好哇! 比對塗鴉與實際物件，好像少了7根羽毛！輸入「少了7支」來進行下一關吧！"
    elif(level == "5"):
        text= "好哇! 收音機播放出「雲林布袋戲館」，輸入「前往雲林布袋戲館」，進入下一關吧!"
    elif(level == "7"):
        text= "好哇! 可以在文字密碼表中3A和0B的位置分別得到「屋」「敷」，輸入「屋敷」進入下一個關卡吧!"
    elif(level == "8"):
        text= "好哇! 一個圓形（Ｃ），兩個三角形（Ｏ），一個菱形（Ｌ）合起來就是cool!輸入「cool」來進行下一關吧！"
    elif(level == "10"):
        text= "好哇! 紅色得到「虎」，黃色得到「堂」，藍色得到「珍」，輸入「前往虎珍堂」進入下一個關卡吧!"
    elif(level == "12"):
        text= "好哇! 2077對應到14:00的區間車，輸入「我搭14:00的區間車出發」進入下一關吧!"
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text)
    )