from time import sleep
import RPi.GPIO as GPIO

relay_power_stepper = 9
DIR = 10   # Direction GPIO Pin
STEP = 17  # Step GPIO Pin
ENABLE = 18
CW = True     # Clockwise Rotation
CCW = False    # Counterclockwise Rotation
SPR = 400   # Steps per Revolution (360 / 7.5)


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(ENABLE, GPIO.OUT)


GPIO.output(ENABLE, GPIO.LOW)
GPIO.output(DIR, GPIO.LOW)

step_count = 150
delay = 0.005


sleep(5)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    
GPIO.output(DIR, GPIO.HIGH) 
sleep(2)
 

for x in range(step_count*2):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    
    
GPIO.output(DIR, GPIO.LOW) 
sleep(2)
 
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
              
sleep(3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
GPIO.output(ENABLE, GPIO.HIGH)



GPIO.cleanup()
