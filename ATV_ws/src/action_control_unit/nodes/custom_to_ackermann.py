#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32,Bool,String
from ackermann_msgs.msg import AckermannDrive
from action_control_unit.msg import movement
from math import pi

global prev_angle
degree_per_tick = 1.8 #deg
absolute_angle = 0.0
max_steering_angle = 0.7 #rad
forward_reverse = "forward"

#debug
status = "manual"

def callback_emergency_stop(em_stop):
    if em_stop:
        print("emergency stop is active")

def callback_mode(message): 
	global mode
	mode = message.data

def callback_status(message):
	global status
	status = message.data

#converts the 'Angle_of_correction' (relative and discrete angle in degrees) from the movement message into the global desired angle for the ackermann steering (absolute ange in radiants)
def m_angle_to_a_angle(m_angle):
    global prev_angle, degree_per_tick
    value_in_ticks = int(float(m_angle) / degree_per_tick)  # find number of ticks for the stepper motor
    a_angle = prev_angle + (float(value_in_ticks*degree_per_tick)/180)*pi # desired angle commanded
    
    if a_angle > 0 : a_angle = min(max_steering_angle,a_angle) 
    if a_angle < 0 : a_angle = max(-max_steering_angle,a_angle) 
    prev_angle = a_angle 
    return a_angle

def m_speed_to_a_speed(m_speed,direction):
    if direction == 'forward':
        coef = 0.1
    elif direction == 'reverse':
        coef = - 0.1
    else:
        print("DEBUG: not defined direction, currently set to: " + direction)
        coef = 0
    
    a_speed = m_speed * coef
    print("a_speed: " + str(a_speed))
    return a_speed

def convert_to_ackerman_callback(movement_msg):
    #global a_msg, stop_a_msg
    
    a_msg.steering_angle ,  a_msg.steering_angle_velocity , a_msg.speed , a_msg.acceleration , a_msg.jerk = [ m_angle_to_a_angle(movement_msg.Angle_of_correction) , 0 , m_speed_to_a_speed(movement_msg.Speed_command, movement_msg.Forward_reverse) , 0 , 0]
    update_ackermann_msg(a_msg)

def update_ackermann_msg(a_msg):
    print("DEBUG: called update" )
    rate =rospy.Rate(10) #Hz
    forward_reverse_last_value = "undefined"
    #while not rospy.is_shutdown(): #run the next set of steps as long as the system is active
    if (status == "go" and mode == "auto"): #if the ATV is ready to move (status="go") and is in automatic mode (mode="auto")
        atv_can_move.publish(True)
        command_pub.publish(a_msg)
    else : # if the ATV is ment to be driven manually (mode="manual") or it is not ready to move (status="stop")
        atv_can_move.publish(False)
        command_pub.publish(stop_a_msg)
        print("ATV can't move, check 'status' and/or 'mode' values")
    
    #rate.sleep()


if __name__ == '__main__':
    try:
        #initialization of the node
        rospy.init_node('custom_to_ackermann') 

        rate = rospy.Rate(100)

        a_msg = AckermannDrive()
        stop_a_msg = AckermannDrive()
        stop_a_msg.steering_angle ,  stop_a_msg.steering_angle_velocity , stop_a_msg.speed , stop_a_msg.acceleration , stop_a_msg.jerk = [ 0 , 0 , 0 , 0 , 0 ]
        prev_angle = 0.0
        coef = 1/10
        status = "go" 
        mode = "auto"

        
        #initialyze the pubblishers

        # Bool value to clarify if the ATV is ready to move 
        atv_can_move= rospy.Publisher('atv_can_move',Bool,queue_size=1)
        # ackermann message pubblisher
        command_pub = rospy.Publisher('ackermann_cmd', AckermannDrive, queue_size = 1)
        # Write logs for debugging
        log = rospy.Publisher('log',String,queue_size=10)
        
        #initialyze subscribers

        # Movement message coming from controller/keybard/scripts
        rospy.Subscriber('command_move',movement,convert_to_ackerman_callback)
        # Bool value that specifies if the emergency stop is active or not (if true, the ATV must stop)
        rospy.Subscriber('emergency_stop_general',Bool,callback_emergency_stop)
        # string value that is either "manual" (ATV driven manually) or "automatic" (ATV driven using controller/keyboard/scripts)
        rospy.Subscriber('mode',String,callback_mode)
        # string that gives info about the ATV (if "go", the system is ok and the ATV can move, if "stop", the ATV can't move)
        rospy.Subscriber('status',String,callback_status)
        
        #node initialization
        rospy.init_node("custom_to_ackermann")
        rospy.loginfo("The 'custom_to_ackermann' node is running ")		
        log.publish("custom_to_ackermann launched")

        #update_ackermann_msg()

        while not rospy.is_shutdown():
            rate.sleep()
        
    except rospy.ROSInterruptException:
        pass



    def shutdown():
    	rospy.loginfo("The node manager is stopped")
