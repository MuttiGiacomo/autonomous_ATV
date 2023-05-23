#!/usr/bin/env python

import rospy
import sys
import tty
import termios
from std_msgs.msg import Float64, Bool
from action_control_unit.msg import movement

# ----->  this file is for SIMULATION ONLY   <------

# emergency stop and stepper motor status info are controlled wuth the ps4 controller
# in the real atv these informations are given by the hardware
# using this node with the real atv will messupp the emergency stop and stepper informations 

# Set the maximum steering angle and speed
MAX_SPEED = 50
SPEED_CHANGE = 2
ANGLE_CHANGE = 3

# Initialize the steering angle and speed
speed = 0
stepper_is_disabled = True
forward_reverse = "forward"
emergency_stop = False


def get_input_char():
    # Get the file descriptor for stdin
    fd = sys.stdin.fileno()

    # Save the current terminal attributes
    old_settings = termios.tcgetattr(fd)

    try:
        # Set the terminal to raw mode
        tty.setraw(sys.stdin.fileno())

        # Read a single character from stdin
        ch = sys.stdin.read(1)
    finally:
        # Restore the old terminal attributes
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def run_control():
    #global steering_angle, speed, brake_activated, forward_reverse, dis_stepper
    #brake_activated = True
    global LEFT, RIGHT, speed, movement_msg, stepper_is_disabled, forward_reverse, emergency_stop, disabled_stepper_pub
    LEFT, RIGHT, VEL_UP, VEL_DOWN = False, False, False, False

    # Read input from the keyboard
    key = get_input_char()

    # Set the steering angle and speed based on the input
    if key == "a":
        LEFT = True
    elif key == "d":
        RIGHT = True
    elif key == "w":
        VEL_UP = True
    elif key == "x": 
        VEL_DOWN = True
    elif key == "s":
        speed = 0
    elif key == "f": #switch forward/reverse
        forward_reverse = "forward"
        speed = 0
    elif key == "r":
        forward_reverse = "reverse"
        speed = 0
    elif key == "t":
        stepper_is_disabled = True
        disabled_stepper_pub.publish(True)
    elif key == "g":
        stepper_is_disabled = False
        disabled_stepper_pub.publish(False)
    elif key == " ":
        emergency_stop = True
    elif key == "m":
        emergency_stop = False

    elif key == "l":
        print("closing teleoperations")
        sys.exit(0)

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

    # Initialize the ROS node
    rospy.init_node("keyboard_control")
    print("keyboard control started:")

    # init pubblishers
    command_pub = rospy.Publisher("/command_move", movement, queue_size=1)
    disabled_stepper_pub = rospy.Publisher('disable_stepper_motor_power', Bool, queue_size=1)
    emergency_pub = rospy.Publisher('Emergency_stop', Bool, queue_size=1)

    rate = rospy.Rate(10)

    msg = """
    Control Your Car!
    ---------------------------
    Moving around:
          w
     a    s    d
          x

    r/f : reverse/forward direction
    t/g : disable/anable stepper motor

    press "l" to quit

    """

    # Set the publishing rate to 10 Hz
    rate = rospy.Rate(10)

    # Loop until the ROS node is shutdown
    while not rospy.is_shutdown():
        # Read input from the keyboard
        print(msg)

        run_control()

        # Publish the ackermann drive message
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
        
        # Sleep to maintain the publishing rate
        rate.sleep()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
