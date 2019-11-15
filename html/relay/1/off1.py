import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(26, False)
sleep(0.1)
GPIO.output(21, False)
