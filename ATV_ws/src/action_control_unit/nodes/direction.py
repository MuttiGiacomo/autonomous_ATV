#!/usr/bin/env python

import rospy 
from std_msgs.msg import Bool,String,Int16,Float32


# REDO ---- controllare tickss
atv_can_move = False 
degree_per_tick = 1.8 #TO-DO search and complete 
value_in_ticks = 0

lock_angle_callback = False 


def callback_angle_of_correction_in_degree(angle_degree):
	global lock_angle_callback
	if (not lock_angle_callback) and atv_can_move :
		lock_angle_callback = True # to prevent the input of a new angle variation while the motor is already spinning ?????? not sure ??????
		value_in_ticks = int(float(angle_degree.data) / degree_per_tick)  # find number of ticks for the stepper motor
		angle_cmd.publish(float(value_in_ticks*degree_per_tick)) # desired angle commanded 
		value_in_ticks = 0
		lock_angle_callback = False 
	
	

def callback_atv_can_move(message):
	global atv_can_move
	atv_can_move = message.data
	

	
def callback_forward_reverse(message):
	if atv_can_move :
		rospy.loginfo(message.data)
		print("ATV ready to move and direction set to: " , message.data)
	if (message.data != "forward") and (message.data != "reverse"):
		rospy.loginfo("topic message /[forward_or_reverse/]  misunderstood ")
		
			
def shutdown():
	rospy.loginfo("The direction node is stopped")
	
	
	
if __name__=="__main__":
	try:
		#init pubblishers

        # pubblisher of ticks for the stepper motor
		angle_cmd = rospy.Publisher('angle_cmd',Float32,queue_size=1)
		# write logs for debugging
		log = rospy.Publisher('log',String,queue_size=10)
		
        #init subscribers

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
