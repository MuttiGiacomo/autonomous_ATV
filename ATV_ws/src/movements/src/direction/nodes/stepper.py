#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import Int16,String,Bool, Float64
from math import pi

#nodo che 
# 1) trova il trova l'angolo complessivo (attuale + angle_of_correction) (come il nodo creato dal francese)
# 2) converte il valore in Ackermann steering per le ruote anteriori (e anche quelle posteriori, idealmente con un toggle)
# 3) pubblica i valori agli attuatori su Gazebo

# (non so se tutto in un nodo, forse meglio fare 1 in un nodo e 2,3 nel nodo ackermann_steering come versione vanilla creata da me)

tick_value_in_degrees = 12
max_steering_angle = 60
	
def callback_actual_angle(message):
    global actual_angle #in degrees
    actual_angle = message.something.something_else * 180/pi #to do check something.something_else from ros and gazebo
		
def go_to_the_pos(command_gap_tick):
	global active 
	rospy.loginfo("command received")
	rospy.loginfo(active)
	desired_abs_angle = actual_angle + command_gap_tick * tick_value_in_degrees
	commanded_angle = min(abs(desired_abs_angle),max_steering_angle)
	angle_pub.publish(float(commanded_angle)) #not sure of the cast to float ????
	rospy.loginfo("commanded an angle change of " + command_gap_tick * tick_value_in_degrees + " degrees, that will reach " + commanded_angle + "degrees")

def callback_rotation(message):
	command_ticks = int(message.data)
	go_to_the_pos(command_ticks)


def shutdown():
	rospy.loginfo("The stepper node is stopped")
	

	
if __name__=="__main__":
	try:		
		angle_pub = rospy.Publisher('stepper_input', Float64, queue_size=1)
		log = rospy.Publisher('log',String,queue_size=10)

		rospy.Subscriber('cape_angle_tick',Int16,callback_rotation)
		#rospy.Subscriber('disable_stepper_motor_power',Bool,callback_power_stepper_motor)
		
		rospy.init_node("stepper")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The stepper node is running ")	
		log.publish("stepper Node launched")	
		rospy.spin()
	except rospy.ROSInterruptException:
		pass

