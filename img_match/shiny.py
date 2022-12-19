from multiprocessing import Process, Value, Queue
from time import sleep

import cv2
import serial

## Pythonでマルチプロセスしながらカメラ映せたし消せた

def send(msg, ser, duration=0):
    """serial sender"""
    print(msg)
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

def restart(ser):
    sleep(0.3)
    send('Button HOME', ser, 0.1)
    sleep(0.8)
    send('Button X', ser, 0.1)
    sleep(0.4)
    send('Button A', ser, 0.1)
    sleep(3.0)

    send('Button A', ser, 0.1)
    sleep(1.0)
    send('Button A', ser, 0.1)
    sleep(18.0)
    send('Button A', ser, 0.1)
    sleep(7.5)

def controlloer(fin_flag, req_q, img_q) -> None:
    print('Regieleki Get Plugin loaded!')
    count = 0
    with serial.Serial('COM6', 9600) as ser:
        send('Button B', ser, 0.1)
        sleep(0.1)
        send('Button B', ser, 0.1)
        sleep(0.1)
        while 1:
            count += 1
            print('counter: ', count)

            # Talk to regieleki
            send('Button A', ser, 0.1)
            sleep(0.7)
            send('Button A', ser, 0.1)
            sleep(0.4)
            send('Button A', ser, 0.1)
            sleep(11.5)
            req_q.put(1)
            w_area = img_q.get()

            if 4 < w_area and w_area < 5:
                restart(ser)
            else:
                print('finish!')
                break
    fin_flag.value = True

def calc_black_whiteArea(bw_image):
    image_size = bw_image.size
    whitePixels = cv2.countNonZero(bw_image)
    blackPixels = bw_image.size - whitePixels

    whiteAreaRatio = (whitePixels/image_size)*100#[%]
    blackAreaRatio = (blackPixels/image_size)*100#[%]

    return whiteAreaRatio

def main():
    flag = Value('b', False)
    req_q = Queue()
    img_q = Queue()
    controller_p = Process(target=controlloer, args=(flag, req_q, img_q))
    capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    controller_p.start()
    counter = 0

    while(not flag.value):
        ret, frame = capture.read()
        if not ret:
            print('failed to capture')
            break
        windowsize = (800, 600)
        frame = cv2.resize(frame, windowsize)

        if not req_q.empty():
            _ = req_q.get()
            gray = cv2.cvtColor(frame[480:580, 0:400], cv2.COLOR_RGB2GRAY)
            ret, bw_image = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
            cv2.imshow('text_area', bw_image)
            counter = 0
            img_q.put(calc_black_whiteArea(bw_image))
        counter += 1
        if counter == 100:
            cv2.destroyWindow('text_area')

        cv2.imshow('capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
    controller_p.join()

if __name__ == "__main__":
    main()
