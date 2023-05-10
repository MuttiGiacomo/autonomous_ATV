#!/usr/bin/env python3.6

#Rodolphe COCKENPOT All Right reserved 

import smbus 


# Get I2C bus
bus = smbus.SMBus(1)
value =[0]


class digital_pot :

    def __init__(self,bus,addr):
        self.bus = bus
        self.addr = addr

        
    def send_value(self,value):
        self.bus.write_i2c_block_data(self.addr, 0x00, value)

    def read_value(self):
        data = self.bus.read_byte_data(self.addr, 0x00) 
        resistance = (data / 256.0 ) * 5.0
        return resistance


        
"""
pot = digital_pot (bus,0x18)

while True :
	val = input("val : ")
	value[0]=int(val)
	pot.send_value(value)
"""
