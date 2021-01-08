import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)


servo = GPIO.PWM(gp_out, 50)


servo.start(0)
#time.sleep(1)

servo.ChangeDutyCycle(2)

time.sleep(3)


servo.stop()
GPIO.cleanup()