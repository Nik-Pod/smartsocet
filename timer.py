import RPi.GPIO as GPIO
from time import sleep

rel1 = 
rel2 =
rel3 =
rel4 = 
led1 =
led2 = 
led3 =
led4 =

GPIO.setmode(GPIO.BCM)
GPIO.setup(rel1, GPIO.OUT)
GPIO.setup(rel2, GPIO.OUT)
GPIO.setup(rel3, GPIO.OUT)
GPIO.setup(rel4, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

t = open('time.txt')
m = open('many.txt')
many = m.read()
timing = t.read()
if timing == 'c':
    GPIO.