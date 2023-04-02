#!/usr/bin/env python

import rospy
import signal
import sys
import tty
import termios
from std_msgs.msg import Float64
from ackermann_msgs.msg import AckermannDrive

# Set the maximum steering angle and speed
MAX_STEERING_ANGLE = 0.4
MAX_SPEED = 2.0

# Initialize the steering angle and speed
steering_angle = 0.0
speed = 0.0

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
    global steering_angle, speed

    # Read input from the keyboard
    key = get_input_char()

    # Set the steering angle and speed based on the input
    if key == "a":
        steering_angle += 0.05
    elif key == "d":
        steering_angle -= 0.05
    elif key == "w":
        speed += 10
    elif key == "x":
        speed -= 10
    elif key == "s":
        speed = 0
    elif key == "l":
        sys.exit(0)

    

    # Limit the steering angle and speed to their maximum values
    steering_angle = max(-MAX_STEERING_ANGLE, min(steering_angle, MAX_STEERING_ANGLE))
    speed = max(-MAX_SPEED, min(speed, MAX_SPEED))

def main():
    global steering_angle, speed

    msg = """
    Control Your Car!
    ---------------------------
    Moving around:
         w
    a    s    d
         x

    w/x : increase/decrease linear velocity
    a/d : increase/decrease angular velocity
    space key, s : force stop
    CTRL-C to quit

    press "l" to exit
    """

    # Initialize the ROS node
    rospy.init_node("keyboard_control")

    # Create a publisher for the ackermann drive message
    pub = rospy.Publisher("/ackermann_cmd", AckermannDrive, queue_size=1)

    # Set the publishing rate to 10 Hz
    rate = rospy.Rate(10)

    # Loop until the ROS node is shutdown
    while not rospy.is_shutdown():
        # Read input from the keyboardù

        print(msg)

        signal.signal(signal.SIGINT, signal_handler)

        keyboard_input()

        

        # Create an ackermann drive message with the current steering angle and speed
        drive_msg = AckermannDrive()
        drive_msg.steering_angle = steering_angle
        drive_msg.speed = speed

        # Publish the ackermann drive message
        pub.publish(drive_msg)

        # Sleep to maintain the publishing rate
        rate.sleep()
        signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
