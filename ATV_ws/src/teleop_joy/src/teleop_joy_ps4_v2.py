#!/usr/bin/env python

import rospy
import sys
import pygame
import json, os
from std_msgs.msg import Bool
from action_control_unit.msg import movement

# Set the maximum steering angle and speed
MAX_SPEED = 50
SPEED_CHANGE = 2
ANGLE_CHANGE = 3

# Initialize the steering angle and speed
steering_angle = 0.0
speed = 0.0
stepper_is_disabled = True
forward_reverse = "forward"

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()

clock = pygame.time.Clock()
color = 0
###########################################################################################




# START OF GAME LOOP
def run_control(button_keys,analog_keys):
    global LEFT, RIGHT,VEL_CHANGE, steering_angle, speed, movement_msg, stepper_is_disabled, forward_reverse
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
            if event.button == button_keys['square']:
                stepper_is_disabled = True
                disable_stepper.publish(True)
            if event.button == button_keys['triangle']:
                stepper_is_disabled = False
                disable_stepper.publish(False)
            if event.button == button_keys['x']:
                forward_reverse = "reverse"
                speed = 0
        ## HANDLES BUTTON RELEASES
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['x']:
                forward_reverse = "forward"
                speed = 0
        #HANDLES ANALOG INPUTS
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            # Horizontal - left Analog
            if analog_keys[0] < -0.7:
                LEFT = True
            else:
                LEFT = False
            if analog_keys[0] > 0.7:
                RIGHT = True
            else:
                RIGHT = False
            # Triggers
            if analog_keys[2] > 0.4:  # Left trigger
                VEL_DOWN = True
            else:
                VEL_DOWN = False
            if analog_keys[5] > 0.4:  # Right Trigger
                VEL_UP = True
            else:
                VEL_UP = False

    ang_corr = 0

    # Handle Player movement
    if RIGHT:   ang_corr = - ANGLE_CHANGE  
    if LEFT:    ang_corr = + ANGLE_CHANGE  
    
    if VEL_UP:   speed += SPEED_CHANGE
    if VEL_DOWN: speed -= SPEED_CHANGE

    # Limit the linear speed to their max and min values
    if not(stepper_is_disabled):
        movement_msg.Speed_command = max( 0 , min(speed, MAX_SPEED) )
        movement_msg.Angle_of_correction = ang_corr
        movement_msg.Forward_reverse = forward_reverse

    #pub.publish(movement_msg)

    return()




def main():
    

    msg = """
    
    joystick controller started:
    use:    left stick for steering
            R2 to speed-up
            L2 to breake
            hold "x" to reverse
    """
    global movement_msg, disable_stepper
    movement_msg = movement() 
    movement_msg.Forward_reverse = "forward"  
    movement_msg.Angle_of_correction = 0 
    movement_msg.Speed_command = 0


    # Initialize the ROS node
    rospy.init_node("joystick_control")

    disable_stepper = rospy.Publisher('disable_stepper_motor_power',Bool,queue_size=1)
    # Create a publisher for the ackermann drive message
    pub = rospy.Publisher("/command_move", movement, queue_size=1)
    

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
        print("stepper:" + str(stepper_is_disabled))
        if not(stepper_is_disabled):  pub.publish(movement_msg)
        else: print("steper motor is disabled")

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
