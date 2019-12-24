# Wireling Simple Input Example
# This example can be used with the Large Button, Small button, Switch, 
# and Digital Hall Sensor Wirelings to read the digital state

import time
import tinycircuits_wireling

wireling = tinycircuits_wireling.Wireling()

while(True):
    wireling.digitalRead(0) # Insert 0-3 correlating with the port label on pi hat
    time.sleep(0.2)