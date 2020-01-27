#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
args = parser.parse_args()

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)


def daychange():
    send('Button HOME', 0.1)
    sleep(0.5)
    send('LY MAX', 0.1)
    sleep(0.2)
    send('LX MAX', 0.05)        # ゲームニュース
    sleep(0.05)
    send('LX MAX', 0.05)
    sleep(0.05)
    send('LX MAX', 0.05)
    sleep(0.05)
    send('LX MAX', 0.05)
    sleep(0.05)
    send('Button A', 0.05)      # 設定画面
    sleep(1)
    send('LY MAX', 1.5)         # 一番したまで突っ切る
    send('Button A', 0.05)
    sleep(0.05)
    send('LY MAX', 0.1)
    sleep(0.05)
    send('LY MAX', 0.1)
    sleep(0.05)
    send('LY MAX', 0.1)
    sleep(0.05)
    send('LY MAX', 0.1)
    sleep(0.05)
    send('Button A', 0.05)      # 日付と時刻ページへ
    sleep(0.2)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('Button A', 0.05)
    sleep(0.05)
    send('Button A', 0.05)      # 年
    sleep(0.05)
    send('Button A', 0.05)      # 月
    sleep(0.05)
    send('Button A', 0.05)      # 日
    sleep(0.05)
    send('LY MIN', 0.1)
    sleep(0.05)
    send('Button A', 0.05)   # 時
    sleep(0.05)
    send('Button A', 0.05)   # 分
    sleep(0.05)
    send('Button A', 0.05)   # OK
    sleep(0.05)
    send('Button A', 0.05)   # 現在の日付と時刻
    sleep(0.15)
    send('Button HOME', 0.1)
    sleep(0.5)
    send('Button HOME', 0.1)
    sleep(0.5)

def drawid():
    send('LY MIN', 0.1)
    sleep(0.1)
    send('LX MIN', 0.05)
    sleep(0.1)
    send('Button A', 0.1)
    sleep(0.5)
    send('Button A', 0.1)   # こんにちロ～
    sleep(0.5)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('Button A', 0.1)   # IDくじ
    sleep(0.8)
    send('Button A', 0.1)   # ただいま
    sleep(0.5)
    send('Button A', 0.1)   # 引いたくじと
    sleep(0.5)

    # くじが引けないときはここで下を向いて処理
    send('LY MAX', 0.1)
    sleep(0.5)

    send('Button A', 0.1)   # みごとあっていると
    sleep(0.5)
    send('Button A', 0.1)   # はい
    sleep(2)
    send('Button A', 0.1)   # 書き残した！
    sleep(0.5)
    send('Button A', 0.1)   # かしこまりロ～
    sleep(0.8)
    send('Button A', 0.1)   # ...
    sleep(0.5)
    send('Button A', 0.1)   # ハイ！でたロミ
    sleep(0.5)
    send('Button A', 0.1)   # どれだけあってるか
    sleep(0.5)
    send('Button A', 0.1)   # 調べてみるロ
    sleep(3)
    send('Button A', 0.1)   # おめでと～
    sleep(0.5)
    send('Button A', 0.1)   # ボックスに預けている
    sleep(0.5)
    send('Button A', 0.1)   # くじのナンバーと
    sleep(0.5)
    send('Button A', 0.1)   # ケタおんなじ
    sleep(0.5)
    send('Button A', 0.1)   # そんな...
    sleep(0.5)
    send('Button A', 0.1)   # プレゼントだロ
    sleep(3)
    send('Button A', 0.1)   # 手に入れた
    sleep(0.5)
    send('Button A', 0.1)   # しまった
    sleep(0.5)
    send('Button A', 0.1)   # それじゃまたの挑戦を
    sleep(0.5)

sleep(3)
send('Button LCLICK', 0.1)

try:
    while 1:
        daychange()
        drawid()

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
