import RPi.GPIO as GPIO
from time import sleep

rel1 = 21
rel2 = 20
rel3 = 16
rel4 = 12
led1 = 26
led2 = 19
led3 = 13
led4 = 6

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
p = open('port.txt')
many = m.read()
timing = t.read()
port = p.read()
if timing == 'c':
    if port == 1:
        GPIO.output(rel1, True)
        GPIO.output(led1, True)
        sleep(int(many))
        GPIO.output(rel1, False)
        GPIO.output(led1, False)
    elif port == 2:
        GPIO.output(rel2, True)
        GPIO.output(led2, True)
        sleep(int(many))
        GPIO.output(rel2, False)
        GPIO.output(led2, False)
    elif port == 3:
        GPIO.output(rel3, True)
        GPIO.output(led3, True)
        sleep(int(many))
        GPIO.output(rel3, False)
        GPIO.output(led3, False)
    elif port == 4:
        GPIO.output(rel4, True)
        GPIO.output(led4, True)
        sleep(int(many))
        GPIO.output(rel4, False)
        GPIO.output(led4, False)
elif timing == 'м':
    if port == 1:
        GPIO.output(rel1, True)
        GPIO.output(led1, True)
        sleep(int(many) * 60)
        GPIO.output(rel1, False)
        GPIO.output(led1, False)
    elif port == 2:
        GPIO.output(rel2, True)
        GPIO.output(led2, True)
        sleep(int(many) * 60)
        GPIO.output(rel2, False)
        GPIO.output(led2, False)
    elif port == 3:
        GPIO.output(rel3, True)
        GPIO.output(led3, True)
        sleep(int(many) * 60)
        GPIO.output(rel3, False)
        GPIO.output(led3, False)
    elif port == 4:
        GPIO.output(rel4, True)
        GPIO.output(led4, True)
        sleep(int(many) * 60)
        GPIO.output(rel4, False)
        GPIO.output(led4, False)
elif timing == 'ч':
    if port == 1:
        GPIO.output(rel1, True)
        GPIO.output(led1, True)
        sleep(int(many))
        GPIO.output(rel1, False)
        GPIO.output(led1, False)
    elif port == 2:
        GPIO.output(rel2, True)
        GPIO.output(led2, True)
        sleep(int(many))
        GPIO.output(rel2, False)
        GPIO.output(led2, False)
    elif port == 3:
        GPIO.output(rel3, True)
        GPIO.output(led3, True)
        sleep(int(many))
        GPIO.output(rel3, False)
        GPIO.output(led3, False)
    elif port == 4:
        GPIO.output(rel4, True)
        GPIO.output(led4, True)
        sleep(int(many))
        GPIO.output(rel4, False)
        GPIO.output(led4, False)
t.close()
m.close()
p.close()