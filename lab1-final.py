import numpy as np
import cv2
LED_PIN = 15
PWM_PIN = 25
DUTY_CYCLE = 50
FREQUENCY = 100
ANGLE = 0
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)
import time

def setServoAngle(angle):
	pwm = GPIO.PWM(PWM_PIN, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	time.sleep(0.3)
	pwm.stop()

faceCascade = cv2.CascadeClassifier('testFaceRecognition.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5
        ,     
        minSize=(20, 20)
    )

    if len(faces) == 0:
        GPIO.output(LED_PIN,False)
    else:
        setServoAngle(ANGLE)
        ANGLE += 15
        GPIO.output(LED_PIN,True) 


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
pwmOutput_0.stop()
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()