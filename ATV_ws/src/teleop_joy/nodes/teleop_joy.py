#!/usr/bin/env python

import rospy
import pygame
import json
import os
from action_control_unit.msg import movement


# ----->  for simulation and real atv 

# same file as "teleop_joy_sim_only.py", but stepper motor and emergency stop are not taken into accout
# this code is ment to run on the atv since emergency stop and stepper motor info come from the hardware/sensors
# (it works fine also with the simulation)



# Set the maximum steering angle and speed
MAX_SPEED = 50
SPEED_CHANGE = 2
ANGLE_CHANGE = 3

# Initialize speed, default direction
speed = 0.0
forward_reverse = "forward"

# Define the paths to json file
yaml_file_path = os.path.join(os.path.dirname(__file__), "../config/ps4_keys.json")

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Run control function
def run_control(button_keys, analog_keys):
    global LEFT, RIGHT, speed, movement_msg, forward_reverse
    LEFT, RIGHT, VEL_UP, VEL_DOWN = False, False, False, False

    for event in pygame.event.get():
        # button press
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['circle']:
                speed = 0
            if event.button == button_keys['x']:
                forward_reverse = "reverse"
                speed = 0
        # button button release
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['x']:
                forward_reverse = "forward"
                speed = 0
        # triggers and sticks
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            if analog_keys[0] < -0.7: #left stick
                LEFT = True
            else:
                LEFT = False
            if analog_keys[0] > 0.7: #left stick
                RIGHT = True
            else:
                RIGHT = False
            if analog_keys[3] > 0.4: #left trigger
                VEL_DOWN = True
            else:
                VEL_DOWN = False
            if analog_keys[4] > 0.4: #right trigger
                VEL_UP = True
            else:
                VEL_UP = False

    ang_corr = 0

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
    global movement_msg

    # initialize movement.msg
    movement_msg = movement()
    movement_msg.Forward_reverse = "forward"
    movement_msg.Angle_of_correction = 0
    movement_msg.Speed_command = 0

    # init node
    rospy.init_node("joystick_control")
    print("joystick controller started:")

    # init pubblishers
    pub = rospy.Publisher("/command_move", movement, queue_size=1)

    rate = rospy.Rate(10)

    #connect to PS4 controller
    controller = pygame.joystick.Joystick(4)    # in the office PC, using "sudo ds4drv", the ps4 controller is /dev/input/js4, this might change depending on the machine
                                                # to check wich device use "ls -la /dev/input" before and after connecting your ps4 controller 
                                                # (if you are using "sudo ds4drv" it will tell you which device has been created, aka the jsN value)
    controller.init()

    with open(yaml_file_path) as file:
        button_keys = json.load(file)

    analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}

    while not rospy.is_shutdown():
        print("use:    left stick for steering")
        print("        R2 to speed-up")
        print("        L2 to brake")
        print("        hold x to reverse")

        run_control(button_keys, analog_keys)

        # Publish the movement.msg message
        pub.publish(movement_msg)

        print("---------------------------------------------------------------------------------------------")
        commanded_vals = " ---- linear speed: " + str(movement_msg.Speed_command) + "  ----- angle of correction: " + str(
            movement_msg.Angle_of_correction) + " deg ---- direction: " + str(movement_msg.Forward_reverse)
        print(commanded_vals)
        print("---------------------------------------------------------------------------------------------")

        # Sleep to maintain the publishing rate
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
