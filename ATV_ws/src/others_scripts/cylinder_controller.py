#!/usr/bin/python3

import RPi.GPIO as GPIO 
import time


pwm_pin = 22
dir_pin = 23



GPIO.setmode(GPIO.BCM)   
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
  
pwm = GPIO.PWM(pwm_pin, 100)


def stop():
    pwm.start(0)
    time.sleep(0.3)




def down(speed):
    GPIO.output(dir_pin, GPIO.HIGH)
    pwm.start(speed)

def up(speed):
    GPIO.output(dir_pin, GPIO.LOW)
    pwm.start(speed)




try:
    down(100)
    while True :
        time.sleep(1)

finally :
    stop()
    GPIO.cleanup()          # when your program exits, tidy up after yours


