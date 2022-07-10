from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('F04h862wfsGOg88QyfvlDhU0lNnrsH/5XUlqwkY+a3UzPy5NVCNZAyUAicX8qBIBR3HcfY/pfptUop3psNzAX20F8I8XpVZE02BMPbStN09C8+rdcs80q333L3ZgJv0y8s0Ym16lMEq74LDMTjoTKAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0ac4e1f1e7546aec14b1f467c68b02ba')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "sing":
        text="OK"
        message=TextSendMessage(text=text)
        line_bot_api.reply_message(event.reply_token, message)
        tones = { "B0": 31,
        "C1": 33, "D1": 37, "E1": 41, "F1": 44, "G1": 49, "A1": 55, "B1": 62,
        "C2": 65, "D2": 73, "E2": 82, "F2": 87, "G2": 98, "A2": 110, "B2": 123,
        "C3": 131, "D3": 147, "E3": 165, "F3": 175, "G3": 196, "A3": 220, "B3": 247,
        "C4": 262, "D4": 294, "E4": 330, "F4": 349, "G4": 392, "A4": 440, "B4": 494,
        "C5": 523, "D5": 587, "E5": 659, "F5": 698, "G5": 784, "A5": 880, "B5": 988,
        "C6": 1047, "D6": 1175, "E6": 1319, "F6": 1397, "G6": 1568, "A6": 1760, "B6": 1976,
        "C7": 2093, "D7": 2349, "E7": 2637, "F7": 2794, "G7": 3136, "A7": 3520, "B7": 3951,
        "C8": 4186, "D8": 4699}

        import RPi.GPIO as GPIO
        import time
        pitches=[tones["C4"],tones["C4"],tones["G4"],tones["G4"],tones["A4"],tones["A4"],tones["G4"],tones["F4"],tones["F4"],tones["E4"],tones["E4"],tones["D4"],tones["D4"],tones["C4"]]
        duration=[1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13,GPIO.OUT)
        buzz = GPIO.PWM(13,100)
        buzz.start(0)
        x=0
        for p in pitches:
            buzz.ChangeFrequency(p*2)
            buzz.ChangeDutyCycle(50)
            time.sleep(duration[x]*0.5)
            buzz.ChangeDutyCycle(100)
            time.sleep(0.015)
            x+=1
        buzz.stop()
        GPIO.cleanup()
    else:
        text="Please try again"
        message=TextSendMessage(text=text)
        line_bot_api.reply_message(event.reply_token, message)
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
