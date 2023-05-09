#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import Bool,String
import RPi.GPIO as GPIO

# DEFINE GPIO
pwm_pin = 22 #TO-DO change GPIO
dir_pin = 23
# DEFINE GPIO


GPIO.setmode(GPIO.BCM)   
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
  
pwm = GPIO.PWM(pwm_pin, 100)

def stop():
    pwm.start(0)
    time.sleep(0.3)


def down(speed):
	# speed value between 0 to 100%
    GPIO.output(dir_pin, GPIO.HIGH)
    pwm.start(speed)

def up(speed):
	# speed value between 0 to 100%
    GPIO.output(dir_pin, GPIO.LOW)
    pwm.start(speed)


def callback_brake(must_brake):
	if must_brake.data == True :
		down(100) #value between 0 to 100%
	else :
		up(100) # speed value between 0 to 100%

def shutdown():
	rospy.loginfo("The brake node is stopped")
	
if __name__=="__main__":
	try:
		rospy.Subscriber('brake',Bool,callback_brake)
		log = rospy.Publisher('log',String,queue_size=10)
		rospy.init_node("brake_node")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The brake node is running ")
		log.publish("brake launched")		
		rospy.spin()
	except rospy.ROSInterruptException:
		pass

