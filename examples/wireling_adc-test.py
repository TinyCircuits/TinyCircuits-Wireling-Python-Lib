# Wireling program demonstrating the functionality of the readADC() function
# Prints out voltage 

import time
import tinycircuits_wireling

# Initialize and enable power to Wireling Pi Hat
tinycircuits_wireling.Wireling()

while(True):
	tinycircuits_wireling.Wireling.readADC()
	time.sleep(1) 