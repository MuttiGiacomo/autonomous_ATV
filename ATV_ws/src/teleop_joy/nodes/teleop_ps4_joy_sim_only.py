#!/usr/bin/env python

import rospy
import sys
import pygame
import json
import os
from std_msgs.msg import Bool
from action_control_unit.msg import movement

# ----->  this file is for SIMULATION ONLY   <------
# buttons where mapped for a PS4 controller connected using ds4drv
# note: there are 2 ways to connect the ps4 controller (using the gui and using "sudo ds4drv": 
# using the first one the button mapping is the same as the third party controller, 
# using ds4drv the mapping is different, therefore 2 more scripts where written. 
# This is one of them.

# emergency stop and stepper motor status info are controlled wuth the ps4 controller
# in the real atv these informations are given by the hardware
# using this node with the real atv will messupp the emergency stop and stepper informations 




# Set the maximum steering angle and speed
MAX_SPEED = 50
SPEED_CHANGE = 2
ANGLE_CHANGE = 3

# Initialize speed, default stepper motor status, default direction
speed = 0
stepper_is_disabled = True
forward_reverse = "forward"
emergency_stop = False

# Define the paths to json file
yaml_file_path = os.path.join(os.path.dirname(__file__), "../config/ps4_ctrl_keys.json")

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Run control function
def run_control(button_keys, analog_keys):
    global LEFT, RIGHT, speed, movement_msg, stepper_is_disabled, forward_reverse, emergency_stop, disabled_stepper_pub
    LEFT, RIGHT, VEL_UP, VEL_DOWN = False, False, False, False

    for event in pygame.event.get():
        # button press
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['circle']:
                speed = 0
            if event.button == button_keys['square']:
                stepper_is_disabled = True
                disabled_stepper_pub.publish(True)
            if event.button == button_keys['triangle']:
                stepper_is_disabled = False
                disabled_stepper_pub.publish(False)
            if event.button == button_keys['x']:
                forward_reverse = "reverse"
                speed = 0
            if event.button == button_keys['PS']:
                speed = 0
                stepper_is_disabled = True
                emergency_stop = True
            if event.button == button_keys['option']:
                emergency_stop = False
            if event.button == button_keys['R1']:
                VEL_UP = True
            if event.button == button_keys['L1']:
                VEL_DOWN = True
        # button button release
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['x']:
                forward_reverse = "forward"
                speed = 0
                emergency_pub.publish(True)
            if event.button == button_keys['R1']:
                VEL_UP = False
            if event.button == button_keys['L1']:
                VEL_DOWN = False
        # triggers and sticks
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            if analog_keys[0] < -0.5: #left stick
                LEFT = True
            else:
                LEFT = False
            if analog_keys[0] > 0.5: #left stick
                RIGHT = True
            else:
                RIGHT = False
            #if analog_keys[2] > 0.4: #left trigger  on 3rd party controller
            if analog_keys[3] > 0.4: #left trigger  on ps4 controller
                VEL_DOWN = True
            else:
                VEL_DOWN = False
            #if analog_keys[5] > 0.4: #right trigger  on 3rd party controller
            if analog_keys[4] > 0.4: #right trigger  on ps4 controller
                VEL_UP = True
            else:
                VEL_UP = False

    ang_corr = 0

    if (not stepper_is_disabled) and (not emergency_stop): #allow teleoperation only if the stepper motor is engaged
        if RIGHT:
            ang_corr = -ANGLE_CHANGE
        if LEFT:
            ang_corr = ANGLE_CHANGE
        if VEL_UP:
            speed += SPEED_CHANGE
        if VEL_DOWN:
            speed -= SPEED_CHANGE

        movement_msg.Speed_command = max(0, min(speed, MAX_SPEED))  # 0 < speed < max_speed
        movement_msg.Angle_of_correction = ang_corr
        movement_msg.Forward_reverse = forward_reverse

    return

def main():
    global movement_msg, disabled_stepper_pub, emergency_pub

    # initialize movement.msg
    movement_msg = movement()
    movement_msg.Forward_reverse = "forward"
    movement_msg.Angle_of_correction = 0
    movement_msg.Speed_command = 0

    # init node
    rospy.init_node("joystick_control")
    print("joystick controller started:")

    # init pubblishers
    command_pub = rospy.Publisher("/command_move", movement, queue_size=1)
    disabled_stepper_pub = rospy.Publisher('disable_stepper_motor_power', Bool, queue_size=1)
    emergency_pub = rospy.Publisher('Emergency_stop', Bool, queue_size=1)

    rate = rospy.Rate(10)

    #connect to PS4 controller
    controller = pygame.joystick.Joystick(0)    # in the office PC, using "sudo ds4drv", the ps4 controller is /dev/input/js4, this might change depending on the machine
                                                # to check wich device use "ls -la /dev/input" before and after connecting your ps4 controller 
                                                # (if you are using "sudo ds4drv" it will tell you which device has been created, aka the jsN value)
    controller.init()

    with open(yaml_file_path) as file:
        button_keys = json.load(file)

    #analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1} 2 5
    analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}

    while not rospy.is_shutdown():
        print('use:    left stick for steering')
        print('        "R2"/"L2" to slow-down/speed-up')
        print('        hold "x" to reverse')
        print('        "square"/"triangle" to disable/enable the stepper motor')
        print('        "PS" button to activate the emergency stop, "option" to resume \n ')

        run_control(button_keys, analog_keys)

        if not stepper_is_disabled:
            print("stepper motor is enabled, you can use the controller")
            command_pub.publish(movement_msg)
        else:
            print("stepper motor is disabled, enable it in order to use the controller")

        print("---------------------------------------------------------------------------------------------")
        commanded_vals = " ---- linear speed: " + str(movement_msg.Speed_command) + "  ----- angle of correction: " + str(
            movement_msg.Angle_of_correction) + " deg ---- direction: " + str(movement_msg.Forward_reverse)
        print(commanded_vals)
        print("---------------------------------------------------------------------------------------------")
        if emergency_stop: print("\n     ************* EMERGENCY STOP ACTIVATED *************     \n")
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
