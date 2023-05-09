#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import Bool,Int16,String
import RPi.GPIO as GPIO

atv_can_move = False 
coeff_pot_per_km_h = 1#TO-DO 


def callback_atv_can_move(message):
	atv_can_move = message.data
	
	
	
def callback_speed_command(message):
	potentiometer_value.publish(int(message.data*coeff_pot_per_km_h))
	


def shutdown():
	rospy.loginfo("The speed node is stopped")
	
	
	
if __name__=="__main__":
	try:
		rospy.Subscriber('speed_command',Int16,callback_speed_command)
		rospy.Subscriber('atv_can_move',Bool,callback_atv_can_move)
		
		potentiometer_value = rospy.Publisher('potentiometer_value',Int16,queue_size=5)
		brake = rospy.Publisher('brake',Bool,queue_size=5)
		log = rospy.Publisher('log',String,queue_size=10)
		rospy.init_node("Speed")
		rospy.loginfo("The speed node is running ")	
		log.publish("speed node launched")	
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
