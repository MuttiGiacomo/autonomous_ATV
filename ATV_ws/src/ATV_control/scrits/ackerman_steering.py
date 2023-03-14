#!/usr/bin/env python


#node used to:
# - reads from /cmd_vel
# - calculates radius of turn
# - calculate alpha_R and alpha_L (steering angles of front wheels) using Ackermann principal
# - calculates vel_R and vel_L (turnng velocity of rear wheels) using Ackermann principal
# - publicates to /FR_wheel_position_controller/command
#                 /FL_wheel_position_controller/command
#                 /RR_wheel_velocity_controller/command
#                 /RL_wheel_velocity_controller/command


import rospy
from std_msgs.msg import Float32, Float64
from gazebo_msgs.msg import LinkStates
from ackermann_msgs.msg import AckermannDrive
import math

# global variables 

# front-rear axle distance
h = 1
# right-left wheel distance
b = 0.5


def get_steering_amgles(msg):
    
    if msg[0] != 0.0 :
        R = h/math.tan(msg[0])
        alpha_l = math.atan2(h*math.tan(msg[0]) , h+0.5*b*math.tan(msg[0]))
        alpha_r = math.atan2(h*math.tan(msg[0]) , h-0.5*b*math.tan(msg[0]))

        gamma = math.atan2(msg[2],R)
        vel_l = math.tan(gamma) * (R+(b/2))
        vel_r = math.tan(gamma) * (R-(b/2))
    else:
        alpha_l = 0.0
        alpha_r = 0.0
        vel_l = msg[2]
        vel_r = msg[2]
    
    return [alpha_l , alpha_r , vel_l , vel_r]

def callback(data):
    info = [ data.steering_angle , data.steering_angle_velocity , data.speed , data.acceleration , data.jerk ]
    alpha_l , alpha_r , vel_l , vel_r = get_steering_amgles(info)

    pub_left_steering.publish(alpha_l)
    pub_right_steering.publish(alpha_r)
    pub_left_vel.publish(vel_l)
    pub_right_vel.publish(vel_r)
    

def main():
    global pub_left_steering , pub_right_steering , pub_left_vel , pub_right_vel
    #initialization of the node
    rospy.init_node('ackerman_controller') 
    sub = rospy.Subscriber('/ATV/ackermann_cmd' , AckermannDrive , callback)
    pub_left_steering = rospy.Publisher('/ATV/FL_wheel_position_controller/command', Float32, queue_size = 1)
    pub_right_steering = rospy.Publisher('/ATV/FR_wheel_position_controller/command', Float32, queue_size = 1)
    pub_left_vel = rospy.Publisher('/ATV/RL_wheel_velocity_controller/command', Float64, queue_size = 1)
    pub_right_vel = rospy.Publisher('/ATV/RR_wheel_velocity_controller/command', Float64, queue_size = 1)
    rate = rospy.Rate(100)
    
    while not rospy.is_shutdown():
        rate.sleep()


if __name__ == '__main__':
    main()
