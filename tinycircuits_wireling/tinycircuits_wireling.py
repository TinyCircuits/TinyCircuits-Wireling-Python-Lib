# tinycircuits_wireling.py - Last modified 17 Dec 2019
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# 
# Written by Laveréna Wienclaw for TinyCircuits.
# 
# The latest version of this library can be found at https://TinyCircuits.com/

import RPi.GPIO as GPIO
from adafruit_bus_device.i2c_device import I2CDevice
from micropython import const
import pigpio
import busio
import board

import adafruit_ads1x15.ads1115 as ADS # Included ADC module
from adafruit_ads1x15.analog_in import AnalogIn
i2c = busio.I2C(board.SCL, board.SDA)

_MULTIPLEXER_ADDRESS = const(0x70)

class Wireling(): 
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT) # provides power to Wireling Pi Hat
        GPIO.output(22,1)

    def enablePower():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT) 
        GPIO.output(22,1)

    def disablePower():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22,0)

    def selectPort(port):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _MULTIPLEXER_ADDRESS)
        pi.i2c_write_byte(h, 0x04 + port)
        pi.i2c_close(h)

    def readADC():
        # Create the ADC object using the I2C bus
        ads = ADS.ADS1115(i2c)

        chan = AnalogIn(ads, ADS.P0)
        chan1 = AnalogIn(ads, ADS.P1)
        chan2 = AnalogIn(ads, ADS.P2)
        chan3 = AnalogIn(ads, ADS.P3)

        # Print channel value, and voltage
        print("{:>5}\t{:>5}".format('raw', 'v'))
        print("port0: ")
        print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
        print("")
        print("port1: ")
        print("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
        print("")
        print("port2: ")
        print("{:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
        print("")
        print("port3: ")
        print("{:>5}\t{:>5.3f}".format(chan3.value, chan3.voltage))
        print("====================================")











	
