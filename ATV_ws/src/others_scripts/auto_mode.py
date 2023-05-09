from relay import relay



GPIO_relay_shunt_potbox = 24
GPIO_relay_potentiometer = 5
GPIO_relay_KSI = 16

relay_shunt_potbox_r1 = relay(GPIO_relay_shunt_potbox)
relay_potentiometer_r3 = relay(GPIO_relay_potentiometer)
relay_KSI = relay(GPIO_relay_KSI)

while True :
	rep = str(input("which relay ? : "))
	rep_on = str(input("on ? 1 or 0 : "))
	if rep == "1" :
		if rep_on == "1" :
			relay_shunt_potbox_r1.switch_on()
		else : 
			relay_shunt_potbox_r1.switch_off()
	elif rep =="2":
		if rep_on == "1" :
			relay_KSI.switch_on()
		else :
			relay_KSI.switch_off()
		
	elif rep =="3":
		if rep_on == "1" :
			relay_potentiometer_r3.switch_on()
		else : 
			relay_potentiometer_r3.switch_off()
		
