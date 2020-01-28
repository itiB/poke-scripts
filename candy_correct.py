#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
args = parser.parse_args()

sleep_time = 50

def send(msg, duration=0):
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)


def candyCorrect():
    send('LY MAX', 0.1)
    sleep(0.3)
    send('Button A', 0.1)
    sleep(1)
    send('Button B', 0.1)
    sleep(0.8)
    send('LY MIN', 0.1)
    sleep(0.5)
    send('Button A', 0.1)
    sleep(0.3)
    send('LY MAX', 0.1)
    sleep(0.2)
    send('Button A', 0.1)
    sleep(0.3)
    send('Button A', 0.1)
    sleep(0.3)
    send('Button A', 0.1)
    sleep(2.5)
    send('Button A', 0.1)
    sleep(1.0)
    send('Button A', 0.1)
    for i in range(0, sleep_time):
        sleep(1)
        if i % 10 == 0:
            print(f'あと {sleep_time - i}秒 スリープします')


sleep(3)
send('Button LCLICK', 0.1)

try:
    while 1:
        candyCorrect()

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
