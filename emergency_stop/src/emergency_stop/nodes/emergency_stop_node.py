#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import Bool,String
import RPi.GPIO as GPIO

#TO-DO create a file with all the GPIO number and  the device conneted on it 
emergency_stop_remote = False
emergency_stop_sensors = False
ack_emergency = True

def callback_emergency_stop_remote(message):
	global emergency_stop_remote
	emergency_stop_remote = message.data
	
def callback_emergency_stop_sensors(message):
	global emergency_stop_sensors
	emergency_stop_sensors = message.data


def run():
	global ack_emergency
	rate=rospy.Rate(5)
	flag = 0
	while not rospy.is_shutdown():
		if emergency_stop_remote  :
			emergency_stop_general.publish(True) 
			status.publish("stop")
			log.publish("EmergencyStopRemote")
			if not flag == 1 :
				rospy.loginfo("EMERGENCY STOP REMOTE ")
				flag = 1
			rospy.sleep(0.5)
				
		elif emergency_stop_sensors :
			emergency_stop_general.publish(True)
			status.publish("stop")
			log.publish("EmergencyStopSensors")
			if not flag == 2 :
				rospy.loginfo("EMERGENCY STOP SENSORS ")
				flag = 2
			rospy.sleep(0.5)
		else :
			if flag != 0 :
				log.publish(" ")
				flag = 0 
			emergency_stop_general.publish(False)
			
		
	
def shutdown():
	rospy.loginfo("The emergency_stop node is stopped")
	
	
	
if __name__=="__main__":
	try:
		
		emergency_stop_general = rospy.Publisher('emergency_stop_general',Bool,queue_size=10)
		log = rospy.Publisher('log',String,queue_size=10)
		status = rospy.Publisher('status',String,queue_size=10)
		
		rospy.Subscriber('emergency_stop_sensors',Bool,callback_emergency_stop_sensors)
		rospy.Subscriber('emergency_stop_remote',Bool,callback_emergency_stop_remote)
		rospy.init_node("emergency_stop")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The emergency_stop node is running ")
		log.publish("Emergency stop")
		log.publish("node launched")
		run()
	except rospy.ROSInterruptException:
		pass

