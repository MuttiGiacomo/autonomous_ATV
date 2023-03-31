#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

# Import the necessary modules for the PS4 controller
import pygame
from pygame import locals

class PS4Controller:
    def __init__(self):
        # Initialize the Pygame module
        pygame.init()

        # Set up the Pygame window (needed to receive events)
        pygame.display.set_mode((1, 1))

        # Initialize the joystick module
        pygame.joystick.init()

        # Connect to the PS4 controller (assuming only one is connected)
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

        # Set up the ROS publisher
        self.joy_pub = rospy.Publisher("/joy", Joy, queue_size=1)

    def read_controller(self):
        # Read the PS4 controller input
        pygame.event.pump()

        buttons = [self.controller.get_button(i) for i in range(self.controller.get_numbuttons())]
        axes = [self.controller.get_axis(i) for i in range(self.controller.get_numaxes())]

        # Create a new Joy message and fill it with the controller input
        joy_msg = Joy()
        joy_msg.header.stamp = rospy.Time.now()
        joy_msg.axes = axes
        joy_msg.buttons = buttons

        # Publish the Joy message on the /joy topic
        self.joy_pub.publish(joy_msg)

if __name__ == "__main__":
    # Initialize the ROS node
    rospy.init_node("ps4_controller")

    # Create an instance of the PS4Controller class
    ps4 = PS4Controller()

    # Set the ROS rate (how often to publish messages)
    rate = rospy.Rate(20)

    # Start the main loop
    while not rospy.is_shutdown():
        # Read the PS4 controller input and publish a Joy message
        ps4.read_controller()

        # Wait for the next loop iteration
        rate.sleep()

    # Clean up the Pygame and joystick modules
    pygame.quit()
    pygame.joystick.quit()
