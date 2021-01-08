import subprocess
import logging
import threading
import time
import os
import RPi.GPIO as GPIO
import nfc
import binascii
import datetime

line = ""
path = f"/home/harano/Documents/project/mysite/allowCardLists.txt"
cards = []

clf = nfc.ContactlessFrontend('usb')


def get_card_list():
    global cards
    with open(path) as f:
        cards = f.readlines()
        cards = [i.replace('\n','') for i in cards]

def reader():
    global line
    filename ="/home/harano/Documents/project/mysite/command.log.txt"
    while True:
        line = subprocess.check_output(['tail', '-1', filename]).decode('utf-8')
        time.sleep(1)

def loop():
    global line
    while True:
        try:
            #print(f"{line}")
            if line != '':
                print(f"{datetime.datetime.now()} waiting...")
                clf.connect(rdwr={'on-connect': connected})
            else:
                print('error')
            time.sleep(1)
        except KeyboardInterrupt:
            clf.close()
            break

def auth_connected(tag):
    print(f"{datetime.datetime.now()} auth_connected")
    idm = binascii.hexlify(tag.idm).decode('utf-8')
    print(idm)
    for card in cards:
        card.encode('utf-8')
        if card == idm:
            GPIO.setmode(GPIO.BCM)
            gp_out = 4
            GPIO.setup(gp_out, GPIO.OUT)
            servo = GPIO.PWM(gp_out, 50)
            servo.start(0)
            servo.ChangeDutyCycle(10.5)
            time.sleep(10.5)
            servo.stop()
            GPIO.cleanup()
    return False

def add_connected(tag):
    print(f"{datetime.datetime.now()} add_connected")
    newflg = True
    idm = binascii.hexlify(tag.idm).decode('utf8')
    print(idm)
    for card in cards:
        card.encode('utf-8')
        if card == idm:
            newflg = False
        else:
            pass
    if newflg:
        print(f"{datetime.datetime.now()} new card!")
        with open(path, mode='a+') as f:
            f.write(f"\n{idm}")
    return False

def connected(tag):
    with open(path) as f:
        cards = f.readlines()
        cards = [i.replace('\n','') for i in cards]
    print(f"{datetime.datetime.now()} connected Mode:{line}")
    if line == 'add':
        newflg = True
        idm = binascii.hexlify(tag.idm).decode('utf8')
        print(idm)
        for card in cards:
            card.encode('utf-8')
            if card == idm:
                newflg = False
            else:
                pass
        if newflg:
            print(f"{datetime.datetime.now()} new card!")
            with open(path, mode='a+') as f:
                f.write(f"\n{idm}")
        return False
    elif line == 'auth':
        idm = binascii.hexlify(tag.idm).decode('utf-8')
        print(idm)
        for card in cards:
            card.encode('utf-8')
            if card == idm:
                GPIO.setmode(GPIO.BCM)
                gp_out = 4
                GPIO.setup(gp_out, GPIO.OUT)
                servo = GPIO.PWM(gp_out, 50)
                servo.start(0)
                servo.ChangeDutyCycle(10.5)
                time.sleep(10.5)
                servo.stop()
                GPIO.cleanup()
        return False
    

if __name__ == '__main__':
    t1 = threading.Thread(target=reader)
    t2 = threading.Thread(target=loop)
    get_card_list()
    t1.start()
    t2.start()