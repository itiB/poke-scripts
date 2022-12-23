#!/usr/bin/env python3
import argparse
import serial
from time import sleep
import datetime

"""
COMMAND:
    `$ python3 sender.py COM??`
    ?? はデバイスマネージャで確認(USB Serial Portとして出てくる)

SETING:
    0. 'pip3 install pyserial'
    1. @PowerShell: Find out which port to connect. `usbipd wsl list`
    2. `usbipd wsl attach --distribution Ubuntu-20.04 --busid <BUSID>`
    3. Search connected USB list from`lsusb`
    4. `sudo chmod 777 /dev/ttyUSB0`
    Finaly: `usbipd wsl detach --busid <busid>`

USAGE:
    1. コライドンを手持ちの上から2番目に置いて6匹埋める
    2. ライド選択してライドフォルムに戻す
    3. ボックスを開いてボックス1に移動
    4. コマンドの実行 `python3 ./sv/item.py /dev/ttyUSB0 --loop 10`
"""

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('-l', '--loop', type=int, default=1)
args = parser.parse_args()

def send(msg, duration=0):
    now = datetime.datetime.now()
    print(f'{now}: {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)
sleep(2)
send('Button LCLICK', 0.1)

def main():
    count = 0

    try:
        for _ in range(0, args.loop):
            send('Button X', 0.2)
            sleep(0.2)
            send('Button X', 0.2)
            sleep(0.3)
            send('Button L', 0.2)
            sleep(0.3)

            # Select Koraidon
            send('Button A', 0.2)
            sleep(0.2)
            send('LY MIN', 0.2)
            sleep(0.2)
            send('LY MIN', 0.2)
            sleep(0.2)
            send('LY MIN', 0.2)
            sleep(0.2)
            send('Button A', 0.2)
            sleep(0.6)

            count += 1
            print("  counter: {}/{}".format(count, args.loop))

            # Close box
            send('Button B', 0.2)
            sleep(2.4)

            # Change to Ride form
            send('LX MIN', 0.2)
            sleep(0.4)
            send('Button A', 0.2)
            sleep(0.4)
            send('LY MIN', 0.2)
            sleep(0.2)
            send('LY MIN', 0.2)
            sleep(0.2)
            send('Button A', 0.2)
            sleep(0.9)
            send('Button A', 0.2)
            sleep(0.3)
            send('Button A', 0.2)
            sleep(2.7)
            send('Button A', 0.2)
            sleep(1.0)

            # Open Box
            send('LX MAX', 0.2)
            sleep(0.4)
            send('LY MAX', 0.2)
            sleep(0.2)
            send('LY MAX', 0.2)
            sleep(0.2)
            send('Button A', 0.2)
            sleep(3.0)

    except KeyboardInterrupt:
        print('Bye...')
        ser.close()

if __name__ == "__main__":
    main()
