#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import Bool,String,Int16
import RPi.GPIO as GPIO
from packages.relay import relay

atv_can_move = False 
degree_per_tick = 1.8 #TO-DO search and complete 
value_in_ticks = 0
GPIO_relay_direction = 25

relay_direction_r2 = relay(GPIO_relay_direction)

lock_angle_callback = False 


def callback_angle_of_correction_in_degree(angle_degree):
	global lock_angle_callback
	if (not lock_angle_callback) and atv_can_move :
		lock_angle_callback = True 
		value_in_ticks = int(float(angle_degree.data) / degree_per_tick)
		cape_angle_tick.publish(value_in_ticks)
		#rospy.loginfo(value_in_ticks)
		value_in_ticks = 0
		lock_angle_callback = False 
	
	

def callback_atv_can_move(message):
	global atv_can_move
	atv_can_move = message.data
	

	
def callback_forward_reverse(message):
	if atv_can_move :
		rospy.loginfo(message.data)
		if message.data == "forward":
			relay_direction_r2.switch_off()
			rospy.loginfo("forward")
		elif message.data == "reverse":
			relay_direction_r2.switch_on()
			rospy.loginfo("reverse")
		else :
			rospy.loginfo("topic message /[forward_or_reverse/]  misunderstood ")
			
	
	

def shutdown():
	rospy.loginfo("The direction node is stopped")
	
	
	
if __name__=="__main__":
	try:
		cape_angle_tick = rospy.Publisher('cape_angle_tick',Int16,queue_size=5)
		log = rospy.Publisher('log',String,queue_size=10)
		
		rospy.Subscriber('angle_of_correction_in_degree',Int16,callback_angle_of_correction_in_degree)
		rospy.Subscriber('atv_can_move',Bool,callback_atv_can_move)
		rospy.Subscriber('forward_reverse',String,callback_forward_reverse)
		
		rospy.init_node("direction")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The direction node is running ")		
		log.publish("direction launched")
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
