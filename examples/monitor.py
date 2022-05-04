#!/usr/bin/python3
"""
Turns down the screen brightness of a connected monitor to 0% as soon as the ToF sensor detects
that a person is standing more than 30cm away from the display. If this person is standing
within these 30cm, the screen brightness is set to 100%.
"""
import os
import sys
import time
import VL53L1X

class ToFVL53L1X(object):

    def __init__(self):
        self.address = 0x29

        # 1 = Short Range, 2 = Medium Range, 3 = Long Range 
        self.range = 1

        self.tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address = self.address)

    def start_sensor(self, pin):
        self.tof.open()
        self.tof.start_ranging(self.range)

    def stop_sensor(self, pin):
        self.tof.stop_ranging()
        
    def set_range(self, range):
        if range == "short":
            self.range = 1
        elif range == "medium":
            self.range = 2
        else:
            self.range = 3

        self.tof.stop_ranging()
        self.tof.start_ranging(self.range)

    def get_range(self):
        if self.range == 1:
            currentRange = "short"
        elif self.range == 2:
            currentRange = "medium"
        else:
            currentRange = "long"

        return currentRange

    def get_distance(self):
        distance = 0.0
        distance = self.tof.get_distance() * 0.1 # mm to cm conversion

        if distance >= 0:
            return distance
        else:
            return -1
          
if __name__ == "__main__":
    output = "VGA-1" # xrandr --listmonitors
    brightness = 1.0 # 100%
  
    tof = ToFVL53L1X()
    tof.start_sensor()
    tof.set_range("short")
    
    while True:
        distance = float(tof.get_distance())
        
        if distance > 30:
            os.system(f'/usr/bin/xrandr --output {output} --brightness {0.0}') # 0%
        else:
            os.system(f'/usr/bin/xrandr --output {output} --brightness {brightness}') # 100%
