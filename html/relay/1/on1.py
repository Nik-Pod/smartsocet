import RPi.GPIO as GPIO
from time import sleep

led1 = 26
rel1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(rel1, GPIO.OUT)

GPIO.output(led1, True)
sleep(0.1)
GPIO.output(rel1, True)
