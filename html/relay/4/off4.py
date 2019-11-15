import RPi.GPIO as GPIO
from time import sleep

led4 = 6
rel4 = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(rel4, GPIO.OUT)

GPIO.output(led4, False)
sleep(0.1)
GPIO.output(rel4, False)
