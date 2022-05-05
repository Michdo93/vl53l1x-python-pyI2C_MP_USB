#!/usr/bin/python3
import VL53L1X

class ToFVL53L1X(object):

    def __init__(self):
        self.address = 0x29

        # 1 = Short Range, 2 = Medium Range, 3 = Long Range 
        self.range = 1

        self.tof = VL53L1X.VL53L1X(i2c_bus=0, i2c_address = self.address)

    def start_sensor(self):
        self.tof.open()
        self.tof.start_ranging(self.range)

    def stop_sensor(self):
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
    tof = ToFVL53L1X()
    tof.start_sensor()
    tof.set_range("short")
    
    while True:
        distance = float(tof.get_distance())
        
        print(distance)
