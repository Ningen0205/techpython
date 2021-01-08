import nfc
import binascii
import os
import RPi.GPIO as GPIO
import time

path = f"{os.getcwd()}/allowCardLists.txt"

with open(path) as f:
    cards = f.readlines()
    cards = [i.replace('\n','') for i in cards]

def connected(tag):
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


#clf.connect(rdwr={'on-connect': connected})
#clf.close()

while True:
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': connected})
