#!/usr/bin/env python

import rospy
import numpy as np
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float64


def pid_controller(actual_velocity, target_velocity, previous_error, integral_error, kp, ki, kd, dt):
    error = target_velocity - actual_velocity
    integral_error += error * dt
    derivative_error = (error - previous_error) / dt
    commanded_value = kp * error + ki * integral_error + kd * derivative_error
    previous_error = error
    return commanded_value, previous_error, integral_error



def RL_brake_callback(data):
    commanded_vel, prev_err, int_err = pid_controller(data, 0.0, prev_err, int_err, kp, ki, kd, dt)
    RL_brake_pub.publish(commanded_vel)

def RR_brake_callback(data):
    commanded_vel, prev_err, int_err = pid_controller(data, 0.0, prev_err, int_err, kp, ki, kd, dt)
    RR_brake_pub.publish(commanded_vel)

def listener():
    rospy.init_node('hand_brake', anonymous=True)
    rospy.Subscriber("/sensors/RL_encoder", JointControllerState, RL_brake_callback)
    rospy.Subscriber("/sensors/RL_encoder", JointControllerState, RR_brake_callback)
    rospy.spin()

if __name__ == '__main__':
    kp, ki, kd, dt = 1000 , 100 , 10 , 0.01 
    prev_err = 0
    int_err = 0
    RL_brake_pub = rospy.Publisher("/ATV/RL_wheel_velocity_controller/command", Float64, queue_size = 1)
    RR_brake_pub = rospy.Publisher("/ATV/RR_wheel_velocity_controller/command", Float64, queue_size = 1)

    listener()
