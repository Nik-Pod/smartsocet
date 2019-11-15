import RPi.GPIO as GPIO
from time import sleep

led2 = 19
rel2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(rel2, GPIO.OUT)

GPIO.output(led2, True)
sleep(0.1)
GPIO.output(rel2, True)
