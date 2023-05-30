#!/usr/bin/env python

import rospy
import sys
import pygame
import json, os
from ackermann_msgs.msg import AckermannDrive


# buttons where mapped for a PS4 controller connected using ds4drv
# note: there are 2 ways to connect the ps4 controller (using the gui and using "sudo ds4drv": 
# using the first one the button mapping is the same as the third party controller, 
# using ds4drv the mapping is different, therefore 2 scripts where written. 
# This is one of them.


# Set the maximum steering angle and speed
MAX_STEERING_ANGLE = 0.4
MAX_SPEED = 5.0

# Initialize the steering angle and speed
steering_angle = 0.0
speed = 0.0

# Define the paths to json file
yaml_file_path = os.path.join(os.path.dirname(__file__), "../config/ps4_ctrl_keys.json")


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

    
    #connect to PS4 controller
    controller = pygame.joystick.Joystick(0)    # in the office PC, using "sudo ds4drv", the ps4 controller is /dev/input/js4, this might change depending on the machine
                                                # to check wich device use "ls -la /dev/input" before and after connecting your ps4 controller 
                                                # (if you are using "sudo ds4drv" it will tell you which device has been created, aka the jsN value)
    controller.init()

    with open(yaml_file_path) as file:
        button_keys = json.load(file)

    drive_msg = AckermannDrive()

    # 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
    # 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
    analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}
    # Loop until the ROS node is shutdown
    while not rospy.is_shutdown():
        print('use:    left stick for steering')
        print('        "R2"/"L2" to slow-down/speed-up')
        print('        "circle" to reset velocity to zero')

        steering_angle,speed = run_control(button_keys,analog_keys)

        # Create an ackermann drive message with the current steering angle and speed
        
        drive_msg.steering_angle = steering_angle
        drive_msg.speed = speed

        # Publish the ackermann drive message
        pub.publish(drive_msg)

        print("---------------------------------------------------------------------------------------------")
        commanded_vals = " ---- linear speed: " + str(drive_msg.speed) + "  ----- steering angle: " + str(drive_msg.steering_angle) + " rad "
        print(commanded_vals)

        # Sleep to maintain the publishing rate
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
