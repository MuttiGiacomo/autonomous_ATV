#!/usr/bin/env python

import rospy 
import sys
import tty
import termios
from std_msgs.msg import Bool,String,Int16
from sensor_msgs.msg import Joy
from action_control_unit.msg import movement    # custom "movement" message:
															#uint16 speed_command
															#int16 angle_of_correction
															#string forward_reverse

max_pot_value = 255

ps4_buttons = {"share":0,
"joystick_left":0,
"joystick_right":0,
"options": 0,
"top_arrow": 0,
"right_arrow": 0,
"bot_arrow": 0,
"left_arrow": 0,
"left_trigger": 0,
"right_trigger": 0,
"left_bumper": 0,
"right_bumper": 0,
"triangle": 0,
"circle": 0,
"cross": 0,
"square": 0,
"home": 0}


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

def callback_joy(message):
	for index,(button_name,value) in enumerate(ps4_buttons.items()):
		ps4_buttons[button_name] = message.buttons[index]
	
	
def run():
	# movement msg initialization 
	movement_msg = movement() 
	movement_msg.forward_reverse = "forward"  
	movement_msg.angle_of_correction = 0 
	movement_msg.speed_command = 0
	total_correction_angle = 0


	while not rospy.is_shutdown():
	
		# steering angle update 
		if ps4_buttons["right_arrow"] :
			movement_msg.angle_of_correction = 12 # arbitrarily chosen 
		if ps4_buttons["left_arrow"] :
			movement_msg.angle_of_correction = -12 # arbitrarily chosen 
		total_correction_angle=total_correction_angle + movement_msg.angle_of_correction

		# linear velocity update
		if ps4_buttons["right_trigger"] :
			movement_msg.speed_command = movement_msg.speed_command  + 2
			if movement_msg.speed_command > max_pot_value :
				movement_msg.speed_command = max_pot_value		
		if ps4_buttons["left_trigger"] :
			movement_msg.speed_command = movement_msg.speed_command  - 2
			if movement_msg.speed_command < 0 :
				movement_msg.speed_command = 0
		if ps4_buttons["circle"]:  
			movement_msg.speed_command = 0	

		# chage forward/reverse mode 	
		if movement_msg.speed_command == 0 :
			if ps4_buttons["triangle"]:
				movement_msg.forward_reverse = "forward"
			if ps4_buttons["cross"]:
				movement_msg.forward_reverse = "reverse"
			
			# stepper mototr on/off
			if ps4_buttons["joystick_right"] :
				disable_stepper.publish(True)
			if ps4_buttons["joystick_left"] :
				disable_stepper.publish(False)
				
		# pubblish movement msg
		command_move.publish(movement_msg)
		
		# write  pusbblished values in the logs
		log.publish("S:{} A:{} {}".format(movement_msg.speed_command,total_correction_angle,movement_msg.forward_reverse))
		
		# reset steering angle correction
		movement_msg.angle_of_correction = 0

		rospy.sleep(0.1)
		
		

def shutdown():
	rospy.loginfo("The remote test node is stopped")
	
	
	
if __name__=="__main__":
	try:
		rospy.Subscriber('joy',Joy,callback_joy)
		command_move = rospy.Publisher('command_move',movement,queue_size=5)
		log = rospy.Publisher('log',String,queue_size=10)
		disable_stepper = rospy.Publisher('disable_stepper_motor_power',Bool,queue_size=1)
		
		rospy.init_node("remote_test")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The wireless remote node is running ")	
		log.publish("w_remote launched")	
		run()
	except rospy.ROSInterruptException:
		pass