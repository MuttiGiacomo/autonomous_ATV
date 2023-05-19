#!/usr/bin/env python

import rospy
import signal
import sys
import tty
import termios
from std_msgs.msg import Float64, Bool
from action_control_unit.msg import movement

# Set the maximum steering angle and speed
MAX_SPEED = 50
ANGLE_CHANGE = 3
SPEED_CHANGE = 2

# Initialize the steering angle and speed
steering_angle = 0
speed = 0
#global forward_reverse, dis_stepper
#forward_reverse = "forward"
#dis_stepper = False


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

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

def keyboard_input():
    global steering_angle, speed, brake_activated, forward_reverse, dis_stepper
    brake_activated = True

    # Read input from the keyboard
    key = get_input_char()

    # Set the steering angle and speed based on the input
    if key == "a":
        steering_angle = + ANGLE_CHANGE
    elif key == "d":
        steering_angle = - ANGLE_CHANGE
    elif key == "w":
        steering_angle = 0
        speed += SPEED_CHANGE  #speed must be always positive, if I want to go backwards the 'forward_reverse' variable is changed
    elif key == "x": 
        steering_angle = 0
        speed -= SPEED_CHANGE
    elif key == "s":
        steering_angle = 0
        speed = 0
    elif key == "f": #switch forward/reverse
        steering_angle = 0
        speed = 0 
        forward_reverse = "forward"
    elif key == "r":
        steering_angle = 0
        speed = 0
        forward_reverse = "reverse"
    elif key == "t":
        steering_angle = 0
        dis_stepper = True
    elif key == "g":
        steering_angle = 0
        dis_stepper = False

    elif key == "l":
        sys.exit(0)

    # Limit the linear speed to their max and min values
    speed = max( 0 , min(speed, MAX_SPEED))

def main():
    global steering_angle, speed, forward_reverse, dis_stepper
    forward_reverse = "forward"
    dis_stepper = False

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

    # Initialize the ROS node
    rospy.init_node("keyboard_control")

    # Create a publisher for the ackermann drive message
    pub = rospy.Publisher("/command_move", movement, queue_size=1)
    disable_stepper = rospy.Publisher("/disable_stepper_motor_power",Bool,queue_size=1)

    # Set the publishing rate to 10 Hz
    rate = rospy.Rate(10)

    # Loop until the ROS node is shutdown
    while not rospy.is_shutdown():
        # Read input from the keyboard
        print(msg)
        signal.signal(signal.SIGINT, signal_handler)
        keyboard_input()

        # Create an ackermann drive message with the current steering angle and speed
        drive_msg = movement()
        drive_msg.Angle_of_correction = steering_angle
        drive_msg.Speed_command = speed
        drive_msg.Forward_reverse = forward_reverse

        # Publish the ackermann drive message
        pub.publish(drive_msg)
        commanded_vals = " ---- linear speed: " + str(speed) + "  ----- steering angle variation: " + str(steering_angle) + " ----"
        print(commanded_vals)
        disable_stepper.publish(dis_stepper)
        other_vals = " direction: " + forward_reverse + "  ----- stepper motor disabled: " + str(dis_stepper) + " ----"
        print(other_vals)

        # Sleep to maintain the publishing rate
        rate.sleep()
        signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
