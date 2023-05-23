from time import sleep
import RPi.GPIO as GPIO

INPUT = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(INPUT,GPIO.RISING)

def d(callback):
    print("detected")

GPIO.add_event_callback(INPUT,d)


while True :
    sleep(1)
