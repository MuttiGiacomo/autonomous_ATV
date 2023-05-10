#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import String,Bool,Int16
import sys
sys.path.append("/home/atv-remote/Desktop/")
from api_move.msg import movement
from packages.relay import relay


mode = "undefined" 
status = "undefined"


GPIO_relay_shunt_potbox = 24
GPIO_relay_potentiometer = 5
GPIO_relay_KSI = 16

relay_shunt_potbox_r1 = relay(GPIO_relay_shunt_potbox)
relay_potentiometer_r3 = relay(GPIO_relay_potentiometer)
relay_KSI = relay(GPIO_relay_KSI)

global speed_command_value, angle_of_correction_value, forward_reverse_value

speed_command_value = 0
angle_of_correction_value = 0
forward_reverse_value = "forward"

def callback_mode(message):
	global mode
	mode = message.data

def callback_status(message):
	global status
	status = message.data
	
def callback_command_move(message):
	global speed_command_value, angle_of_correction_value, forward_reverse_value
	speed_command_value = message.speed_command
	angle_of_correction_value = message.angle_of_correction
	forward_reverse_value = message.forward_reverse
	

def callback_emergency_stop(message):
	print("emergency stop")
	

def run():
	rate =rospy.Rate(10)
	forward_reverse_last_value = "undefined"
	while not rospy.is_shutdown():
		if mode == "auto" :
			relay_shunt_potbox_r1.switch_on()
			relay_potentiometer_r3.switch_on()
			relay_KSI.switch_on()
		else :
			relay_shunt_potbox_r1.switch_off()
			relay_potentiometer_r3.switch_off()
			relay_KSI.switch_off()
			
		if (status == "go" and mode == "auto"):
			atv_can_move.publish(True)
			speed_command.publish(speed_command_value)
			angle_of_correction_in_degree.publish(angle_of_correction_value)
			
			if (speed_command_value == 0 and (forward_reverse_last_value != forward_reverse_value)):
				#To-Do replace speed_command_value by the real speed 
				rospy.loginfo(forward_reverse_value)
				forward_reverse.publish(forward_reverse_value)
				forward_reverse_last_value = forward_reverse_value
			
		else :
			atv_can_move.publish(False)
			speed_command.publish(0)
			
		
		
		rate.sleep()
			
	
def shutdown():
	rospy.loginfo("The node manager is stopped")
	
	
if __name__=="__main__":
	try:
		atv_can_move= rospy.Publisher('atv_can_move',Bool,queue_size=10)
		speed_command = rospy.Publisher('speed_command',Int16,queue_size=10)
		angle_of_correction_in_degree = rospy.Publisher('angle_of_correction_in_degree',Int16,queue_size=10)
		forward_reverse = rospy.Publisher('forward_reverse',String,queue_size=10)
		log = rospy.Publisher('log',String,queue_size=10)
		
		rospy.Subscriber('command_move',movement,callback_command_move)
		rospy.Subscriber('Emergency_stop_general',Bool,callback_emergency_stop)
		rospy.Subscriber('mode',String,callback_mode)
		rospy.Subscriber('status',String,callback_status)

		rospy.init_node("API_move")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The API_move is running ")		
		log.publish("api_move launched")
		run()
	except rospy.ROSInterruptException:
		pass

