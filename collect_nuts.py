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
    send('Button HOME', 0.2)
    sleep(0.8)
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
    sleep(0.7)
    send('Button HOME', 0.1)
    sleep(1.0)


def getnuts():
    send('LY MIN', 0.1) # 上を向く
    sleep(0.1)
    send('Button A', 0.1)
    sleep(0.2)
    send('Button A', 0.1)
    sleep(0.2)
    send('Button A', 0.1)
    sleep(4)

    send('Button A', 0.1) # 収穫一回目
    sleep(1.5)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('Button A', 0.1)
    sleep(1.5)
    send('LY MAX', 0.1) # もっと揺らす
    sleep(0.1)
    send('Button A', 0.1) # Get 3 nuts
    sleep(1.5)
    send('LY MAX', 0.1) # もっと揺らす
    sleep(0.1)
    send('Button A', 0.1) # Get 3 nuts
    sleep(1.5)
    send('Button A', 0.1) # Get 3 nuts
    sleep(1.5)
    send('LY MAX', 0.1) # もっと揺らす
    sleep(0.1)
    send('Button A', 0.1) # Get 3 nuts
    sleep(1.5)
    send('LY MAX', 0.1) # もっと揺らす
    sleep(0.1)
    send('Button A', 0.1) # Get 3 nuts
    sleep(1)
    # send('LY MAX', 0.1) # もっと揺らす
    # sleep(1)

sleep(2)
send('Button LCLICK', 0.2)
sleep(2)

try:
    while 1:
        getnuts()
        daychange()

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
