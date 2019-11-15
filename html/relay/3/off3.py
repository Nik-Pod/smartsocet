import RPi.GPIO as GPIO
from time import sleep

led3 = 13
rel3 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(rel3, GPIO.OUT)

GPIO.output(led3, False)
sleep(0.1)
GPIO.output(rel3, False)
