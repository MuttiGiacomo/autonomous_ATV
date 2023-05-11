#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import String,Bool,Int16
from action_control_unit.msg import movement


mode = "undefined" 
status = "undefined"

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
	print("emergency stop is: ", message)
	

def run():
	rate =rospy.Rate(10) #Hz
	forward_reverse_last_value = "undefined"
	while not rospy.is_shutdown(): #run the next set of steps as long as the system is active
		
		print("mode set to: " , mode )
					
		if (status == "go" and mode == "auto"): #if the ATV is ready to move (status="go") and is in automatic mode (mode="auto")
			atv_can_move.publish(True) 
			speed_command.publish(speed_command_value)
			angle_of_correction_in_degree.publish(angle_of_correction_value)
			
			if (speed_command_value == 0 and (forward_reverse_last_value != forward_reverse_value)): # if the direction "forward_reverse" value has been changed update it in the proper topic
				#To-Do replace speed_command_value by the real speed 
				rospy.loginfo(forward_reverse_value)
				forward_reverse.publish(forward_reverse_value)
				forward_reverse_last_value = forward_reverse_value
			
		else : # if the ATV is ment to be driven manually (mode="manual") or it is not ready to move (status="stop")
			atv_can_move.publish(False)
			speed_command.publish(0)
			
		
		
		rate.sleep()
			
	
def shutdown():
	rospy.loginfo("The node manager is stopped")
	
	
if __name__=="__main__":
	try:
		#initialyze the pubblishers

        # Bool value to clarify if the ATV is ready to move 
		atv_can_move= rospy.Publisher('atv_can_move',Bool,queue_size=1)
		# Int16 linear velocity of the ATV
		speed_command = rospy.Publisher('speed_command',Int16,queue_size=1)
		# Int16 angle variation of the steering
		angle_of_correction_in_degree = rospy.Publisher('angle_of_correction_in_degree',Int16,queue_size=1)
		# Direction of movement (either "forward" or "reverse")
		forward_reverse = rospy.Publisher('forward_reverse',String,queue_size=10)
		# Write logs for debugging
		log = rospy.Publisher('log',String,queue_size=10)
		
        #initialyze subscribers

        # Movement message coming from controller/keybard/scripts
		rospy.Subscriber('command_move',movement,callback_command_move)
		# Bool value that specifies if the emergency stop is active or not (if true, the ATV must stop)
		rospy.Subscriber('Emergency_stop_general',Bool,callback_emergency_stop)
		# string value that is either "manual" (ATV driven manually) or "automatic" (ATV driven using controller/keyboard/scripts)
		rospy.Subscriber('mode',String,callback_mode)
		# string that gives info about the ATV (if "go", the system is ok and the ATV can move, if "stop", the ATV can't move)
		rospy.Subscriber('status',String,callback_status)
		
        #node initialization
		rospy.init_node("api_acu")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The api_acu is running ")		
		log.publish("api_acu launched")
		
        # run procedure
		run()
	except rospy.ROSInterruptException:
		pass