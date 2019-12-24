# Simple Wireling example that prints I2C device address detected
# at the port selected (0-3) below

import pigpio
import RPi.GPIO as GPIO
import tinycircuits_wireling

pi = pigpio.pi()

# Initialize and enable power to Wireling Pi Hat
wireling = tinycircuits_wireling.Wireling()

# Toggle this variable to use Wireling on a different port (0-3)
port = 0
wireling.selectPort(port)

for device in range(128):
	h = pi.i2c_open(1, device)
	try:
		for port in range(0,3):
			pi.i2c_write_byte(h,port)
			d=pi.i2c_read_byte(h)

		# Ignore addresses of ADC, RTC, and MUX (respectively)
		if device == 0x48: pass
		elif device == 0x68: pass
		elif device == 0x70: pass
		else: 				
			print(hex(device))	# Print I2C address
	except:
		pass
	pi.i2c_close(h)

pi.stop
	
