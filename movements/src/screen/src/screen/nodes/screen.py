#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import String
from collections import deque


#TO-DO create a file with all the GPIO number and  the device conneted on it 
queue_line_1 = deque([])
queue_line_2 = deque([])
queue_line_34 = deque([])


def callback_mode(message):
	global queue_line_1
	queue_line_1.append("mode : {}".format(message.data))


def callback_status(message):
	global queue_line_2
	queue_line_2.append("status : {}".format(message.data))

def callback_log(message):
    global queue_line_34
    global time_last_update_l34
    queue_line_34.append(message.data)
    time_last_update_l34 = rospy.get_time()


def run():
	global time_last_update_l34
	last_message_l1 = " "
	last_message_l2 = " " 
	timer_refresh_l34 = 3# 3 seconds 
	time_last_update_l34 = rospy.get_time()
	flag_clear = True
	
	while not rospy.is_shutdown():
		if queue_line_1 : # is not empty 
			message_l1 = queue_line_1.popleft()
			if message_l1 != last_message_l1 :
				screen_l1.publish(message_l1)
				last_message_l1 = message_l1
			
		if queue_line_2 : # is not empty 
			message_l2 = queue_line_2.popleft()
			if message_l2 != last_message_l2 :
				screen_l2.publish(message_l2)
				last_message_l2 = message_l2
				
		if queue_line_34 : # is not empty 
			screen_l3.publish(queue_line_34.popleft())
			flag_clear = False
			
		if queue_line_34 : # is not empty 
			screen_l4.publish(queue_line_34.popleft())
			
		if (time_last_update_l34 + timer_refresh_l34 < rospy.get_time() and  not flag_clear) :
			clear_l34()
			flag_clear = True 
			
		rospy.sleep(0.1)
			
	
def clear_l34():
	screen_l4.publish("                   ")
	screen_l3.publish("                   ")
	
	

def shutdown():
	rospy.loginfo("The remote node is stopped")
	
	
	
if __name__=="__main__":
	try:
		screen_l1 = rospy.Publisher('screen_line_1',String,queue_size=10)
		screen_l2 = rospy.Publisher('screen_line_2',String,queue_size=10)
		screen_l3 = rospy.Publisher('screen_line_3',String,queue_size=10)
		screen_l4 = rospy.Publisher('screen_line_4',String,queue_size=10)
		rospy.Subscriber('mode',String,callback_mode)
		rospy.Subscriber('status',String,callback_status)
		rospy.Subscriber('log',String,callback_log)

		rospy.init_node("screen")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The screen node is running ")
		screen_l3.publish("screen launched")
		run()
	except rospy.ROSInterruptException:
		pass

