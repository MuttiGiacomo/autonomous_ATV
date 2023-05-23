#!/usr/bin/env python3.6

import rospy 
from std_msgs.msg import String,Int16
import sys
sys.path.append("~/i2c_fifo/src/i2c_fifo/nodes/")
from package.digital_pot.digital_pot import digital_pot
from package.lcd.lcddriver import lcd
import smbus

bus = smbus.SMBus(1)



digit_pot = digital_pot(bus,0x18)

try : 
	screen = lcd(0x27,bus)
	screen_degraded_mode = False 
except:
	rospy.logwarn("Screen not connected or defected ")
	rospy.loginfo("node in degraded mode")
	screen_degraded_mode = True 
	

#TO-DO create a file with all the GPIO number and  the device conneted on it 
#ADD value Stop for thr potentiometer if the node shutdown 


line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""

lock = False


def callback_lcd_line1(message):
	global line_1
	line_1 = str(message.data)
	
def callback_lcd_line2(message):
	global line_2
	line_2 = str(message.data)
	
def callback_lcd_line3(message):
	global line_3
	line_3 = str(message.data)
	
def callback_lcd_line4(message):
	global line_4
	line_4 = str(message.data)
	
def callback_pot(message):
	global lock 
	if not lock :
		lock = True
		digit_pot.send_value([int(message.data)])
		rospy.loginfo("digit pot data : {}".format(message.data))
		rospy.loginfo(str(digit_pot.read_value()))
		lock = False
		
	
	


def run():
	last_mode = " "
	global lock
	last_lines = [line_1,line_2,line_3,line_4]
	while not rospy.is_shutdown():
		
		if (not lock and last_lines != [line_1,line_2,line_3,line_4] and not screen_degraded_mode):
			lock = True 
			screen.lcd_clear()
			screen.lcd_display_string(line_1, 1)
			screen.lcd_display_string(line_2, 2)
			screen.lcd_display_string(line_3, 3)
			screen.lcd_display_string(line_4, 4)
			last_lines = [line_1,line_2,line_3,line_4]
			lock = False 
			rospy.sleep(1)
		
			
def shutdown():
	rospy.loginfo("The remote node is stopped")
	screen.lcd_clear()
	
	
	
if __name__=="__main__":
	try:
		rospy.Subscriber('screen_line_1',String,callback_lcd_line1)
		rospy.Subscriber('screen_line_2',String,callback_lcd_line2)
		rospy.Subscriber('screen_line_3',String,callback_lcd_line3)
		rospy.Subscriber('screen_line_4',String,callback_lcd_line4)
        
		rospy.Subscriber('potentiometer_value',Int16,callback_pot)

		rospy.init_node("i2c_fifo")
		rospy.on_shutdown(shutdown)
		rospy.loginfo("The i2c_fifo node node is running ")		
		run()
	except rospy.ROSInterruptException:
		pass

