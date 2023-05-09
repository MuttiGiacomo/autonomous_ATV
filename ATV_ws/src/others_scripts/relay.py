import RPi.GPIO as GPIO
import time

class relay():


    def __init__(self,pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        
    def switch_on(self):
        GPIO.output(self.pin, GPIO.HIGH)


    def switch_off(self):
        GPIO.output(self.pin, GPIO.LOW)



"""

test=relay(27)
test.switch_on()
time.sleep(5)
test.switch_off()
GPIO.cleanup()
"""




