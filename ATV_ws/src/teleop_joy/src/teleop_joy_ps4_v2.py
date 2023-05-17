#!/usr/bin/env python

import rospy
import sys
import pygame
import json, os
from std_msgs.msg import Bool
from ackermann_msgs.msg import AckermannDrive
from action_control_unit.msg import movement

# Set the maximum steering angle and speed
MAX_STEERING_ANGLE = 0.4
MAX_SPEED = 5.0

# Initialize the steering angle and speed
steering_angle = 0.0
speed = 0.0

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()

clock = pygame.time.Clock()
color = 0
###########################################################################################







# START OF GAME LOOP
def run_control(button_keys,analog_keys):
    global LEFT, RIGHT,VEL_CHANGE, steering_angle, speed, movement_msg
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
                speed = 0
            if event.button == button_keys['triangle']:
                movement_msg.Forward_reverse = "forward"
            if event.button == button_keys['cross']:
                movement_msg.Forward_reverse = "reverse"
            if event.button == button_keys['cross']:
                disable_stepper.publish(True)
            if event.button == button_keys['left_stick_click']:
                disable_stepper.publish(True)
        #    if event.button == button_keys['left_arrow']:
        #        LEFT = True
        #    if event.button == button_keys['right_arrow']:
        #        RIGHT = True
        #    if event.button == button_keys['d\own_arrow']:
        #        VEL_DOWN = True
        #    if event.button == button_keys['up_arrow']:
        #        VEL_UP = True
        ## HANDLES BUTTON RELEASES
        #if event.type == pygame.JOYBUTTONUP:
        #    if event.button == button_keys['left_arrow']:
        #        LEFT = False
        #    if event.button == button_keys['right_arrow']:
        #        RIGHT = False
        #    if event.button == button_keys['down_arrow']:
        #        VEL_DOWN = False
        #    if event.button == button_keys['up_arrow']:
        #        VEL_UP = False
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
            #if abs(analog_keys[4]) > .4:
            #    if analog_keys[4] < -.7:
            #        VEL_UP = True
            #    else:
            #        VEL_UP = False
            #    if analog_keys[4] > .7:
            #        VEL_DOWN = True
            #    else:
            #        VEL_DOWN = False
            #    # Triggers
            if analog_keys[2] > 0.4:  # Left trigger
                VEL_DOWN = True
            else:
                VEL_DOWN = False
            if analog_keys[5] > 0.4:  # Right Trigger
                VEL_UP = True
            else:
                VEL_UP = False

    # Handle Player movement
    if LEFT:
        movement_msg.angle_of_correction = +3 # arbitrarily chosen 
    if RIGHT:
        movement_msg.angle_of_correction = -3 # arbitrarily chosen 
    if VEL_UP:
        speed += 0.5
    if VEL_DOWN:
        speed -= 0.5

    steering_angle = max(-MAX_STEERING_ANGLE, min(steering_angle, MAX_STEERING_ANGLE))
    speed = max(-MAX_SPEED, min(speed, MAX_SPEED))

    #pub.publish(movement_msg)

    return()




def main():
    

    msg = """
    
    joystick controller started:
    use:    left stick for steering
            R2 to speed-up
            L2 to breake
    """
    global movement_msg, disable_stepper
    movement_msg = movement() 
    movement_msg.Forward_reverse = "forward"  
    movement_msg.Angle_of_correction = 0 
    movement_msg.Speed_command = 0
    total_correction_angle = 0


    # Initialize the ROS node
    rospy.init_node("joystick_control")

    disable_stepper = rospy.Publisher('disable_stepper_motor_power',Bool,queue_size=1)
    # Create a publisher for the ackermann drive message
    pub = rospy.Publisher("/command_move", AckermannDrive, queue_size=1)
    

    # Set the publishing rate to 10 Hz
    rate = rospy.Rate(10)

    #Initialize controller
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
    for joystick in joysticks:
        joystick.init()

    with open("src/teleop_joy/src/ps4_keys.json") as file:
        button_keys = json.load(file)

    # 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
    # 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
    analog_keys = {0:0, 1:0, 2:0, 3:0, 4: -1, 5: -1 }

    # Loop until the ROS node is shutdown
    while not rospy.is_shutdown(): 

        print(msg)

        run_control(button_keys,analog_keys)

        pub.publish(movement_msg)

        # print pubblished values
        commanded_vals = " ---- linear speed: " + str(movement_msg.Speed_command) + "  ----- angle of correction: " + str(movement_msg.Angle_of_correction) + " ---- direction: " + str(movement_msg.Forward_reverse)
        print(commanded_vals)

        # Sleep to maintain the publishing rate
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
