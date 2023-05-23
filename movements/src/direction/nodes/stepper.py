#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import Int16,String,Bool
import RPi.GPIO as GPIO


debug = True

#TO-DO create a file with all the GPIO number and  the device conneted on it 



# DEFINE GPIO
GPIO_DIR = 10 # Direction GPIO Pin
GPIO_STEP = 17  # Step GPIO Pin
GPIO_DISABLE = 18
# DEFINE GPIO

CW = True     # Clockwise Rotation
CCW = False    # Counterclockwise Rotation
SPR = 400   # Steps per Revolution (360 / 7.5)

delay_between_two_steps = 0.005


GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_DIR, GPIO.OUT)
GPIO.setup(GPIO_STEP, GPIO.OUT)
GPIO.setup(GPIO_DISABLE, GPIO.OUT)

GPIO.output(GPIO_DISABLE, GPIO.LOW)
GPIO.output(GPIO_DIR, GPIO.HIGH)

# Init the sense of rotation 
counterclockwise = GPIO.HIGH #TO-DO  change HIGH or LOW 
clockwise = not counterclockwise


# Limit switches

gpio_limit_switch_clockwise = 20 # TO-DO ADD limit switch
gpio_limit_switch_counterclockwise = 19 # TO-DO ADD limit switch

GPIO.setup(gpio_limit_switch_clockwise, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_limit_switch_counterclockwise, GPIO.IN,pull_up_down=GPIO.PUD_UP)


def callback_limit_switch_clockwise(channel):
	rospy.loginfo("limit switch clockwise has been pushed ")
	if not GPIO.input(gpio_limit_switch_clockwise):
		pos_stepper_motor = "limit_switch_clockwise"
	else:
		pos_stepper_motor = "between_the_two_limits_switches"
		
	
def callback_limit_switch_counter_clockwise(channel):
	rospy.loginfo("limit switch counter_clockwise has been pushed ")
	if not GPIO.input(gpio_limit_switch_clockwise):
		pos_stepper_motor = "limit_switch_counter_clockwise"
	else:
		pos_stepper_motor = "between_the_two_limits_switches"
		
			
	
GPIO.add_event_detect(gpio_limit_switch_clockwise,GPIO.FALLING,callback=callback_limit_switch_clockwise,bouncetime=300)
GPIO.add_event_detect(gpio_limit_switch_counterclockwise,GPIO.FALLING,callback=callback_limit_switch_counter_clockwise,bouncetime=300)


active = False 

def steppermotor_change_status():
	global active
	active = not active 
	


def init():
	global pos_stepper_motor
	if not GPIO.input(gpio_limit_switch_clockwise):
		pos_stepper_motor = "limit_switch_clockwise"
	elif not GPIO.input(gpio_limit_switch_clockwise):
		pos_stepper_motor = "limit_switch_counter_clockwise"
	else :
		pos_stepper_motor = "between_the_two_limits_switches"
		
	#TO-DO ADD switch at the center of the shaft and create a calibrtion program 
		
	
		
		
def go_to_the_pos(command_gap_tick):
	global active 
	rospy.loginfo("command received")
	rospy.loginfo(active)
	if not active : 
		if (command_gap_tick !=0):
			steppermotor_change_status()
			if command_gap_tick > 0 :
				if pos_stepper_motor != "limit_switch_counter_clockwise" :
					rotation_sense = counterclockwise
				else :
					rospy.loginfo("Can't rotate in the counterclockwise , limit switch pushed")
					return
			elif command_gap_tick < 0 :
				if pos_stepper_motor != "limit_switch_clockwise" :
					rotation_sense = clockwise
				else :
					rospy.loginfo("Can't rotate in the clockwise , limit switch pushed")
					return
			if debug :
				rospy.loginfo("command_gap_tick : {}".format(str(command_gap_tick)))
				
			GPIO.output(GPIO_DIR,rotation_sense)
			for x in range(abs(command_gap_tick)) :
				GPIO.output(GPIO_STEP, GPIO.HIGH)
				rospy.sleep(delay_between_two_steps)
				GPIO.output(GPIO_STEP, GPIO.LOW)
				rospy.sleep(delay_between_two_steps)
			if debug :
				rospy.loginfo("command okay")
			steppermotor_change_status()



def callback_rotation(message):
	command_ticks = int(message.data)
	go_to_the_pos(command_ticks)
	
def callback_power_stepper_motor(message):
	global active 
	if not active: 
		if message.data:
			GPIO.output(GPIO_DISABLE, GPIO.LOW)
		else:
			GPIO.output(GPIO_DISABLE, GPIO.HIGH)
	else:
		rospy.loginfo("The stepper is active,you disable it ")
		

def shutdown():
	rospy.loginfo("The stepper node is stopped")
	GPIO.cleanup()
	

	
if __name__=="__main__":
	try:
		init()
		log = rospy.Publisher('log',String,queue_size=10)
		rospy.Subscriber('cape_angle_tick',Int16,callback_rotation)
		rospy.Subscriber('disable_stepper_motor_power',Bool,callback_power_stepper_motor)
		rospy.init_node("stepper_motor ")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The stepper_motor node is running ")	
		log.publish("stepperNode launched")	
		rospy.spin()
	except rospy.ROSInterruptException:
		pass

