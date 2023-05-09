#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import Bool,String
import RPi.GPIO as GPIO

#TO-DO create a file with all the GPIO number and  the device conneted on it 

GPIO.setmode(GPIO.BCM)

# DEFINE GPIO
gpio_button_mode_auto = 27
gpio_button_mode_manu = 26
gpio_button_go = 21
gpio_button_stop =13
# DEFINE GPIO

GPIO.setup(gpio_button_mode_auto,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_button_mode_manu,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_button_go,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_button_stop,GPIO.IN,pull_up_down=GPIO.PUD_UP)


emergency_stop = False


def callback_emergency_stop(message):
	global emergency_stop
	emergency_stop = message.data

def callback_go(message):
	if (currently_mode == "auto" and not emergency_stop ):
		status.publish("go")
		rospy.loginfo("go")
	else :
		rospy.loginfo("Need to be in mode auto to put the status to go or the emergency STOP is still activated  ")
	
def callback_stop(message):
	status.publish("stop")
	rospy.loginfo("stop")
	
GPIO.add_event_detect(gpio_button_go,GPIO.FALLING,callback=callback_go,bouncetime=300)
GPIO.add_event_detect(gpio_button_stop,GPIO.FALLING,callback=callback_stop,bouncetime=300)


def run():
	last_mode = " "
	global currently_mode
	while not rospy.is_shutdown():
		if not GPIO.input(gpio_button_mode_auto) and not GPIO.input(gpio_button_mode_manu) :
			currently_mode = "auto"
		elif GPIO.input(gpio_button_mode_auto) and not GPIO.input(gpio_button_mode_manu):
			currently_mode="manu"
			status.publish("stop")	
		else : 
			currently_mode="Undefined"
			status.publish("stop")	
			
		if currently_mode != last_mode :
			mode.publish(currently_mode)
			rospy.loginfo(currently_mode)
			last_mode=currently_mode
					
		rospy.sleep(0.1)
		
		
		
	
def shutdown():
	rospy.loginfo("The remote node is stopped")
	
	
	
if __name__=="__main__":
	try:
		mode = rospy.Publisher('mode',String,queue_size=10)
		status = rospy.Publisher('status',String,queue_size=10)
		rospy.Subscriber('emergency_stop_general',Bool,callback_emergency_stop)
		rospy.init_node("remote")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The remote node is running ")	
		status.publish("stop")		
		run()
	except rospy.ROSInterruptException:
		pass

