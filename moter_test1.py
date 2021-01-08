import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO4を出力端子設定
GPIO.setup(4, GPIO.OUT)

#GPIO4をPWM設定、周波数は50Hz
p = GPIO.PWM(4, 50)

#Duty Cycle 0%
p.start(0.0)

#-90°の位置へ移動
p.ChangeDutyCycle(2.5)
time.sleep(1.0)
#少しずつ回転
for degree in range(-90, 91):
    dc = 2.5 + (12.0-2.5)/180*(degree+90)
    p.ChangeDutyCycle(dc)
    time.sleep(0.03)
    p.ChangeDutyCycle(0.0)#一旦DutyCycle0%にする

GPIO.cleanup()