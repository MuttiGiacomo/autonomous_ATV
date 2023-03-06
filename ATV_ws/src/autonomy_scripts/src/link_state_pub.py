#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import LinkStates
from geometry_msgs.msg import Pose, Twist, Point, Quaternion
import os

RATE = float(os.getenv("RATE", 10))


def talker():
    pub = rospy.Publisher('/gazebo/link_states', LinkStates, queue_size = 1)
    rospy.init_node('link_state_pub')
    rate = rospy.Rate(RATE)

    Point p


    while not rospy.is_shutdown():
        
        
        hello_str = "hello_world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass