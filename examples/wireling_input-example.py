# Wireling Simple Input Example
# This example can be used with the Large Button, Small button, Switch, 
# and Digital Hall Sensor Wirelings to show state being activated low

import time
import board
import RPi.GPIO as GPIO
import tinycircuits_wireling

tinycircuits_wireling.Wireling()

pin = 10 # On Wireling Pi Hat - Port0: Pin 10, Port1: Pin 12, Port2: 18, Port3: Pin 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
    input_state = GPIO.input(pin)
    if input_state == False:
        print('State Low')
        time.sleep(0.2)