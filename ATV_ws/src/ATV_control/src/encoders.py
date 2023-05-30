#!/usr/bin/env python

import rospy
import numpy as np
from control_msgs.msg import JointControllerState
from std_msgs.msg import Float64

def RL_callback(data):
    noise_std_dev = 0.01
    noise = np.random.normal(0, noise_std_dev)
    noisy_data = data.process_value + noise
    print(noisy_data)
    RL_pub.publish(noisy_data)

def RR_callback(data):
    noise_std_dev = 0.01
    noise = np.random.normal(0, noise_std_dev)
    noisy_data = data.process_value + noise
    print(noisy_data)
    RL_pub.publish(noisy_data)

def listener():
    rospy.init_node('encoders', anonymous=True)
    rospy.Subscriber("/ATV/RL_wheel_velocity_controller/state", JointControllerState, RL_callback)
    rospy.Subscriber("/ATV/RR_wheel_velocity_controller/state", JointControllerState, RR_callback)
    rospy.spin()

if __name__ == '__main__':
    RL_pub = rospy.Publisher("/sensors/RL_encoder", Float64, queue_size = 1)
    RR_pub = rospy.Publisher("/sensors/RR_encoder", Float64, queue_size = 1)

    listener()
