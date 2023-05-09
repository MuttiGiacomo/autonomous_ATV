#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
import RPi.GPIO as GPIO


class encoder : 
	
    def __init__(self,pin_clock,pin_data,pin_cs,reverse_angle):
        self.pin_clock = pin_clock
        self.pin_data = pin_data
        self.pin_cs = pin_cs
        self.reverse_angle = reverse_angle
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin_clock,GPIO.OUT)
        GPIO.setup(self.pin_data,GPIO.IN)
        GPIO.setup(self.pin_cs,GPIO.OUT)


        GPIO.output(self.pin_clock,GPIO.HIGH)
        GPIO.output(self.pin_cs,GPIO.LOW)



    def run(self):
        rospy.init_node('encoder', anonymous=True)
        encoder_pub = rospy.Publisher("encoder_steering",Int16,queue_size=10)
        rospy.loginfo("the encoder node is launched")
        rate = rospy.Rate(1) # 10hz
        while not rospy.is_shutdown():
           encoder_pub.publish(self.analog_to_degree(self.read_data()))
           rate.sleep()


    def read_data(self):
        GPIO.output(self.pin_cs,GPIO.HIGH)
        GPIO.output(self.pin_cs,GPIO.LOW)
        pos=0

        for i in range(10):
            GPIO.output(self.pin_clock,GPIO.LOW)
            GPIO.output(self.pin_clock,GPIO.HIGH)
            if GPIO.input(self.pin_data):
                pos = pos + pow (2,10-(i+1))
     
          
        for i in range(6):
            GPIO.output(self.pin_clock,GPIO.LOW)
            GPIO.output(self.pin_clock,GPIO.HIGH)


        GPIO.output(self.pin_clock,GPIO.LOW)
        GPIO.output(self.pin_clock,GPIO.HIGH)
        rospy.sleep(0.001)

        if self.reverse_angle:
            pos = abs(1024 - pos) 
        
        return pos



    def analog_to_degree(self,pos_in_analog):
        pos_in_degree = int((pos_in_analog+1)/1024*360)
        return pos_in_degree
        


if __name__ == '__main__':

    pin_clock = 12
    pin_data = 19
    pin_cs = 20
    reverse_angle = False
    encoder_inst = encoder(pin_clock,pin_data,pin_cs,reverse_angle)
    try:
        encoder_inst.run()
    except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass






