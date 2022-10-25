SERVO_PIN = 25

import sys
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0) 

def Setangle(angle):
    duty=angle/18+2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty) 
    sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

print("angel 0")
Setangle(0)
print("angel 45")
sleep(0.5)
Setangle(45)
print("angel 90")
sleep(0.5)
Setangle(30)
print("angel 190")
sleep(0.5)
Setangle(180)
sleep(0.5)
print("done")
GPIO.cleanup()