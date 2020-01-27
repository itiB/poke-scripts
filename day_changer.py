#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--count', type=int, default=30)
args = parser.parse_args()

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

sleep(1)
send('Button LCLICK', 0.1)

try:
    for i in range(0, args.count):
        print(f'{i + 1}日目')

        send('Button A', 0.05)   # 現在の日付と時刻
        sleep(0.15)
        send('LX MIN', 0.05)     # 分
        sleep(0.05)
        send('LX MIN', 0.05)     # 時
        sleep(0.05)
        send('LX MIN', 0.05)     # 日
        sleep(0.05)
        send('LY MIN', 0.05)     # 進める
        sleep(0.05)
        send('Button A', 0.05)   # 時
        sleep(0.05)
        send('Button A', 0.05)   # 分
        sleep(0.05)
        send('Button A', 0.05)   # OK
        sleep(0.05)
        send('Button A', 0.05)   # 現在の日付と時刻
        sleep(0.15)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
