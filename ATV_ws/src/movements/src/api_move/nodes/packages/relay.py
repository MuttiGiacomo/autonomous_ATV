#!/usr/bin/env python3
# license removed for brevity

import RPi.GPIO as GPIO


class relay():
	def __init__(self,pin_input):
		GPIO.setmode(GPIO.BCM)
		self.pin_input = pin_input
		GPIO.setup(pin_input,GPIO.OUT)
		
	def switch_on(self):
		GPIO.output(self.pin_input,GPIO.HIGH)

	def switch_off(self):
		GPIO.output(self.pin_input,GPIO.LOW)

	def clean(self):
		GPIO.cleanup()
		
	def listener(self, boolean):
		if (boolean.data==True ):
			self.switch_on()
		else:
			self.switch_off()
