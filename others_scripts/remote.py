
import RPi.GPIO as GPIO
import time
#TO-DO create a file with all the GPIO number and  the device conneted on it 

GPIO.setmode(GPIO.BCM)


gpio_button_mode_auto = 27
gpio_button_mode_manu = 26
gpio_button_go = 21
gpio_button_stop =13


GPIO.setup(gpio_button_go,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_button_stop,GPIO.IN,pull_up_down=GPIO.PUD_UP)



while True :
	print("go : {}".format(str(GPIO.input(gpio_button_go))))
	print("stop : {}".format(str(GPIO.input(gpio_button_stop))))
	time.sleep(0.1)
