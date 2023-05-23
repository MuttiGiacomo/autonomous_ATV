#!/usr/bin/env python

import rospy
import sys
import pygame
import json, os
from ackermann_msgs.msg import AckermannDrive

# Set the maximum steering angle and speed
MAX_STEERING_ANGLE = 0.4
MAX_SPEED = 5.0

# Initialize the steering angle and speed
steering_angle = 0.0
speed = 0.0

# Define the paths to json file
yaml_file_path = os.path.join(os.path.dirname(__file__), "../config/ps4_keys.json")


pygame.init()

clock = pygame.time.Clock()

# START OF GAME LOOP
def run_control(button_keys,analog_keys):
    global LEFT, RIGHT,VEL_CHANGE, steering_angle, speed
    LEFT, RIGHT, VEL_UP, VEL_DOWN = False,  False, False,  False
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            ############### UPDATE SPRITE IF SPACE IS PRESSED #################################
            pass
        # HANDLES BUTTON PRESSES
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['circle']:
                speed = 0.0
            if event.button == button_keys['left_arrow']:
                LEFT = True
            if event.button == button_keys['right_arrow']:
                RIGHT = True
            if event.button == button_keys['down_arrow']:
                DOWN = True
            if event.button == button_keys['up_arrow']:
                UP = True
        # HANDLES BUTTON RELEASES
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['left_arrow']:
                LEFT = False
            if event.button == button_keys['right_arrow']:
                RIGHT = False
            if event.button == button_keys['down_arrow']:
                DOWN = False
            if event.button == button_keys['up_arrow']:
                UP = False
        #HANDLES ANALOG INPUTS
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            # print(analog_keys)
            # Horizontal - left Analog
            if abs(analog_keys[0]) > .4:
                if analog_keys[0] < -.7:
                    LEFT = True
                else:
                    LEFT = False
                if analog_keys[0] > .7:
                    RIGHT = True
                else:
                    RIGHT = False
            # Vertical Analog
            if abs(analog_keys[4]) > .4:
                if analog_keys[4] < -.7:
                    VEL_UP = True
                else:
                    VEL_UP = False
                if analog_keys[4] > .7:
                    VEL_DOWN = True
                else:
                    VEL_DOWN = False

    # Handle Player movement
    if LEFT:
        steering_angle += 0.05 #*(-1 * analog_keys[0])
    if RIGHT:
        steering_angle -= 0.05 #* analog_keys[0]
    if VEL_UP:
        speed += 0.5
    if VEL_DOWN:
        speed -= 0.5

    steering_angle = max(-MAX_STEERING_ANGLE, min(steering_angle, MAX_STEERING_ANGLE))
    speed = max(-MAX_SPEED, min(speed, MAX_SPEED))

    return(steering_angle,speed)




def main():
    

    msg = """
    
    joystick controller started:
    use:    left stick for steering
            R2 to speed-up
            L2 to breake
    """

    # Initialize the ROS node
    rospy.init_node("joystick_control")

    # Create a publisher for the ackermann drive message
    pub = rospy.Publisher("/ackermann_cmd", AckermannDrive, queue_size=1)

    # Set the publishing rate to 10 Hz
    rate = rospy.Rate(10)

    #Initialize controller
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
    for joystick in joysticks:
        joystick.init()

    with open(yaml_file_path) as file:
        button_keys = json.load(file)

    # 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
    # 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
    analog_keys = {0:0, 1:0, 2:0, 3:0, 4: -1, 5: -1 }

    # Loop until the ROS node is shutdown
    while not rospy.is_shutdown(): 

        print(msg)


        steering_angle,speed = run_control(button_keys,analog_keys)

        # Create an ackermann drive message with the current steering angle and speed
        drive_msg = AckermannDrive()
        drive_msg.steering_angle = steering_angle
        drive_msg.speed = speed

        # Publish the ackermann drive message
        pub.publish(drive_msg)

        # Sleep to maintain the publishing rate
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
