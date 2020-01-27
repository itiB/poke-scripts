#!/usr/bin/env python3

# 条件
# - 1つ目のたまごができている
# - 手持ちがほのおのからだのポケモンのみ
# - ボックスに十分なあきがある
# - ハシノマ原っぱにいる
# - メニューのカーソルがMapになっている
# - 自転車に乗っている

import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--cycle', type = int, default = 20)
parser.add_argument('--count', type = int, default = 60)
args = parser.parse_args()

ser = serial.Serial(args.port, 9600)

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

# 空を飛ぶ
def fly():
    send('Button X', 0.1)
    sleep(1)
    send('Button A', 0.1)
    sleep(2.5)
    send('Button A', 0.1)
    sleep(0.5)
    send('Button A', 0.1)
    sleep(3)

# たまごをもらう
def receiveEgg():
    fly()

    send('LY MAX', 0.7)     # 育て屋さんへ移動
    send('LX MAX', 0.2)
    sleep(0.5)

    send('Button A', 0.1)   # キミのポケモンが…
    sleep(0.5)
    send('Button A', 0.1)   # 欲しいですよね
    sleep(0.5)
    send('Button A', 0.1)   # はい
    sleep(3)
    send('Button A', 0.1)   # 預け屋さんからタマゴをもらった
    sleep(2.5)
    send('Button A', 0.1)   # 手持ちに加えました
    sleep(1.5)
    send('Button A', 0.1)   # 大事に育ててくださいね
    sleep(0.2)

def runAround(laps):
    fly()
    send('LX MAX', 1)
    for lap in range(0, int(laps)):
        print(f'{lap + 1}周目')
        send('RXLY MIN', 4.02)   # 1周

def hatchEgg():
    global hatched_eggs

    send('Button B', 0.1)               # おや？
    sleep(16)
    send('Button B', 0.1)               # おめでとう
    sleep(4)
    hatched_eggs = hatched_eggs + 1
    print(f'{hatched_eggs}つ目のたまご孵化完了 ({round(time.time() - start_time, 2)}秒経過)')

def get5eggs():
    # pastlaps = 0                      # いままで回った回数を記録
    action_cycle = args.cycle * 0.4     # アクション起こすまでのサイクル数

    receiveEgg()                        # 1つ目のたまごをもらう

    for i in range(0, 6):
        runAround(action_cycle)
        if( i > 0 ):
            hatchEgg()
        if( i < 4 ):
            receiveEgg()

def sendToBox():
    global hatched_eggs

    send('Button X', 0.1)       # メニュー画面
    sleep(1)
    send('LX MAX', 0.1)         # 右
    sleep(0.1)
    send('LY MIN', 0.1)         # 上
    sleep(0.1)
    send('Button A', 0.1)       # ポケモン
    sleep(2)
    send('Button R', 0.1)       # ボックスを開く
    sleep(2)

    if ( hatched_eggs % 30 == 0):
        send('LY MIN', 0.1)     # ボックス名
        sleep(0.1)
        send('Button R', 0.1)   # 移動
        sleep(0.1)
        send('LY MAX', 0.1)     # 戻る

    send('LX MIN', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)         # タマゴにカーソル
    sleep(0.1)
    send('Button Y', 0.1)
    sleep(0.1)
    send('Button Y', 0.1)       # 複数選択モード
    sleep(0.1)
    send('Button A', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('Button A', 0.1)       # 全選択完了
    sleep(0.1)

    send('LX MAX', 0.1)         # 右
    sleep(0.1)
    send('LY MAX', 0.1)         # 下 4回
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('Button A', 0.1)       # ボックス一覧
    sleep(0.5)
    send('Button A', 0.1)       # ボックスに置く
    sleep(0.5)
    send('Button B', 0.1)       # もどる
    sleep(0.1)
    send('Button B', 0.1)       # もどる
    sleep(2)

    send('Button B', 0.1)       # メニュー画面
    sleep(1.5)
    send('LY MAX', 0.1)
    sleep(0.1)
    send('LX MIN', 0.1)
    sleep(0.1)
    send('Button B', 0.1)       # もどる
    sleep(1.5)


start_time = time.time()
hatched_eggs = 0

sleep(2)
send('Button LCLICK', 0.5)

try:
    while hatched_eggs < args.count:
        get5eggs()
        sendToBox()

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()